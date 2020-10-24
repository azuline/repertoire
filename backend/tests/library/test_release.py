from datetime import date
from sqlite3 import Cursor

import pytest

from backend.enums import CollectionType, ReleaseSort, ReleaseType
from backend.errors import AlreadyExists, DoesNotExist, Duplicate
from backend.library import artist, release


def test_release_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(release.from_id(2, db))


def test_release_from_id_failure(db: Cursor):
    assert release.from_id(900000, db) is None


def test_release_tracks(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    snapshot.assert_match(release.tracks(rls, db))


def test_release_search_all(db: Cursor, snapshot):
    snapshot.assert_match(release.search(cursor=db))


def test_release_search_search(db: Cursor, snapshot):
    snapshot.assert_match(release.search(search="Aaron", cursor=db))


def test_release_search_page(db: Cursor, snapshot):
    snapshot.assert_match(release.search(page=1, per_page=2, cursor=db))


def test_release_search_page_2(db: Cursor, snapshot):
    snapshot.assert_match(release.search(page=2, per_page=2, cursor=db))


def test_release_search_sort_recently_added(db: Cursor):
    _, releases = release.search(sort=ReleaseSort.RECENTLY_ADDED, asc=True, cursor=db)
    added_ons = [rls.added_on for rls in releases]

    assert added_ons == sorted(added_ons)


def test_release_search_sort_title(db: Cursor):
    _, releases = release.search(sort=ReleaseSort.TITLE, asc=True, cursor=db)
    titles = [rls.title for rls in releases]

    assert titles == sorted(titles)


def test_release_search_sort_year(db: Cursor):
    _, releases = release.search(sort=ReleaseSort.YEAR, asc=True, cursor=db)
    years = [rls.release_year for rls in releases]

    assert years == sorted(years)


def test_release_search_sort_random(db: Cursor):
    # Make sure it returns **something**.
    assert release.search(sort=ReleaseSort.RANDOM, asc=True, cursor=db)


def test_release_search_asc(db: Cursor, snapshot):
    _, asc_true = release.search(sort=ReleaseSort.TITLE, asc=True, cursor=db)
    _, asc_false = release.search(sort=ReleaseSort.TITLE, asc=False, cursor=db)

    assert asc_true == asc_false[::-1]


def test_release_search_filter_collections(db: Cursor, snapshot):
    total, inbox = release.search(db, collections=[1])

    assert total == 2
    snapshot.assert_match(inbox)

    total, folk = release.search(db, collections=[12])

    assert total == 1
    snapshot.assert_match(folk)


def test_release_search_filter_artist(db: Cursor, snapshot):
    total, releases = release.search(db, artists=[4, 5])

    assert total == 1
    snapshot.assert_match(releases)


def test_release_search_filter_release_type(db: Cursor, snapshot):
    total, releases = release.search(db, release_types=[ReleaseType.EP])

    assert total == 1
    snapshot.assert_match(releases)


def test_create(db: Cursor):
    rls = release.create(
        title="New Release",
        artists=[artist.from_id(2, db), artist.from_id(4, db)],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        cursor=db,
    )

    assert rls.id == 4
    assert rls == release.from_id(4, db)
    assert len(release.artists(rls, db)) == 2


def test_create_same_album_name_no_duplicate_trigger(db: Cursor):
    rls = release.create(
        title="Departure",
        artists=[artist.from_id(2, db), artist.from_id(4, db)],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        cursor=db,
        allow_duplicate=False,
    )

    assert rls.id == 4
    assert rls == release.from_id(4, db)
    assert len(release.artists(rls, db)) == 2


def test_create_same_album_name_artist_subset_no_duplicate_trigger(db: Cursor):
    rls = release.create(
        title="Departure",
        artists=[artist.from_id(4, db)],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        cursor=db,
        allow_duplicate=False,
    )

    assert rls.id == 4
    assert rls == release.from_id(4, db)
    assert len(release.artists(rls, db)) == 1


def test_create_duplicate_allow(db: Cursor):
    rls = release.create(
        title="Departure",
        artists=[artist.from_id(4, db), artist.from_id(5, db)],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        cursor=db,
        allow_duplicate=True,
    )

    assert rls.id == 4
    assert rls == release.from_id(4, db)


def test_create_duplicate_disallow(db: Cursor):
    with pytest.raises(Duplicate) as e:
        release.create(
            title="Departure",
            artists=[artist.from_id(4, db), artist.from_id(5, db)],
            release_type=ReleaseType.ALBUM,
            release_year=2020,
            cursor=db,
            allow_duplicate=False,
        )

    assert e.value.entity.id == 3


def test_update_fields(db: Cursor, snapshot):
    rls = release.update(
        release.from_id(2, db),
        cursor=db,
        title="New Title",
        release_type=ReleaseType.COMPILATION,
        release_year=2040,
        release_date=date(2040, 10, 28),
    )
    snapshot.assert_match(rls)
    assert rls == release.from_id(2, db)


def test_update_nothing(db: Cursor):
    rls = release.from_id(2, db)
    new_rls = release.update(rls, cursor=db)
    assert rls == new_rls


def test_artists(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    snapshot.assert_match(release.artists(rls, db))


def test_add_artist(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    art = artist.from_id(3, db)

    release.add_artist(rls, art, db)
    snapshot.assert_match(release.artists(rls, db))


def test_add_artist_failure(db: Cursor):
    rls = release.from_id(2, db)
    art = artist.from_id(2, db)

    with pytest.raises(AlreadyExists):
        release.add_artist(rls, art, db)


def test_del_artist(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    art = artist.from_id(2, db)

    release.del_artist(rls, art, db)
    snapshot.assert_match(release.artists(rls, db))


def test_del_artist_failure(db: Cursor):
    rls = release.from_id(2, db)
    art = artist.from_id(3, db)

    with pytest.raises(DoesNotExist):
        release.del_artist(rls, art, db)


def test_release_collections(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    snapshot.assert_match(release.collections(rls, db))


def test_release_collections_filter_type(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    collections = release.collections(rls, db, type=CollectionType.SYSTEM)

    assert len(collections) == 1
    snapshot.assert_match(collections)
