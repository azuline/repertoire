from sqlite3 import Cursor

from backend.enums import CollectionType
from backend.lib import collection


def test_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(collection.from_id(16, db))


def test_from_id_failure(db: Cursor):
    assert collection.from_id(90000, db) is None


def test_all(db: Cursor, snapshot):
    collections = collection.all(db)
    snapshot.assert_match(collections)


def test_all_filter_type(db: Cursor, snapshot):
    collections = collection.all(db, type=CollectionType.SYSTEM)
    snapshot.assert_match(collections)


def test_releases(db: Cursor, snapshot):
    art = collection.from_id(16, db)
    snapshot.assert_match(collection.releases(art, db))


def test_top_genres(db: Cursor, snapshot):
    art = collection.from_id(16, db)
    snapshot.assert_match(collection.top_genres(art, db))
