import logging

import quart
from quart import Blueprint, Response

from src.library import user

bp = Blueprint("register", __name__, url_prefix="/api/register")

logger = logging.getLogger(__name__)


@bp.route("", methods=["POST"])
async def register() -> Response:
    """
    Sign up for a new account. Requires a valid invite code.

    :status 200: Successfully registered.
    """
    return quart.jsonify({"status": "success"})


@bp.route("/has-first-user", methods=["GET"])
async def has_first_user() -> Response:
    """
    Return whether a user has registered on this server. This is used on the frontend to
    determine whether to present an initial admin register page.

    :status 200: Response
    """
    return quart.jsonify({"hasFirstUser": user.exists(1, quart.g.db)})
