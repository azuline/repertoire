from dataclasses import asdict
from pathlib import Path
from sqlite3 import Connection
from unittest.mock import Mock, call, patch

import pytest

from src.enums import ArtistRole, CollectionType, ReleaseType
from src.indexer.scanner import (
    _fetch_or_create_artist,
    _fetch_or_create_release,
    _fix_album_artists,
    _fix_release_types,
    _get_release_type,
    _insert_into_genre_collections,
    _insert_into_inbox_collection,
    _insert_into_label_collection,
    _split_genres,
    catalog_file,
    scan_directories,
    scan_directory,
)
from src.library import artist, collection, release, track
from src.fixtures.conftest import SEED_DATA
from src.fixtures.factory import Factory

FAKE_MUSIC = SEED_DATA / "fake_music"
NEW_ALBUM = FAKE_MUSIC / "New Album"


@patch("src.indexer.scanner.scan_directory")
def test_scan_directories(mock_scan_directory, seed_data):
    scan_directories()

    mock_scan_directory.assert_has_calls([call("/dir1"), call("/dir2")])


@patch("src.indexer.scanner._fix_release_types")
@patch("src.indexer.scanner.catalog_file")
def test_scan_directory(
    mock_catalog_file,
    mock_fix_release_types,
    factory: Factory,
    db: Connection,
):
    # Add one track to the library; it should be skipped in the scan.
    factory.track(filepath=NEW_ALBUM / "track1.flac", conn=db)
    db.commit()

    scan_directory(str(FAKE_MUSIC))

    filepaths = {
        str(NEW_ALBUM / "track2.m4a"),
        str(NEW_ALBUM / "track3.mp3"),
        str(NEW_ALBUM / "track4.vorbis.ogg"),
        str(NEW_ALBUM / "track5.opus.ogg"),
    }

    assert filepaths == {c[1][0] for c in mock_catalog_file.mock_calls}


@patch("src.indexer.scanner._fetch_or_create_release")
def test_catalog_file(
    mock_fetch_or_create_release,
    factory: Factory,
    db: Connection,
    snapshot,
):
    rls = factory.release(conn=db)

    mock_fetch_or_create_release.return_value = Mock(id=rls.id)

    filepath = NEW_ALBUM / "track1.flac"
    catalog_file(str(filepath), db)

    trk = track.from_filepath(filepath, db)
    assert trk is not None

    # Because filepath is not a reproducible value (depends on environment), we exclude
    # it from our snapshot and test it separately.
    track_dict = asdict(trk)
    del track_dict["filepath"]

    assert str(trk.filepath).endswith("/track1.flac")
    snapshot.assert_match(track_dict)
    snapshot.assert_match(track.artists(trk, db))


@patch("src.indexer.scanner._fetch_or_create_release")
@patch("src.indexer.scanner.calculate_sha_256")
@patch("src.indexer.scanner.TagFile")
def test_catalog_file_null_title(
    tagfile,
    calc_sha,
    mock_fetch_or_create_release,
    factory: Factory,
    db: Connection,
    snapshot,
):
    filepath = "/tmp/music.m4a"
    rls = factory.release(conn=db)
    mock_fetch_or_create_release.return_value = Mock(id=rls.id)
    calc_sha.return_value = b"0" * 32
    tagfile.return_value = Mock(
        artist={ArtistRole.MAIN: ["art1"]},
        title=None,
        version=None,
        path=Path(filepath),
        mut=Mock(info=Mock(length=1)),
        track_number="1",
        disc_number="1",
    )

    catalog_file(filepath, db)

    trk = track.from_filepath(filepath, db)
    assert trk is not None
    assert trk.title == "Untitled"


@patch("src.indexer.scanner._fetch_or_create_release")
@patch("src.indexer.scanner.calculate_sha_256")
@patch("src.indexer.scanner.TagFile")
def test_catalog_file_duplicate_artist(
    tagfile,
    calc_sha,
    mock_fetch_or_create_release,
    factory: Factory,
    db: Connection,
    snapshot,
):
    filepath = "/tmp/music.m4a"
    rls = factory.release(conn=db)
    mock_fetch_or_create_release.return_value = Mock(id=rls.id)
    calc_sha.return_value = b"0" * 32
    tagfile.return_value = Mock(
        artist={ArtistRole.MAIN: ["art1", "art1"]},
        title=None,
        version=None,
        path=Path(filepath),
        mut=Mock(info=Mock(length=1)),
        track_number="1",
        disc_number="1",
    )

    catalog_file(filepath, db)

    trk = track.from_filepath(filepath, db)
    assert trk is not None
    assert len(track.artists(trk, db)) == 1


def test_fetch_or_create_release_unknown(db: Connection):
    assert release.from_id(1, db) == _fetch_or_create_release(Mock(album=None), db)


