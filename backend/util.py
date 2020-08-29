import sqlite3
from contextlib import contextmanager
from datetime import datetime
from typing import ContextManager, Dict

from backend.constants import DATABASE_PATH


@contextmanager
def database() -> ContextManager[sqlite3.Connection]:
    """A simple wrapper for the sqlite3 connection context manager."""
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        yield conn


def to_posix_time(time: str) -> int:
    """Take a YYYY-MM-DD HH:MM:SS UTC timestamp and convert it to unix time."""
    if time:
        return datetime.fromisoformat(f"{time}+00:00").timestamp()
    return None


def hours_to_crontab(hours: int) -> Dict:
    """
    Given an integer that represents hours, return a dict of params that
    matches Huey's crontab parameter format.
    """
    if not hours:
        return {}
    elif hours == 24:
        return {"day": "*/1"}
    return {"hour": f"*/{hours}"}
