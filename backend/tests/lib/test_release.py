from sqlite3 import Cursor

import pytest

from backend.enums import ReleaseSort, ReleaseType
from backend.errors import Duplicate
from backend.lib import artist, release


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


def test_create_same_album_name(db: Cursor):
    rls = release.create(
        title="Departure",
        artists=[artist.from_id(2, db), artist.from_id(4, db)],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        cursor=db,
    )
    assert rls.id == 4
    assert rls == release.from_id(4, db)
    assert len(release.artists(rls, db)) == 2


def test_create_duplicate(db: Cursor):
    with pytest.raises(Duplicate):
        release.create(
            title="Departure",
            artists=[artist.from_id(4, db)],
            release_type=ReleaseType.ALBUM,
            release_year=2020,
            cursor=db,
        )


def test_release_artists(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    snapshot.assert_match(release.artists(rls, db))


def test_release_collections(db: Cursor, snapshot):
    rls = release.from_id(2, db)
    snapshot.assert_match(release.collections(rls, db))