def test_fetch_or_create_release_fetch(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    assert release.from_id(rls.id, db) == _fetch_or_create_release(
        tf=Mock(
            album=rls.title,
            artist_album=[art.name for art in release.artists(rls, conn=db)],
        ),
        conn=db,
    )


def test_fetch_or_create_release_no_fetch(db: Connection):
    assert release.from_id(3, db) != _fetch_or_create_release(
        Mock(
            album="Departure",
            artist_album=["Bacchus"],
            date=Mock(year=2020, date="2020-01-01"),
            label=None,
            genre=[],
        ),
        db,
    )


def test_fetch_or_create_release_duplicate_artists(db: Connection):
    rls = _fetch_or_create_release(
        Mock(
            album="aaaaa",
            artist_album=["Bacchus", "Bacchus"],
            date=Mock(year=2020, date="2020-01-01"),
            label=None,
            genre=[],
        ),
        db,
    )

    assert len(release.artists(rls, db)) == 1


def test_fetch_or_create_release_bad_date(db: Connection):
    rls = _fetch_or_create_release(
        Mock(
            album="Departure",
            artist_album=["Bacchus"],
            date=Mock(year=2020, date="0000-01-01"),
            label=None,
            genre=[],
        ),
        db,
    )
    assert rls.release_date is None


def test_get_release_type_unknown():
    assert ReleaseType.UNKNOWN == _get_release_type(Mock(release_type=None))


def test_get_release_type_matching():
    assert ReleaseType.COMPILATION == _get_release_type(
        Mock(release_type="CoMpiLaTiOn")
    )


def test_get_release_type_no_match():
    assert ReleaseType.UNKNOWN == _get_release_type(Mock(release_type="efjaefj"))


def test_fetch_or_create_artist_unknown(db: Connection):
    assert artist.from_id(1, db) == _fetch_or_create_artist("", db)


def test_fetch_or_create_artist_duplicate(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    assert artist.from_id(art.id, db) == _fetch_or_create_artist(art.name, db)


def test_insert_into_inbox_collection(factory: Factory, db: Connection):
    inbox = collection.from_id(1, db)
    assert inbox is not None

    rls = factory.release(conn=db)
    assert rls not in collection.releases(inbox, db)

    _insert_into_inbox_collection(rls, db)
    assert release.from_id(rls.id, db) in collection.releases(inbox, db)


def test_insert_into_label_collection_nonexistent(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    _insert_into_label_collection(rls, "", db)
    assert not release.collections(rls, db)


def test_insert_into_label_collection_existing(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    col = factory.collection(type=CollectionType.LABEL, conn=db)
    _insert_into_label_collection(rls, col.name, db)
    assert collection.from_id(col.id, db) in release.collections(rls, db)


def test_insert_into_label_collection_new(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    _insert_into_label_collection(rls, "asdf", db)
    col = collection.from_name_and_type("asdf", CollectionType.LABEL, db)
    assert col in release.collections(rls, db)


def test_insert_into_genre_collections(factory: Factory, db: Connection):
    rls = factory.release(conn=db)

    _insert_into_genre_collections(rls, ["1, 2, 3", "4; 5"], db)
    collections = release.collections(rls, db)
    for genre in ["1", "2", "3", "4", "5"]:
        col = collection.from_name_and_type(genre, CollectionType.GENRE, db)
        assert col in collections


def test_duplicate_genre(factory: Factory, db: Connection):
    rls = factory.release(conn=db)

    _insert_into_genre_collections(rls, ["1, 2, 3", "2/3"], db)
    collections = release.collections(rls, db)
    for genre in ["1", "2", "3"]:
        col = collection.from_name_and_type(genre, CollectionType.GENRE, db)
        assert col in collections


def test_insert_into_genre_preexisting(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    col = factory.collection(type=CollectionType.GENRE, conn=db)

    _insert_into_genre_collections(rls, [col.name], db)
    assert collection.from_id(col.id, db) in release.collections(rls, db)


def test_insert_into_genre_collections_nothing(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    _insert_into_genre_collections(rls, ["  "], db)
    assert not release.collections(rls, db)


@pytest.mark.parametrize(
    "string, genres",
    [
        ("a \\\\b", ["a", "b"]),
        ("a/b", ["a", "b"]),
        ("a,b", ["a", "b"]),
        ("a;b", ["a", "b"]),
    ],
)
def test_split_genres(string, genres):
    assert genres == _split_genres(string)


def test_fix_album_artists_track_artists(factory: Factory, db: Connection):
    rls = factory.release(artist_ids=[], conn=db)

    art1 = factory.artist(conn=db)
    art2 = factory.artist(conn=db)

    factory.track(
        release_id=rls.id,
        artists=[
            {"artist_id": art1.id, "role": ArtistRole.MAIN},
            {"artist_id": art2.id, "role": ArtistRole.FEATURE},
        ],
        conn=db,
    )

    _fix_album_artists(db)

    rls = release.from_id(rls.id, db)  # type: ignore
    assert rls is not None
    album_artists = release.artists(rls, db)
    assert len(album_artists) == 1
    assert album_artists[0].id == art1.id


@pytest.mark.parametrize(
    "num_tracks, release_type",
    [
        (1, ReleaseType.SINGLE),
        (2, ReleaseType.SINGLE),
        (3, ReleaseType.EP),
        (4, ReleaseType.EP),
        (5, ReleaseType.EP),
        (6, ReleaseType.ALBUM),
        (7, ReleaseType.ALBUM),
        (8, ReleaseType.ALBUM),
        (9, ReleaseType.ALBUM),
    ],
)
def test_fix_release_types(factory: Factory, db: Connection, num_tracks, release_type):
    rls = factory.release(release_type=ReleaseType.UNKNOWN, conn=db)

    for i in range(num_tracks):
        track.create(
            title="a",
            filepath=Path(f"/lol{i}.flac"),
            sha256=bytes([i] * 32),
            release_id=rls.id,
            artists=[],
            duration=4,
            track_number="1",
            disc_number="1",
            conn=db,
        )

    _fix_release_types(db)

    new_rls = release.from_id(rls.id, db)
    assert new_rls is not None
    assert new_rls.release_type == release_type
