from sqlite3 import Cursor

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


def test_exists(db: Cursor):
    assert collection.exists(1, db)


def test_does_not_exist(db: Cursor):
    assert not collection.exists(9999999, db)


def test_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(collection.from_id(16, db))


def test_from_id_failure(db: Cursor):
    assert collection.from_id(90000, db) is None


def test_from_name_and_type_success(db: Cursor):
    col = collection.from_name_and_type("Electronic", CollectionType.GENRE, db)
    assert col.name == "Electronic"  # type: ignore
    assert col.type == CollectionType.GENRE  # type: ignore


def test_from_name_and_type_failure(db: Cursor):
    col1 = collection.from_name_and_type("Electronic", CollectionType.COLLAGE, db)
    col2 = collection.from_name_and_type("Inb0x", CollectionType.SYSTEM, db)

    assert col1 is None
    assert col2 is None


def test_all(db: Cursor, snapshot):
    collections = collection.all(db)
    snapshot.assert_match(collections)


def test_all_filter_type(db: Cursor, snapshot):
    collections = collection.all(db, types=[CollectionType.SYSTEM])
    snapshot.assert_match(collections)


def test_all_filter_type_multiple(db: Cursor, snapshot):
    collections = collection.all(
        db, types=[CollectionType.SYSTEM, CollectionType.GENRE]
    )
    snapshot.assert_match(collections)


@pytest.mark.parametrize(
    "type", [CollectionType.COLLAGE, CollectionType.LABEL, CollectionType.GENRE]
)
def test_create(db: Cursor, type):
    col = collection.create("new collage", type, starred=True, cursor=db)
    assert col.id == 21
    assert col == collection.from_id(21, db)


def test_create_duplicate(db: Cursor):
    with pytest.raises(Duplicate):
        collection.create("Folk", CollectionType.GENRE, db)


@pytest.mark.parametrize("type", [CollectionType.SYSTEM, CollectionType.RATING])
def test_create_invalid_type(db: Cursor, type):
    with pytest.raises(InvalidCollectionType):
        collection.create("new collage", type, cursor=db)


def test_update_fields(db: Cursor, snapshot):
    col = collection.update(
        collection.from_id(13, db),  # type: ignore
        cursor=db,
        name="New Name",
        starred=True,
    )
    snapshot.assert_match(col)
    assert col == collection.from_id(13, db)


@pytest.mark.parametrize("col_id", [1, 5])
def test_update_immutable(db: Cursor, col_id):
    with pytest.raises(Immutable):
        collection.update(
            collection.from_id(6, db),  # type: ignore
            cursor=db,
            name="New Name",
        )


@pytest.mark.parametrize("col_id", [1, 5])
def test_update_duplicate(db: Cursor, col_id):
    with pytest.raises(Duplicate) as e:
        collection.update(
            collection.from_id(18, db),  # type: ignore
            cursor=db,
            name="Folk",
        )

    assert e.value.entity.id == 12


def test_update_nothing(db: Cursor):
    col = collection.from_id(13, db)
    new_col = collection.update(col, cursor=db)  # type: ignore
    assert col == new_col


def test_update_starred(db: Cursor):
    col = collection.update(
        collection.from_id(12, db),  # type: ignore
        cursor=db,
        starred=True,
    )
    assert col.starred is True
    assert col == collection.from_id(12, db)


def test_releases(db: Cursor, snapshot):
    art = collection.from_id(16, db)
    snapshot.assert_match(collection.releases(art, db))  # type: ignore


def test_add_release(db: Cursor, snapshot):
    col = collection.from_id(3, db)

    snapshot.assert_match(collection.add_release(col, 2, db))  # type: ignore
    snapshot.assert_match(collection.releases(col, db))  # type: ignore


def test_add_release_failure(db: Cursor):
    col = collection.from_id(12, db)

    with pytest.raises(AlreadyExists):
        collection.add_release(col, 2, db)  # type: ignore


def test_del_release(db: Cursor, snapshot):
    col = collection.from_id(12, db)

    snapshot.assert_match(collection.del_release(col, 2, db))  # type: ignore
    snapshot.assert_match(collection.releases(col, db))  # type: ignore


def test_del_release_failure(db: Cursor):
    col = collection.from_id(3, db)

    with pytest.raises(DoesNotExist):
        collection.del_release(col, 2, db)  # type: ignore


def test_top_genres(db: Cursor, snapshot):
    art = collection.from_id(16, db)
    snapshot.assert_match(collection.top_genres(art, db))  # type: ignore


def test_image(db: Cursor):
    col = collection.from_id(12, db)
    assert collection.image(col, db).id == 1  # type: ignore


def test_image_nonexistent(db: Cursor):
    col = collection.from_id(2, db)
    assert collection.image(col, db) is None  # type: ignore
