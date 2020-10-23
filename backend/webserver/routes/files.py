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
    Accepts a track ID and returns the track file.
    """
    if not (trk := track.from_id(track_id, quart.g.db)):
        quart.abort(404)

    ext = os.path.splitext(trk.filepath)[1]
    return await quart.send_file(trk.filepath, attachment_filename=f"track{ext}")


@bp.route("/covers/<release_id>", methods=["GET"])
@check_auth()
@validate_data(Schema({"thumbnail": StringBool}))
async def get_cover(release_id: int, thumbnail: bool = False) -> Response:
    """
    Accepts a release ID and returns the cover art.
    """
    if not (rls := release.from_id(release_id, quart.g.db)):
        quart.abort(404)

    image_path = rls.image_path
    if thumbnail:
        image_path += ".thumbnail"

    ext = os.path.splitext(rls.image_path)[1]
    return await quart.send_file(image_path, attachment_filename=f"cover{ext}")
