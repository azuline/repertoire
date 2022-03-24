import quart
from quart import Blueprint
from voluptuous import Schema

from src.webserver.util import check_auth, validate_data

bp = Blueprint("session", __name__, url_prefix="/api")


@bp.route("/session", methods=["POST"])
@check_auth()
@validate_data(Schema({"permanent": bool}))
async def create_session(permanent=False):
    """
    Generate and return a new session.

    Returns the user's CSRF token as the response body. The response has the following
    format:

    .. code-block:: json

       {
         "csrfToken": "hex-encoded token"
       }

    :reqheader Authorization: An authorization token.
    :status 201: Successfully generated a session.
    :status 401: Invalid authorization token.
    """
    quart.session["user_id"] = quart.g.user.id
    quart.session.permanent = permanent

    return quart.jsonify({"csrfToken": quart.g.user.csrf_token.hex()}), 201


@bp.route("/session", methods=["DELETE"])
@check_auth(csrf=True)
async def delete_session():
    """
    Delete the session cookie of the requesting user.

    As our cookies are HTTPOnly, clients cannot delete their own sessions. Thus, we must
    expose this endpoint.

    :status 200: Successfully deleted the session.
    """
    quart.session.clear()

    return "success"
