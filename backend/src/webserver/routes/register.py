import logging
from typing import Optional

from voluptuous import Required, Schema
from src.webserver.util import validate_data

import quart
from quart import Blueprint, Response

from src.library import user

bp = Blueprint("register", __name__, url_prefix="/api/register")

logger = logging.getLogger(__name__)


@bp.route("", methods=["POST"])
@validate_data(
    Schema(
        {
            Required("nickname"): str,
            "code": str,
        }
    )
)
async def register(nickname: str, code: Optional[str] = None) -> Response:
    """
    Sign up for a new account. Requires a valid invite code.

    :query code: The invite code.

    :status 200: Successfully registered.
    """
    # No user exists, create admin user without a code.
    if not user.exists(1, quart.g.db):
        _, token = user.create(nickname, quart.g.db)
        return quart.jsonify({"token": token.hex()})

    # TODO: Invites.
    quart.abort(400)
    raise Exception("For type checker.")


@bp.route("/has-first-user", methods=["GET"])
async def has_first_user() -> Response:
    """
    Return whether a user has registered on this server. This is used on the frontend to
    determine whether to present an initial admin register page.

    :status 200: Response
    """
    return quart.jsonify({"hasFirstUser": user.exists(1, quart.g.db)})
