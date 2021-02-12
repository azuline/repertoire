from __future__ import annotations

import logging
import secrets
import string
from dataclasses import dataclass
from sqlite3 import Cursor, Row
from typing import Dict, Optional, Tuple, Union

from werkzeug.security import check_password_hash, generate_password_hash

from src.errors import InvalidNickname, TokenGenerationFailure
from src.util import update_dataclass

TOKEN_LENGTH = 32
PREFIX_LENGTH = 12
VALID_USERNAME_CHARACTERS = set(string.ascii_letters + string.digits)

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class T:
    """A user dataclass."""

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    nickname: str


def exists(id: int, cursor: Cursor) -> bool:
    """
    Return whether a user exists with the given ID.

    :param id: The ID to check.
    :return: Whether a user has the given ID.
    """
    cursor.execute("SELECT 1 FROM system__users WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Union[Dict, Row]) -> T:
    """
    Return a user dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A user dataclass.
    """
    return T(**row)  # type: ignore


def from_id(id: int, cursor: Cursor) -> Optional[T]:
    """
    Get a user tuple from the user's ID.

    :param id: The ID of the user to get.
    :param cursor: A cursor to the database.
    :return: The user, if they exist.
    """
    cursor.execute("SELECT id, nickname FROM system__users WHERE id = ?", (id,))

    if row := cursor.fetchone():
        logger.debug("Fetched user {id}.")
        return from_row(row)

    logger.debug("Failed to fetch user {id}.")
    return None


def from_nickname(nickname: str, cursor: Cursor) -> Optional[T]:
    """
    Get a user tuple from the user's nickname.

    :param nickname: The nickname of the user to get.
    :param cursor: A cursor to the database.
    :return: The user, if they exist.
    """
    cursor.execute(
        "SELECT id, nickname FROM system__users WHERE nickname = ?",
        (nickname,),
    )

    if row := cursor.fetchone():
        logger.debug(f"Fetched user {row['id']} from nickname {nickname}.")
        return from_row(row)

    logger.debug(f"Failed to fetch user from nickname {nickname}.")
    return None


def from_token(token: bytes, cursor: Cursor) -> Optional[T]:
    """
    Get a user tuple from the user's token. The returned user is necessarily
    authenticated.

    How it works: We store a unique prefix of each user's token and match on that.

    :param token: The token of the user to get.
    :param cursor: A cursor to the database.
    :return: The user, if they exist.
    """
    if len(token) != TOKEN_LENGTH:
        return None

    token_prefix = token[:PREFIX_LENGTH]

    cursor.execute(
        "SELECT id, nickname FROM system__users WHERE token_prefix = ?",
        (token_prefix,),
    )

    if row := cursor.fetchone():
        usr = from_row(row)
        if check_token(usr, token, cursor):
            logger.debug(f"Fetched user {usr.id} from token {token_prefix.hex()}.")
            return usr

    logger.debug(f"Failed to fetch user from token {token_prefix.hex()}.")
    return None


def create(nickname: str, cursor: Cursor) -> Tuple[T, bytes]:
    """
    Create a user.

    :param nickname: The nickname of the user to create.
    :param cursor: A cursor to the database.
    :return: The newly created user and their token.
    :raises InvalidNickname: If the nickname is invalid.
    :raises TokenGenerationFailure: If we could not generate a suitable token.
    """
    if not _validate_nickname(nickname):
        raise InvalidNickname

    # Generate the token for the new user and hash it.
    token, token_prefix = _generate_token(cursor)
    token_hash = generate_password_hash(token)

    # Generate a CSRF token.
    csrf_token = secrets.token_bytes(TOKEN_LENGTH)

    cursor.execute(
        """
        INSERT INTO system__users
        (nickname, token_prefix, token_hash, csrf_token)
        VALUES (?, ?, ?, ?)
        """,
        (nickname, token_prefix, token_hash, csrf_token),
    )

    logger.info(f"Created user {nickname} with ID {cursor.lastrowid}.")

    return T(id=cursor.lastrowid, nickname=nickname), token


def update(usr: T, cursor: Cursor, **changes) -> T:
    """
    Update a user and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    :param usr: The user to update.
    :param cursor: A cursor to the database.
    :param nickname: New user nickname.
    :type  nickname: :py:obj:`str`
    :return: The updated user.
    """
    if changes.get("nickname", None) and not _validate_nickname(changes["nickname"]):
        raise InvalidNickname

    cursor.execute(
        """
        UPDATE system__users
        SET nickname = ?
        WHERE id = ?
        """,
        (changes.get("nickname", usr.nickname), usr.id),
    )

    logger.info(f"Updated user {usr.id} with {changes}.")

    return update_dataclass(usr, **changes)


def new_token(usr: T, cursor: Cursor) -> bytes:
    """
    Generate a new token for a given user.

    :param usr: The user to generate a new token for.
    :param cursor: A cursor to the database.
    :return: The new token.
    :raises TokenGenerationFailure: If we could not generate a suitable token.
    """
    token, token_prefix = _generate_token(cursor)
    token_hash = generate_password_hash(token)

    cursor.execute(
        "UPDATE system__users SET token_prefix = ?, token_hash = ? WHERE id = ?",
        (token_prefix, token_hash, usr.id),
    )

    logger.info(f"Updated token of user {usr.id}.")

    return token


def check_token(usr: T, token: bytes, cursor: Cursor) -> bool:
    """
    Check if a given token is valid for a user.

    :param usr: The user to check.
    :param token: The token to check.
    :param cursor: A cursor to the database.
    :return: Whether the token is valid.
    """
    cursor.execute("SELECT token_hash FROM system__users WHERE id = ?", (usr.id,))
    if not (row := cursor.fetchone()):
        logger.debug(f"Did not find token for user {usr.id}.")
        return False

    return check_password_hash(row["token_hash"], token)


def _validate_nickname(nickname: str) -> bool:
    """
    Validate a potential nickname:

    - Ensure that it is less than 24 characters.

    :param nickname: The nickname to validate.
    :param cursor: A cursor to the database.
    :return: Whether the nickname is valid.
    """
    return len(nickname) < 24


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

        logger.debug("Token prefix clashed with existing token.")

    # If we do not find a suitable token after 64 cycles, raise an exception.
    logger.info("Failed to generate token after 64 cycles o.O")  # pragma: no cover
    raise TokenGenerationFailure(  # pragma: no cover
        "Failed to generate token after 64 cycles o.O"
    )
