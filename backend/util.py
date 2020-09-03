import sqlite3
from contextlib import contextmanager
from datetime import datetime
from string import punctuation
from typing import ContextManager, Dict

from backports.datetime_fromisoformat import MonkeyPatch
from unidecode import unidecode

from backend.constants import DATABASE_PATH

MonkeyPatch.patch_fromisoformat()
punctuation = set(punctuation)


@contextmanager
def database() -> ContextManager[sqlite3.Connection]:
    """A simple wrapper for the sqlite3 connection context manager."""
    with sqlite3.connect(str(DATABASE_PATH)) as conn:
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
        return {"minute": "0", "hour": "0", "day": "*/1"}
    return {"minute": "0", "hour": f"*/{hours}"}


def strip_punctuation(string: str) -> str:
    """Strip the punctuation from a string."""
    return "".join(c for c in unidecode(string) if c not in punctuation)
