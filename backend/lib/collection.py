from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from sqlite3 import Cursor, Row
from typing import Dict, List, Optional

from backend.enums import CollectionType
from backend.errors import Duplicate
from backend.util import without_key

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
    num_releases: Optional[int] = None
    #:
    last_updated_on: Optional[datetime] = None


def from_row(row: Row) -> T:
    """
    Return a collection dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A collection dataclass.
    """
    return T(
        **dict(
            row,
            favorite=bool(row["favorite"]),
            type=CollectionType(row["type"]),
        )
    )


def from_id(id: int, cursor: Cursor) -> Optional[T]:
    """
    Return the collection with the provided ID.

    :param id: The ID of the collection to fetch.
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
        WHERE cols.id = ?
        GROUP BY cols.id
        """,
        (id,),
    )

    if row := cursor.fetchone():
        return from_row(row)


def from_name_and_type(name: str, type: CollectionType, cursor: Cursor) -> Optional[T]:
    """
    Return the collection with the given name and type, if it exists.

    :param name: The name of the collection.
    :param type: The type of the collection.
    :param cursor: A cursor to the database.
    :return: The collection, if it exists.
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
        WHERE cols.name = ?
            AND cols.type = ?
        GROUP BY cols.id
        """,
        (name, type.value),
    )

    if row := cursor.fetchone():
        return from_row(row)


def all(cursor: Cursor, type: CollectionType = None) -> List[T]:
    """
    Get all collections.

    :param cursor: A cursor to the database.
    :param type: Filter by a collection type. Pass ``None`` to fetch all types.
    :return: All collections stored on the backend.
    """
    cursor.execute(
        f"""
        SELECT
            cols.*,
            COUNT(colsrls.release_id) AS num_releases,
            MAX(colsrls.added_on) AS last_updated_on
        FROM music__collections AS cols
        LEFT JOIN music__collections_releases AS colsrls
            ON colsrls.collection_id = cols.id
        {"WHERE cols.type = ?" if type else ""}
        GROUP BY cols.id
        """,
        ((type.value,) if type else ()),
    )
    return [from_row(row) for row in cursor.fetchall()]


def create(
    name: str, type: CollectionType, cursor: Cursor, favorite: bool = False
) -> T:
    """
    Create a collection and persist it to the database.

    :param name: The name of the collection.
    :param type: The type of the collection.
    :cursor: A cursor to the database.
    :param favorite: Whether the collection is a favorite or not.
    :return: The newly created collection.
    :raises Duplicate: If an collection with the same name and type already exists. The
                       duplicate collection is passed as the ``entity`` argument.
    """
    if col := from_name_and_type(name, type, cursor):
        raise Duplicate(col)

    cursor.execute(
        """INSERT INTO music__collections (name, type, favorite) VALUES (?, ?, ?)""",
        (name, type.value, favorite),
    )
    cursor.connection.commit()

    return T(
        id=cursor.lastrowid,
        name=name,
        type=type,
        favorite=favorite,
        num_releases=0,
    )


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

    return [
        {
            "genre": from_row(without_key(row, "num_matches")),
            "num_matches": row["num_matches"],
        }
        for row in cursor.fetchall()
    ]


def add_release(col: T, rls: release.T, cursor: Cursor) -> None:
    """
    TODO:

    If release is already in collection, raise exception!
    """
