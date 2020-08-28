import os

import flask

from src.util import database
from src.web.util import check_auth

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
        cursor.close()

    ext = os.path.splitext(filepath)[1]
    return flask.send_file(filepath, attachment_filename=f"track{track_id}{ext}")


@bp.route("/files/covers/<release_id>", methods=["GET"])
@check_auth
def get_cover(release_id):
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
        cursor.close()

    ext = os.path.splitext(filepath)[1]
    return flask.send_file(filepath, attachment_filename=f"cover{release_id}{ext}")
