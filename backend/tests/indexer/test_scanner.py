from dataclasses import asdict
from datetime import date
from unittest.mock import Mock, call, patch

import pytest

from backend.enums import CollectionType, ReleaseType
from backend.indexer.scanner import (
    _get_release_type,
    _split_genres,
    catalog_file,
    fetch_or_create_artist,
    fetch_or_create_release,
    fix_release_types,
    insert_into_genre_collections,
    insert_into_inbox_collection,
    insert_into_label_collection,
    scan_directories,
    scan_directory,
)
from backend.library import artist, collection, release, track
from backend.tests.conftest import FAKE_DATA

FAKE_MUSIC = FAKE_DATA / "fake_music"
NEW_ALBUM = FAKE_MUSIC / "New Album"


@patch("backend.indexer.scanner.scan_directory")
def test_scan_directories(mock_scan_directory):
    scan_directories()

    mock_scan_directory.assert_has_calls([call("/dir1"), call("/dir2")])


@patch("backend.indexer.scanner.fix_release_types")
@patch("backend.indexer.scanner.catalog_file")
def test_scan_directory(mock_catalog_file, mock_fix_release_types, db):
    # Add one track to the library; it should be skipped in the scan.
    track.create(
        title="a",
        filepath=NEW_ALBUM / "track1.flac",
        sha256=b"0" * 32,
        release=release.from_id(1, db),
        artists=[],
        duration=4,
        track_number="1",
        disc_number="1",
        cursor=db,
    )

    scan_directory(FAKE_MUSIC)

    filepaths = {
        str(NEW_ALBUM / "track2.m4a"),
        str(NEW_ALBUM / "track3.mp3"),
        str(NEW_ALBUM / "track4.vorbis.ogg"),
        str(NEW_ALBUM / "track5.opus.ogg"),
    }

    assert filepaths == {c[1][0] for c in mock_catalog_file.mock_calls}


@patch("backend.indexer.scanner.fetch_or_create_release")
def test_catalog_file(mock_fetch_or_create_release, db, snapshot):
    mock_fetch_or_create_release.return_value = Mock(id=3)
    filepath = NEW_ALBUM / "track1.flac"
    catalog_file(filepath, db)

    trk = track.from_filepath(filepath, db)

    # Because filepath is not a reproducible value (depends on environment), we exclude
    # it from our snapshot and test it separately.
    track_dict = asdict(trk)
    del track_dict["filepath"]

    snapshot.assert_match(track_dict)
    assert str(trk.filepath).endswith("/track1.flac")
    snapshot.assert_match(track.artists(trk, db))


def test_fetch_or_create_release_unknown(db):
    assert release.from_id(1, db) == fetch_or_create_release(Mock(album=None), db)


def test_fetch_or_create_release_fetch(db):
    assert release.from_id(3, db) == fetch_or_create_release(
        Mock(album="Departure", artist_album=["Abakus", "Bacchus"]), db
    )


def test_fetch_or_create_release_no_fetch(db):
    assert release.from_id(3, db) != fetch_or_create_release(
        Mock(
            album="Departure",
            artist_album=["Bacchus"],
            date=Mock(year=2020, date=date(2020, 1, 1)),
            label=None,
            genre=[],
        ),
        db,
    )


def test_get_release_type_unknown():
    assert ReleaseType.UNKNOWN == _get_release_type(Mock(release_type=None))


def test_get_release_type_matching():
    assert ReleaseType.COMPILATION == _get_release_type(
        Mock(release_type="CoMpiLaTiOn")
    )


def test_get_release_type_no_match():
    assert ReleaseType.UNKNOWN == _get_release_type(Mock(release_type="efjaefj"))


def test_fetch_or_create_artist_unknown(db):
    assert artist.from_id(1, db) == fetch_or_create_artist("", db)


def test_fetch_or_create_artist_duplicate(db):
    assert artist.from_id(5, db) == fetch_or_create_artist("Bacchus", db)


def test_insert_into_inbox_collection(db):
    inbox = collection.from_id(1, db)
    rls = release.from_id(1, db)

    assert rls not in collection.releases(inbox, db)

    insert_into_inbox_collection(rls, db)

    assert release.from_id(1, db) in collection.releases(inbox, db)


def test_insert_into_label_collection_nonexistent(db):
    rls = release.from_id(1, db)
    insert_into_label_collection(rls, "", db)

    assert not release.collections(rls, db)


def test_insert_into_label_collection_existing(db):
    rls = release.from_id(1, db)
    insert_into_label_collection(rls, "MyLabel", db)

    col = collection.from_id(20, db)

    assert col in release.collections(rls, db)


def test_insert_into_label_collection_new(db):
    rls = release.from_id(1, db)
    insert_into_label_collection(rls, "asdf", db)

    col = collection.from_name_and_type("asdf", CollectionType.LABEL, db)

    assert col in release.collections(rls, db)


def test_insert_into_genre_collections(db):
    rls = release.from_id(1, db)
    insert_into_genre_collections(rls, ["1, 2, 3", "4; 5"], db)

    collections = release.collections(rls, db)

    for genre in ["1", "2", "3", "4", "5"]:
        col = collection.from_name_and_type(genre, CollectionType.GENRE, db)
        assert col in collections


def test_insert_into_genre_preexisting(db):
    rls = release.from_id(1, db)
    insert_into_genre_collections(rls, ["Folk"], db)

    assert collection.from_id(12, db) in release.collections(rls, db)


def test_insert_into_genre_collections_nothing(db):
    rls = release.from_id(1, db)
    insert_into_genre_collections(rls, "  ", db)

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
def test_fix_release_types(db, num_tracks, release_type):
    rls = release.from_id(1, db)

    for i in range(num_tracks):
        track.create(
            title="a",
            filepath=f"/lol{i}.flac",
            sha256=bytes([i] * 32),
            release=rls,
            artists=[],
            duration=4,
            track_number="1",
            disc_number="1",
            cursor=db,
        )

    fix_release_types(db)

    print(release.from_id(1, db).num_tracks)
    assert release.from_id(1, db).release_type == release_type
