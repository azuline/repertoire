"""
This module contains our configuration. The configuration is stored in the database, as
an untyped (all strings) set of key/value pairs.

All exposed functions besides `initialize_config` and `write_default_config` fetch a
configuration value from the database.
"""

import json
import logging
from sqlite3 import Connection
from typing import Callable

from huey import crontab

from src.errors import InvalidConfig
from src.util import flatten_dict, parse_crontab, transaction

logger = logging.getLogger(__name__)

MUSIC_DIRECTORIES = "music_directories"
INDEX_CRONTAB = "index_crontab"

DEFAULT_CONFIG = {
    MUSIC_DIRECTORIES: '["/music"]',
    INDEX_CRONTAB: "0 0 * * *",
}


def initialize_config() -> None:
    """
    Write the default config if a config file doesn't exist. And if the
    existing config lacks keys, update it with new default values.
    """
    with transaction() as conn:
        cursor = conn.execute("SELECT key FROM system__config")
        keys = [r["key"] for r in cursor]

        if not keys:
            write_default_config(conn)
        else:
            _update_config(conn)


def write_default_config(conn: Connection) -> None:
    logger.info("Writing default configuration.")

    question_marks = ", ".join(["(?, ?)"] * len(DEFAULT_CONFIG))
    conn.execute(
        f"INSERT INTO system__config VALUES {question_marks}",
        flatten_dict(DEFAULT_CONFIG),
    )
    conn.commit()


def _update_config(conn: Connection):
    logger.debug("Adding missing config keys to existing config.")

    for key, value in DEFAULT_CONFIG.items():
        cursor = conn.execute("SELECT 1 FROM system__config WHERE key = ?", (key,))
        if cursor.fetchone():
            continue

        conn.execute(
            "INSERT INTO system__config (key, value) VALUES (?, ?)",
            (key, value),
        )


def music_directories() -> list[str]:
    """
    The directories to scan when indexing the library.
    """
    with transaction() as conn:
        cursor = conn.execute(
            "SELECT value FROM system__config WHERE key = ?",
            (MUSIC_DIRECTORIES,),
        )
        try:
            return json.loads(cursor.fetchone()["value"])
        except (TypeError, ValueError):
            raise InvalidConfig("music_directories is not a valid JSON-encoded list.")


def set_music_directories(dirs: list[str], conn: Connection) -> None:
    """
    :raises InvalidConfig: If any directories don't exist.
    """
    conn.execute(
        "UPDATE system__config SET value = ? WHERE key = ?",
        (json.dumps(dirs), MUSIC_DIRECTORIES),
    )


def index_crontab() -> Callable:
    try:
        return crontab(**parse_crontab(index_crontab_str()), strict=True)
    except (TypeError, ValueError):
        raise InvalidConfig("index_crontab is not a valid crontab.")


def index_crontab_str() -> str:
    """
    A crontab representing when to index the library.
    """
    with transaction() as conn:
        cursor = conn.execute(
            "SELECT value FROM system__config WHERE key = ?",
            (INDEX_CRONTAB,),
        )
        return cursor.fetchone()["value"]


def set_index_crontab(value: str, conn: Connection) -> None:
    """
    :raises InvalidConfig: If the crontab is syntactically invalid.
    """
    try:
        crontab(**parse_crontab(value), strict=True)
    except ValueError:
        raise InvalidConfig(f"{value} is not a valid crontab.")

    conn.execute(
        "UPDATE system__config SET value = ? WHERE key = ?",
        (value, INDEX_CRONTAB),
    )
