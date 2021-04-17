from sqlite3 import Connection

import pytest

from src.errors import NotFound
from src.fixtures.factory import Factory

from . import playlist
from . import playlist_entry as pentry


def test_exists(factory: Factory, db: Connection):
    ety = factory.playlist_entry(conn=db)
    assert pentry.exists(ety.id, db)


def test_does_not_exist(db: Connection):
    assert not pentry.exists(9999999, db)


def test_exists_playlist_and_track(factory: Factory, db: Connection):
    ety = factory.playlist_entry(conn=db)
    assert pentry.exists_playlist_and_track(ety.playlist_id, ety.track_id, db)


def test_does_not_exist_playlist_and_track(db: Connection):
    assert not pentry.exists_playlist_and_track(1, 99999, db)


def test_from_id_success(factory: Factory, db: Connection):
    ety = factory.playlist_entry(conn=db)
    new_ety = pentry.from_id(1, db)
    assert new_ety == ety


def test_from_id_failure(db: Connection):
    assert pentry.from_id(90000, db) is None


def test_from_playlist_and_track_success(factory: Factory, db: Connection):
    ety = factory.playlist_entry(conn=db)
    new_ety = pentry.from_playlist_and_track(ety.playlist_id, ety.track_id, db)
    assert new_ety == [ety]


def test_from_playlist_and_track_failure(db: Connection):
    assert pentry.from_playlist_and_track(1, 99999, db) == []


def test_create_success(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    trk = factory.track(conn=db)
    ety = pentry.create(ply.id, trk.id, db)
    assert ety.track_id == trk.id
    assert ety.playlist_id == ply.id
    assert ety.position == 1


def test_create_invalid_playlist(db: Connection):
    with pytest.raises(NotFound):
        pentry.create(9999999, 1, db)


def test_create_invalid_track(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    with pytest.raises(NotFound):
        pentry.create(ply.id, 9999999, db)


def test_delete(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)

    entries = [factory.playlist_entry(playlist_id=ply.id, conn=db) for _ in range(5)]
    pentry.delete(entries[2], db)

    new_entries = playlist.entries(ply, db)
    assert entries[2].id not in {e.id for e in new_entries}

    for i, ety in enumerate(entries[:2] + entries[3:], start=1):
        new_ety = pentry.from_id(ety.id, db)
        assert new_ety is not None
        assert new_ety.position == i


@pytest.mark.parametrize(
    "position, final_order",
    [
        (1, [2, 0, 1, 3, 4]),
        (2, [0, 2, 1, 3, 4]),
        (3, [0, 1, 2, 3, 4]),
        (4, [0, 1, 3, 2, 4]),
        (5, [0, 1, 3, 4, 2]),
    ],
)
def test_update(
    position: int,
    final_order: list[int],
    factory: Factory,
    db: Connection,
):
    ply = factory.playlist(conn=db)
    entries = [factory.playlist_entry(playlist_id=ply.id, conn=db) for _ in range(5)]

    ety = pentry.update(entries[2], position=position, conn=db)
    assert ety.position == position

    cursor = db.execute(
        """
        SELECT id
        FROM music__playlists_tracks
        WHERE playlist_id = ?
        ORDER BY position ASC
        """,
        (ply.id,),
    )

    order = [row["id"] for row in cursor]
    expected = [entries[i].track_id for i in final_order]
    assert order == expected


@pytest.mark.parametrize("position", [-1, 0, 7])
def test_update_out_of_bounds(position: int, factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    entries = [factory.playlist_entry(playlist_id=ply.id, conn=db) for _ in range(5)]
    with pytest.raises(IndexError):
        pentry.update(entries[2], position=position, conn=db)


def test_playlist(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    ety = factory.playlist_entry(playlist_id=ply.id, conn=db)
    assert pentry.playlist(ety, db).id == ply.id


def test_track(factory: Factory, db: Connection):
    trk = factory.track(conn=db)
    ety = factory.playlist_entry(track_id=trk.id, conn=db)
    assert pentry.track(ety, db).id == trk.id
