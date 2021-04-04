from __future__ import annotations

import logging
import secrets
from dataclasses import dataclass
from datetime import datetime
from sqlite3 import Connection, Row
from typing import Optional, Union

from src.errors import CodeGenerationFailure
from src.util import update_dataclass

from . import user

INVITE_LENGTH = 32

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class T:
    """An invite dataclass."""

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #: The invite code.
    code: bytes
    #: The ID of the user the invite was created by.
    created_by: int
    #: The date the invite was created. Invites are only valid for 24 hours.
    created_at: datetime
    #: The ID of the user that used the invite.
    used_by: Optional[int]


def from_row(row: Union[dict, Row]) -> T:
    """
    Return an invite dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: An invite dataclass.
    """
    return T(**dict(row))


def from_id(id: int, conn: Connection) -> Optional[T]:
    """
    Get an invite dataclass from the invite's ID.

    :param id: The ID of the invite to get.
    :param conn: A connection to the database.
    :return: The invite, if it exists.
    """
    cursor = conn.execute("SELECT * FROM system__invites WHERE id = ?", (id,))

    if row := cursor.fetchone():
        logger.debug(f"Fetched invite {id}.")
        return from_row(row)

    logger.debug(f"Failed to fetch invite {id}.")
    return None


def from_code(code: bytes, conn: Connection) -> Optional[T]:
    """
    Get an invite dataclass from the invite's code.

    :param code: The code of the invite to get.
    :param conn: A connection to the database.
    :return: The invite, if it exists.
    """
    cursor = conn.execute("SELECT * FROM system__invites WHERE code = ?", (code,))

    if row := cursor.fetchone():
        logger.debug(f"Fetched invite {row['id']} from code {code.hex()}.")
        return from_row(row)

    logger.debug(f"Failed to fetch invite from code {code.hex()}.")
    return None


def create(by_user: user.T, conn: Connection) -> T:
    """
    Create an invite.

    :param by_user: The user creating the invite.
    :param conn: A connection to the database.
    :return: The newly created invite.
    """
    code = _generate_code(conn)

    cursor = conn.execute(
        """
        INSERT INTO system__invites (code, created_by) VALUES (?, ?)
        """,
        (code, by_user.id),
    )

    logger.info(f"Created invite {cursor.lastrowid}.")

    inv = from_id(cursor.lastrowid, conn)
    assert inv is not None
    return inv


def update(inv: T, conn: Connection, **changes) -> T:
    """
    Update an invite and persist changes to the database. To update a value, pass it in
    as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    :param inv: The invite to update.
    :param conn: A connection to the database.
    :param used_by: The user that used the invite.
    :type  used_by: :py:obj:`src.library.user.T`
    :return: The updated invite.
    """
    if changes.get("used_by"):
        changes["used_by"] = changes["used_by"].id

    conn.execute(
        """
        UPDATE system__invites
        SET used_by = ?
        WHERE id = ?
        """,
        (changes.get("used_by", inv.used_by), inv.id),
    )

    logger.info(f"Updated invite {inv.id} with {changes}.")

    return update_dataclass(inv, **changes)


def _generate_code(conn: Connection) -> bytes:
    """
    Generate a new unique invite code. If we fail to generate a unique invite code after
    64 rounds, ``CodeGenerationFailure`` will be raised.

    :param conn: A connection to the database.
    :return: The token and its prefix, in that order.
    :raises CodeGenerationFailure: If a unique token prefix could not be found.
    """
    # Try to generate a suitable code 64 times.
    for _ in range(64):
        code = secrets.token_bytes(INVITE_LENGTH)

        # Check for token prefix uniqueness.
        cursor = conn.execute(
            "SELECT 1 FROM system__invites WHERE code = ?",
            (code,),
        )
        if not cursor.fetchone():
            return code

        logger.debug("Invite code clashed with existing invite.")

    # If we do not find a suitable token after 64 cycles, raise an exception.
    logger.info(
        "Failed to generate invite code after 64 cycles o.O"
    )  # pragma: no cover
    raise CodeGenerationFailure(  # pragma: no cover
        "Failed to generate invite code after 64 cycles o.O"
    )
