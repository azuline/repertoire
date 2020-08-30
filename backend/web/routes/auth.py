import flask

from backend.web.util import check_auth

bp = flask.Blueprint("user", __name__)


@bp.route("/api/user", methods=["GET"])
@check_auth
def get_user():
    """Returns the current user."""
    return flask.jsonify({"username": flask.g.current_user})
