from pathlib import Path
from sqlite3 import Connection

import pytest
from PIL import Image

from src.errors import Duplicate, InvalidImage
from src.library import image
from src.conftest import SEED_DATA
from src.fixtures.factory import Factory

FAKE_COVER = SEED_DATA / "fake_cover.jpg"


def test_from_id(factory: Factory, db: Connection):
    img = factory.mock_image(conn=db)
    new_img = image.from_id(img.id, db)
    assert img == new_img


def test_from_id_nonexistent(db: Connection):
    assert image.from_id(999, db) is None


def test_from_path(factory: Factory, db: Connection):
    img = factory.mock_image(path=Path("/lol"), conn=db)
    assert img == image.from_path("/lol", db)


def test_from_path_nonexistent(db: Connection):
    assert image.from_path("/lol", db) is None


def test_create(factory: Factory, db: Connection):
    img = factory.image(conn=db)

    # Check thumbnail was generated.
    im = Image.open(img.path.with_suffix(".thumbnail"))
    assert im.size == (300, 300)


def test_create_duplicate(factory: Factory, db: Connection):
    img = factory.mock_image(conn=db)

    with pytest.raises(Duplicate) as e:
        image.create(img.path, db)

    assert e.value.entity == img


def test_create_invalid_image(factory: Factory, db: Connection):
    image_path = Path.cwd() / "cover.jpg"
    with image_path.open("wb") as f:
        f.write(b"not an image lol!")

    with pytest.raises(InvalidImage):
        image.create(image_path, db)

    assert not image_path.exists()


def test_delete_image(factory: Factory, db: Connection):
    image_path = Path.cwd() / "cover.jpg"
    thumbnail_path = Path.cwd() / "cover.thumbnail"
    image_path.touch()
    thumbnail_path.touch()

    img = factory.mock_image(path=image_path, conn=db)
    image.delete(img, db)

    assert not image.from_id(img.id, db)
    assert not image_path.exists()
    assert not thumbnail_path.exists()


def test_delete_image_files_missing(factory: Factory, db: Connection):
    image_path = Path.cwd() / "cover.jpg"
    img = factory.mock_image(path=image_path, conn=db)
    image.delete(img, db)
    assert not image.from_id(img.id, db)


def test_thumbnail_path():
    image_path = Path("/lol.jpg")
    assert Path("/lol.thumbnail") == image.thumbnail_path(
        image.T(id=1, path=image_path)
    )
