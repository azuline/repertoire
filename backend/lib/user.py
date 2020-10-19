from __future__ import annotations

import secrets
import string
from dataclasses import dataclass
from sqlite3 import Cursor, Row
from typing import Optional, Tuple

from werkzeug.security import check_password_hash, generate_password_hash

from backend.errors import InvalidUsername, TokenGenerationFailure

TOKEN_LENGTH = 32
PREFIX_LENGTH = 12
VALID_USERNAME_CHARACTERS = set(string.ascii_letters + string.digits)


@dataclass(frozen=True)
class T:
    """
    A user dataclass. This dataclass is frozen (immutable).
    """

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    username: str


def from_row(row: Row) -> T:
    """
    Return a user dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A user dataclass.
    """
    return T(**row)


def from_id(id: int, cursor: Cursor) -> Optional[T]:
    """
    Get a user tuple from the user's ID.

    :param id: The ID of the user to get.
    :param cursor: A cursor to the database.
    :return: The user, if they exist.
    """
    cursor.execute("SELECT id, username FROM system__users WHERE id = ?", (id,))

    if row := cursor.fetchone():
        return from_row(row)


def from_username(username: str, cursor: Cursor) -> Optional[T]:
    """
    Get a user tuple from the user's username.

    :param username: The username of the user to get.
    :param cursor: A cursor to the database.
    :return: The user, if they exist.
    """
    cursor.execute(
        """SELECT id, username FROM system__users WHERE username = ?""",
        (username,),
    )

    if row := cursor.fetchone():
        return from_row(row)


def from_token(token: bytes, cursor: Cursor) -> Optional[T]:
    """
    Get a user tuple from the user's token.

    How it works: We store a unique prefix of each user's token and match on that.

    :param token: The token of the user to get.
    :param cursor: A cursor to the database.
    :return: The user, if they exist.
    """
    if len(token) != TOKEN_LENGTH:
        return None

    token_prefix = token[:PREFIX_LENGTH]

    cursor.execute(
        """SELECT id, username FROM system__users WHERE token_prefix = ?""",
        (token_prefix,),
    )

    if row := cursor.fetchone():
        return from_row(row)


def create(username: str, cursor: Cursor) -> Tuple[T, bytes]:
    """
    Create a user.

    :param username: The username of the user to create.
    :param cursor: A cursor to the database.
    :return: The newly created user and their token.
    :raises InvalidUsername: If the username is not alphanumeric.
    :raises TokenGenerationFailure: If we could not generate a suitable token.
    """
    if not _validate_username(username, cursor):
        raise InvalidUsername

    # Generate the token for the new user and hash it.
    token, token_prefix = _generate_token(cursor)
    token_hash = generate_password_hash(token)

    cursor.execute(
        """
        INSERT INTO system__users (username, token_prefix, token_hash) VALUES (?, ?, ?)
        """,
        (username, token_prefix, token_hash),
    )
    cursor.connection.commit()

    return T(id=cursor.lastrowid, username=username), token


def _validate_username(username: str, cursor: Cursor) -> bool:
    """
    Validate a potential username in two ways: ensure that it is unique and that it is
    alphanumeric.

    :param username: The username to validate.
    :param cursor: A cursor to the database.
    :return: Whether the username is valid.
    """
    # First check to see if the username is in-use.
    cursor.execute("SELECT 1 FROM system__users WHERE username = ?", (username,))
    if cursor.fetchone():
        return False

    # Finally, validate the contents of the username.
    return all(c in VALID_USERNAME_CHARACTERS for c in username)


def _generate_token(cursor: Cursor) -> Tuple[bytes, bytes]:
    """
    Generate a new token with a unique prefix. If we fail to generate a token with a
    unique prefix after 64 rounds, ``TokenGenerationFailure`` will be raised.

    :param cursor: A cursor to the database.
    :return: The token and its prefix, in that order.
    :raises TokenGenerationFailure: If a unique token prefix could not be found.
    """
    # Try to generate a suitable token 64 times.
    for _ in range(64):
        token = secrets.token_bytes(TOKEN_LENGTH)
        prefix = token[:PREFIX_LENGTH]

        # Check for token prefix uniqueness.
        cursor.execute("SELECT 1 FROM system__users WHERE token_prefix = ?", (prefix,))
        if not cursor.fetchone():
            return token, prefix

    # If we do not find a suitable token after 64 cycles, raise an exception.
    raise TokenGenerationFailure


def new_token(user: T, cursor: Cursor) -> bytes:
    """
    Generate a new token for a given user.

    :param user: The user to generate a new token for.
    :param cursor: A cursor to the database.
    :return: The new token.
    :raises TokenGenerationFailure: If we could not generate a suitable token.
    """
    token, token_prefix = _generate_token(cursor)
    token_hash = generate_password_hash(token)

    cursor.execute(
        """UPDATE system__users SET token_prefix = ?, token_hash = ? WHERE id = ?""",
        (token_prefix, token_hash, user.id),
    )
    cursor.connection.commit()

    return token


def check_token(user: T, token: bytes, cursor: Cursor) -> bool:
    """
    Check if a given token is valid for a user.

    :param user: The user to check.
    :param token: The token to check.
    :param cursor: A cursor to the database.
    :return: Whether the token is valid.
    """
    cursor.execute("SELECT token_hash FROM system__users WHERE id = ?", (user.id,))
    if not (row := cursor.fetchone()):
        return False

    return check_password_hash(row["token_hash"], token)
