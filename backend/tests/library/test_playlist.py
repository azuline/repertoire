import pytest
from pysqlite3 import Connection

from src.enums import PlaylistType
from src.errors import Duplicate, Immutable, InvalidPlaylistType
from src.library import playlist
from tests.conftest import NUM_PLAYLISTS


def test_exists(db: Connection):
    assert playlist.exists(1, db)


def test_does_not_exist(db: Connection):
    assert not playlist.exists(9999999, db)


def test_from_id_success(db: Connection, snapshot):
    snapshot.assert_match(playlist.from_id(2, db))


def test_from_id_failure(db: Connection):
    assert playlist.from_id(90000, db) is None


def test_from_name_and_type_success(db: Connection):
    ply = playlist.from_name_and_type("AAAAAA", PlaylistType.PLAYLIST, db)
    assert ply is not None

    assert ply.name == "AAAAAA"
    assert ply.type == PlaylistType.PLAYLIST


def test_from_name_and_type_failure(db: Connection):
    assert playlist.from_name_and_type("CCCCCC", PlaylistType.PLAYLIST, db) is None


def test_search(db: Connection, snapshot):
    plys = playlist.search(db)
    snapshot.assert_match(plys)


def test_search_name(db: Connection, snapshot):
    plys = playlist.search(db, searchstr="AaA")
    assert len(plys) == 1
    assert plys[0].name == "AAAAAA"


def test_search_one(db: Connection, snapshot):
    plys = playlist.search(
        db,
        types=[PlaylistType.SYSTEM, PlaylistType.PLAYLIST],
        searchstr="aaaa",
    )
    assert plys[0].name == "AAAAAA"


def test_search_page(db: Connection, snapshot):
    p1 = playlist.search(db, page=1, per_page=1)[0]
    p2 = playlist.search(db, page=2, per_page=1)[0]
    assert p1 != p2


def test_search_per_page(db: Connection, snapshot):
    plys = playlist.search(db, page=1, per_page=2)
    assert len(plys) == 2


def test_count_all(db: Connection, snapshot):
    count = playlist.count(db)
    assert count == NUM_PLAYLISTS


def test_count_one(db: Connection, snapshot):
    count = playlist.count(
        db,
        types=[PlaylistType.SYSTEM, PlaylistType.PLAYLIST],
        searchstr="aaaa",
    )
    assert count == 1


@pytest.mark.parametrize("type", [PlaylistType.PLAYLIST])
def test_create(db: Connection, type):
    ply = playlist.create("new plylist", type, starred=True, conn=db)
    assert ply.id == 4
    assert ply == playlist.from_id(4, db)


def test_create_duplicate(db: Connection):
    with pytest.raises(Duplicate):
        playlist.create("AAAAAA", PlaylistType.PLAYLIST, db)


def test_create_invalid_type(db: Connection):
    with pytest.raises(InvalidPlaylistType):
        playlist.create("new playlist", PlaylistType.SYSTEM, conn=db)


def test_update_fields(db: Connection, snapshot):
    ply = playlist.from_id(2, db)
    assert ply is not None

    ply = playlist.update(ply, conn=db, name="New Name", starred=True)
    snapshot.assert_match(ply)
    assert ply == playlist.from_id(2, db)


def test_update_immutable(db: Connection):
    ply = playlist.from_id(1, db)
    assert ply is not None

    with pytest.raises(Immutable):
        playlist.update(ply, conn=db, name="New Name")


def test_update_duplicate(db: Connection):
    ply = playlist.from_id(2, db)
    assert ply is not None

    with pytest.raises(Duplicate) as e:
        playlist.update(ply, conn=db, name="BBBBBB")

    assert e.value.entity.id == 3


def test_update_nothing(db: Connection):
    ply = playlist.from_id(2, db)
    assert ply is not None

    new_ply = playlist.update(ply, conn=db)
    assert ply == new_ply


def test_update_starred(db: Connection):
    ply = playlist.from_id(3, db)
    assert ply is not None

    ply = playlist.update(ply, conn=db, starred=True)
    assert ply.starred is True
    assert ply == playlist.from_id(3, db)


def test_entries(db: Connection, snapshot):
    ply = playlist.from_id(2, db)
    assert ply is not None

    snapshot.assert_match(playlist.entries(ply, db))


def test_top_genres(db: Connection, snapshot):
    ply = playlist.from_id(2, db)
    assert ply is not None

    snapshot.assert_match(playlist.top_genres(ply, db))


def test_image(db: Connection):
    ply = playlist.from_id(1, db)
    assert ply is not None
    img = playlist.image(ply, db)
    assert img is not None
    assert img.id == 1


def test_multiple_images(db: Connection):
    ply = playlist.from_id(1, db)
    assert ply is not None
    img = playlist.image(ply, db)
    assert img is not None
    assert isinstance(img.id, int)


def test_image_nonexistent(db: Connection):
    ply = playlist.from_id(3, db)
    assert ply is not None

    assert playlist.image(ply, db) is None
