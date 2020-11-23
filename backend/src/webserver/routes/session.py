import quart
from quart import Blueprint
from voluptuous import Schema

from src.webserver.util import check_auth, validate_data
from src.webserver.validators import StringBool

bp = Blueprint("session", __name__, url_prefix="/session")


@bp.route("", methods=["POST"])
@check_auth
@validate_data(Schema({"permanent": StringBool}))
async def create_session(permanent=False):
    """
    Generate and return a new session.

    :reqheader Authorization: An authorization token.
    :status 201: Successfully generated a session.
    :status 401: Invalid authorization token.
    """
    quart.session["user_id"] = quart.g.user.id
    quart.session.permanent = permanent
    return "success", 201
