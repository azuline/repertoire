from sqlite3 import Connection

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
    assert art.name == "Aaron West and the Roaring Twenties"  # type: ignore


def test_from_name_failure(db: Connection):
    assert artist.from_name("nonexistent", db) is None


def test_all(db: Connection, snapshot):
    artists = artist.all(db)
    assert all(art.num_releases for art in artists)
    snapshot.assert_match(artists)


def test_create(db: Connection):
    art = artist.create("new artist", starred=True, conn=db)
    assert art.id == 6
    assert art == artist.from_id(6, db)


def test_create_duplicate(db: Connection):
    with pytest.raises(Duplicate):
        artist.create("aaron west and the roaring twenties", db)


def test_update_fields(db: Connection, snapshot):
    col = artist.update(
        artist.from_id(2, db),  # type: ignore
        conn=db,
        name="New Name",
        starred=True,
    )
    snapshot.assert_match(col)
    assert col == artist.from_id(2, db)


def test_update_duplicate(db: Connection, snapshot):
    with pytest.raises(Duplicate) as e:
        artist.update(
            artist.from_id(5, db),  # type: ignore
            conn=db,
            name="Abakus",
        )

    assert e.value.entity.id == 4


def test_update_nothing(db: Connection):
    col = artist.from_id(2, db)
    new_col = artist.update(col, conn=db)  # type: ignore
    assert col == new_col


def test_releases(db: Connection, snapshot):
    art = artist.from_id(2, db)
    snapshot.assert_match(artist.releases(art, db))  # type: ignore


def test_top_genres(db: Connection, snapshot):
    art = artist.from_id(2, db)
    snapshot.assert_match(artist.top_genres(art, db))  # type: ignore


def test_image(db: Connection):
    art = artist.from_id(2, db)
    assert artist.image(art, db).id == 1  # type: ignore


def test_image_nonexistent(db: Connection):
    art = artist.from_id(1, db)
    assert artist.image(art, db) is None  # type: ignore
