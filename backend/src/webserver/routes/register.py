import logging

import quart
from quart import Blueprint, Response
from voluptuous import Required, Schema

from src.library import user
from src.webserver.util import validate_data

bp = Blueprint("register", __name__, url_prefix="/api/register")

logger = logging.getLogger(__name__)


@bp.route("", methods=["POST"])
@validate_data(
    Schema(
        {
            Required("nickname"): str,
        }
    )
)
async def register(nickname: str) -> Response:
    """
    Sign up for a new account. At the moment, this only allows for a first user to be
    registered. Soon, another PR will increase the scope of this endpoint to allow
    invited users to register.

    Returns the user's new authorization token as the response body. The response has
    the following format:

    .. code-block:: json

       {
         "token": "hex-encoded token"
       }

    :query nickname: The nickname to register with.

    :status 200: Successfully registered.
    """
    if user.exists(1, quart.g.db):
        # Already have a user; abort.
        quart.abort(401)

    _, token = user.create(nickname, quart.g.db)
    quart.g.db.commit()

    return quart.jsonify({"token": token.hex()})


@bp.route("/has-first-user", methods=["GET"])
async def has_first_user() -> Response:
    """
    Return whether a user has registered on this server. This is used on the frontend to
    determine whether to present an initial admin register page.

    :status 200: Response
    """
    return quart.jsonify({"hasFirstUser": user.exists(1, quart.g.db)})
