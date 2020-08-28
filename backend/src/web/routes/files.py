import os

import flask

from src.util import database
from src.web.util import check_auth

bp = flask.Blueprint("library", __name__, url_prefix="/files")


@bp.route("/tracks/<track_id>", methods=["GET"])
@check_auth
def get_music_file(track_id):
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
