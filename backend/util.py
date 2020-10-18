import sqlite3
from contextlib import contextmanager
from functools import wraps
from string import punctuation
from typing import Callable, ContextManager, Dict

from unidecode import unidecode

from backend.constants import DATABASE_PATH

punctuation = set(punctuation)


@contextmanager
def database() -> ContextManager[sqlite3.Connection]:
    """A simple wrapper for the sqlite3 connection context manager."""
    with sqlite3.connect(DATABASE_PATH, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        yield conn


def cached_property(func: Callable) -> property:
    """
    A replacement for `property` that caches the result for future accesses.
    """

    @wraps(func)
    def wrapper(self):
        try:
            return self.__property_cache[func.__name__]
        except AttributeError:
            self.__property_cache = {}
        except KeyError:
            pass

        rval = self.__property_cache[func.__name__] = func(self)
        return rval

    return property(wrapper)


def parse_crontab(crontab: str) -> Dict:
    """
    Given a crontab entry from the config, split the values and create a dictionary
    mapping each value to their huey key.

    :raises ValueError: If there are not the correct number of fields in ``crontab``.
    """
    minute, hour, day, month, day_of_week = crontab.split(" ")

    return dict(
        minute=minute,
        hour=hour,
        day=day,
        month=month,
        day_of_week=day_of_week,
    )


def strip_punctuation(string: str) -> str:
    """Strip the punctuation from a string."""
    return "".join(c for c in unidecode(string) if c not in punctuation)
