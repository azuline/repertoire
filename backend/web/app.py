"""
This module implements the Flask application function pattern. To create a new
Flask app instance, call ``create_app()``.
"""

import logging
import sqlite3

import flask
from flask import Flask, Response
from werkzeug.exceptions import HTTPException

from backend.constants import DATABASE_PATH, PROJECT_ROOT
from backend.web.routes import files, graphql

STATIC_FOLDER = PROJECT_ROOT / "frontend" / "build"

logger = logging.getLogger(__name__)


def create_app() -> Flask:
    """
    Create, set up, and return a new Flask application object. If a ``config``
    is passed in, it will be modified and used; however, if one is not passed
    in, then the default configuration will be used.

    :param object config: A config object to configure Flask with.

    :return: The created Flask application.
    """
    app = flask.Flask(__name__, static_folder=str(STATIC_FOLDER), static_url_path="/")

    if app.debug:  # Disable CORS if we are in debug mode.
        from flask_cors import CORS

        CORS(app)

    @app.route("/", methods=["GET"])
    @app.route("/<path>", methods=["GET"])
    def index(path=None):
        return app.send_static_file("index.html")

    with app.app_context():
        _register_blueprints(app)
        _register_error_handler(app)
        _register_database_handler(app)

    return app


def _register_blueprints(app: Flask):
    """
    Find all blueprints in the ``backend.web.routes`` package and register
    them with the passed-in Flask application.

    :param app: The application to register the blueprints with.
    """
    app.register_blueprint(files.bp)
    app.register_blueprint(graphql.bp)


def _register_error_handler(app: Flask):
    """
    Register a default error handler on the passed-in Flask application.

    :param app: The application to register the error handler with.
    """

    def handle_error(error):
        response = error.get_response()
        return response.data, response.status_code

    app.register_error_handler(HTTPException, handle_error)


def _register_database_handler(app: Flask):
    """
    Register a per-request database connection opener/closer on the app.

    :param app: The application to register the handler functions with.
    """

    @app.before_request
    def connect_to_db() -> None:
        conn = sqlite3.connect(DATABASE_PATH, detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        flask.g.db = conn.cursor()

    @app.after_request
    def close_db_connection(response: Response) -> None:
        flask.g.db.connection.close()
        return response
