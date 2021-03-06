import logging

import quart
from quart import Blueprint

from src.indexer import run_indexer

logger = logging.getLogger(__name__)

bp = Blueprint("dev", __name__, url_prefix="/api/dev")


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
        DELETE FROM system__users WHERE token_prefix = X'000000000000000000000000'
        """
    )

    quart.g.db.execute(
        """
        INSERT INTO system__users (
            nickname,
            token_prefix,
            token_hash,
            csrf_token
        ) VALUES (
            'tester',
            X'000000000000000000000000',
            'pbkdf2:sha256:150000$b26LpXBc$ab7f9cf988532362beed5db5c974a3759aef479042364994df568c0284a5fee2',
            X'0000000000000000000000000000000000000000000000000000000000000000'
        )
        """
    )

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
