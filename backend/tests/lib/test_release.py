from sqlite3 import Cursor

from backend.lib import release


def test_release_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(release.from_id(2, db))


def test_release_from_id_failure(db: Cursor):
    assert release.from_id(900000, db) is None


def test_release_tracks(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    snapshot.assert_match(release.tracks(rls, db))


def test_release_artists(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    snapshot.assert_match(release.artists(rls, db))


def test_release_collections(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    snapshot.assert_match(release.collections(rls, db))
