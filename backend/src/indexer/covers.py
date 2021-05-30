import logging
import os
from hashlib import sha256
from pathlib import Path
from sqlite3 import Connection
from typing import Generator, Optional

from tagfiles import TagFile

from src.constants import constants
from src.errors import Duplicate
from src.library import image
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
        for rls_id in _get_pending_releases(conn):
            logger.debug(f"Searching for cover art in release {rls_id}.")

            track_path = _get_track_path_of_release(rls_id, conn)
            if not track_path:
                logger.debug(f"No tracks found for release {rls_id}.")
                _delete_release_from_pending(rls_id, conn)
                continue

            img = save_image(TagFile(track_path), conn)
            if not img:
                logger.debug(f"No image found for release {rls_id}.")
                _delete_release_from_pending(rls_id, conn)
                continue

            _update_release_image(rls_id, img, conn)
            _delete_release_from_pending(rls_id, conn)

        conn.commit()


def _get_pending_releases(conn: Connection) -> list[int]:
    """
    Return the release ids of the releases pending cover art extraction.

    :param conn: A connection to the database.
    :return: Release IDs pending extraction.
    """
    cursor = conn.execute("SELECT release_id FROM music__releases_images_to_fetch")
    return [row[0] for row in cursor]


def _get_track_path_of_release(rls_id: int, conn: Connection) -> Optional[str]:
    """
    Return the filepath of a track belonging to a release with the provided ID.

    :param rls_id: The ID of the release whose track we are fetching.
    :param conn: A connection to the database.
    :return: The filepath of a track, if there is a track.
    """
    cursor = conn.execute(
        "SELECT filepath FROM music__tracks WHERE release_id = ? LIMIT 1",
        (rls_id,),
    )
    if (track := cursor.fetchone()) and os.path.isfile(track[0]):
        return track[0]

    return None


def _update_release_image(rls_id: int, img: image.T, conn: Connection) -> None:
    """
    Update the image path of a release with the given ID in the database.

    :param rls_id: The ID of the release to update.
    :param image_path: The image path to set for the release.
    :param conn: A conn to the database.
    """
    logger.debug(f"setting image for release {rls_id}.")
    conn.execute(
        "UPDATE music__releases SET image_id = ? WHERE id = ?", (img.id, rls_id)
    )


def _delete_release_from_pending(rls_id: int, conn: Connection) -> None:
    """
    Remove the provided release ID from the pending cover extraction table.

    :param rls_id: The release ID to remove.
    :param conn: A connection to the database.
    """
    logger.debug(f"Removing release {rls_id} from pending cover extraction.")
    conn.execute(
        "DELETE FROM music__releases_images_to_fetch WHERE release_id = ?", (rls_id,)
    )


def save_image(tf: TagFile, conn: Connection) -> Optional[image.T]:
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
    image_path = _save_embedded_image(tf) or _save_external_image(tf)
    if not image_path:
        return None

    try:
        return image.create(image_path, conn)
    except Duplicate as e:
        return e.entity


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
        logger.debug(f"Embedded image with invalid mimetype found for `{tf.path}`.")
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
) -> Generator[tuple[Path, str], None, None]:
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
    filepath = constants.cover_art_dir / f"{sha256sum}.{extension}"

    if filepath.exists():
        logger.debug("Embedded image already saved!")
    else:
        logger.debug(f"Writing image file to {filepath}.")
        with filepath.open("wb") as f:
            f.write(data)

    return filepath
