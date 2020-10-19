from sqlite3 import Cursor

from backend.lib import artist


def test_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(artist.from_id(2, db))


def test_from_id_failure(db: Cursor):
    assert artist.from_id(90000, db) is None


def test_all(db: Cursor, snapshot):
    artists = artist.all(db)
    assert all(art.num_releases for art in artists)
    snapshot.assert_match(artists)


def test_releases(db: Cursor, snapshot):
    art = artist.from_id(2, db)
    snapshot.assert_match(artist.releases(art, db))


def test_top_genres(db: Cursor, snapshot):
    art = artist.from_id(2, db)
    snapshot.assert_match(artist.top_genres(art, db))
