from sqlite3 import Cursor

import pytest

from src.enums import PlaylistType
from src.errors import NotFound
from src.library import playlist
from src.library import playlist_entry as pentry


def test_exists(db: Cursor):
    assert pentry.exists(1, db)


def test_does_not_exist(db: Cursor):
    assert not pentry.exists(9999999, db)


def test_exists_playlist_and_track(db: Cursor):
    assert pentry.exists_playlist_and_track(1, 1, db)


def test_does_not_exist_playlist_and_track(db: Cursor):
    assert not pentry.exists_playlist_and_track(1, 99999, db)


def test_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(pentry.from_id(1, db))


def test_from_id_failure(db: Cursor):
    assert pentry.from_id(90000, db) is None


def test_create_success(db: Cursor):
    ety = pentry.create(1, 1, db)
    assert ety.id == 8
    assert ety.track_id == 1
    assert ety.playlist_id == 1
    assert ety.position == 3


def test_create_invalid_playlist(db: Cursor):
    with pytest.raises(NotFound):
        pentry.create(9999999, 1, db)


def test_create_invalid_track(db: Cursor):
    with pytest.raises(NotFound):
        pentry.create(1, 9999999, db)


def test_insert_first_track(db: Cursor):
    ply = playlist.create("Test", PlaylistType.PLAYLIST, db)
    ety = pentry.create(ply.id, 2, db)
    assert ety.playlist_id == ply.id


def test_delete(db: Cursor):
    ety = pentry.from_id(4, db)

    p3 = pentry.from_id(3, db).position
    p5 = pentry.from_id(5, db).position
    p6 = pentry.from_id(6, db).position

    pentry.delete(ety, db)

    assert pentry.from_id(3, db).position == p3
    assert pentry.from_id(5, db).position == p5 - 1
    assert pentry.from_id(6, db).position == p6 - 1


@pytest.mark.parametrize(
    "position, final_order",
    [
        (1, [5, 3, 4, 6, 7]),
        (2, [3, 5, 4, 6, 7]),
        (3, [3, 4, 5, 6, 7]),
        (4, [3, 4, 6, 5, 7]),
        (5, [3, 4, 6, 7, 5]),
    ],
)
def test_update(position: int, final_order: int, db: Cursor):
    ety = pentry.update(pentry.from_id(5, db), position=position, cursor=db)
    assert ety.position == position

    db.execute(
        """
        SELECT id
        FROM music__playlists_tracks
        WHERE playlist_id = 2
        ORDER BY position ASC
        """
    )

    order = [row["id"] for row in db.fetchall()]
    assert order == final_order


@pytest.mark.parametrize("position", [-1, 0, 6])
def test_update_out_of_bounds(position: int, db: Cursor):
    with pytest.raises(IndexError):
        pentry.update(pentry.from_id(5, db), position=position, cursor=db)


def test_playlist(db: Cursor):
    assert pentry.playlist(pentry.from_id(3, db), db).id == 2


def test_track(db: Cursor):
    assert pentry.track(pentry.from_id(3, db), db).id == 3
