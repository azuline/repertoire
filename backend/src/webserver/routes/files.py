import os

import quart
from quart import Blueprint, Response
from voluptuous import Schema

from src.library import image, track
from src.webserver.util import check_auth, validate_data
from src.webserver.validators import StringBool

bp = Blueprint("files", __name__, url_prefix="/files")


@bp.route("/tracks/<track_id>", methods=["GET"])
@check_auth()
async def get_track(track_id: int):
    """
    Returns a track's audio file.

    :param track_id: The ID of the track to fetch.

    :reqheader Authorization: An authorization token.
    :status 200: Audio file exists and is returned.
    :status 404: Track or audio file does not exist.
    """
    if not (trk := track.from_id(track_id, quart.g.db)):
        quart.abort(404)

    ext = os.path.splitext(trk.filepath)[1]

    try:
        return await quart.send_file(
            trk.filepath,
            attachment_filename=f"track{ext}",
            cache_timeout=604_800,
        )
    except FileNotFoundError:
        quart.abort(404)


@bp.route("/images/<id>", methods=["GET"])
@check_auth()
@validate_data(Schema({"thumbnail": StringBool}))
async def get_cover(id: int, thumbnail: bool = False) -> Response:
    """
    Returns an image stored on the backend.

    :param id: The ID of the image to fetch.
    :query thumbnail: Whether to return a thumbnail (300x300) version of the image.

    :reqheader Authorization: An authorization token.
    :status 200: Image exists and is returned.
    :status 404: Image does not exist.
    """
    if not (img := image.from_id(id, quart.g.db)):
        quart.abort(404)

    ext = os.path.splitext(img.path)[1]

    try:
        return await quart.send_file(
            image.thumbnail_path(img) if thumbnail else img.path,
            attachment_filename=f"image{ext}",
            cache_timeout=604_800,
        )
    except FileNotFoundError:
        quart.abort(404)
