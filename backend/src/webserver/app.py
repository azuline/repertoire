"""
This module implements the Quart application function pattern. To create a new
Quart app instance, call ``create_app()``.
"""

import logging
import secrets
import sqlite3
import sys

import quart
from quart import Quart, Response
from werkzeug.exceptions import HTTPException

from src.constants import Constants
from src.util import database
from src.webserver.routes import files, graphql, session

SECRET_LENGTH = 32

logger = logging.getLogger(__name__)


def create_app() -> Quart:
    """
    Create, set up, and return a new Quart application object. If a ``config``
    is passed in, it will be modified and used; however, if one is not passed
    in, then the default configuration will be used.

    :param object config: A config object to configure Quart with.

    :return: The created Quart application.
    """
    logger.debug("Creating Quart app.")

    cons = Constants()

    app = Quart(
        __name__,
        static_folder=str(cons.built_frontend_dir),
        static_url_path="/",
    )

    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )

    if app.debug:  # pragma: no cover
        app.config.update(SESSION_COOKIE_SECURE=False)

    app.secret_key = _get_secret_key()

    @app.route("/", methods=["GET"])
    @app.route("/<path>", methods=["GET"])
    async def index(path=None):
        return await app.send_static_file("index.html")

    _register_blueprints(app)
    _register_error_handler(app)
    _register_database_handler(app)

    return app


def _get_secret_key():
    # This function is called whenever webserver starts, but when Sphinx is generating
    # docs, we don't have a database. So just return random bytes.
    logger.debug("Fetching/generating webserver secret key.")
    if "sphinx" in sys.modules:  # pragma: no cover
        return secrets.token_bytes(32)

    with database() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT key FROM system__secret_key LIMIT 1")
        if row := cursor.fetchone():
            return row[0]

        secret_key = secrets.token_bytes(32)
        cursor.execute("INSERT INTO system__secret_key (key) VALUES (?)", (secret_key,))
        conn.commit()

        return secret_key


def _register_blueprints(app: Quart):
    """
    Find all blueprints in the ``src.webserver.routes`` package and register
    them with the passed-in Quart application.

    :param app: The application to register the blueprints with.
    """
    logger.debug("Registering blueprints on Quart app.")
    app.register_blueprint(files.bp)
    app.register_blueprint(graphql.bp)
    app.register_blueprint(session.bp)


def _register_error_handler(app: Quart):
    """
    Register a default error handler on the passed-in Quart application.

    :param app: The application to register the error handler with.
    """
    logger.debug("Registering error handler on Quart app.")

    def handle_error(error):
        response = error.get_response()
        return response.data, response.status_code

    app.register_error_handler(HTTPException, handle_error)


def _register_database_handler(app: Quart):
    """
    Register a per-request database connection opener/closer on the app.

    :param app: The application to register the handler functions with.
    """
    logger.debug("Registering database wrapper for Quart app.")

    @app.before_request
    def connect_to_db() -> None:
        cons = Constants()
        logger.debug(f"Opening a connection to database {cons.database_path}.")
        conn = sqlite3.connect(
            cons.database_path,
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False,
        )
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        quart.g.db = conn  # type: ignore

    @app.after_request
    def close_db_connection(response: Response) -> Response:
        quart.g.db.close()
        logger.debug("Closing the database connection.")
        return response
