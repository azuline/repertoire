from sqlite3 import Cursor

import pytest

from backend.enums import CollectionType
from backend.errors import Duplicate
from backend.lib import collection


def test_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(collection.from_id(16, db))


def test_from_id_failure(db: Cursor):
    assert collection.from_id(90000, db) is None


def test_from_name_and_type_success(db: Cursor):
    col = collection.from_name_and_type("Electronic", CollectionType.GENRE, db)
    assert col.name == "Electronic"
    assert col.type == CollectionType.GENRE


def test_from_name_and_type_failure(db: Cursor):
    col1 = collection.from_name_and_type("Electronic", CollectionType.COLLAGE, db)
    col2 = collection.from_name_and_type("Inb0x", CollectionType.SYSTEM, db)

    assert col1 is None
    assert col2 is None


def test_all(db: Cursor, snapshot):
    collections = collection.all(db)
    snapshot.assert_match(collections)


def test_all_filter_type(db: Cursor, snapshot):
    collections = collection.all(db, type=CollectionType.SYSTEM)
    snapshot.assert_match(collections)


def test_create(db: Cursor):
    col = collection.create(
        "new collage", CollectionType.COLLAGE, favorite=True, cursor=db
    )
    assert col.id == 20
    assert col == collection.from_id(20, db)


def test_create_duplicate(db: Cursor):
    with pytest.raises(Duplicate):
        collection.create("Folk", CollectionType.GENRE, db)


def test_releases(db: Cursor, snapshot):
    art = collection.from_id(16, db)
    snapshot.assert_match(collection.releases(art, db))


def test_top_genres(db: Cursor, snapshot):
    art = collection.from_id(16, db)
    snapshot.assert_match(collection.top_genres(art, db))
