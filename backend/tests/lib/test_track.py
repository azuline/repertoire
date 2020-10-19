from pathlib import Path
from sqlite3 import Cursor

import pytest

from backend.enums import ArtistRole
from backend.errors import Duplicate
from backend.lib import artist, release, track


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


def test_create(db: Cursor):
    trk = track.create(
        title="new track",
        filepath=Path("/tmp/repertoire-library/09-track.m4a"),
        sha256=b"0" * 32,
        release=release.from_id(2, db),
        artists=[{"artist": artist.from_id(2, db), "role": ArtistRole.MAIN}],
        duration=9001,
        track_number="1",
        disc_number="2",
        cursor=db,
    )
    assert trk.id == 22
    assert trk == track.from_id(22, db)


def test_create_same_sha256(db: Cursor):
    filepath = Path("/tmp/repertoire-library/09-track.m4a")
    trk = track.create(
        title="new track",
        filepath=filepath,
        sha256=bytes.fromhex(
            "75ca14432165a9ee87ee63df654ef77f45d009bbe57da0610a453c48c6b26a1a"
        ),
        release=release.from_id(2, db),
        artists=[{"artist": artist.from_id(2, db), "role": ArtistRole.MAIN}],
        duration=9001,
        track_number="1",
        disc_number="2",
        cursor=db,
    )
    assert trk.id == 1
    assert trk.filepath == filepath
    assert trk == track.from_id(1, db)


def test_create_duplicate_filepath(db: Cursor):
    with pytest.raises(Duplicate):
        track.create(
            title="Airwaves",
            filepath=Path(
                "/tmp/repertoire-library/Abakus/2016. Departure/11. Airwaves.m4a"
            ),
            sha256=b"0" * 32,
            release=release.from_id(3, db),
            artists=[{"artist": artist.from_id(2, db), "role": ArtistRole.MAIN}],
            duration=9001,
            track_number="1",
            disc_number="1",
            cursor=db,
        )
