from dataclasses import dataclass
from sqlite3 import Row

from backend.enums import CollectionType


@dataclass
class T:
    """
    A collection dataclass. This dataclass is frozen (immutable).
    """

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    name: str
    #:
    favorite: bool
    #:
    type: CollectionType


def from_row(row: Row) -> T:
    """
    Return a collection dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A collection dataclass.
    """
    return T(**row, role=CollectionType(row["type"]) if "type" in row else None)
