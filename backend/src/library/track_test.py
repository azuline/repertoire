from hashlib import sha256
from pathlib import Path
from sqlite3 import Connection
from unittest import mock

import pytest

from src.enums import ArtistRole, TrackSort
from src.errors import AlreadyExists, DoesNotExist, Duplicate, NotFound
from src.fixtures.factory import Factory

from . import playlist_entry as pentry
from . import track


def test_exists(factory: Factory, db: Connection):
    trk = factory.track(conn=db)
    assert track.exists(trk.id, db)


def test_does_not_exist(db: Connection):
    assert not track.exists(9999999, db)


def test_from_id_success(factory: Factory, db: Connection):
    trk = factory.track(conn=db)
    new_trk = track.from_id(trk.id, db)
    assert new_trk == trk


def test_from_id_failure(db: Connection):
    assert track.from_id(99999, db) is None


def test_from_filepath_success(factory: Factory, db: Connection):
    trk = factory.track(conn=db)
    new_trk = track.from_filepath(trk.filepath, db)
    assert new_trk == trk


def test_from_filepath_failure(db: Connection):
    assert track.from_filepath("lol!", db) is None


def test_from_sha256_success(factory: Factory, db: Connection):
    trk = factory.track(sha256=b"0" * 32, conn=db)
    assert trk.sha256 is not None
    new_trk = track.from_sha256(trk.sha256, db)
    assert new_trk == trk


def test_from_sha256_failure(db: Connection):
    assert track.from_sha256(b"0" * 32, db) is None


def test_search_all(factory: Factory, db: Connection):
    tracks = {factory.track(conn=db) for _ in range(5)}
    out = track.search(conn=db)
    assert set(out) == tracks


def test_search_one(factory: Factory, db: Connection):
    art = factory.artist(name="Baron East", conn=db)
    trk = factory.track(
        title="One Track",
        artists=[{"artist_id": art.id, "role": ArtistRole.MAIN}],
        conn=db,
    )
    out = track.search(search="Baron Track", conn=db)
    assert out == [trk]


def test_search_page(factory: Factory, db: Connection):
    for _ in range(5):
        factory.track(conn=db)

    out1 = track.search(page=1, per_page=2, conn=db)
    out2 = track.search(page=2, per_page=2, conn=db)

    assert len(out1) == 2
    assert len(out2) == 2
    assert out1 != out2


def test_search_sort_recently_added(factory: Factory, db: Connection):
    tracks = [factory.track(conn=db) for _ in range(5)]
    out = track.search(sort=TrackSort.RECENTLY_ADDED, asc=True, conn=db)
    # The order of tracks is already by recently added.
    assert tracks == out


def test_search_sort_title(factory: Factory, db: Connection):
    for _ in range(5):
        factory.track(conn=db)

    out = track.search(sort=TrackSort.TITLE, asc=True, conn=db)
    titles = [t.title for t in out]

    assert titles == sorted(titles, key=str.casefold)


def test_search_sort_year(factory: Factory, db: Connection):
    # Unknown Release has no year.
    factory.track(release_id=1, conn=db)

    # Now create five track with a year.
    for _ in range(5):
        rls = factory.release(release_year=factory.rand_year(), conn=db)
        factory.track(release_id=rls.id, conn=db)

    out = track.search(sort=TrackSort.YEAR, asc=True, conn=db)
    years = [track.release(t, db).release_year for t in out]

    # Assert the track attached to Unknown Release has no year and is last.
    assert years[-1] is None

    not_null_years = years[:-1]
    assert not_null_years == sorted(not_null_years)  # type: ignore


def test_search_sort_year_desc(factory: Factory, db: Connection):
    # Unknown Release has no year.
    factory.track(release_id=1, conn=db)

    # Now create five track with a year.
    for _ in range(5):
        rls = factory.release(release_year=factory.rand_year(), conn=db)
        factory.track(release_id=rls.id, conn=db)

    out = track.search(sort=TrackSort.YEAR, asc=False, conn=db)
    years = [track.release(t, db).release_year for t in out]

    # Assert the track attached to Unknown Release has no year and is last.
    assert years[-1] is None

    not_null_years = years[:-1]
    assert not_null_years == sorted(not_null_years, reverse=True)  # type: ignore


