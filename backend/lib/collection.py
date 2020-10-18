from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from sqlite3 import Cursor, Row
from typing import Dict, List, Optional

from backend.enums import CollectionType

from . import release


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
    #:
    num_releases: Optional[int]
    #:
    last_updated_on: Optional[datetime]


def from_row(row: Row) -> T:
    """
    Return a collection dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A collection dataclass.
    """
    return T(**row, role=CollectionType(row["type"]))


def from_id(id_: int, cursor: Cursor) -> Optional[T]:
    """
    Return the collection with the provided ID.

    :param id_: The ID of the collection to fetch.
    :param cursor: A cursor to the database.
    :return: The collection with the provided ID, if it exists.
    """
    cursor.execute(
        """
        SELECT
            cols.*,
            COUNT(colsrls.release_id) AS num_releases,
            MAX(colsrls.added_on) AS last_updated_on
        FROM music__collections AS cols
        LEFT JOIN music__collections_releases AS colsrls
            ON colsrls.collection_id = cols.id
        """,
        (id_,),
    )

    row = cursor.fetchone()
    return from_row(row) if row else None


def all(cursor: Cursor) -> List[T]:
    """
    Get all collections.

    :param cursor: A cursor to the database.
    :return: All collections stored on the backend.
    """
    cursor.execute(
        """
        SELECT
            cols.*,
            COUNT(colsrls.release_id) AS num_releases,
            MAX(colsrls.added_on) AS last_updated_on
        FROM music__collections AS cols
        LEFT JOIN music__collections_releases AS colsrls
            ON colsrls.collection_id = cols.id
        GROUP BY cols.id
        """
    )
    return [from_row(row) for row in cursor.fetchall()]


def releases(collection: T, cursor: Cursor) -> List[release.T]:
    """
    Get the releases in a collection.

    :param collection: The collection whose releases we want to get.
    :param cursor: A cursor to the database.
    :return: A list of releases in the collection.
    """
    _, releases = release.search(collections=[collection], cursor=cursor)
    return releases


def top_genres(collection: T, cursor: Cursor, *, num_genres: int = 5) -> List[Dict]:
    """
    Get the top genre collections of the releases in a collection.

    The returned genres are in the following format:

    .. code-block:: python

       [
         {
           "genre": genre.T,
           "num_matches": int,
         },
         ...
       ]

    :param collection: The collection whose top genres to fetch.
    :param cursor: A cursor to the database.
    :param num_genres: The number of top genres to fetch.
    :return: The top genres.
    """
    cursor.execute(
        """
        SELECT
            genres.*,
            COUNT(genresrls.release_id) AS num_matches
        FROM music__collections AS genres
        LEFT JOIN music__collections_releases AS genresrls
            ON genresrls.collection_id = genres.id
        LEFT JOIN music__collections_releases AS colsrls
            ON colsrls.release_id = genresrls.release_id
        WHERE colsrls.collection_id = ? AND genres.type = ?
        GROUP BY genres.id
        ORDER BY num_matches DESC
        LIMIT ?
        """,
        (collection.id, CollectionType.GENRE.value, num_genres),
    )

    top_genres = []

    for row in cursor.fetchall():
        matches = row["num_matches"]
        del row["num_matches"]
        top_genres.append({"genre": from_row(row), "num_matches": matches})

    return top_genres
