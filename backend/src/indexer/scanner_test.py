import random
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from sqlite3 import Connection
from unittest import mock

import pytest

from src.conftest import TEST_DATA_PATH
from src.enums import ArtistRole, CollectionType, ReleaseType
from src.fixtures.factory import Factory
from src.library import artist, collection, release, track

from .scanner import (
    _fetch_or_create_artist,
    _fetch_or_create_release,
    _fix_album_artists,
    _fix_release_types,
    _get_release_type,
    _insert_into_genre_collections,
    _insert_into_inbox_collections,
    _insert_into_label_collection,
    _split_genres,
    catalog_file,
    handle_track_batch,
    scan_directories,
    scan_directory,
)

FAKE_MUSIC = TEST_DATA_PATH / "fake_music"
NEW_ALBUM = FAKE_MUSIC / "New Album"


@mock.patch("src.indexer.scanner.scan_directory")
def test_scan_directories(mock_scan_directory: mock.MagicMock):
    scan_directories()

    mock_scan_directory.assert_called_once()


@mock.patch("src.indexer.scanner.handle_track_batch")
@mock.patch("src.indexer.scanner.catalog_file")
def test_scan_directory(
    mock_catalog_file: mock.MagicMock,
    mock_handle_track_batch: mock.MagicMock,
    factory: Factory,
    db: Connection,
):
    # Add one track to the library; it should be skipped in the scan.
    factory.track(filepath=NEW_ALBUM / "track1.flac", conn=db)
    db.commit()

    scan_directory(FAKE_MUSIC)

    filepaths = {
        str(NEW_ALBUM / "track2.m4a"),
        str(NEW_ALBUM / "track3.mp3"),
        str(NEW_ALBUM / "track4.vorbis.ogg"),
        str(NEW_ALBUM / "track5.opus.ogg"),
    }

    assert filepaths == {c[1][0] for c in mock_catalog_file.mock_calls}


def test_handle_track_batch(factory: Factory, db: Connection):
    filepath1, sum1 = _create_dummy_file_with_hash(factory)
    trk1 = factory.track(filepath=filepath1, sha256_initial=sum1, conn=db)

    filepath2, sum2 = _create_dummy_file_with_hash(factory)
    trk2 = factory.track(filepath=filepath2, sha256_initial=sum2, conn=db)

    trk3 = factory.track(sha256_initial=b"0" * 32, sha256=b"0" * 32, conn=db)

    handle_track_batch([trk1, trk2])

    new1 = track.from_id(trk1.id, db)
    assert new1 is not None
    assert new1.sha256 == sum1

    new2 = track.from_id(trk2.id, db)
    assert new2 is not None
    assert new2.sha256 == sum2

    new3 = track.from_id(trk3.id, db)
    assert new3 is not None
    assert new3.sha256 == trk3.sha256


def _create_dummy_file_with_hash(factory: Factory) -> tuple[Path, bytes]:
    filepath = factory.rand_path(".m4a")
    content = random.randbytes(12)
    with filepath.open("wb") as fp:
        fp.write(content)

    sha256sum = sha256(content).digest()

    return filepath, sha256sum


@mock.patch("src.indexer.scanner._fetch_or_create_release")
def test_catalog_file(
    mock_fetch_or_create_release: mock.MagicMock,
    factory: Factory,
    db: Connection,
    snapshot,
):
    rls = factory.release(conn=db)

    mock_fetch_or_create_release.return_value = mock.Mock(id=rls.id)

    filepath = NEW_ALBUM / "track1.flac"
    trk = catalog_file(str(filepath), db)
    assert trk is not None

    # Because filepath is not a reproducible value (depends on environment),
    # we exclude it from our snapshot and test it separately.
    track_dict = asdict(trk)
    del track_dict["filepath"]

    assert str(trk.filepath).endswith("/track1.flac")
    snapshot.assert_match(track_dict)
    snapshot.assert_match(track.artists(trk, db))


@mock.patch("src.indexer.scanner._fetch_or_create_release")
@mock.patch("src.indexer.scanner.calculate_initial_sha256")
@mock.patch("src.indexer.scanner.TagFile")
def test_catalog_file_null_title(
    tagfile: mock.MagicMock,
    calc_sha: mock.MagicMock,
    mock_fetch_or_create_release: mock.MagicMock,
    factory: Factory,
    db: Connection,
):
    filepath = "/tmp/music.m4a"
    rls = factory.release(conn=db)
    mock_fetch_or_create_release.return_value = mock.Mock(id=rls.id)
    calc_sha.return_value = b"0" * 32
    tagfile.return_value = mock.Mock(
        artist={ArtistRole.MAIN: ["art1"]},
        title=None,
        version=None,
        path=Path(filepath),
        mut=mock.Mock(info=mock.Mock(length=1)),
        track_number="1",
        disc_number="1",
    )

    catalog_file(filepath, db)

    trk = track.from_filepath(filepath, db)
    assert trk is not None
    assert trk.title == "Untitled"


