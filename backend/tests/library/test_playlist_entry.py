from sqlite3 import Connection

import pytest

from src.enums import PlaylistType
from src.errors import NotFound
from src.library import playlist
from src.library import playlist_entry as pentry


def test_exists(db: Connection):
    assert pentry.exists(1, db)


def test_does_not_exist(db: Connection):
    assert not pentry.exists(9999999, db)


def test_exists_playlist_and_track(db: Connection):
    assert pentry.exists_playlist_and_track(1, 1, db)


def test_does_not_exist_playlist_and_track(db: Connection):
    assert not pentry.exists_playlist_and_track(1, 99999, db)


def test_from_id_success(db: Connection, snapshot):
    snapshot.assert_match(pentry.from_id(1, db))


def test_from_id_failure(db: Connection):
    assert pentry.from_id(90000, db) is None


def test_from_playlist_and_track_success(db: Connection, snapshot):
    snapshot.assert_match(pentry.from_playlist_and_track(1, 1, db))


def test_from_playlist_and_track_failure(db: Connection):
    assert pentry.from_playlist_and_track(1, 99999, db) == []


def test_create_success(db: Connection):
    ety = pentry.create(1, 1, db)
    assert ety.id == 9
    assert ety.track_id == 1
    assert ety.playlist_id == 1
    assert ety.position == 3


def test_create_invalid_playlist(db: Connection):
    with pytest.raises(NotFound):
        pentry.create(9999999, 1, db)


def test_create_invalid_track(db: Connection):
    with pytest.raises(NotFound):
        pentry.create(1, 9999999, db)


def test_insert_first_track(db: Connection):
    ply = playlist.create("Test", PlaylistType.PLAYLIST, db)
    ety = pentry.create(ply.id, 2, db)
    assert ety.playlist_id == ply.id


def test_delete(db: Connection):
    ety = pentry.from_id(4, db)
    assert ety is not None

    p3 = pentry.from_id(3, db).position  # type: ignore
    p5 = pentry.from_id(5, db).position  # type: ignore
    p6 = pentry.from_id(6, db).position  # type: ignore

    pentry.delete(ety, db)

    assert pentry.from_id(3, db).position == p3  # type: ignore
    assert pentry.from_id(5, db).position == p5 - 1  # type: ignore
    assert pentry.from_id(6, db).position == p6 - 1  # type: ignore


@pytest.mark.parametrize(
    "position, final_order",
    [
        (1, [5, 3, 4, 6, 7, 8]),
        (2, [3, 5, 4, 6, 7, 8]),
        (3, [3, 4, 5, 6, 7, 8]),
        (4, [3, 4, 6, 5, 7, 8]),
        (5, [3, 4, 6, 7, 5, 8]),
    ],
)
def test_update(position: int, final_order: int, db: Connection):
    ety = pentry.from_id(5, db)
    assert ety is not None

    ety = pentry.update(ety, position=position, conn=db)
    assert ety.position == position

    cursor = db.execute(
        """
        SELECT id
        FROM music__playlists_tracks
        WHERE playlist_id = 2
        ORDER BY position ASC
        """
    )

    order = [row["id"] for row in cursor.fetchall()]
    assert order == final_order


@pytest.mark.parametrize("position", [-1, 0, 7])
def test_update_out_of_bounds(position: int, db: Connection):
    ety = pentry.from_id(5, db)
    assert ety is not None

    with pytest.raises(IndexError):
        pentry.update(ety, position=position, conn=db)


def test_playlist(db: Connection):
    ety = pentry.from_id(3, db)
    assert ety is not None

    assert pentry.playlist(ety, db).id == 2


def test_track(db: Connection):
    ety = pentry.from_id(3, db)
    assert ety is not None

    assert pentry.track(ety, db).id == 3
