import shutil
from pathlib import Path

import pytest
from PIL import Image

from src.errors import Duplicate, InvalidImage
from src.library import image
from tests.conftest import SEED_DATA

FAKE_COVER = SEED_DATA / "fake_cover.jpg"


def test_from_id(db, snapshot):
    snapshot.assert_match(image.from_id(1, db))


def test_from_id_nonexistent(db):
    assert image.from_id(999, db) is None


def test_from_path(db, snapshot):
    db.execute("UPDATE images SET path = '/lol' WHERE id = 1")

    assert image.from_path("/lol", db).id == 1


def test_from_path_nonexistent(db, snapshot):
    assert image.from_path("/lol", db) is None


def test_create(db):
    image_path = Path.cwd() / "cover.jpg"
    shutil.copyfile(FAKE_COVER, image_path)
    img = image.create(image_path, db)

    assert img.id == 3
    assert img.path == image_path
    assert img == image.from_id(3, db)

    # Check thumbnail was generated.
    im = Image.open(Path.cwd() / "cover.thumbnail")
    assert im.size == (300, 300)


def test_create_duplicate(db):
    db.execute("UPDATE images SET path = '/lol' WHERE id = 1")

    with pytest.raises(Duplicate) as e:
        image.create("/lol", db)

    assert e.value.entity.id == 1


def test_create_invalid_image(db):
    image_path = Path.cwd() / "cover.jpg"
    with image_path.open("wb") as f:
        f.write(b"not an image lol!")

    with pytest.raises(InvalidImage):
        image.create(image_path, db)

    assert image.from_id(3, db) is None
    assert not image_path.exists()


def test_delete_image(db):
    image_path = Path.cwd() / "cover.jpg"
    thumbnail_path = Path.cwd() / "cover.thumbnail"
    image_path.touch()
    thumbnail_path.touch()

    cursor = db.execute("INSERT INTO images (path) VALUES (?)", (str(image_path),))
    image_id = cursor.lastrowid

    image.delete(image.from_id(image_id, db), db)

    assert not image.from_id(image_id, db)
    assert not image_path.exists()
    assert not thumbnail_path.exists()


def test_thumbnail_path():
    image_path = Path("/lol.jpg")
    assert Path("/lol.thumbnail") == image.thumbnail_path(
        image.T(id=1, path=image_path)
    )
