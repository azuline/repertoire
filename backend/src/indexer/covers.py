import logging
import os
from hashlib import sha256
from pathlib import Path
from sqlite3 import Cursor
from typing import Generator, List, Optional, Tuple

from PIL import Image, UnidentifiedImageError
from tagfiles import TagFile

from src.constants import COVER_ART_DIR
from src.util import database

logger = logging.getLogger()

MIME_TO_EXTS = {"image/jpeg": "jpg", "image/png": "png"}

COVER_FILENAMES = [
    ("album.jpg", "jpg"),
    ("album.jpeg", "jpg"),
    ("album.png", "png"),
    ("cover.jpg", "jpg"),
    ("cover.jpeg", "jpg"),
    ("cover.png", "png"),
    ("folder.jpg", "jpg"),
    ("folder.jpeg", "jpg"),
    ("folder.png", "png"),
]


def save_pending_covers() -> None:
    """
    For the releases with pending covers-to-save, look at their first track for a cover
    art to save. If a cover art is found, save it to the ``COVER_ART_DIR``, generate a
    thumbnail, and update the database with the filename.
    """
    logger.info("Saving cover art for newly-found releases.")

    with database() as conn:
        cursor = conn.cursor()

        for rls_id in _get_pending_releases(cursor):
            logger.debug(f"Searching for cover art in release {rls_id}.")

            if not (track_path := _get_track_path_of_release(rls_id, cursor)):
                logger.debug(f"No tracks found for release {rls_id}.")
                continue

            if not (image_path := save_image(TagFile(track_path))):
                logger.debug(f"No image found for release {rls_id}.")
                continue

            try:
                generate_thumbnail(image_path)
                _update_image_path(rls_id, image_path, cursor)
            except UnidentifiedImageError:
                image_path.unlink()

            _delete_release_from_pending(rls_id, cursor)

        conn.commit()


def _get_pending_releases(cursor: Cursor) -> List[int]:
    """
    Return the release ids of the releases pending cover art extraction.

    :param cursor: A cursor to the database.
    :return: Release IDs pending extraction.
    """
    cursor.execute("SELECT release_id FROM music__releases_to_fetch_images")
    return [row[0] for row in cursor.fetchall()]


def _get_track_path_of_release(rls_id: int, cursor: Cursor) -> Optional[str]:
    """
    Return the filepath of a track belonging to a release with the provided ID.

    :param rls_id: The ID of the release whose track we are fetching.
    :param cursor: A cursor to the database.
    :return: The filepath of a track, if there is a track.
    """
    cursor.execute(
        "SELECT filepath FROM music__tracks WHERE release_id = ? LIMIT 1", (rls_id,)
    )
    if (track := cursor.fetchone()) and os.path.isfile(track[0]):
        return track[0]

    return None


def _update_image_path(rls_id: int, image_path: Path, cursor: Cursor) -> None:
    """
    Update the image path of a release with the given ID in the database.

    :param rls_id: The ID of the release to update.
    :param image_path: The image path to set for the release.
    :param cursor: A cursor to the database.
    """
    logger.debug(f"Setting image for release {rls_id}.")
    cursor.execute(
        "UPDATE music__releases SET image_path = ? WHERE id = ?",
        (str(image_path), rls_id),
    )


def _delete_release_from_pending(rls_id: int, cursor: Cursor) -> None:
    """
    Remove the provided release ID from the pending cover extraction table.

    :param rls_id: The release ID to remove.
    :param cursor: A cursor to the database.
    """
    logger.debug(f"Removing release {rls_id} from pending cover extraction.")
    cursor.execute(
        "DELETE FROM music__releases_to_fetch_images WHERE release_id = ?", (rls_id,)
    )


def save_image(tf: TagFile) -> Optional[Path]:
    """
    If the track has attached cover art, save it to the cover_arts dir with
    the sha256 of the cover art as the filename.

    Otherwise, look in the directory of the file and the directory above it for
    a `cover` or `folder` file (case insensitive) if embedded art does not
    exist.

    If neither exist, return None.

    :param tf: The tagfile whose image we want to save.
    :return: The filepath of the saved image, if one was saved.
    """
    return _save_embedded_image(tf) or _save_external_image(tf)


def _save_embedded_image(tf: TagFile) -> Optional[Path]:
    """
    If an embedded image exists, save the image embedded in a tagfile to a file on disk
    and return the path to the saved image. Otherwise, return ``None``.

    :param tf: The tagfile whose embedded image we are saving.
    :return: The path to the saved image, if it exists.
    """
    if not tf.image_mime:
        logger.debug(f"No embedded image found for `{tf.path}`.")
        return None

    extension = MIME_TO_EXTS.get(tf.image_mime, None)

    if not extension:
        logger.debug("Embedded image with invalid mimetype found for `{tf.path}`.")
        return None

    return _save_image_file(tf.image, extension)


def _save_external_image(tf: TagFile) -> Optional[Path]:
    """
    Given a tagfile, search its directory and its parent directory for a cover image. If
    one is found, save it to ``COVER_ARTS_DIR``, otherwise, return ``None``.

    We look in both the parent and the parent's parent due to some tracks being nested a
    directory deeper than the cover in a multi-disc folder layout.

    :param tf: The tagfile whose cover we are searching for.
    :return: The path to the saved image, if one was found.
    """
    for filepath, ext in _get_possible_cover_paths(tf.path):
        if filepath.exists():
            with filepath.open("rb") as f:
                return _save_image_file(f.read(), ext)

    return None


def _get_possible_cover_paths(
    track_path: Path,
) -> Generator[Tuple[Path, str], None, None]:
    """
    Generate and yield tuples of possible cover filepaths and the file extension of that
    path.

    :param track_path: The path to the track.
    :return: A generator of possible paths + their extensions.
    """
    for dir_ in [track_path.parent, track_path.parent.parent]:
        for filename, ext in COVER_FILENAMES:
            yield dir_ / filename, ext


def _save_image_file(data: bytes, extension: str) -> Path:
    """
    Given the contents of an image file (as bytes) and its extension, save it to
    ``COVER_ART_DIR``. Calculate the file's sha256sum and use it as the filename.

    :param data: The bytes of the image file.
    :param extension: The file extension of the image.
    :return: The filepath that the image was saved to.
    """
    sha256sum = sha256(data).hexdigest()

    filepath = COVER_ART_DIR / f"{sha256sum}.{extension}"

    if filepath.exists():
        logger.debug("Embedded image already saved!")
    else:
        logger.debug(f"Writing image file to {filepath}.")
        with filepath.open("wb") as f:
            f.write(data)

    return filepath


def generate_thumbnail(image_path: Path) -> None:
    """
    Given a path to a saved image file, generate a 300x300 thumbnail and save it to
    ``{image_path}.extension``.

    :param image_path: The path to the original image file.
    """
    logger.debug(f"Generating thumbnail for {image_path}.")
    image = Image.open(image_path).convert("RGB")
    image.thumbnail((300, 300))
    image.save(image_path.with_suffix(".thumbnail"), "JPEG")
