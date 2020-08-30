"""
This module contains various helper functions, endpoint decorators, and
utilities for the web application package.
"""

import functools
import json

import flask
from voluptuous import Invalid

from backend.util import database


def check_auth(func):
    """
    Ensure that the wrapped function can only be accessed by a request that
    passes a valid APIKey in the header. If the API Key is not present or
    incorrect, a ``HTTPException`` with a status code of 401 will be raised.

    :param Callable func: The function to be decorated.

    :return: The decorated function.
    :rtype: Callable
    :raises: HTTPException
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            token = bytes.fromhex(_get_token(flask.request.headers))
        except (TypeError, ValueError):
            flask.abort(401)

        with database() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT username FROM system__users WHERE token = ?""",
                (token,),
            )
            row = cursor.fetchone()
            if not row:
                flask.abort(401)

            flask.g.current_user = row["username"]

        return func(*args, **kwargs)

    return wrapper


def _get_token(headers):
    """
    Given the HTTP headers, parse the Authorization header for the token and
    extract the API Key. Returns ``None`` if the Authorization header is not
    present or malformed.

    :param dict headers: A dict of HTTP headers.

    :return: The API key.
    :rtype: str
    """
    try:
        key, value = headers["Authorization"].split()
        if key == "Token":
            return value
    except (KeyError, TypeError, ValueError):
        pass

    return None


def validate_data(schema):
    """
    This decorates a flask endpoint. Given a voluptuous schema, this returns a
    decorator that parses the argument/form data, depending on the request
    method, and validates it against the schema. If the schema is valid, then
    the function will be called, expanding the schema keys as keyword
    arguments.  If the schema is invalid, a HTTPException with a status code of
    400 will be raised.

    :param voluptuous.Schema schema: The schema to validate against.

    :return: A decorator that will validate against the provided schema.
    :rtype: Callable
    :raises: HTTPException
    """

    def wrapper(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            try:
                kwargs.update(schema(_get_request_data()))
            except Invalid as e:
                flask.abort(400, description=f"Invalid data: {e.msg}")

            return func(*args, **kwargs)

        return new_func

    return wrapper


def _get_request_data():
    """
    Helper function for ``validate_data``. Depending on the request method,
    it decides whether or not to process the query_string or form. If the
    form data is not valid JSON, an Invalid exception will be raised.

    :return: The request data (empty dict if no data present).
    :rtype: dict
    :raises: voluptuous.Invalid
    """
    if flask.request.method == "GET":
        return flask.request.args.to_dict()

    try:
        data = flask.request.get_data()
        return json.loads(data) if data else {}
    except ValueError:  # JSONDecodeError subclasses ValueError.
        raise Invalid("Unable to parse data.")
