from sqlite3 import Cursor

from backend.lib import track


def test_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(track.from_id(1, db))


def test_from_id_failure(db: Cursor):
    assert track.from_id(90, db) is None


def test_from_filepath_success(db: Cursor):
    trk = track.from_filepath(
        "/tmp/repertoire-library/Aaron West and the Roaring Twenties/"
        "2014. We Don’t Have Each Other/01. Our Apartment.m4a",
        db,
    )
    assert trk.id == 1


def test_from_filepath_failure(db: Cursor):
    assert track.from_filepath("lol!", db) is None


def test_from_sha256_success(db: Cursor):
    sha256 = bytes.fromhex(
        "75ca14432165a9ee87ee63df654ef77f45d009bbe57da0610a453c48c6b26a1a"
    )
    trk = track.from_sha256(sha256, db)
    assert trk.id == 1


def test_from_sha256_failure(db: Cursor):
    assert track.from_sha256(b"0" * 32, db) is None
