import logging
import os
from hashlib import sha256
from pathlib import Path
from typing import Optional

import click
from PIL import Image
from tagfiles import TagFile

from backend.constants import COVER_ART_DIR
from backend.util import database

logger = logging.getLogger()

MIME_TO_EXTS = {"image/jpeg": "jpg", "image/png": "png"}


def save_pending_images():
    """
    For the releases with pending images-to-save, look at their
    first track for a cover art to save.
    """
    click.echo("Saving cover art for newly-found releases.")
    logger.info("Saving cover art for newly-found releases.")

    with database() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT rls_id FROM music__releases_to_fetch_images""")
        rls_ids = [row[0] for row in cursor.fetchall()]

    for rls_id in rls_ids:
        logger.debug(f"Searching for cover art in release {rls_id}.")

        cursor.execute(
            "SELECT filepath FROM music__tracks WHERE rls_id = ? LIMIT 1", (rls_id,)
        )
        track = cursor.fetchone()
        if not track or not os.path.isfile(track["filepath"]):
            logger.debug(f"No tracks found for release {rls_id}.")
            continue

        tf = TagFile(track["filepath"])
        image_path = save_image(tf)
        if not image_path:
            logger.debug(f"No image found for release {rls_id}.")
            continue

        logger.debug(f"Setting image for release {rls_id}.")
        cursor.execute(
            """UPDATE music__releases SET image_path = ? WHERE id = ?""",
            (image_path, rls_id),
        )
        cursor.execute(
            """DELETE FROM music__releases_to_fetch_images WHERE rls_id = ?""",
            (rls_id,),
        )
        cursor.connection.commit()

        generate_thumbnail(image_path)


def save_image(tf: TagFile) -> Optional[str]:
    """
    If the track has attached cover art, save it to the cover_arts dir under
    the sha256 of the cover art.

    Otherwise, look in the directory of the file and the directory above it for
    a `cover` or `folder` file (case insensitive) if embedded art does not
    exist.

    If neither exist, return None.
    """
    return _save_embedded_image(tf) or _save_external_image(tf)


def _save_embedded_image(tf: TagFile) -> Optional[str]:
    if not tf.image_mime:
        logger.debug("No embedded image found for `{tf.path}`.")
        return None

    extension = MIME_TO_EXTS.get(tf.image_mime, None)

    if not extension:
        logger.debug("Embedded image with invalid mimetype found for `{tf.path}`.")
        return None

    return _save_image_file(tf.image, extension)


def _save_external_image(tf: TagFile) -> Optional[str]:
    filenames = {
        "cover.jpg": "jpg",
        "cover.jpeg": "jpg",
        "cover.png": "png",
        "folder.jpg": "jpg",
        "folder.jpeg": "jpg",
        "folder.png": "png",
    }

    track_path = Path(tf.path)
    for dir_ in (track_path.parent, track_path.parent.parent):
        for filename, ext in filenames.items():
            filepath = dir_ / filename
            if filepath.exists():
                with filepath.open("rb") as f:
                    return _save_image_file(f.read(), ext)

    return None


def _save_image_file(data: bytes, extension: str) -> str:
    hash_ = sha256(data).hexdigest()

    filepath = COVER_ART_DIR / f"{hash_}.{extension}"

    if filepath.exists():
        logger.debug("Embedded image already saved!")
    else:
        with open(filepath, "wb") as f:
            f.write(data)

    return str(filepath)


def generate_thumbnail(image_path: str) -> None:
    logger.debug(f"Generating thumbnail for {image_path}.")
    image = Image.open(image_path).convert("RGB")
    image.thumbnail((300, 300))
    image.save(f"{image_path}.thumbnail", "JPEG")
