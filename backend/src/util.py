import logging
from contextlib import contextmanager
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from string import ascii_uppercase
from typing import Any, Dict, Iterable, List, Union

import pysqlite3 as sqlite3

from src.constants import Constants

logger = logging.getLogger(__name__)


@contextmanager
def database():
    """
    A simple wrapper for the sqlite3 connection context manager.

    :return: A context manager that yields a database connection.
    """
    cons = Constants()
    logger.debug(f"Opening a connection to database {cons.database_path}.")
    with sqlite3.connect(
        cons.database_path,
        detect_types=sqlite3.PARSE_DECLTYPES,
    ) as conn:
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


def calculate_sha_256(filepath: Path) -> bytes:
    """Calculate the SHA256 of a file."""
    hash_ = sha256()
    with filepath.open("rb") as fp:
        for block in iter(lambda: fp.read(65536), b""):
            hash_.update(block)

    return hash_.digest()


def convert_keys_case(mapping: Dict) -> Dict:
    """
    Given a dict, convert the keys from camelCase to snake_case.

    :param mapping: A dict whose keys' cases to convert.
    :return: A converted dict.
    """
    return {camelCase_to_snake_case(key): value for key, value in mapping.items()}


def camelCase_to_snake_case(string: str) -> str:
    """
    Convert a camelCase string to snake_case.

    :param string: The string to convert.
    :return: A snake case string.
    """
    return "".join(f"_{c.lower()}" if c in ascii_uppercase else c for c in string)


# Generics when?
def update_dataclass(dataclass: Any, **kwargs) -> Any:
    """
    Immutably update a dataclass with the changes passed in ``kwargs``. Each key in
    ``kwargs`` updates the dataclass' attribute with the same name to its value.

    :param dataclass: The dataclass to update.
    :param kwargs: The changes to make.
    :return: The updated dataclass.
    """
    return dataclass.__class__(**dict(asdict(dataclass), **kwargs))


def uniq_list(list_: Iterable) -> List:
    """
    Given a list, return a new list with any duplicate elements removed. Preserves
    order.

    Elements must be hashable.

    :param list_: The list to filter.
    :return: The filtered list.
    """
    seen = set()
    rval = []

    for elem in list_:
        if elem in seen:
            continue

        rval.append(elem)
        seen.add(elem)

    return rval


def make_fts_match_query(search: str) -> str:
    """
    Convert a search string into a FTS match query parameter. This function returns a
    parameter that searches for a result matching each space-delimited fragment in the
    search.

    :param search: A list of space-delimited search terms.
    :return: A FTS match query parameter.
    """
    # We surround each term with double quotes because that is FTS standard. It is also
    # standard for double quotes inside the term to be escaped as "".

    # First do the escaping for double quotes in the search string.
    search = search.replace('"', '""')
    return " AND ".join(f'"{w}"' for w in search.split(" "))


def del_pagination_keys(mapping: Dict) -> Dict:
    """
    Delete the keys related to pagination: page, per_page, sort, asc.

    :param mapping: The dict to alter.
    :return: An altered dict.
    """
    illegal_keys = ["page", "per_page", "sort", "asc"]
    return {k: v for k, v in mapping.items() if k not in illegal_keys}
