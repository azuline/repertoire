from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from datetime import datetime
from sqlite3 import Cursor, Row
from typing import Any, Dict, List, Optional

from backend.enums import CollectionType
from backend.errors import (
    AlreadyExists,
    DoesNotExist,
    Duplicate,
    Immutable,
    InvalidCollectionType,
    NotFound,
)
from backend.util import without_key

from . import release

ILLEGAL_UPDATE_TYPES = {CollectionType.SYSTEM, CollectionType.RATING}

logger = logging.getLogger(__name__)


@dataclass
class T:
    """A collection dataclass."""

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


def exists(id: int, cursor: Cursor) -> bool:
    """
    Return whether a collection exists with the given ID.

    :param id: The ID to check.
    :return: Whether a collection has the given ID.
    """
    cursor.execute("SELECT 1 FROM music__collections WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Row) -> T:
    """
    Return a collection dataclass containing data from a row from the database.

    _Note: For some reason, SQLite doesn't parse the ``last_updated_on`` row as a
    ``datetime`` object, instead parsing it as a string. So we do the manual conversion
    here to a datetime object.

    :param row: A row from the database.
    :return: A collection dataclass.
    """
    try:
        last_updated_on = datetime.fromisoformat(row["last_updated_on"])
    except (KeyError, TypeError):
        last_updated_on = None

    return T(
        **dict(
            row,
            favorite=bool(row["favorite"]),
            type=CollectionType(row["type"]),
            last_updated_on=last_updated_on,
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
        WHERE cols.name = ? AND cols.type = ?
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
    if type in [CollectionType.SYSTEM, CollectionType.RATING]:
        raise InvalidCollectionType("Cannot modify system or rating collections.")

    if col := from_name_and_type(name, type, cursor):
        raise Duplicate(f'Collection "{name}" already exists.', col)

    cursor.execute(
        "INSERT INTO music__collections (name, type, favorite) VALUES (?, ?, ?)",
        (name, type.value, favorite),
    )
    cursor.connection.commit()

    logger.info(
        f'Created collection "{name}" of type {type} with ID {cursor.lastrowid}.'
    )

    return T(
        id=cursor.lastrowid,
        name=name,
        type=type,
        favorite=favorite,
        num_releases=0,
    )


def update(col: T, cursor: Cursor, **changes: Dict[str, Any]) -> T:
    """
    Update a collection and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    **Note: The type of a collection cannot be changed.**

    :param col: The collection to update.
    :param cursor: A cursor to the database.
    :param name: New collection name.
    :type  name: :py:obj:`str`
    :param favorite: New collection favorite.
    :type  favorite: :py:obj:`bool`
    :return: The updated collection.
    :raises Immutable: If the collection cannot be updated.
    :raises Duplicate: If the new name conflicts with another collection.
    """
    if col.type in [CollectionType.SYSTEM, CollectionType.RATING]:
        raise Immutable("System and rating collections cannot be modified.")

    if (
        "name" in changes
        and (dupl := from_name_and_type(changes["name"], col.type, cursor))
        and dupl != col
    ):
        raise Duplicate(f'Collection "{changes["name"]}" already exists.', dupl)

    cursor.execute(
        """
        UPDATE music__collections
        SET name = ?,
            favorite = ?
        WHERE id = ?
        """,
        (
            changes.get("name", col.name),
            changes.get("favorite", col.favorite),
            col.id,
        ),
    )
    cursor.connection.commit()

    logger.info(f"Updated collection {col.id} with {changes}.")

    return T(**dict(asdict(col), **changes))


def releases(col: T, cursor: Cursor) -> List[release.T]:
    """
    Get the releases in a collection.

    :param col: The collection whose releases we want to get.
    :param cursor: A cursor to the database.
    :return: A list of releases in the collection.
    """
    _, releases = release.search(collection_ids=[col.id], cursor=cursor)
    return releases


def add_release(col: T, release_id: int, cursor: Cursor) -> None:
    """
    Add the provided release to the provided collection.

    :param col: The collection to add the release to.
    :param rls_id: The ID of the release to add.
    :param cursor: A cursor to the database.
    :raises NotFound: If no release has the given release ID.
    :raises AlreadyExists: If the release is already in the collection.
    """
    if not release.exists(release_id, cursor):
        raise NotFound(f"Releasse {release_id} does not exist.")

    cursor.execute(
        """
        SELECT 1 FROM music__collections_releases
        WHERE collection_id = ? AND release_id = ?
        """,
        (col.id, release_id),
    )
    if cursor.fetchone():
        raise AlreadyExists("Release is already in collection.")

    cursor.execute(
        """
        INSERT INTO music__collections_releases (collection_id, release_id)
        VALUES (?, ?)
        """,
        (col.id, release_id),
    )
    cursor.connection.commit()


def del_release(col: T, release_id: int, cursor: Cursor) -> None:
    """
    Remove the provided release from the provided collection.

    :param col: The collection to remove the release from.
    :param rls: The release to remove.
    :param cursor: A cursor to the database.
    :raises NotFound: If no release has the given release ID.
    :raises DoesNotExist: If the release is not in the collection.
    """
    if not release.exists(release_id, cursor):
        raise NotFound(f"Release {release_id} does not exist.")

    cursor.execute(
        """
        SELECT 1 FROM music__collections_releases
        WHERE collection_id = ? AND release_id = ?
        """,
        (col.id, release_id),
    )
    if not cursor.fetchone():
        raise DoesNotExist("Release is not in collection.")

    cursor.execute(
        """
        DELETE FROM music__collections_releases
        WHERE collection_id = ? AND release_id = ?
        """,
        (col.id, release_id),
    )
    cursor.connection.commit()


def top_genres(col: T, cursor: Cursor, *, num_genres: int = 5) -> List[Dict]:
    """
    Get the top genre collections of the releases in a collection.

    The returned genres are in the following format:

    .. code-block:: python

       [
         {
           "genre": collection.T,
           "num_matches": int,
         },
         ...
       ]

    The fields ``num_releases`` and ``last_updated_on`` in the genre collections are set
    to ``None``.

    :param col: The collection whose top genres to fetch.
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
        (col.id, CollectionType.GENRE.value, num_genres),
    )

    return [
        {
            "genre": from_row(without_key(row, "num_matches")),
            "num_matches": row["num_matches"],
        }
        for row in cursor.fetchall()
    ]
