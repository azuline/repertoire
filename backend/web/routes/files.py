import os

import flask
from flask import Blueprint, Response
from voluptuous import Schema

from backend.lib import release, track
from backend.web.util import check_auth, validate_data
from backend.web.validators import StringBool

bp = Blueprint("files", __name__, url_prefix="/files")


@bp.route("/tracks/<track_id>", methods=["GET"])
@check_auth()
def get_track(track_id: int):
    """
    Accepts a track ID and returns the track file.
    """
    if not (trk := track.from_id(track_id, flask.g.db)):
        flask.abort(404)

    ext = os.path.splitext(trk.filepath)[1]
    return flask.send_file(trk.filepath, attachment_filename=f"track{track_id}{ext}")


@bp.route("/covers/<release_id>", methods=["GET"])
@check_auth()
@validate_data(Schema({"thumbnail": StringBool}))
def get_cover(release_id: int, thumbnail: bool = False) -> Response:
    """
    Accepts a release ID and returns the cover art.
    """
    if not (rls := release.from_id(release_id, flask.g.db)):
        flask.abort(404)

    ext = os.path.splitext(rls.image_path)[1]
    return flask.send_file(
        rls.image_path, attachment_filename=f"cover{release_id}{ext}"
    )
