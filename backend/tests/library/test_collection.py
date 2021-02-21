import pytest
from pysqlite3 import Connection

from src.enums import CollectionType
from src.errors import (
    AlreadyExists,
    DoesNotExist,
    Duplicate,
    Immutable,
    InvalidCollectionType,
)
from src.library import collection
from tests.conftest import NUM_COLLECTIONS


def test_exists(db: Connection):
    assert collection.exists(1, db)


def test_does_not_exist(db: Connection):
    assert not collection.exists(9999999, db)


def test_from_id_success(db: Connection, snapshot):
    snapshot.assert_match(collection.from_id(7, db))


def test_from_id_failure(db: Connection):
    assert collection.from_id(90000, db) is None


def test_from_name_and_type_success(db: Connection):
    col = collection.from_name_and_type("Electronic", CollectionType.GENRE, db)
    assert col is not None

    assert col.name == "Electronic"
    assert col.type == CollectionType.GENRE


def test_from_name_and_type_failure(db: Connection):
    col1 = collection.from_name_and_type("Electronic", CollectionType.COLLAGE, db)
    col2 = collection.from_name_and_type("Inb0x", CollectionType.SYSTEM, db)

    assert col1 is None
    assert col2 is None


def test_search_all(db: Connection, snapshot):
    collections = collection.search(db)
    snapshot.assert_match(collections)


def test_search_filters(db: Connection, snapshot):
    collections = collection.search(
        db,
        types=[CollectionType.SYSTEM, CollectionType.GENRE],
        search="Folk",
    )
    assert len(collections) == 1
    assert collections[0].name == "Folk"


def test_search_page(db: Connection, snapshot):
    c1 = collection.search(db, page=1, per_page=1)[0]
    c2 = collection.search(db, page=2, per_page=1)[0]
    assert c1 != c2


def test_search_per_page(db: Connection, snapshot):
    cols = collection.search(db, page=1, per_page=2)
    assert len(cols) == 2


def test_count_all(db: Connection, snapshot):
    count = collection.count(db)
    assert count == NUM_COLLECTIONS


def test_count_one(db: Connection, snapshot):
    count = collection.count(
        db,
        types=[CollectionType.SYSTEM, CollectionType.GENRE],
        search="Folk",
    )
    assert count == 1


@pytest.mark.parametrize(
    "type", [CollectionType.COLLAGE, CollectionType.LABEL, CollectionType.GENRE]
)
def test_create(db: Connection, type):
    col = collection.create("new collage", type, starred=True, conn=db)
    assert col.id == 12
    assert col == collection.from_id(12, db)


def test_create_duplicate(db: Connection):
    with pytest.raises(Duplicate):
        collection.create("Folk", CollectionType.GENRE, db)


def test_create_invalid_type(db: Connection):
    with pytest.raises(InvalidCollectionType):
        collection.create("new collage", CollectionType.SYSTEM, conn=db)


def test_update_fields(db: Connection, snapshot):
    col = collection.from_id(4, db)
    assert col is not None

    col = collection.update(col, conn=db, name="New Name", starred=True)
    snapshot.assert_match(col)
    assert col == collection.from_id(4, db)


def test_update_immutable(db: Connection):
    col = collection.from_id(1, db)
    assert col is not None

    with pytest.raises(Immutable):
        collection.update(col, conn=db, name="New Name")


def test_update_duplicate(db: Connection):
    col = collection.from_id(9, db)
    assert col is not None

    with pytest.raises(Duplicate) as e:
        collection.update(
            col,
            conn=db,
            name="Folk",
        )

    assert e.value.entity.id == 3


def test_update_nothing(db: Connection):
    col = collection.from_id(4, db)
    assert col is not None

    new_col = collection.update(col, conn=db)
    assert col == new_col


def test_update_starred(db: Connection):
    col = collection.from_id(3, db)
    assert col is not None

    col = collection.update(col, conn=db, starred=True)
    assert col.starred is True
    assert col == collection.from_id(3, db)


def test_releases(db: Connection, snapshot):
    col = collection.from_id(7, db)
    assert col is not None

    snapshot.assert_match(collection.releases(col, db))


def test_add_release(db: Connection, snapshot):
    col = collection.from_id(2, db)
    assert col is not None

    snapshot.assert_match(collection.add_release(col, 2, db))
    snapshot.assert_match(collection.releases(col, db))


def test_add_release_failure(db: Connection):
    col = collection.from_id(3, db)
    assert col is not None

    with pytest.raises(AlreadyExists):
        collection.add_release(col, 2, db)


def test_del_release(db: Connection, snapshot):
    col = collection.from_id(3, db)
    assert col is not None

    snapshot.assert_match(collection.del_release(col, 2, db))
    snapshot.assert_match(collection.releases(col, db))


def test_del_release_failure(db: Connection):
    col = collection.from_id(2, db)
    assert col is not None

    with pytest.raises(DoesNotExist):
        collection.del_release(col, 2, db)


def test_top_genres(db: Connection, snapshot):
    col = collection.from_id(7, db)
    assert col is not None

    snapshot.assert_match(collection.top_genres(col, db))


def test_image(db: Connection):
    col = collection.from_id(3, db)
    assert col is not None
    img = collection.image(col, db)
    assert img is not None
    assert img.id == 1


def test_image_nonexistent(db: Connection):
    col = collection.from_id(2, db)
    assert col is not None

    assert collection.image(col, db) is None
