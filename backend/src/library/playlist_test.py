from sqlite3 import Connection

import pytest

from src.enums import CollectionType, PlaylistType
from src.errors import Duplicate, Immutable, InvalidArgument, InvalidPlaylistType
from src.fixtures.factory import Factory

from . import collection, playlist
from . import playlist_entry as pentry


def test_exists(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    assert playlist.exists(ply.id, db)


def test_does_not_exist(db: Connection):
    assert not playlist.exists(9999999, db)


def test_from_id_success(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    new_ply = playlist.from_id(ply.id, db)
    assert new_ply == ply


def test_from_id_failure(db: Connection):
    assert playlist.from_id(90000, db) is None


def test_from_name_type_user_success(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    new_ply = playlist.from_name_type_user(ply.name, ply.type, db)
    assert ply == new_ply


def test_from_name_type_user_failure(db: Connection):
    ply = playlist.from_name_type_user("CCCCCC", PlaylistType.PLAYLIST, db)
    assert ply is None


def test_search_all(factory: Factory, db: Connection):
    plys = {factory.playlist(conn=db) for _ in range(5)}
    assert plys == set(playlist.search(db))


def test_search_name(factory: Factory, db: Connection):
    factory.playlist(name="AAAAAA", conn=db)
    plys = playlist.search(db, search="AaA")
    assert len(plys) == 1
    assert plys[0].name == "AAAAAA"


def test_search_one(factory: Factory, db: Connection):
    plys = [factory.playlist(conn=db) for _ in range(5)]
    out = playlist.search(db, types=[plys[0].type], search=plys[0].name)
    assert plys[0] == out[0]


def test_search_page(factory: Factory, db: Connection):
    for _ in range(5):
        factory.playlist(conn=db)

    p1 = playlist.search(db, page=1, per_page=1)[0]
    p2 = playlist.search(db, page=2, per_page=1)[0]
    assert p1 != p2


def test_search_per_page(factory: Factory, db: Connection):
    plys = [factory.playlist(conn=db) for _ in range(5)]
    plys = playlist.search(db, page=1, per_page=2)
    assert len(plys) == 2


def test_count_all(factory: Factory, db: Connection):
    plys = [factory.playlist(conn=db) for _ in range(5)]
    count = playlist.count(db)
    assert count == len(plys)


def test_count_one(factory: Factory, db: Connection):
    plys = [factory.playlist(conn=db) for _ in range(5)]
    count = playlist.count(db, types=[plys[0].type], search=plys[0].name)
    assert count == 1


def test_create(db: Connection):
    ply = playlist.create("new plylist", PlaylistType.PLAYLIST, starred=True, conn=db)
    assert ply == playlist.from_id(ply.id, db)


def test_create_general_with_user(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    with pytest.raises(InvalidArgument):
        playlist.create(
            "new plylist",
            PlaylistType.PLAYLIST,
            user_id=usr.id,
            starred=True,
            conn=db,
        )


def test_create_personal(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    ply = playlist.create(
        "new plylist",
        PlaylistType.PERSONAL,
        user_id=usr.id,
        starred=True,
        conn=db,
    )
    assert ply == playlist.from_id(ply.id, db)


def test_create_personal_without_user(db: Connection):
    with pytest.raises(InvalidArgument):
        playlist.create(
            "new plylist",
            PlaylistType.PERSONAL,
            starred=True,
            conn=db,
        )


def test_create_duplicate(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    with pytest.raises(Duplicate):
        playlist.create(ply.name, ply.type, db)


def test_create_invalid_type(factory: Factory, db: Connection):
    with pytest.raises(InvalidPlaylistType):
        playlist.create("new playlist", PlaylistType.SYSTEM, conn=db)


def test_create_invalid_type_override(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    ply = playlist.create(
        "new playlist",
        PlaylistType.SYSTEM,
        user_id=usr.id,
        conn=db,
        override_immutable=True,
    )
    assert ply is not None


def test_update_fields(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    new_ply = playlist.update(ply, conn=db, name="New Name", starred=True)
    assert new_ply == playlist.from_id(ply.id, db)
    assert new_ply.name == "New Name"
    assert new_ply.starred is True


def test_update_immutable(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    ply = factory.playlist(type=PlaylistType.SYSTEM, user=usr, conn=db)

    with pytest.raises(Immutable):
        playlist.update(ply, conn=db, name="New Name")


def test_update_duplicate(factory: Factory, db: Connection):
    ply1 = factory.playlist(conn=db)
    ply2 = factory.playlist(conn=db)

    with pytest.raises(Duplicate) as e:
        playlist.update(ply2, conn=db, name=ply1.name)

    assert e.value.entity == ply1


def test_update_starred(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    new_ply = playlist.update(ply, conn=db, starred=True)
    assert new_ply.starred is True
    assert new_ply == playlist.from_id(ply.id, db)


def test_entries(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    tracks = [factory.track(conn=db) for _ in range(5)]

    for trk in tracks:
        pentry.create(ply.id, trk.id, db)

    track_ids = {trk.id for trk in tracks}
    entries = playlist.entries(ply, db)
    assert track_ids == {e.track_id for e in entries}


def test_top_genres(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    releases = [factory.release(conn=db) for _ in range(4)]
    genres = [factory.collection(type=CollectionType.GENRE, conn=db) for _ in range(4)]

    for i, rls in enumerate(releases):
        trk = factory.track(release_id=rls.id, conn=db)
        pentry.create(ply.id, trk.id, db)
        for grn in genres[: i + 1]:
            collection.add_release(grn, rls.id, db)

    tg = playlist.top_genres(ply, db)

    for i in range(4):
        assert tg[i]["genre"].id == genres[i].id
        assert tg[i]["num_matches"] == 4 - i


def test_image(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    img = factory.mock_image(conn=db)
    rls = factory.release(image_id=img.id, conn=db)
    trk = factory.track(release_id=rls.id, conn=db)

    pentry.create(ply.id, trk.id, db)

    new_img = playlist.image(ply, db)
    assert new_img is not None
    assert new_img.id == img.id


def test_image_nonexistent(factory: Factory, db: Connection):
    ply = factory.playlist(conn=db)
    assert playlist.image(ply, db) is None
