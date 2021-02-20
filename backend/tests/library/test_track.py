from pathlib import Path
from sqlite3 import Connection

import pytest

from src.enums import ArtistRole
from src.errors import AlreadyExists, DoesNotExist, Duplicate, NotFound
from src.library import track


def test_exists(db: Connection):
    assert track.exists(1, db)


def test_does_not_exist(db: Connection):
    assert not track.exists(9999999, db)


def test_from_id_success(db: Connection, snapshot):
    snapshot.assert_match(track.from_id(1, db))


def test_from_id_failure(db: Connection):
    assert track.from_id(90, db) is None


def test_from_filepath_success(db: Connection):
    trk = track.from_filepath(
        "/tmp/repertoire-library/Aaron West and the Roaring Twenties/"
        "2014. We Don’t Have Each Other/01. Our Apartment.m4a",
        db,
    )
    assert trk.id == 1


def test_from_filepath_failure(db: Connection):
    assert track.from_filepath("lol!", db) is None


def test_from_sha256_success(db: Connection):
    sha256 = bytes.fromhex(
        "75ca14432165a9ee87ee63df654ef77f45d009bbe57da0610a453c48c6b26a1a"
    )
    trk = track.from_sha256(sha256, db)
    assert trk.id == 1


def test_from_sha256_failure(db: Connection):
    assert track.from_sha256(b"0" * 32, db) is None


def test_create(db: Connection, snapshot):
    artists = [{"artist_id": 2, "role": ArtistRole.MAIN}]

    trk = track.create(
        title="new track",
        filepath=Path("/tmp/repertoire-library/09-track.m4a"),
        sha256=b"0" * 32,
        release_id=2,
        artists=artists,
        duration=9001,
        track_number="1",
        disc_number="2",
        conn=db,
    )

    assert trk.id == 22
    assert trk == track.from_id(22, db)
    snapshot.assert_match(track.artists(trk, db))


def test_create_same_sha256(db: Connection):
    filepath = Path("/tmp/repertoire-library/09-track.m4a")
    trk = track.create(
        title="new track",
        filepath=filepath,
        sha256=bytes.fromhex(
            "75ca14432165a9ee87ee63df654ef77f45d009bbe57da0610a453c48c6b26a1a"
        ),
        release_id=2,
        artists=[{"artist_id": 2, "role": ArtistRole.MAIN}],
        duration=9001,
        track_number="1",
        disc_number="2",
        conn=db,
    )
    assert trk.id == 1
    assert trk.filepath == filepath
    assert trk == track.from_id(1, db)


def test_create_duplicate_filepath(db: Connection):
    with pytest.raises(Duplicate):
        track.create(
            title="Airwaves",
            filepath=Path(
                "/tmp/repertoire-library/Abakus/2016. Departure/11. Airwaves.m4a"
            ),
            sha256=b"0" * 32,
            release_id=3,
            artists=[{"artist_id": 2, "role": ArtistRole.MAIN}],
            duration=9001,
            track_number="1",
            disc_number="1",
            conn=db,
        )


def test_create_bad_release_id(db: Connection, snapshot):
    with pytest.raises(NotFound) as e:
        track.create(
            title="new track",
            filepath=Path("/tmp/repertoire-library/09-track.m4a"),
            sha256=b"0" * 32,
            release_id=999,
            artists=[{"artist_id": 2, "role": ArtistRole.MAIN}],
            duration=9001,
            track_number="1",
            disc_number="2",
            conn=db,
        )

    assert "Release 999" in e.value.message


def test_create_bad_artist_ids(db: Connection, snapshot):
    with pytest.raises(NotFound) as e:
        track.create(
            title="new track",
            filepath=Path("/tmp/repertoire-library/09-track.m4a"),
            sha256=b"0" * 32,
            release_id=2,
            artists=[
                {"artist_id": 2, "role": ArtistRole.MAIN},
                {"artist_id": 1000, "role": ArtistRole.MAIN},
                {"artist_id": 1001, "role": ArtistRole.MAIN},
            ],
            duration=9001,
            track_number="1",
            disc_number="2",
            conn=db,
        )

    assert "Artist(s) 1000, 1001" in e.value.message


def test_update_fields(db: Connection, snapshot):
    trk = track.update(
        track.from_id(1, db),
        conn=db,
        title="New Title",
        release_id=3,
        track_number="X Æ",
        disc_number="A-12",
    )
    snapshot.assert_match(trk)
    assert trk == track.from_id(1, db)


def test_update_nothing(db: Connection):
    trk = track.from_id(1, db)
    new_trk = track.update(trk, conn=db)
    assert trk == new_trk


def test_artists(db: Connection, snapshot):
    trk = track.from_id(10, db)
    snapshot.assert_match(track.artists(trk, db))


def test_add_artist(db: Connection, snapshot):
    trk = track.from_id(10, db)

    snapshot.assert_match(track.add_artist(trk, 4, ArtistRole.MAIN, db))
    artists = track.artists(trk, db)

    assert len(artists) == 3
    snapshot.assert_match(artists)


def test_add_artist_new_role(db: Connection, snapshot):
    trk = track.from_id(10, db)

    snapshot.assert_match(track.add_artist(trk, 2, ArtistRole.REMIXER, db))
    artists = track.artists(trk, db)

    assert len(artists) == 3
    snapshot.assert_match(artists)


def test_add_artist_failure(db: Connection):
    trk = track.from_id(10, db)

    with pytest.raises(AlreadyExists):
        track.add_artist(trk, 2, ArtistRole.MAIN, db)


def test_del_artist(db: Connection, snapshot):
    trk = track.from_id(10, db)

    snapshot.assert_match(track.del_artist(trk, 3, ArtistRole.COMPOSER, db))
    artists = track.artists(trk, db)

    assert len(artists) == 1
    snapshot.assert_match(artists)


def test_del_artist_failure(db: Connection):
    trk = track.from_id(10, db)

    with pytest.raises(DoesNotExist):
        track.del_artist(trk, 4, ArtistRole.MAIN, db)


def test_del_artist_failure_bad_role(db: Connection):
    trk = track.from_id(10, db)

    with pytest.raises(DoesNotExist):
        track.del_artist(trk, 3, ArtistRole.MAIN, db)