def test_search_sort_random(factory: Factory, db: Connection):
    for _ in range(5):
        factory.track(conn=db)

    # Make sure it returns **something**.
    results = track.search(sort=TrackSort.RANDOM, asc=True, conn=db)
    assert len(results) > 0


def test_search_asc(factory: Factory, db: Connection):
    for _ in range(5):
        factory.track(conn=db)

    asc_true = track.search(sort=TrackSort.TITLE, asc=True, conn=db)
    asc_false = track.search(sort=TrackSort.TITLE, asc=False, conn=db)

    assert asc_true == asc_false[::-1]


def test_search_filter_playlists(factory: Factory, db: Connection):
    tracks = [factory.track(conn=db) for _ in range(5)]

    ply1 = factory.playlist(conn=db)
    ply2 = factory.playlist(conn=db)

    for trk in tracks[:3]:
        pentry.create(ply1.id, trk.id, db)
    for trk in tracks[1:]:
        pentry.create(ply2.id, trk.id, db)

    out = track.search(db, playlist_ids=[ply1.id, ply2.id])
    assert set(out) == set(tracks[1:3])


def test_search_filter_artists(factory: Factory, db: Connection):
    tracks = [factory.track(conn=db) for _ in range(5)]

    art1 = factory.artist(conn=db)
    art2 = factory.artist(conn=db)

    for trk in tracks[:3]:
        track.add_artist(trk, art1.id, ArtistRole.MAIN, db)
    for trk in tracks[1:]:
        track.add_artist(trk, art2.id, ArtistRole.MAIN, db)

    out = track.search(db, artist_ids=[art1.id, art2.id])
    assert set(out) == set(tracks[1:3])


def test_search_filter_year(factory: Factory, db: Connection):
    # Create tracks with years we want.
    releases = [factory.release(release_year=year, conn=db) for year in [2014, 2016]]

    wanted = []
    for rls in releases:
        wanted.extend([factory.track(release_id=rls.id, conn=db) for _ in range(2)])

    # Create tracks with years we don't want (1 No Year and 5 Unwanted Year).
    factory.track(release_id=1, conn=db)

    bad_rls = factory.release(release_year=1700, conn=db)
    for _ in range(5):
        factory.track(release_id=bad_rls.id, conn=db)

    # Fetch and compare.
    tracks = track.search(db, years=[2014, 2016])
    assert set(tracks) == set(wanted)


def test_count_all(factory: Factory, db: Connection):
    for _ in range(5):
        factory.track(conn=db)

    count = track.count(db)
    assert count == 5


def test_count_one(factory: Factory, db: Connection):
    tracks = [factory.track(conn=db) for _ in range(5)]

    count = track.count(db, search=tracks[0].title)
    assert count == 1


