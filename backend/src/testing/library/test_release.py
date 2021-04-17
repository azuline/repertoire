from datetime import date
from sqlite3 import Connection

import pytest

from src.enums import CollectionType, ReleaseSort, ReleaseType
from src.errors import AlreadyExists, DoesNotExist, Duplicate
from src.library import collection, release
from src.testing.factory import Factory


def test_exists(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    assert release.exists(rls.id, db)


def test_does_not_exist(db: Connection):
    assert not release.exists(9999999, db)


def test_release_from_id_success(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    new_rls = release.from_id(2, db)
    assert rls == new_rls


def test_release_from_id_failure(db: Connection):
    assert release.from_id(900000, db) is None


def test_release_tracks(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    tracks = [factory.track(release_id=rls.id, conn=db) for _ in range(5)]
    out = release.tracks(rls, db)
    assert {t.id for t in tracks} == {t.id for t in out}


def test_search_all(factory: Factory, db: Connection):
    releases = {factory.release(conn=db) for _ in range(5)}
    # Exclude the Unknown release for easier comparison.
    out = {rls for rls in release.search(conn=db) if rls.id != 1}
    assert releases == out


def test_search_search(factory: Factory, db: Connection):
    art = factory.artist(name="Aaron West", conn=db)
    rls = factory.release(title="Music for Sleepy Devs", artist_ids=[art.id], conn=db)
    out = release.search(search="Aaron Sleepy", conn=db)
    assert out == [rls]


def test_search_page(factory: Factory, db: Connection):
    for _ in range(5):
        factory.release(conn=db)

    out1 = release.search(page=1, per_page=2, conn=db)
    out2 = release.search(page=2, per_page=2, conn=db)
    assert len(out1) == 2
    assert len(out2) == 2
    assert out1 != out2


def test_search_sort_recently_added(factory: Factory, db: Connection):
    releases = [factory.release(conn=db) for _ in range(5)]
    out = release.search(sort=ReleaseSort.RECENTLY_ADDED, asc=True, conn=db)
    # Don't include Unknown Release in the comparison.
    assert releases == [r for r in out if r.id != 1]


def test_search_sort_title(factory: Factory, db: Connection):
    for _ in range(5):
        factory.release(conn=db)

    out = release.search(sort=ReleaseSort.TITLE, asc=True, conn=db)
    titles = [rls.title for rls in out]

    assert titles == sorted(titles, key=str.casefold)


def test_search_sort_year(factory: Factory, db: Connection):
    for _ in range(5):
        factory.release(release_year=factory.rand_year(), conn=db)

    releases = release.search(sort=ReleaseSort.YEAR, asc=True, conn=db)

    # This is the Unknown Release (with a null year). Should be sorted last.
    assert releases[-1].release_year is None

    not_null_years = [rls.release_year for rls in releases[:-1]]
    assert None not in not_null_years
    assert not_null_years == sorted(not_null_years)  # type: ignore


def test_search_sort_year_desc(factory: Factory, db: Connection):
    for _ in range(5):
        factory.release(release_year=factory.rand_year(), conn=db)

    releases = release.search(sort=ReleaseSort.YEAR, asc=False, conn=db)
    # This is the Unknown Release (with a null year). Should be sorted last.
    assert releases[-1].release_year is None

    not_null_years = [rls.release_year for rls in releases[:-1]]
    assert None not in not_null_years
    assert not_null_years == sorted(not_null_years, reverse=True)  # type: ignore


def test_search_sort_random(factory: Factory, db: Connection):
    for _ in range(5):
        factory.release(conn=db)

    # Make sure it returns **something**.
    results = release.search(sort=ReleaseSort.RANDOM, asc=True, conn=db)
    assert len(results) > 0


def test_search_asc(factory: Factory, db: Connection):
    for _ in range(5):
        factory.release(conn=db)

    asc_true = release.search(sort=ReleaseSort.TITLE, asc=True, conn=db)
    asc_false = release.search(sort=ReleaseSort.TITLE, asc=False, conn=db)

    assert asc_true == asc_false[::-1]


def test_search_filter_collections(factory: Factory, db: Connection):
    releases = [factory.release(conn=db) for _ in range(5)]

    col1 = factory.collection(conn=db)
    col2 = factory.collection(conn=db)

    for rls in releases[:3]:
        collection.add_release(col1, rls.id, db)
    for rls in releases[1:]:
        collection.add_release(col2, rls.id, db)

    out = release.search(db, collection_ids=[col1.id, col2.id])
    assert set(releases[1:3]) == set(out)


def test_search_filter_artists(factory: Factory, db: Connection):
    art1 = factory.artist(conn=db)
    art2 = factory.artist(conn=db)

    # Create some releases only on one artist.
    factory.release(artist_ids=[art1.id], conn=db)
    factory.release(artist_ids=[art2.id], conn=db)

    # Now create some for both; these are what we want to see in search results.
    releases = [
        factory.release(artist_ids=[art1.id, art2.id], conn=db) for _ in range(5)
    ]

    out = release.search(db, artist_ids=[art1.id, art2.id])
    assert set(releases) == set(out)


def test_search_filter_release_type(factory: Factory, db: Connection):
    # Create a release that we don't want to show up.
    factory.release(release_type=ReleaseType.ALBUM, conn=db)

    # Create the releases we want to get.
    releases = [factory.release(release_type=ReleaseType.EP, conn=db) for _ in range(5)]

    out = release.search(db, release_types=[ReleaseType.EP])
    assert set(releases) == set(out)


def test_search_filter_year(factory: Factory, db: Connection):
    factory.release(release_year=None, conn=db)
    factory.release(release_year=2000, conn=db)
    rls = factory.release(release_year=2014, conn=db)

    releases = release.search(db, years=[2014])
    assert releases == [rls]


def test_search_filter_rating(factory: Factory, db: Connection):
    factory.release(rating=2, conn=db)
    factory.release(rating=None, conn=db)

    rls1 = factory.release(rating=4, conn=db)
    rls2 = factory.release(rating=6, conn=db)

    releases = release.search(db, ratings=[6, 4])
    assert {rls1, rls2} == set(releases)


def test_count_all(factory: Factory, db: Connection):
    for _ in range(5):
        factory.release(conn=db)

    count = release.count(db)
    # One extra for Unknown Release.
    assert count == 5 + 1


def test_count_one(factory: Factory, db: Connection):
    factory.release(title="We Will Always Have Seventy Children", conn=db)
    for _ in range(5):
        factory.release(conn=db)

    count = release.count(db, search="Have Seventy Will Children")
    assert count == 1


def test_create(factory: Factory, db: Connection):
    art = factory.artist(conn=db)

    rls = release.create(
        title="New Release",
        artist_ids=[art.id],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        conn=db,
    )

    assert rls == release.from_id(rls.id, db)

    artists = release.artists(rls, db)
    assert len(artists) == 1
    assert artists[0].id == art.id


def test_create_same_album_name_no_duplicate_trigger(factory: Factory, db: Connection):
    rls1 = factory.release(conn=db)
    new_art = factory.artist(conn=db)

    new_rls = release.create(
        title=rls1.title,
        artist_ids=[new_art.id],
        release_type=rls1.release_type,
        release_year=rls1.release_year,
        conn=db,
        allow_duplicate=False,
    )

    assert rls1.id != new_rls.id


def test_create_same_album_name_artist_subset_no_duplicate_trigger(
    factory: Factory,
    db: Connection,
):
    art1 = factory.artist(conn=db)
    art2 = factory.artist(conn=db)
    rls1 = factory.release(artist_ids=[art1.id, art2.id], conn=db)

    new_rls = release.create(
        title=rls1.title,
        artist_ids=[art1.id],
        release_type=rls1.release_type,
        release_year=rls1.release_year,
        conn=db,
        allow_duplicate=False,
    )

    assert rls1.id != new_rls.id


def test_create_duplicate_allow(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    rls = factory.release(artist_ids=[art.id], conn=db)

    new_rls = release.create(
        title=rls.title,
        artist_ids=[art.id],
        release_type=rls.release_type,
        release_year=rls.release_year,
        conn=db,
        allow_duplicate=True,
    )

    assert rls.id != new_rls.id


def test_create_duplicate_disallow(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    rls = factory.release(artist_ids=[art.id], conn=db)

    with pytest.raises(Duplicate) as e:
        release.create(
            title=rls.title,
            artist_ids=[art.id],
            release_type=rls.release_type,
            release_year=rls.release_year,
            conn=db,
            allow_duplicate=False,
        )

    assert e.value.entity == rls


def test_update_fields(factory: Factory, db: Connection):
    rls = factory.release(conn=db)

    new_rls = release.update(
        rls,
        title="New Title",
        release_type=ReleaseType.COMPILATION,
        release_year=2040,
        release_date=date(2040, 10, 28),
        rating=1,
        conn=db,
    )

    assert new_rls.title == "New Title"
    assert new_rls.release_type == ReleaseType.COMPILATION
    assert new_rls.release_year == 2040
    assert new_rls.release_date == date(2040, 10, 28)
    assert new_rls.rating == 1
    assert new_rls == release.from_id(rls.id, db)


def test_update_nothing(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    new_rls = release.update(rls, conn=db)
    assert rls == new_rls


def test_reset_rating(factory: Factory, db: Connection):
    rls = factory.release(rating=8, conn=db)
    new_rls = release.update(rls, rating=0, conn=db)
    assert new_rls.rating is None


def test_artists(factory: Factory, db: Connection):
    art1 = factory.artist(conn=db)
    art2 = factory.artist(conn=db)
    rls = factory.release(artist_ids=[art1.id, art2.id], conn=db)

    artists = release.artists(rls, db)
    assert {a.id for a in artists} == {art1.id, art2.id}


def test_add_artist(factory: Factory, db: Connection):
    rls = factory.release(artist_ids=[], conn=db)
    art = factory.artist(conn=db)

    release.add_artist(rls, art.id, db)
    artists = release.artists(rls, db)

    assert len(artists) == 1
    assert artists[0].id == art.id


def test_add_artist_failure(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    rls = factory.release(artist_ids=[art.id], conn=db)

    with pytest.raises(AlreadyExists):
        release.add_artist(rls, art.id, db)


def test_del_artist(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    rls = factory.release(artist_ids=[art.id], conn=db)
    new_rls = release.del_artist(rls, 2, db)

    assert rls == new_rls
    assert release.artists(rls, db) == []


def test_del_artist_failure(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    art = factory.artist(conn=db)

    with pytest.raises(DoesNotExist):
        release.del_artist(rls, art.id, db)


def test_release_collections(factory: Factory, db: Connection):
    rls = factory.release(conn=db)
    cols = [factory.collection(conn=db) for _ in range(5)]

    for col in cols:
        collection.add_release(col, rls.id, db)

    out = release.collections(rls, db)
    assert {c.id for c in cols} == {c.id for c in out}


def test_release_collections_filter_type(factory: Factory, db: Connection):
    rls = factory.release(conn=db)

    cols = [factory.collection(type=CollectionType.SYSTEM, conn=db) for _ in range(2)]
    for _ in range(3):
        cols.append(factory.collection(type=CollectionType.COLLAGE, conn=db))

    for col in cols:
        collection.add_release(col, rls.id, db)

    out = release.collections(rls, db, type=CollectionType.SYSTEM)

    assert len(out) == 2
    assert {c.id for c in out} == {c.id for c in cols[:2]}


def test_all_years(factory: Factory, db: Connection):
    factory.release(release_year=2016, conn=db)
    factory.release(release_year=2014, conn=db)
    factory.release(release_year=None, conn=db)

    years = release.all_years(db)
    assert set(years) == {2016, 2014}
