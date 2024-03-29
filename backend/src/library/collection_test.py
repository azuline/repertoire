from sqlite3 import Connection

import pytest

from src.enums import CollectionType
from src.errors import (
    AlreadyExists,
    DoesNotExist,
    Duplicate,
    Immutable,
    InvalidArgument,
    InvalidCollectionType,
)
from src.fixtures.factory import Factory

from . import collection


def test_exists(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    assert collection.exists(col.id, db)


def test_does_not_exist(db: Connection):
    assert not collection.exists(9999999, db)


def test_from_id_success(factory: Factory, db: Connection):
    col_id = factory.collection(conn=db).id
    col = collection.from_id(col_id, db)
    assert col is not None
    assert col.id == col_id


def test_from_id_failure(db: Connection):
    assert collection.from_id(90000, db) is None


def test_from_name_type_user_success(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    new_col = collection.from_name_type_user(col.name, col.type, db)
    assert new_col is not None

    assert col.name == new_col.name
    assert col.type == new_col.type


def test_from_name_type_user_with_user_id(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    col = factory.collection(conn=db, type=CollectionType.PERSONAL, user=usr)
    new_col = collection.from_name_type_user(col.name, col.type, db, usr.id)
    assert col == new_col


def test_from_name_type_user_failure(db: Connection):
    col1 = collection.from_name_type_user("Electronic", CollectionType.COLLAGE, db)
    col2 = collection.from_name_type_user("Inb0x", CollectionType.SYSTEM, db)

    assert col1 is None
    assert col2 is None


def test_from_name_and_type(factory: Factory, db: Connection):
    usr1, _ = factory.user(conn=db)
    col1 = factory.collection(
        name="test", type=CollectionType.SYSTEM, user=usr1, conn=db
    )

    usr2, _ = factory.user(conn=db)
    col2 = factory.collection(
        name="test", type=CollectionType.SYSTEM, user=usr2, conn=db
    )

    factory.collection(name="other", type=CollectionType.COLLAGE, conn=db)

    cols = collection.from_name_and_type("test", CollectionType.SYSTEM, conn=db)
    assert {c.id for c in cols} == {col1.id, col2.id}


def test_search_all(factory: Factory, db: Connection):
    cols = {factory.collection(conn=db) for _ in range(5)}
    assert cols == set(collection.search(db))


def test_search_types(factory: Factory, db: Connection):
    col = factory.collection(type=CollectionType.GENRE, conn=db)
    collections = collection.search(
        db,
        types=[CollectionType.SYSTEM, CollectionType.GENRE],
        search=col.name,
    )
    assert len(collections) == 1
    assert collections[0].id == col.id


def test_search_user(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    unused_usr, _ = factory.user(conn=db)

    col1 = factory.collection(type=CollectionType.PERSONAL, user=usr, conn=db)
    col2 = factory.collection(type=CollectionType.PERSONAL, user=usr, conn=db)

    col3 = factory.collection(type=CollectionType.PERSONAL, user=unused_usr, conn=db)
    col4 = factory.collection(conn=db)

    cols = collection.search(db, user_ids=[usr.id])
    ids = [c.id for c in cols]
    assert all(c.id in ids for c in [col1, col2])
    assert not any(c.id in ids for c in [col3, col4])


def test_search_page(factory: Factory, db: Connection):
    for _ in range(5):
        factory.collection(conn=db)

    c1 = collection.search(db, page=1, per_page=1)[0]
    c2 = collection.search(db, page=2, per_page=1)[0]
    assert c1 != c2


def test_search_per_page(factory: Factory, db: Connection):
    cols = [factory.collection(conn=db) for _ in range(5)]
    cols = collection.search(db, page=1, per_page=2)
    assert len(cols) == 2


def test_count_all(factory: Factory, db: Connection):
    cols = [factory.collection(conn=db) for _ in range(5)]
    assert len(cols) == collection.count(db)


def test_count_one(factory: Factory, db: Connection):
    cols = [factory.collection(conn=db) for _ in range(5)]
    count = collection.count(db, types=[cols[0].type], search=cols[0].name)
    assert count == 1


@pytest.mark.parametrize(
    "type",
    [
        CollectionType.COLLAGE,
        CollectionType.LABEL,
        CollectionType.GENRE,
    ],
)
def test_create(db: Connection, type):
    col = collection.create("new collage", type, conn=db)
    assert col == collection.from_id(col.id, db)


def test_create_collage_with_user(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    with pytest.raises(InvalidArgument):
        collection.create(
            "new collage",
            CollectionType.COLLAGE,
            user_id=usr.id,
            conn=db,
        )


def test_create_personal(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    col = collection.create(
        "new collection",
        CollectionType.PERSONAL,
        user_id=usr.id,
        conn=db,
    )
    assert col == collection.from_id(col.id, db)


def test_create_personal_without_user(db: Connection):
    with pytest.raises(InvalidArgument):
        collection.create(
            "new collection",
            CollectionType.PERSONAL,
            conn=db,
        )


def test_create_duplicate(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    with pytest.raises(Duplicate):
        collection.create(col.name, col.type, db)


def test_create_invalid_type(db: Connection):
    with pytest.raises(InvalidCollectionType):
        collection.create("new collage", CollectionType.SYSTEM, conn=db)


def test_create_invalid_type_override(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    col = collection.create(
        "new collage",
        CollectionType.SYSTEM,
        user_id=usr.id,
        conn=db,
        override_immutable=True,
    )
    assert col is not None


def test_update_fields(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    new_col = collection.update(col, conn=db, name="New Name")
    assert new_col == collection.from_id(col.id, db)
    assert new_col.name == "New Name"


def test_update_immutable(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    col = factory.collection(type=CollectionType.SYSTEM, user=usr, conn=db)

    with pytest.raises(Immutable):
        collection.update(col, conn=db, name="New Name")


def test_update_duplicate(factory: Factory, db: Connection):
    col1 = factory.collection(conn=db)
    col2 = factory.collection(conn=db)

    with pytest.raises(Duplicate) as e:
        collection.update(
            col2,
            conn=db,
            name=col1.name,
        )

    assert e.value.entity == col1


def test_star(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    col = factory.collection(conn=db)
    collection.star(col, usr.id, db)
    assert collection.starred(col, usr.id, db) is True


def test_unstar(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    col = factory.collection(conn=db, starred_for_user=usr.id)
    collection.unstar(col, usr.id, db)
    assert not collection.starred(col, usr.id, db) is True


def test_releases(factory: Factory, db: Connection):
    releases = [factory.release(conn=db) for _ in range(4)]
    col = factory.collection(conn=db)

    for rls in releases:
        collection.add_release(col, rls.id, db)

    out = collection.releases(col, db)
    assert {r.id for r in releases} == {r.id for r in out}


def test_add_release(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    rls = factory.release(conn=db)

    new_col = collection.add_release(col, rls.id, db)
    assert new_col.num_releases == col.num_releases + 1  # type: ignore

    releases = collection.releases(col, db)
    assert len(releases) == new_col.num_releases  # type: ignore
    assert releases[0].id == rls.id


def test_add_release_failure(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    rls = factory.release(conn=db)
    collection.add_release(col, rls.id, db)

    with pytest.raises(AlreadyExists):
        collection.add_release(col, rls.id, db)


def test_del_release(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    rls = factory.release(conn=db)
    collection.add_release(col, rls.id, db)

    new_col = collection.del_release(col, rls.id, db)
    assert new_col.num_releases == col.num_releases - 1  # type: ignore

    releases = collection.releases(col, db)
    assert releases == []


def test_del_release_failure(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    rls = factory.release(conn=db)

    with pytest.raises(DoesNotExist):
        collection.del_release(col, rls.id, db)


def test_top_genres(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    releases = [factory.release(conn=db) for _ in range(4)]
    genres = [factory.collection(type=CollectionType.GENRE, conn=db) for _ in range(4)]

    for i, rls in enumerate(releases):
        collection.add_release(col, rls.id, db)
        for grn in genres[: i + 1]:
            collection.add_release(grn, rls.id, db)

    tg = collection.top_genres(col, db)

    for i in range(4):
        assert tg[i]["genre"].id == genres[i].id
        assert tg[i]["num_matches"] == 4 - i


def test_image(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    img = factory.mock_image(conn=db)
    rls = factory.release(image_id=img.id, conn=db)

    collection.add_release(col, rls.id, db)

    new_img = collection.image(col, db)
    assert new_img is not None
    assert new_img.id == img.id


def test_image_nonexistent(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    assert collection.image(col, db) is None


def test_user(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    col = factory.collection(user=usr, type=CollectionType.SYSTEM, conn=db)
    col_user = collection.user(col, conn=db)
    assert col_user is not None
    assert usr.id == col_user.id
