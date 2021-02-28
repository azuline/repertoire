from sqlite3 import Connection

import pytest

from src.enums import CollectionType
from src.errors import (
    AlreadyExists,
    DoesNotExist,
    Duplicate,
    Immutable,
    InvalidCollectionType,
)
from src.library import collection
from tests.factory import Factory


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


def test_from_name_and_type_success(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    new_col = collection.from_name_and_type(col.name, col.type, db)
    assert new_col is not None

    assert col.name == new_col.name
    assert col.type == new_col.type


def test_from_name_and_type_failure(db: Connection):
    col1 = collection.from_name_and_type("Electronic", CollectionType.COLLAGE, db)
    col2 = collection.from_name_and_type("Inb0x", CollectionType.SYSTEM, db)

    assert col1 is None
    assert col2 is None


def test_search_all(factory: Factory, db: Connection):
    cols = {factory.collection(conn=db) for _ in range(5)}
    # Remove inbox & favorites collections for a better comparison.
    out = {col for col in collection.search(db) if col.id not in [1, 2]}
    assert cols == out


def test_search_filters(factory: Factory, db: Connection):
    col = factory.collection(type=CollectionType.GENRE, conn=db)
    collections = collection.search(
        db,
        types=[CollectionType.SYSTEM, CollectionType.GENRE],
        search=col.name,
    )
    assert len(collections) == 1
    assert collections[0].id == col.id


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
    count = collection.count(db)
    # Two extras are inbox & favorites.
    assert len(cols) == count - 2


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
    col = collection.create("new collage", type, starred=True, conn=db)
    assert col == collection.from_id(col.id, db)


def test_create_duplicate(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    with pytest.raises(Duplicate):
        collection.create(col.name, col.type, db)


def test_create_invalid_type(db: Connection):
    with pytest.raises(InvalidCollectionType):
        collection.create("new collage", CollectionType.SYSTEM, conn=db)


def test_create_invalid_type_override(db: Connection):
    col = collection.create(
        "new collage",
        CollectionType.SYSTEM,
        conn=db,
        override_immutable=True,
    )
    assert col is not None


def test_update_fields(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    new_col = collection.update(col, conn=db, name="New Name", starred=True)
    assert new_col == collection.from_id(col.id, db)
    assert new_col.name == "New Name"
    assert new_col.starred is True


def test_update_immutable(factory: Factory, db: Connection):
    col = factory.collection(type=CollectionType.SYSTEM, conn=db)
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


def test_update_starred(factory: Factory, db: Connection):
    col = factory.collection(conn=db)
    new_col = collection.update(col, conn=db, starred=True)
    assert new_col.starred is True
    assert new_col == collection.from_id(col.id, db)


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
