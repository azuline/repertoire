from datetime import date
from sqlite3 import Connection

import pytest

from src.enums import CollectionType, ReleaseSort, ReleaseType
from src.errors import AlreadyExists, DoesNotExist, Duplicate
from src.library import release


def test_exists(db: Connection):
    assert release.exists(1, db)


def test_does_not_exist(db: Connection):
    assert not release.exists(9999999, db)


def test_release_from_id_success(db: Connection, snapshot):
    snapshot.assert_match(release.from_id(2, db))


def test_release_from_id_failure(db: Connection):
    assert release.from_id(900000, db) is None


def test_release_tracks(db: Connection, snapshot):
    rls = release.from_id(2, db)
    assert rls is not None
    snapshot.assert_match(release.tracks(rls, db))


def test_release_search_all(db: Connection, snapshot):
    snapshot.assert_match(release.search(conn=db))


def test_release_search_search(db: Connection, snapshot):
    snapshot.assert_match(release.search(search="Aaron", conn=db))


def test_release_search_page(db: Connection, snapshot):
    snapshot.assert_match(release.search(page=1, per_page=2, conn=db))


def test_release_search_page_2(db: Connection, snapshot):
    snapshot.assert_match(release.search(page=2, per_page=2, conn=db))


def test_release_search_sort_recently_added(db: Connection):
    _, releases = release.search(sort=ReleaseSort.RECENTLY_ADDED, asc=True, conn=db)
    added_ons = [rls.added_on for rls in releases]

    assert added_ons == sorted(added_ons)


def test_release_search_sort_title(db: Connection):
    _, releases = release.search(sort=ReleaseSort.TITLE, asc=True, conn=db)
    titles = [rls.title for rls in releases]

    assert titles == sorted(titles)


def test_release_search_sort_year(db: Connection):
    _, releases = release.search(sort=ReleaseSort.YEAR, asc=True, conn=db)
    assert [rls.release_year for rls in releases] == [2014, 2016, None]


def test_release_search_sort_year_desc(db: Connection):
    _, releases = release.search(sort=ReleaseSort.YEAR, asc=False, conn=db)
    assert [rls.release_year for rls in releases] == [2016, 2014, None]


def test_release_search_sort_random(db: Connection):
    # Make sure it returns **something**.
    assert release.search(sort=ReleaseSort.RANDOM, asc=True, conn=db)


def test_release_search_asc(db: Connection, snapshot):
    _, asc_true = release.search(sort=ReleaseSort.TITLE, asc=True, conn=db)
    _, asc_false = release.search(sort=ReleaseSort.TITLE, asc=False, conn=db)

    assert asc_true == asc_false[::-1]


def test_release_search_filter_collections(db: Connection):
    total, inbox = release.search(db, collection_ids=[1])

    assert total == 2
    assert {r.id for r in inbox} == {2, 3}

    total, folk = release.search(db, collection_ids=[3])

    assert total == 1
    assert {r.id for r in folk} == {2}


def test_release_search_filter_artists(db: Connection):
    total, releases = release.search(db, artist_ids=[4, 5])

    assert total == 1
    assert {r.id for r in releases} == {3}


def test_release_search_filter_release_type(db: Connection):
    total, releases = release.search(db, release_types=[ReleaseType.EP])

    assert total == 1
    assert {r.id for r in releases} == {3}


def test_release_search_filter_year(db: Connection):
    total, releases = release.search(db, years=[2014])

    assert total == 1
    assert {r.id for r in releases} == {2}


def test_release_search_filter_rating(db: Connection):
    total, releases = release.search(db, ratings=[6, 4])

    assert total == 1
    assert {r.id for r in releases} == {2}


def test_create(db: Connection):
    rls = release.create(
        title="New Release",
        artist_ids=[2, 4],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        conn=db,
    )

    assert rls.id == 4
    assert rls == release.from_id(4, db)
    assert len(release.artists(rls, db)) == 2


def test_create_same_album_name_no_duplicate_trigger(db: Connection):
    rls = release.create(
        title="Departure",
        artist_ids=[2, 4],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        conn=db,
        allow_duplicate=False,
    )

    assert rls.id == 4
    assert rls == release.from_id(4, db)
    assert len(release.artists(rls, db)) == 2


def test_create_same_album_name_artist_subset_no_duplicate_trigger(db: Connection):
    rls = release.create(
        title="Departure",
        artist_ids=[4],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        conn=db,
        allow_duplicate=False,
    )

    assert rls.id == 4
    assert rls == release.from_id(4, db)
    assert len(release.artists(rls, db)) == 1


def test_create_duplicate_allow(db: Connection):
    rls = release.create(
        title="Departure",
        artist_ids=[4, 5],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        conn=db,
        allow_duplicate=True,
    )

    assert rls.id == 4
    assert rls == release.from_id(4, db)


def test_create_duplicate_disallow(db: Connection):
    with pytest.raises(Duplicate) as e:
        release.create(
            title="Departure",
            artist_ids=[4, 5],
            release_type=ReleaseType.ALBUM,
            release_year=2020,
            conn=db,
            allow_duplicate=False,
        )

    assert e.value.entity.id == 3


def test_update_fields(db: Connection, snapshot):
    rls = release.from_id(2, db)
    assert rls is not None

    rls = release.update(
        rls,
        conn=db,
        title="New Title",
        release_type=ReleaseType.COMPILATION,
        release_year=2040,
        release_date=date(2040, 10, 28),
        rating=1,
    )
    snapshot.assert_match(rls)
    assert rls == release.from_id(2, db)


def test_update_nothing(db: Connection):
    rls = release.from_id(2, db)
    assert rls is not None

    new_rls = release.update(rls, conn=db)
    assert rls == new_rls


def test_reset_rating(db: Connection):
    rls = release.from_id(2, db)
    assert rls is not None

    new_rls = release.update(rls, rating=0, conn=db)
    assert new_rls.rating is None


def test_artists(db: Connection, snapshot):
    rls = release.from_id(2, db)
    assert rls is not None

    snapshot.assert_match(release.artists(rls, db))


def test_add_artist(db: Connection, snapshot):
    rls = release.from_id(2, db)
    assert rls is not None

    snapshot.assert_match(release.add_artist(rls, 3, db))
    snapshot.assert_match(release.artists(rls, db))


def test_add_artist_failure(db: Connection):
    rls = release.from_id(2, db)
    assert rls is not None

    with pytest.raises(AlreadyExists):
        release.add_artist(rls, 2, db)


def test_del_artist(db: Connection, snapshot):
    rls = release.from_id(2, db)
    assert rls is not None

    snapshot.assert_match(release.del_artist(rls, 2, db))
    snapshot.assert_match(release.artists(rls, db))


def test_del_artist_failure(db: Connection):
    rls = release.from_id(2, db)
    assert rls is not None

    with pytest.raises(DoesNotExist):
        release.del_artist(rls, 3, db)


def test_release_collections(db: Connection, snapshot):
    rls = release.from_id(2, db)
    assert rls is not None

    snapshot.assert_match(release.collections(rls, db))


def test_release_collections_filter_type(db: Connection, snapshot):
    rls = release.from_id(2, db)
    assert rls is not None

    collections = release.collections(rls, db, type=CollectionType.SYSTEM)

    assert len(collections) == 1
    snapshot.assert_match(collections)


def test_all_years(db: Connection):
    years = release.all_years(db)
    assert years == [2016, 2014]
