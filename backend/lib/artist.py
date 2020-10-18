from dataclasses import dataclass
from sqlite3 import Row
from typing import Optional

from backend.enums import ArtistRole


@dataclass
class T:
    """
    An artist dataclass. This dataclass is frozen (immutable).
    """

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    name: str
    #:
    favorite: bool
    #: The artist's role (for when the artist is attributed on a track).
    role: Optional[ArtistRole]


def from_row(row: Row) -> T:
    """
    Return an artist dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: An artist dataclass.
    """
    return T(**row, role=ArtistRole(row["role"]) if "role" in row else None)
