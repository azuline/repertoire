import logging

import quart
from quart import Blueprint

from src.indexer import run_indexer
from src.library import user

logger = logging.getLogger(__name__)

bp = Blueprint("dev", __name__, url_prefix="/api/dev")

ZERO_TOKEN_HASH = "pbkdf2:sha256:150000$b26LpXBc$ab7f9cf988532362beed5db5c974a3759aef479042364994df568c0284a5fee2"  # noqa


@bp.route("/testuser", methods=["POST"])
async def make_test_user() -> tuple[str, int]:
    """
    **Developer endpoint.**

    Creates a test user (all keys set to 0s) if we are in debug mode,
    otherwise raises a 404.
    """
    if not quart.current_app.debug:
        quart.abort(404)

    logger.info("Making test user.")

    # Delete the existing test user.
    quart.g.db.execute(
        """
        DELETE FROM system__users WHERE token_prefix = ?
        """,
        (b"\x00" * 12,),
    )

    # Create a new test user.
    cursor = quart.g.db.execute(
        """
        INSERT INTO system__users
        (nickname, token_prefix, token_hash, csrf_token)
        VALUES ('tester', ?, ?, ?)
        """,
        (
            b"\x00" * 12,
            ZERO_TOKEN_HASH,
            b"\x00" * 32,
        ),
    )
    user.post_create(cursor.lastrowid, quart.g.db)

    quart.g.db.commit()

    return "success", 200


@bp.route("/indexlib", methods=["POST"])
async def index_library() -> tuple[str, int]:
    """
    **Developer endpoint.**

    Indexes the library in a blocking request if we are in debug mode,
    otherwise raises a 404.
    """
    if not quart.current_app.debug:
        quart.abort(404)

    logger.info("Indexing library in blocking request.")

    # This better be under 30s...
    run_indexer()

    return "success", 200