@mock.patch("src.indexer.scanner._fetch_or_create_release")
@mock.patch("src.indexer.scanner.calculate_initial_sha256")
@mock.patch("src.indexer.scanner.TagFile")
def test_catalog_file_duplicate_artist(
    tagfile: mock.MagicMock,
    calc_sha: mock.MagicMock,
    mock_fetch_or_create_release: mock.MagicMock,
    factory: Factory,
    db: Connection,
):
    filepath = "/tmp/music.m4a"
    rls = factory.release(conn=db)
    mock_fetch_or_create_release.return_value = mock.Mock(id=rls.id)
    calc_sha.return_value = b"0" * 32
    tagfile.return_value = mock.Mock(
        artist={ArtistRole.MAIN: ["art1", "art1"]},
        title=None,
        version=None,
        path=Path(filepath),
        mut=mock.Mock(info=mock.Mock(length=1)),
        track_number="1",
        disc_number="1",
    )

    catalog_file(filepath, db)

    trk = track.from_filepath(filepath, db)
    assert trk is not None
    assert len(track.artists(trk, db)) == 1


def test_fetch_or_create_release_unknown(db: Connection):
    assert release.from_id(1, db) == _fetch_or_create_release(mock.Mock(album=None), db)


def test_fetch_or_create_release_fetch(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    assert release.from_id(rls.id, db) == _fetch_or_create_release(
        tf=mock.Mock(
            album=rls.title,
            artist_album=[art["artist"].name for art in release.artists(rls, conn=db)],
        ),
        conn=db,
    )


def test_fetch_or_create_release_no_fetch(db: Connection):
    assert release.from_id(3, db) != _fetch_or_create_release(
        mock.Mock(
            album="Departure",
            artist_album=["Bacchus"],
            date=mock.Mock(year=2020, date="2020-01-01"),
            label=None,
            genre=[],
        ),
        db,
    )


def test_fetch_or_create_release_duplicate_artists(db: Connection):
    rls = _fetch_or_create_release(
        mock.Mock(
            album="aaaaa",
            artist_album=["Bacchus", "Bacchus"],
            date=mock.Mock(year=2020, date="2020-01-01"),
            label=None,
            genre=[],
        ),
        db,
    )

    assert len(release.artists(rls, db)) == 1


def test_fetch_or_create_release_bad_date(db: Connection):
    rls = _fetch_or_create_release(
        mock.Mock(
            album="Departure",
            artist_album=["Bacchus"],
            date=mock.Mock(year=2020, date="0000-01-01"),
            label=None,
            genre=[],
        ),
        db,
    )
    assert rls.release_date is None


def test_get_release_type_unknown():
    assert ReleaseType.UNKNOWN == _get_release_type(mock.Mock(release_type=None))


def test_get_release_type_matching():
    assert ReleaseType.COMPILATION == _get_release_type(
        mock.Mock(release_type="CoMpiLaTiOn")
    )


def test_get_release_type_no_match():
    assert ReleaseType.UNKNOWN == _get_release_type(mock.Mock(release_type="efjaefj"))


def test_fetch_or_create_artist_unknown(db: Connection):
    assert artist.from_id(1, db) == _fetch_or_create_artist("", db)


def test_fetch_or_create_artist_duplicate(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    assert artist.from_id(art.id, db) == _fetch_or_create_artist(art.name, db)


def test_insert_into_inbox_collection(factory: Factory, db: Connection):
    # Create two new inboxes.
    usr1, _ = factory.user(conn=db)
    usr2, _ = factory.user(conn=db)

    rls = factory.release(conn=db)
    _insert_into_inbox_collections(rls, db)

    inbox1 = collection.inbox_of(usr1.id, db)
    inbox2 = collection.inbox_of(usr2.id, db)

    assert rls in collection.releases(inbox1, db)
    assert rls in collection.releases(inbox2, db)


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
    col = collection.from_name_type_user("asdf", CollectionType.LABEL, db)
    assert col in release.collections(rls, db)


def test_insert_into_genre_collections(factory: Factory, db: Connection):
    rls = factory.release(conn=db)

    _insert_into_genre_collections(rls, ["1, 2, 3", "4; 5"], db)
    collections = release.collections(rls, db)
    for genre in ["1", "2", "3", "4", "5"]:
        col = collection.from_name_type_user(genre, CollectionType.GENRE, db)
        assert col in collections


def test_duplicate_genre(factory: Factory, db: Connection):
    rls = factory.release(conn=db)

    _insert_into_genre_collections(rls, ["1, 2, 3", "2/3"], db)
    collections = release.collections(rls, db)
    for genre in ["1", "2", "3"]:
        col = collection.from_name_type_user(genre, CollectionType.GENRE, db)
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
    rls = factory.release(artists=[], conn=db)

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
    assert album_artists[0]["artist"].id == art1.id


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
        factory.track(
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
