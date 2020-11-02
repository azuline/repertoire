"""
This module implements the Quart application function pattern. To create a new
Quart app instance, call ``create_app()``.
"""

import logging
import sqlite3

import quart
from quart import Quart, Response
from werkzeug.exceptions import HTTPException

from src.constants import DATABASE_PATH, PROJECT_ROOT
from src.webserver.routes import files, graphql

STATIC_FOLDER = PROJECT_ROOT / "frontend" / "build"

logger = logging.getLogger(__name__)


def create_app() -> Quart:
    """
    Create, set up, and return a new Quart application object. If a ``config``
    is passed in, it will be modified and used; however, if one is not passed
    in, then the default configuration will be used.

    :param object config: A config object to configure Quart with.

    :return: The created Quart application.
    """
    app = Quart(__name__, static_folder=str(STATIC_FOLDER), static_url_path="/")

    if app.debug:  # Disable CORS if we are in debug mode.
        from quart_cors import cors

        cors(app)

    @app.route("/", methods=["GET"])
    @app.route("/<path>", methods=["GET"])
    async def index(path=None):
        return await app.send_static_file("index.html")

    _register_blueprints(app)
    _register_error_handler(app)
    _register_database_handler(app)

    return app


def _register_blueprints(app: Quart):
    """
    Find all blueprints in the ``src.webserver.routes`` package and register
    them with the passed-in Quart application.

    :param app: The application to register the blueprints with.
    """
    app.register_blueprint(files.bp)
    app.register_blueprint(graphql.bp)


def _register_error_handler(app: Quart):
    """
    Register a default error handler on the passed-in Quart application.

    :param app: The application to register the error handler with.
    """

    def handle_error(error):
        response = error.get_response()
        return response.data, response.status_code

    app.register_error_handler(HTTPException, handle_error)


def _register_database_handler(app: Quart):
    """
    Register a per-request database connection opener/closer on the app.

    :param app: The application to register the handler functions with.
    """

    @app.before_request
    def connect_to_db() -> None:
        conn = sqlite3.connect(
            DATABASE_PATH,
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False,
        )
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        quart.g.db = conn.cursor()

    @app.after_request
    def close_db_connection(response: Response) -> None:
        quart.g.db.connection.close()
        return response
