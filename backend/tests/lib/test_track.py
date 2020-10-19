from sqlite3 import Cursor

from backend.lib import track


def test_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(track.from_id(1, db))


def test_from_id_failure(db: Cursor):
    assert track.from_id(90, db) is None
