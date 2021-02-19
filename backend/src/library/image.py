from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from sqlite3 import Cursor, Row
from typing import Dict, Optional, Union

from PIL import Image, UnidentifiedImageError

from src.errors import Duplicate, InvalidImage

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class T:
    """An image dataclass."""

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    path: Path


def from_row(row: Union[Dict, Row]) -> T:
    """
    Return an image dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: An image dataclass.
    """
    return T(id=row["id"], path=Path(row["path"]))


def from_id(id: int, conn: Connection) -> Optional[T]:
    """
    Return the image with the provided ID.

    :param id: The ID of the image to fetch.
    :param conn: A connection to the database.
    :return: An image with the provided ID, if it exists.
    """
    cursor.execute("SELECT * from images WHERE id = ?", (id,))
    if row := cursor.fetchone():
        logger.debug(f"Fetched image {id}.")
        return from_row(row)

    logger.debug(f"Failed to fetch image {id}.")
    return None


def from_path(path: Union[Path, str], conn: Connection) -> Optional[T]:
    """
    Return the image with the provided path.

    :param path: The path of the image to fetch.
    :param conn: A connection to the database.
    :return: An image with the provided ID, if it exists.
    """
    cursor.execute("SELECT * from images WHERE path = ?", (str(path),))
    if row := cursor.fetchone():
        logger.debug(f"Fetched image {row['id']} from path {path}.")
        return from_row(row)

    logger.debug(f"Failed to fetch image from path {path}.")
    return None


def create(path: Union[Path, str], conn: Connection) -> T:
    """
    Create an image with the given path.

    :param path: The path of the image file.
    :param conn: A connection to the database.
    :return: The newly created image.
    :raises Duplicate: If an image with the given path already exists. The duplicate
                       image is passed as the ``entity`` argument.
    """
    if img := from_path(path, cursor):
        raise Duplicate("An image with the given path already exists.", img)

    cursor.execute("INSERT INTO images (path) VALUES (?)", (str(path),))
    img = T(id=cursor.lastrowid, path=Path(path))

    logger.info(f"Created image {cursor.lastrowid} with path {path}")

    try:
        _generate_thumbnail(img)
    except UnidentifiedImageError:
        delete(img, cursor)
        raise InvalidImage("The image file could not be read.")

    return img


def _generate_thumbnail(img: T) -> None:
    """
    Given an image, generate its 300x300 thumbnail.

    :param img: The image object whose thumbnail to generate.
    """
    logger.debug(f"Generating thumbnail for {img.path}.")
    thumbnail = Image.open(img.path).convert("RGB")
    thumbnail.thumbnail((300, 300))
    thumbnail.save(thumbnail_path(img), "JPEG")


def delete(img: T, conn: Connection) -> None:
    """
    Delete an image (and its associated image on disk).

    :param img: The image to delete.
    :param conn: A connection to the database.
    """
    cursor.execute("DELETE FROM images WHERE id = ?", (img.id,))
    logger.info(f"Deleted image {img.id}")

    if img.path.exists():
        img.path.unlink()
        logger.debug(f"Deleted image {img.id} off disk.")
    if (thumbnail := thumbnail_path(img)).exists():
        thumbnail.unlink()
        logger.debug(f"Deleted image {img.id}'s thumbnail off disk.")


def thumbnail_path(img: T) -> Path:
    """
    Given an image, return the path to the thumbnail of an image.

    :param img: An image.
    :return: The path to the thumbnail.
    """
    return img.path.with_suffix(".thumbnail")
