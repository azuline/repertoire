from pysqlite3 import Connection

import pytest

from src.errors import Duplicate
from src.library import artist


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


def test_all(db: Connection, snapshot):
    artists = artist.all(db)
    snapshot.assert_match(artists)


def test_create(db: Connection):
    art = artist.create("new artist", starred=True, conn=db)
    assert art.id == 6
    assert art == artist.from_id(6, db)


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
