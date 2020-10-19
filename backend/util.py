import sqlite3
from contextlib import contextmanager
from functools import wraps
from hashlib import sha256
from pathlib import Path
from string import punctuation
from typing import Any, Callable, ContextManager, Dict, Union

from unidecode import unidecode

from backend.constants import DATABASE_PATH

punctuation = set(punctuation)


@contextmanager
def database() -> ContextManager[sqlite3.Connection]:
    """
    A simple wrapper for the sqlite3 connection context manager.

    :return: A context manager that yields a database connection.
    """
    with sqlite3.connect(DATABASE_PATH, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        yield conn


def without_key(mapping: Union[Dict, sqlite3.Row], key: Any) -> Dict:
    """
    Return a dict/Row without a certain key. This function does not modify the original
    dictionary/Row.

    :param mapping: The original dict/row.
    :param key: The key to remove.
    :return: The dict without the passed-in key.
    """
    return {k: mapping[k] for k in mapping.keys() if k != key}


def cached_property(func: Callable) -> property:
    """
    A replacement for `property` that caches the result for future accesses.

    :param func: A function to turn into a property.
    :return: A property object.
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

    :param crontab: The string-encoded crontab.
    :return: A dictionary of crontab keyword arguments that huey accepts.
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
    """
    Strip the punctuation from a string.

    :param string: The string to strip.
    :return: The stripped string.
    """
    return "".join(c for c in unidecode(string) if c not in punctuation)


def calculate_sha_256(filepath: Path) -> bytes:
    """Calculate the SHA256 of a file."""
    hash_ = sha256()
    with filepath.open("rb") as fp:
        for block in iter(lambda: fp.read(65536), b""):
            hash_.update(block)

    return hash_.digest()
