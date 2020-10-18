import os

import flask
from voluptuous import Schema

from backend.util import database
from backend.web.util import check_auth, validate_data
from backend.web.validators import StringBool

bp = flask.Blueprint("files", __name__)


@bp.route("/files/tracks/<track_id>", methods=["GET"])
@check_auth
def get_track(track_id):
    """Accepts a track ID and returns the track file."""
    with database() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT filepath FROM music__tracks WHERE id = ?""", (track_id,)
        )

        row = cursor.fetchone()
        if not row:
            flask.abort(404)

        filepath = row["filepath"]

    ext = os.path.splitext(filepath)[1]
    return flask.send_file(filepath, attachment_filename=f"track{track_id}{ext}")


@bp.route("/files/covers/<release_id>", methods=["GET"])
@check_auth
@validate_data(Schema({"thumbnail": StringBool}))
def get_cover(release_id, thumbnail=False):
    """Accepts a release ID and returns the cover art."""
    with database() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT image_path FROM music__releases WHERE id = ?""", (release_id,)
        )

        row = cursor.fetchone()
        if not row:
            flask.abort(404)

        filepath = row["image_path"]

    ext = os.path.splitext(filepath)[1]
    return flask.send_file(filepath, attachment_filename=f"cover{release_id}{ext}")
