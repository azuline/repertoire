"""
This module contains various helper functions, endpoint decorators, and
utilities for the web application package.
"""

import functools
import json
import logging
import secrets
from typing import Optional

import quart
from voluptuous import Invalid
from werkzeug.datastructures import Headers

from src.library import user

logger = logging.getLogger(__name__)


def check_auth(csrf=False):
    """
    Ensure that the wrapped function can only be accessed by a request that
    passes a valid APIKey in the header. If the API Key is not present or
    incorrect, a ``HTTPException`` with a status code of 401 will be raised.

    :param Callable func: The function to be decorated.

    :return: The decorated function.
    :rtype: Callable
    :raises: HTTPException
    """

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            quart.g.user = None

            logger.debug("Attempting to authenticate request.")

            if _check_session_auth(csrf):
                logger.debug(
                    "Successfully authenticated with session as "
                    f"user {quart.g.user.id}."  # type: ignore
                )
                return await func(*args, **kwargs)

            if _check_token_auth():
                logger.debug(
                    "Successfully authenticated with token as "
                    f"user {quart.g.user.id}."  # type: ignore
                )
                return await func(*args, **kwargs)

            # Failed to authenticate, abort!
            logger.debug("Failed to authenticate request.")
            quart.abort(401)

        return wrapper

    return decorator


def _check_session_auth(csrf: bool) -> bool:
    """
    Check to see if the current request has valid session authentication. If ``csrf`` is
    set, validate the CSRF header as well.

    If it is valid, set `quart.g.user` and return ``True``, otherwise return ``False``.

    :param csrf: Whether to validate the CSRF header.
    :return: Whether current request has valid session authentication.
    """
    try:
        quart.g.user = user.from_id(  # type: ignore
            quart.session["user_id"],
            quart.g.db,
        )
    except KeyError:
        return False

    if quart.g.user and csrf and not _check_csrf():
        quart.abort(400)

    return bool(quart.g.user)


def _check_csrf():
    """
    Check if the current request contains a valid ``X-CSRF-Token`` header.

    :return: Whether the current request contains a valid CSRF header.
    """
    logger.debug("Checking CSRF token of request.")
    try:
        provided_csrf_token = bytes.fromhex(quart.request.headers["X-CSRF-Token"])
    except (KeyError, TypeError, ValueError):
        return False

    cursor = quart.g.db.execute(
        "SELECT csrf_token FROM system__users WHERE id = ?", (quart.g.user.id,)
    )
    stored_csrf_token = cursor.fetchone()[0]

    return secrets.compare_digest(provided_csrf_token, stored_csrf_token)


def _check_token_auth() -> bool:
    """
    Check to see if the current request has valid token authentication.

    If it is valid, set `quart.g.user` and return ``True``, otherwise return ``False``.

    :return: Whether current request has valid token authentication.
    """
    token_str = _get_token(quart.request.headers)
    if token_str is None:
        logger.debug("Failed to parse token.")
        return False

    try:
        token = bytes.fromhex(token_str)
    except ValueError:
        logger.debug("Failed to deserialize token from bytes.")
        return False

    quart.g.user = user.from_token(token, quart.g.db)  # type: ignore
    return quart.g.user is not None


def _get_token(headers: Headers) -> Optional[str]:
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
    except (AttributeError, KeyError, TypeError, ValueError):
        pass

    return None


def validate_data(schema):
    """
    This decorates a quart endpoint. Given a voluptuous schema, this returns a
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
        async def new_func(*args, **kwargs):
            logger.debug("Validating request data against the schema.")
            try:
                kwargs.update(schema(await _get_request_data()))
            except Invalid as e:
                quart.abort(400, description=f"Invalid data: {e.msg}")

            return await func(*args, **kwargs)

        return new_func

    return wrapper


async def _get_request_data():
    """
    Helper function for ``validate_data``. Depending on the request method,
    it decides whether or not to process the query_string or form. If the
    form data is not valid JSON, an Invalid exception will be raised.

    :return: The request data (empty dict if no data present).
    :rtype: dict
    :raises: voluptuous.Invalid
    """
    if quart.request.method == "GET":
        return quart.request.args.to_dict()

    try:
        data = await quart.request.get_data()
        return json.loads(data) if data else {}
    except ValueError:  # JSONDecodeError subclasses ValueError.
        raise Invalid("Unable to parse data.")
