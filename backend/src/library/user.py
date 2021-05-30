from __future__ import annotations

import logging
import secrets
import string
from dataclasses import dataclass
from sqlite3 import Connection, Row
from typing import Optional, Union

from werkzeug.security import check_password_hash, generate_password_hash

from src.enums import CollectionType, PlaylistType
from src.errors import InvalidNickname, TokenGenerationFailure
from src.tasks import huey
from src.util import database, update_dataclass

from . import collection, playlist

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
    #:
    csrf_token: bytes


def exists(id: int, conn: Connection) -> bool:
    """
    Return whether a user exists with the given ID.

    :param id: The ID to check.
    :return: Whether a user has the given ID.
    """
    cursor = conn.execute("SELECT 1 FROM system__users WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Union[dict, Row]) -> T:
    """
    Return a user dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A user dataclass.
    """
    return T(**dict(row))


def from_id(id: int, conn: Connection) -> Optional[T]:
    """
    Get a user dataclass from the user's ID.

    :param id: The ID of the user to get.
    :param conn: A connection to the database.
    :return: The user, if they exist.
    """
    cursor = conn.execute(
        "SELECT id, nickname, csrf_token FROM system__users WHERE id = ?",
        (id,),
    )

    if row := cursor.fetchone():
        logger.debug(f"Fetched user {id}.")
        return from_row(row)

    logger.debug(f"Failed to fetch user {id}.")
    return None


def from_nickname(nickname: str, conn: Connection) -> Optional[T]:
    """
    Get a user dataclass from the user's nickname.

    :param nickname: The nickname of the user to get.
    :param conn: A connection to the database.
    :return: The user, if they exist.
    """
    cursor = conn.execute(
        "SELECT id, nickname, csrf_token FROM system__users WHERE nickname = ?",
        (nickname,),
    )

    if row := cursor.fetchone():
        logger.debug(f"Fetched user {row['id']} from nickname {nickname}.")
        return from_row(row)

    logger.debug(f"Failed to fetch user from nickname {nickname}.")
    return None


def from_token(token: bytes, conn: Connection) -> Optional[T]:
    """
    Get a user dataclass from the user's token. The returned user is necessarily
    authenticated.

    How it works: We store a unique prefix of each user's token and match on that.

    :param token: The token of the user to get.
    :param conn: A connection to the database.
    :return: The user, if they exist.
    """
    if len(token) != TOKEN_LENGTH:
        return None

    token_prefix = token[:PREFIX_LENGTH]

    cursor = conn.execute(
        "SELECT id, nickname, csrf_token FROM system__users WHERE token_prefix = ?",
        (token_prefix,),
    )

    if row := cursor.fetchone():
        usr = from_row(row)
        if check_token(usr, token, conn):
            logger.debug(f"Fetched user {usr.id} from token {token_prefix.hex()}.")
            return usr

    logger.debug(f"Failed to fetch user from token {token_prefix.hex()}.")
    return None


def create(nickname: str, conn: Connection) -> tuple[T, bytes]:
    """
    Create a user.

    :param nickname: The nickname of the user to create.
    :param conn: A connection to the database.
    :return: The newly created user and their token.
    :raises InvalidNickname: If the nickname is invalid.
    :raises TokenGenerationFailure: If we could not generate a suitable token.
    """
    if not _validate_nickname(nickname):
        raise InvalidNickname

    # Generate the token for the new user and hash it.
    token, token_prefix = _generate_token(conn)
    token_hash = generate_password_hash(token)

    # Generate a CSRF token.
    csrf_token = secrets.token_bytes(TOKEN_LENGTH)

    cursor = conn.execute(
        """
        INSERT INTO system__users
        (nickname, token_prefix, token_hash, csrf_token)
        VALUES (?, ?, ?, ?)
        """,
        (nickname, token_prefix, token_hash, csrf_token),
    )

    usr = from_id(cursor.lastrowid, conn)
    assert usr is not None

    logger.info(f"Created user {nickname} with ID {usr.id}.")
    post_create(usr.id, conn)
    return usr, token


def post_create(user_id: int, conn: Connection) -> None:
    """
    This is a helper function used in the create function. If you create a user
    manually, without using the create function, call this afterwards. This is used in
    the e2e testing developer endpoint.
    """
    _create_system_collections_and_playlists(user_id, conn)
    _populate_inbox.schedule(args=(user_id,), delay=0)


def _create_system_collections_and_playlists(user_id: int, conn: Connection) -> None:
    for name in ["Inbox", "Favorites"]:
        col = collection.create(
            name,
            CollectionType.SYSTEM,
            user_id=user_id,
            conn=conn,
            override_immutable=True,
        )
        collection.star(col, user_id, conn)

    ply = playlist.create(
        "Favorites",
        PlaylistType.SYSTEM,
        user_id=user_id,
        conn=conn,
        override_immutable=True,
    )
    playlist.star(ply, user_id, conn)

    logger.info(f"Created system collections and playlists for user {user_id}.")


@huey.task()
def _populate_inbox(user_id: int) -> None:
    with database() as conn:
        inbox = collection.inbox_of(user_id, conn)

        conn.execute(
            """
            INSERT INTO music__collections_releases
            (collection_id, release_id)
            SELECT ?, rls.id
            FROM music__releases AS rls
            WHERE rls.id != 1
            """,
            (inbox.id,),
        )

        conn.commit()


def update(usr: T, conn: Connection, **changes) -> T:
    """
    Update a user and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    :param usr: The user to update.
    :param conn: A connection to the database.
    :param nickname: New user nickname.
    :type  nickname: :py:obj:`str`
    :return: The updated user.
    """
    if changes.get("nickname", None) and not _validate_nickname(changes["nickname"]):
        raise InvalidNickname

    conn.execute(
        """
        UPDATE system__users
        SET nickname = ?
        WHERE id = ?
        """,
        (changes.get("nickname", usr.nickname), usr.id),
    )

    logger.info(f"Updated user {usr.id} with {changes}.")

    return update_dataclass(usr, **changes)


def new_token(usr: T, conn: Connection) -> bytes:
    """
    Generate a new token for a given user.

    :param usr: The user to generate a new token for.
    :param conn: A connection to the database.
    :return: The new token.
    :raises TokenGenerationFailure: If we could not generate a suitable token.
    """
    token, token_prefix = _generate_token(conn)
    token_hash = generate_password_hash(token)

    conn.execute(
        "UPDATE system__users SET token_prefix = ?, token_hash = ? WHERE id = ?",
        (token_prefix, token_hash, usr.id),
    )

    logger.info(f"Updated token of user {usr.id}.")

    return token


def check_token(usr: T, token: bytes, conn: Connection) -> bool:
    """
    Check if a given token is valid for a user.

    :param usr: The user to check.
    :param token: The token to check.
    :param conn: A connection to the database.
    :return: Whether the token is valid.
    """
    cursor = conn.execute(
        "SELECT token_hash FROM system__users WHERE id = ?",
        (usr.id,),
    )

    row = cursor.fetchone()
    if not row:
        logger.debug(f"Did not find token for user {usr.id}.")
        return False

    return check_password_hash(row["token_hash"], token)


def _validate_nickname(nickname: str) -> bool:
    """
    Validate a potential nickname:

    - Ensure that it is less than 24 characters.

    :param nickname: The nickname to validate.
    :param conn: A connection to the database.
    :return: Whether the nickname is valid.
    """
    return len(nickname) < 24


def _generate_token(conn: Connection) -> tuple[bytes, bytes]:
    """
    Generate a new token with a unique prefix. If we fail to generate a token with a
    unique prefix after 64 rounds, ``TokenGenerationFailure`` will be raised.

    :param conn: A connection to the database.
    :return: The token and its prefix, in that order.
    :raises TokenGenerationFailure: If a unique token prefix could not be found.
    """
    # Try to generate a suitable token 64 times.
    for _ in range(64):
        token = secrets.token_bytes(TOKEN_LENGTH)
        prefix = token[:PREFIX_LENGTH]

        # Check for token prefix uniqueness.
        cursor = conn.execute(
            "SELECT 1 FROM system__users WHERE token_prefix = ?",
            (prefix,),
        )
        if not cursor.fetchone():
            return token, prefix

        logger.debug("Token prefix clashed with existing token.")  # pragma: no cover

    # If we do not find a suitable token after 64 cycles, raise an exception.
    message = "Failed to generate token after 64 cycles o.O"  # pragma: no cover
    logger.info(message)  # pragma: no cover
    raise TokenGenerationFailure(message)  # pragma: no cover
