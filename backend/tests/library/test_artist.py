from sqlite3 import Cursor

import pytest

from src.errors import Duplicate
from src.library import artist


def test_exists(db: Cursor):
    assert artist.exists(1, db)


def test_does_not_exist(db: Cursor):
    assert not artist.exists(9999999, db)


def test_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(artist.from_id(2, db))


def test_from_id_failure(db: Cursor):
    assert artist.from_id(90000, db) is None


def test_from_name_success(db: Cursor):
    art = artist.from_name("aaron west and the roaring twenties", db)
    assert art.name == "Aaron West and the Roaring Twenties"


def test_from_name_failure(db: Cursor):
    assert artist.from_name("nonexistent", db) is None


def test_all(db: Cursor, snapshot):
    artists = artist.all(db)
    assert all(art.num_releases for art in artists)
    snapshot.assert_match(artists)


def test_create(db: Cursor):
    art = artist.create("new artist", starred=True, cursor=db)
    assert art.id == 6
    assert art == artist.from_id(6, db)


def test_create_duplicate(db: Cursor):
    with pytest.raises(Duplicate):
        artist.create("aaron west and the roaring twenties", db)


def test_update_fields(db: Cursor, snapshot):
    col = artist.update(
        artist.from_id(2, db),
        cursor=db,
        name="New Name",
        starred=True,
    )
    snapshot.assert_match(col)
    assert col == artist.from_id(2, db)


def test_update_duplicate(db: Cursor, snapshot):
    with pytest.raises(Duplicate) as e:
        artist.update(
            artist.from_id(5, db),
            cursor=db,
            name="Abakus",
        )

    assert e.value.entity.id == 4


def test_update_nothing(db: Cursor):
    col = artist.from_id(2, db)
    new_col = artist.update(col, cursor=db)
    assert col == new_col


def test_releases(db: Cursor, snapshot):
    art = artist.from_id(2, db)
    snapshot.assert_match(artist.releases(art, db))


def test_top_genres(db: Cursor, snapshot):
    art = artist.from_id(2, db)
    snapshot.assert_match(artist.top_genres(art, db))
