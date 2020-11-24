import quart
from quart import Blueprint
from voluptuous import Schema

from src.webserver.util import check_auth, validate_data
from src.webserver.validators import StringBool

bp = Blueprint("session", __name__, url_prefix="/session")


@bp.route("", methods=["POST"])
@check_auth()
@validate_data(Schema({"permanent": StringBool}))
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

    quart.g.db.execute(
        "SELECT csrf_token FROM system__users WHERE id = ?", (quart.g.user.id,)
    )
    csrf_token = quart.g.db.fetchone()[0]

    return quart.jsonify({"csrfToken": csrf_token.hex()}), 201
