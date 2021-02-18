from sqlite3 import Cursor

import pytest

from src.enums import PlaylistType
from src.errors import Duplicate, Immutable, InvalidPlaylistType
from src.library import playlist


def test_exists(db: Cursor):
    assert playlist.exists(1, db)


def test_does_not_exist(db: Cursor):
    assert not playlist.exists(9999999, db)


def test_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(playlist.from_id(2, db))


def test_from_id_failure(db: Cursor):
    assert playlist.from_id(90000, db) is None


def test_from_name_and_type_success(db: Cursor):
    ply = playlist.from_name_and_type("AAAAAA", PlaylistType.PLAYLIST, db)
    assert ply.name == "AAAAAA"  # type: ignore
    assert ply.type == PlaylistType.PLAYLIST  # type: ignore


def test_from_name_and_type_failure(db: Cursor):
    assert playlist.from_name_and_type("CCCCCC", PlaylistType.PLAYLIST, db) is None


def test_all(db: Cursor, snapshot):
    playlists = playlist.all(db)
    snapshot.assert_match(playlists)


def test_all_filter_type(db: Cursor, snapshot):
    playlists = playlist.all(db, types=[PlaylistType.PLAYLIST])
    snapshot.assert_match(playlists)


def test_all_filter_type_multiple(db: Cursor, snapshot):
    playlists = playlist.all(db, types=[PlaylistType.SYSTEM, PlaylistType.PLAYLIST])
    snapshot.assert_match(playlists)


@pytest.mark.parametrize("type", [PlaylistType.PLAYLIST])
def test_create(db: Cursor, type):
    ply = playlist.create("new plylist", type, starred=True, cursor=db)
    assert ply.id == 4
    assert ply == playlist.from_id(4, db)


def test_create_duplicate(db: Cursor):
    with pytest.raises(Duplicate):
        playlist.create("AAAAAA", PlaylistType.PLAYLIST, db)


def test_create_invalid_type(db: Cursor):
    with pytest.raises(InvalidPlaylistType):
        playlist.create("new playlist", PlaylistType.SYSTEM, cursor=db)


def test_update_fields(db: Cursor, snapshot):
    ply = playlist.update(
        playlist.from_id(2, db),  # type: ignore
        cursor=db,
        name="New Name",
        starred=True,
    )
    snapshot.assert_match(ply)
    assert ply == playlist.from_id(2, db)


def test_update_immutable(db: Cursor):
    with pytest.raises(Immutable):
        playlist.update(
            playlist.from_id(1, db),  # type: ignore
            cursor=db,
            name="New Name",
        )


def test_update_duplicate(db: Cursor):
    with pytest.raises(Duplicate) as e:
        playlist.update(
            playlist.from_id(2, db),  # type: ignore
            cursor=db,
            name="BBBBBB",
        )

    assert e.value.entity.id == 3


def test_update_nothing(db: Cursor):
    ply = playlist.from_id(2, db)
    new_ply = playlist.update(ply, cursor=db)  # type: ignore
    assert ply == new_ply


def test_update_starred(db: Cursor):
    ply = playlist.update(
        playlist.from_id(3, db),  # type: ignore
        cursor=db,
        starred=True,
    )
    assert ply.starred is True
    assert ply == playlist.from_id(3, db)


def test_entries(db: Cursor, snapshot):
    ply = playlist.from_id(2, db)
    snapshot.assert_match(playlist.entries(ply, db))  # type: ignore


def test_top_genres(db: Cursor, snapshot):
    ply = playlist.from_id(2, db)
    snapshot.assert_match(playlist.top_genres(ply, db))  # type: ignore


def test_image(db: Cursor):
    ply1 = playlist.from_id(1, db)
    assert playlist.image(ply1, db).id == 1  # type: ignore

    ply2 = playlist.from_id(1, db)
    assert isinstance(playlist.image(ply2, db).id, int)  # type: ignore


def test_image_nonexistent(db: Cursor):
    ply = playlist.from_id(3, db)
    assert playlist.image(ply, db) is None  # type: ignore
