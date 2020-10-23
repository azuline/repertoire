import os

import quart
from quart import Blueprint, Response
from voluptuous import Schema

from backend.library import release, track
from backend.webserver.util import check_auth, validate_data
from backend.webserver.validators import StringBool

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
        return await quart.send_file(trk.filepath, attachment_filename=f"track{ext}")
    except FileNotFoundError:
        quart.abort(404)


@bp.route("/covers/<release_id>", methods=["GET"])
@check_auth()
@validate_data(Schema({"thumbnail": StringBool}))
async def get_cover(release_id: int, thumbnail: bool = False) -> Response:
    """
    Returns a release's cover art image.

    :param release_id: The ID of the release whose cover to fetch.
    :query thumbnail: Whether to return a thumbnail (300x300) version of the image.

    :reqheader Authorization: An authorization token.
    :status 200: Cover image exists and is returned.
    :status 404: Release or cover image does not exist.
    """
    if not (rls := release.from_id(release_id, quart.g.db)):
        quart.abort(404)

    ext = os.path.splitext(rls.image_path)[1]
    try:
        return await quart.send_file(
            rls.image_path.with_suffix(".thumbnail") if thumbnail else rls.image_path,
            attachment_filename=f"cover{ext}",
        )
    except FileNotFoundError:
        quart.abort(404)
