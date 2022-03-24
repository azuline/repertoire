import logging
from typing import Optional

import quart
from quart import Blueprint, Response
from voluptuous import Required, Schema

from src.library import invite, user
from src.webserver.util import validate_data

bp = Blueprint("register", __name__, url_prefix="/api")

logger = logging.getLogger(__name__)


@bp.route("/register", methods=["POST"])
@validate_data(
    Schema(
        {
            Required("nickname"): str,
            "inviteCode": str,
        }
    )
)
async def register(nickname: str, inviteCode: Optional[str] = None) -> Response:
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
    if not inviteCode:
        token = _register_admin(nickname)
    else:
        token = _register_user(nickname, inviteCode)

    return quart.jsonify({"token": token.hex()})


def _register_admin(nickname: str) -> bytes:
    if user.exists(1, quart.g.db):
        # Already have a user; abort.
        logger.debug("Already have an admin user.")
        quart.abort(401)

    _, token = user.create(nickname, quart.g.db)
    quart.g.db.commit()

    return token


def _register_user(nickname: str, hex_invite_code: str) -> bytes:
    try:
        invite_code = bytes.fromhex(hex_invite_code)
    except ValueError:
        logger.debug("Failed to deserialize token from bytes.")
        quart.abort(401)
        return b""

    inv = invite.from_code(invite_code, quart.g.db)
    if inv is None:
        quart.abort(401)
        return b""

    usr, token = user.create(nickname, quart.g.db)
    invite.update(inv, conn=quart.g.db, used_by=usr)
    quart.g.db.commit()

    return token


@bp.route("/register/has-first-user", methods=["GET"])
async def has_first_user() -> Response:
    """
    Return whether a user has registered on this server. This is used on the frontend to
    determine whether to present an initial admin register page.

    :status 200: Response
    """
    return quart.jsonify({"hasFirstUser": user.exists(1, quart.g.db)})


@bp.route("/register/validate-invite", methods=["GET"])
@validate_data(
    Schema(
        {
            Required("inviteCode"): str,
        }
    )
)
async def validate_code(inviteCode: str) -> Response:
    """
    Check whether an invite code is valid or not.

    Returns the invite's status as the response body. The response has the following
    format:

    .. code-block:: json

       {
         "valid": False
       }

    :query inviteCode: The hex-encoded invite code to check.

    :status 200: Successfully determined invite code status.
    """
    try:
        invite_code = bytes.fromhex(inviteCode)
    except ValueError:
        logger.debug("Failed to deserialize token from bytes.")
        return quart.jsonify({"valid": False})

    return quart.jsonify(
        {"valid": invite.from_code(invite_code, quart.g.db) is not None}
    )
