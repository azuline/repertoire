from sqlite3 import Connection

import pytest

from src.errors import Duplicate
from src.library import artist
from tests.conftest import NEXT_ARTIST_ID, NUM_ARTISTS


def test_exists(db: Connection):
    assert artist.exists(1, db)


def test_does_not_exist(db: Connection):
    assert not artist.exists(9999999, db)


def test_from_id_success(db: Connection, snapshot):
    snapshot.assert_match(artist.from_id(2, db))


def test_from_id_failure(db: Connection):
    assert artist.from_id(90000, db) is None


def test_from_name_success(db: Connection):
    art = artist.from_name("aaron west and the roaring twenties", db)
    assert art is not None
    assert art.name == "Aaron West and the Roaring Twenties"


def test_from_name_failure(db: Connection):
    assert artist.from_name("nonexistent", db) is None


def test_search_all(db: Connection, snapshot):
    artists = artist.search(db)
    snapshot.assert_match(artists)


def test_search_one(db: Connection, snapshot):
    artists = artist.search(db, search="aba")
    assert len(artists) == 1
    assert artists[0].name == "Abakus"


def test_search_page(db: Connection, snapshot):
    a1 = artist.search(db, page=1, per_page=1)[0]
    a2 = artist.search(db, page=2, per_page=1)[0]
    assert a1 != a2


def test_search_per_page(db: Connection, snapshot):
    arts = artist.search(db, page=1, per_page=2)
    assert len(arts) == 2


def test_count_all(db: Connection, snapshot):
    count = artist.count(db)
    assert count == NUM_ARTISTS


def test_count_search(db: Connection, snapshot):
    count = artist.count(db, search="aba")
    assert count == 1


def test_create(db: Connection):
    art = artist.create("new artist", starred=True, conn=db)
    assert art.id == NEXT_ARTIST_ID
    assert art == artist.from_id(NEXT_ARTIST_ID, db)


def test_create_duplicate(db: Connection):
    with pytest.raises(Duplicate):
        artist.create("aaron west and the roaring twenties", db)


def test_update_fields(db: Connection, snapshot):
    art = artist.from_id(2, db)
    assert art is not None

    art = artist.update(
        art,
        conn=db,
        name="New Name",
        starred=True,
    )
    snapshot.assert_match(art)
    assert art == artist.from_id(2, db)


def test_update_duplicate(db: Connection, snapshot):
    art = artist.from_id(5, db)
    assert art is not None

    with pytest.raises(Duplicate) as e:
        artist.update(art, conn=db, name="Abakus")

    assert e.value.entity.id == 4


def test_update_nothing(db: Connection):
    art = artist.from_id(2, db)
    assert art is not None

    new_art = artist.update(art, conn=db)
    assert art == new_art


def test_releases(db: Connection, snapshot):
    art = artist.from_id(2, db)
    assert art is not None

    snapshot.assert_match(artist.releases(art, db))


def test_top_genres(db: Connection, snapshot):
    art = artist.from_id(2, db)
    assert art is not None

    snapshot.assert_match(artist.top_genres(art, db))


def test_image(db: Connection):
    art = artist.from_id(2, db)
    assert art is not None
    img = artist.image(art, db)
    assert img is not None
    assert img.id == 1


def test_image_nonexistent(db: Connection):
    art = artist.from_id(1, db)
    assert art is not None

    assert artist.image(art, db) is None