def test_create(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    artists = [{"artist_id": art.id, "role": ArtistRole.MAIN}]

    rls = factory.release(conn=db)

    trk = track.create(
        title="new track",
        filepath=Path("/tmp/repertoire-library/09-track.m4a"),
        sha256_initial=b"0" * 32,
        release_id=rls.id,
        artists=artists,
        duration=9001,
        track_number="1",
        disc_number="2",
        conn=db,
    )

    assert trk == track.from_id(trk.id, db)
    trk_arts = track.artists(trk, db)
    assert len(trk_arts) == 1
    assert trk_arts[0]["artist"].id == art.id


def test_create_duplicate_filepath(factory: Factory, db: Connection):
    trk = factory.track(conn=db)

    with pytest.raises(Duplicate):
        track.create(
            title="Airwaves",
            filepath=trk.filepath,
            sha256_initial=b"0" * 32,
            release_id=trk.release_id,
            artists=[],
            duration=9001,
            track_number="1",
            disc_number="1",
            conn=db,
        )


def test_create_bad_release_id(db: Connection):
    with pytest.raises(NotFound) as e:
        track.create(
            title="new track",
            filepath=Path("/tmp/repertoire-library/09-track.m4a"),
            sha256_initial=b"0" * 32,
            release_id=999,
            artists=[],
            duration=9001,
            track_number="1",
            disc_number="2",
            conn=db,
        )

    assert e.value.message is not None
    assert "Release 999" in e.value.message


def test_create_bad_artist_ids(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    rls = factory.release(conn=db)

    with pytest.raises(NotFound) as e:
        track.create(
            title="new track",
            filepath=Path("/tmp/repertoire-library/09-track.m4a"),
            sha256_initial=b"0" * 32,
            release_id=rls.id,
            artists=[
                {"artist_id": art.id, "role": ArtistRole.MAIN},
                {"artist_id": 1000, "role": ArtistRole.MAIN},
                {"artist_id": 1001, "role": ArtistRole.MAIN},
            ],
            duration=9001,
            track_number="1",
            disc_number="2",
            conn=db,
        )

    assert e.value.message is not None
    assert "Artist(s) 1000, 1001" in e.value.message


@mock.patch("src.library.track.calculate_track_full_sha256")
def test_create_same_sha256_precalculated_sha256(
    mock_calculate_full: mock.MagicMock,
    factory: Factory,
    db: Connection,
):
    filepath, sha256sum = _create_dummy_file_with_hash(factory)
    trk = factory.track(
        filepath=filepath,
        sha256_initial=sha256sum,
        sha256=sha256sum,
        conn=db,
    )

    new_filepath, _ = _create_dummy_file_with_hash(factory)
    new_trk = track.create(
        title="new track",
        filepath=new_filepath,
        sha256_initial=sha256sum,
        release_id=trk.release_id,
        artists=[],
        duration=9001,
        track_number="1",
        disc_number="2",
        conn=db,
    )

    assert new_trk.id == trk.id
    assert new_trk.filepath == new_filepath
    assert new_trk == track.from_id(trk.id, db)

    mock_calculate_full.assert_not_called()


def test_create_same_sha256_uncalculated_sha256(factory: Factory, db: Connection):
    filepath, sha256sum = _create_dummy_file_with_hash(factory)
    trk = factory.track(
        filepath=filepath,
        sha256_initial=sha256sum,
        conn=db,
    )

    new_filepath, _ = _create_dummy_file_with_hash(factory)
    new_trk = track.create(
        title="new track",
        filepath=new_filepath,
        sha256_initial=sha256sum,
        release_id=trk.release_id,
        artists=[],
        duration=9001,
        track_number="1",
        disc_number="2",
        conn=db,
    )

    assert new_trk.id == trk.id
    assert new_trk.filepath == new_filepath
    assert new_trk == track.from_id(trk.id, db)


def test_create_same_initial_sha256_different_full(factory: Factory, db: Connection):
    filepath, sha256sum = _create_dummy_file_with_hash(factory)
    trk = factory.track(sha256_initial=sha256sum, conn=db)

    new_trk = track.create(
        title="new track",
        filepath=filepath,
        sha256_initial=sha256sum,
        sha256=b"0" * 32,
        release_id=trk.release_id,
        artists=[],
        duration=9001,
        track_number="1",
        disc_number="2",
        conn=db,
    )

    assert new_trk.id != trk.id


def test_calculate_track_full_sha256(factory: Factory, db: Connection):
    trk = factory.track(conn=db)
    assert trk.sha256 is None

    with trk.filepath.open("wb") as fp:
        fp.write(b"123")

    sha256sum = track.calculate_track_full_sha256(trk, db)

    expected = sha256(b"123").digest()
    assert sha256sum == expected

    trk2 = track.from_id(trk.id, db)
    assert trk2 is not None
    assert trk2.sha256 == expected


def test_calculate_track_full_sha256_duplicate(factory: Factory, db: Connection):
    filepath, sha256sum = _create_dummy_file_with_hash(factory)
    trk1 = factory.track(filepath=filepath, sha256=sha256sum, conn=db)

    new_filepath, _ = _create_dummy_file_with_hash(factory)
    trk2 = factory.track(filepath=new_filepath, conn=db)
    assert trk2.sha256 is None

    with pytest.raises(Duplicate) as e:
        track.calculate_track_full_sha256(trk2, db)
        assert e.value.entity.id == trk1.id

    # Assert that the new track is deleted.
    assert track.from_id(trk2.id, db) is None


def test_update_fields(factory: Factory, db: Connection):
    trk = factory.track(conn=db)
    rls = factory.release(conn=db)

    new_trk = track.update(
        trk,
        conn=db,
        title="New Title",
        release_id=rls.id,
        track_number="X Æ",
        disc_number="A-12",
    )

    assert new_trk.title == "New Title"
    assert new_trk.release_id == rls.id
    assert new_trk.track_number == "X Æ"
    assert new_trk.disc_number == "A-12"
    assert new_trk == track.from_id(trk.id, db)


def test_update_nothing(factory: Factory, db: Connection):
    trk = factory.track(conn=db)
    new_trk = track.update(trk, conn=db)
    assert trk == new_trk


def test_delete(factory: Factory, db: Connection):
    trk = factory.track(conn=db)
    track.delete(trk, db)
    assert track.from_id(trk.id, db) is None


def test_release(factory: Factory, db: Connection):
    trk = factory.track(conn=db)
    assert track.release(trk, db).id == trk.release_id


def test_artists(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    trk = factory.track(
        artists=[{"artist_id": art.id, "role": ArtistRole.MAIN}],
        conn=db,
    )

    artists = track.artists(trk, db)
    assert len(artists) == 1
    assert artists[0]["role"] == ArtistRole.MAIN
    assert artists[0]["artist"].id == art.id


def test_add_artist(factory: Factory, db: Connection):
    trk = factory.track(conn=db)
    art = factory.artist(conn=db)

    track.add_artist(trk, art.id, ArtistRole.MAIN, db)
    artists = track.artists(trk, db)

    assert len(artists) == 2
    assert art.id in [a["artist"].id for a in artists]


def test_add_artist_new_role(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    trk = factory.track(
        artists=[{"artist_id": art.id, "role": ArtistRole.MAIN}],
        conn=db,
    )

    track.add_artist(trk, art.id, ArtistRole.REMIXER, db)
    artists = track.artists(trk, db)

    assert len(artists) == 2
    assert all(art.id == a["artist"].id for a in artists)


def test_add_artist_failure(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    trk = factory.track(
        artists=[{"artist_id": art.id, "role": ArtistRole.MAIN}],
        conn=db,
    )

    with pytest.raises(AlreadyExists):
        track.add_artist(trk, art.id, ArtistRole.MAIN, db)


def test_del_artist(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    trk = factory.track(
        artists=[
            {"artist_id": art.id, "role": ArtistRole.MAIN},
            {"artist_id": art.id, "role": ArtistRole.REMIXER},
        ],
        conn=db,
    )

    track.del_artist(trk, art.id, ArtistRole.REMIXER, db)
    artists = track.artists(trk, db)

    assert len(artists) == 1
    assert artists[0]["role"] == ArtistRole.MAIN


def test_del_artist_failure(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    trk = factory.track(
        artists=[{"artist_id": art.id, "role": ArtistRole.MAIN}],
        conn=db,
    )

    # Wrong ID.
    with pytest.raises(DoesNotExist):
        track.del_artist(trk, art.id + 1, ArtistRole.MAIN, db)

    # Wrong role.
    with pytest.raises(DoesNotExist):
        track.del_artist(trk, art.id, ArtistRole.REMIXER, db)


def _create_dummy_file_with_hash(factory: Factory) -> tuple[Path, bytes]:
    filepath = factory.rand_path(".m4a")
    with filepath.open("wb") as fp:
        fp.write(b"123")

    sha256sum = sha256(b"123").digest()

    return filepath, sha256sum
