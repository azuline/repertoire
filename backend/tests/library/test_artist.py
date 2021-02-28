from sqlite3 import Connection

import pytest

from src.enums import CollectionType
from src.errors import Duplicate
from src.library import artist, collection
from tests.factory import Factory


def test_exists(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    assert artist.exists(art.id, db)


def test_does_not_exist(db: Connection):
    assert not artist.exists(9999999, db)


def test_from_id_success(factory: Factory, db: Connection):
    art_id = factory.artist(conn=db).id
    art = artist.from_id(art_id, db)
    assert art is not None
    assert art.id == art_id


def test_from_id_failure(db: Connection):
    assert artist.from_id(90000, db) is None


def test_from_name_success(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    new_art = artist.from_name(art.name.lower(), db)
    assert new_art is not None
    assert new_art.name == art.name


def test_from_name_failure(db: Connection):
    assert artist.from_name("nonexistent", db) is None


def test_search_all(factory: Factory, db: Connection):
    arts = {factory.artist(conn=db) for _ in range(5)}
    # Remove the unknown artist so we can easily compare.
    out = {art for art in artist.search(db) if art.id != 1}
    assert arts == out


def test_search_one(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    artists = artist.search(db, search=art.name)
    assert len(artists) == 1
    assert artists[0].name == art.name


def test_search_page(factory: Factory, db: Connection):
    for _ in range(5):
        factory.artist(conn=db)

    a1 = artist.search(db, page=1, per_page=1)[0]
    a2 = artist.search(db, page=2, per_page=1)[0]
    assert a1 != a2


def test_search_per_page(factory: Factory, db: Connection):
    arts = [factory.artist(conn=db) for _ in range(5)]
    arts = artist.search(db, page=1, per_page=2)
    assert len(arts) == 2


def test_count_all(factory: Factory, db: Connection):
    for _ in range(5):
        factory.artist(conn=db)

    count = artist.count(db)
    # The extra 1 is the Unknown Artist.
    assert count == 5 + 1


def test_count_search(factory: Factory, db: Connection):
    arts = [factory.artist(conn=db) for _ in range(5)]
    count = artist.count(db, search=arts[0].name)
    assert count == 1


def test_create(factory: Factory, db: Connection):
    prev_id = factory.artist(conn=db).id
    art = artist.create("new artist", starred=True, conn=db)
    assert art.id == prev_id + 1
    assert art == artist.from_id(prev_id + 1, db)


def test_create_duplicate(factory: Factory, db: Connection):
    factory.artist(name="Aaron West and the Roaring Twenties", conn=db)
    with pytest.raises(Duplicate):
        artist.create("aaron west and the roaring twenties", db)


def test_update_fields(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    new_art = artist.update(
        art,
        conn=db,
        name="New Name",
        starred=True,
    )

    assert new_art.name == "New Name"
    assert new_art.starred is True
    assert new_art == artist.from_id(art.id, db)


def test_update_duplicate(factory: Factory, db: Connection):
    art1 = factory.artist(conn=db)
    art2 = factory.artist(conn=db)

    with pytest.raises(Duplicate) as e:
        artist.update(art2, conn=db, name=art1.name)

    assert e.value.entity == art1


def test_update_nothing(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    new_art = artist.update(art, conn=db)
    assert art == new_art


def test_releases(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    releases = {factory.release(artist_ids=[art.id], conn=db) for _ in range(4)}
    assert releases == set(artist.releases(art, db))


def test_top_genres(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    releases = [factory.release(artist_ids=[art.id], conn=db) for _ in range(4)]
    genres = [factory.collection(type=CollectionType.GENRE, conn=db) for _ in range(4)]

    for i, rls in enumerate(releases):
        for col in genres[: i + 1]:
            collection.add_release(col, rls.id, db)

    tg = artist.top_genres(art, db)

    for i in range(4):
        assert tg[i]["genre"].id == genres[i].id
        assert tg[i]["num_matches"] == 4 - i


def test_image(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    img = factory.mock_image(conn=db)
    factory.release(artist_ids=[art.id], image_id=img.id, conn=db)

    new_img = artist.image(art, db)
    assert new_img is not None
    assert new_img.id == img.id


def test_image_nonexistent(factory: Factory, db: Connection):
    art = factory.artist(conn=db)
    assert artist.image(art, db) is None
