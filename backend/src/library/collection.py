from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from sqlite3 import Connection, Row
from typing import Dict, List, Optional, Tuple, Union

from src.enums import CollectionType
from src.errors import (
    AlreadyExists,
    DoesNotExist,
    Duplicate,
    Immutable,
    InvalidCollectionType,
    NotFound,
)
from src.util import make_fts_match_query, update_dataclass, without_key

from . import image as libimage
from . import release

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class T:
    """A collection dataclass."""

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    name: str
    #:
    starred: bool
    #:
    type: CollectionType
    #:
    num_releases: Optional[int] = None
    #:
    last_updated_on: Optional[datetime] = None


def exists(id: int, conn: Connection) -> bool:
    """
    Return whether a collection exists with the given ID.

    :param id: The ID to check.
    :return: Whether a collection has the given ID.
    """
    cursor = conn.execute("SELECT 1 FROM music__collections WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Union[Dict, Row]) -> T:
    """
    Return a collection dataclass containing data from a row from the database.

    _Note: For some reason, SQLite doesn't parse the ``last_updated_on`` row as a
    ``datetime`` object, instead parsing it as a string. So we do the manual conversion
    here to a datetime object.

    :param row: A row from the database.
    :return: A collection dataclass.
    """
    last_updated_on: Optional[datetime] = None

    try:
        last_updated_on = datetime.fromisoformat(row["last_updated_on"])
    except (KeyError, TypeError):
        pass

    return T(
        **dict(
            row,
            starred=bool(row["starred"]),
            type=CollectionType(row["type"]),
            last_updated_on=last_updated_on,
        )
    )


def from_id(id: int, conn: Connection) -> Optional[T]:
    """
    Return the collection with the provided ID.

    :param id: The ID of the collection to fetch.
    :param conn: A connection to the database.
    :return: The collection with the provided ID, if it exists.
    """
    cursor = conn.execute(
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
        logger.debug(f"Fetched collection {id}.")
        return from_row(row)

    logger.debug(f"Failed to fetch collection {id}.")
    return None


def from_name_and_type(
    name: str, type: CollectionType, conn: Connection
) -> Optional[T]:
    """
    Return the collection with the given name and type, if it exists.

    :param name: The name of the collection.
    :param type: The type of the collection.
    :param conn: A connection to the database.
    :return: The collection, if it exists.
    """
    cursor = conn.execute(
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
        logger.debug(
            f'Fetched collection {row["id"]} with name "{name}" and type {type}.'
        )
        return from_row(row)

    logger.debug(f'Failed to fetch collection with name "{name}" and type {type}.')
    return None


def search(
    conn: Connection,
    *,
    search: str = "",
    types: List[CollectionType] = [],
    page: int = 1,
    per_page: Optional[int] = None,
) -> List[T]:
    """
    Search for collections. Parameters are optional; omitted ones are excluded from the
    matching criteria.

    :param conn: A connection to the database.
    :param search: A search string. We split this up into individual punctuation-less
                   tokens and return collections whose titles contain each token. If
                   specified, the returned collections will be sorted by match
                   proximity.
    :param types: Filter by collection types.
    :param page: Which page of collections to return.
    :param per_page: The number of collections per page. Pass ``None`` to return all
                     collections (this will ignore ``page``).
    :return: All matching collections.
    """
    filters, params = _generate_filters(search, types)

    if per_page:
        params.extend([per_page, (page - 1) * per_page])

    cursor = conn.execute(
        f"""
        SELECT
            cols.*,
            COUNT(colsrls.release_id) AS num_releases,
            MAX(colsrls.added_on) AS last_updated_on
        FROM music__collections AS cols
        JOIN music__collections__fts AS fts ON fts.rowid = cols.id
        LEFT JOIN music__collections_releases AS colsrls
            ON colsrls.collection_id = cols.id
        {"WHERE " + " AND ".join(filters) if filters else ""}
        GROUP BY cols.id
        ORDER BY
            {"fts.rank" if search else "cols.type, cols.starred DESC, cols.name"}
        {"LIMIT ? OFFSET ?" if per_page else ""}
        """,
        params,
    )

    logger.debug(f"Fetched all collections of types {type}.")
    return [from_row(row) for row in cursor]


def count(
    conn: Connection,
    *,
    search: str = "",
    types: List[CollectionType] = [],
) -> List[T]:
    """
    Fetch the number of collections matching the passed-in criteria. Parameters are
    optional; omitted ones are excluded from the matching criteria.

    :param conn: A connection to the database.
    :param search: A search string. We split this up into individual punctuation-less
                   tokens and return collections whose titles contain each token.
    :param types: Filter by collection types.
    :return: The number of matching collections.
    """
    filters, params = _generate_filters(search, types)

    cursor = conn.execute(
        f"""
        SELECT COUNT(1)
        FROM music__collections AS cols
        JOIN music__collections__fts AS fts ON fts.rowid = cols.id
        {"WHERE " + " AND ".join(filters) if filters else ""}
        """,
        params,
    )

    count = cursor.fetchone()[0]
    logger.debug(f"Counted {count} collections that matched the filters.")
    return count


def _generate_filters(
    search: str = "",
    types: List[CollectionType] = [],
) -> Tuple[List[str], List[Union[str, int]]]:
    """
    Dynamically generate the SQL filters and parameters from the criteria. See the
    search and total functions for parameter descriptions.

    :return: A tuple of SQL filter strings and parameters. The SQL filter strings can be
    joined with `` AND `` and injected into the where clause.
    """
    filters: List[str] = []
    params: List[Union[str, int]] = []

    if search:
        filters.append("fts.music__collections__fts MATCH ?")
        params.append(make_fts_match_query(search))

    if types:
        filters.append(f"cols.type IN ({','.join('?' * len(types))})")
        params.extend([t.value for t in types])

    return filters, params


def create(
    name: str, type: CollectionType, conn: Connection, starred: bool = False
) -> T:
    """
    Create a collection and persist it to the database.

    :param name: The name of the collection.
    :param type: The type of the collection.
    :param conn: A connection to the database.
    :param starred: Whether the collection is starred or not.
    :return: The newly created collection.
    :raises Duplicate: If an collection with the same name and type already exists. The
                       duplicate collection is passed as the ``entity`` argument.
    """
    if type == CollectionType.SYSTEM:
        raise InvalidCollectionType("Cannot create system collections.")

    if col := from_name_and_type(name, type, conn):
        raise Duplicate(f'Collection "{name}" already exists.', col)

    cursor = conn.execute(
        "INSERT INTO music__collections (name, type, starred) VALUES (?, ?, ?)",
        (name, type.value, starred),
    )

    logger.info(
        f'Created collection "{name}" of type {type} with ID {cursor.lastrowid}.'
    )

    return T(
        id=cursor.lastrowid,
        name=name,
        type=type,
        starred=starred,
        num_releases=0,
    )


def update(col: T, conn: Connection, **changes) -> T:
    """
    Update a collection and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    **Note: The type of a collection cannot be changed.**

    :param col: The collection to update.
    :param conn: A connection to the database.
    :param name: New collection name.
    :type  name: :py:obj:`str`
    :param starred: Whether ew collection is starred.
    :type  starred: :py:obj:`bool`
    :return: The updated collection.
    :raises Immutable: If the collection cannot be updated.
    :raises Duplicate: If the new name conflicts with another collection.
    """
    if col.type == CollectionType.SYSTEM:
        raise Immutable("System collections cannot be modified.")

    if (
        "name" in changes
        and (dupl := from_name_and_type(changes["name"], col.type, conn))
        and dupl != col
    ):
        raise Duplicate(f'Collection "{changes["name"]}" already exists.', dupl)

    conn.execute(
        """
        UPDATE music__collections
        SET name = ?,
            starred = ?
        WHERE id = ?
        """,
        (
            changes.get("name", col.name),
            changes.get("starred", col.starred),
            col.id,
        ),
    )

    logger.info(f"Updated collection {col.id} with {changes}.")

    return update_dataclass(col, **changes)


def releases(col: T, conn: Connection) -> List[release.T]:
    """
    Get the releases in a collection.

    :param col: The collection whose releases we want to get.
    :param conn: A connection to the database.
    :return: A list of releases in the collection.
    """
    releases = release.search(collection_ids=[col.id], conn=conn)
    logger.debug(f"Fetched releases of collection {col.id}.")
    return releases


def add_release(col: T, release_id: int, conn: Connection) -> T:
    """
    Add the provided release to the provided collection.

    :param col: The collection to add the release to.
    :param release_id: The ID of the release to add.
    :param conn: A connection to the database.
    :return: The collection with the number of tracks (if present) updated.
    :raises NotFound: If no release has the given release ID.
    :raises AlreadyExists: If the release is already in the collection.
    """
    if not release.exists(release_id, conn):
        logger.debug(f"Release {release_id} does not exist.")
        raise NotFound(f"Release {release_id} does not exist.")

    cursor = conn.execute(
        """
        SELECT 1 FROM music__collections_releases
        WHERE collection_id = ? AND release_id = ?
        """,
        (col.id, release_id),
    )
    if cursor.fetchone():
        logger.debug(f"Release {release_id} already in collection {col.id}.")
        raise AlreadyExists("Release is already in collection.")

    conn.execute(
        """
        INSERT INTO music__collections_releases (collection_id, release_id)
        VALUES (?, ?)
        """,
        (col.id, release_id),
    )

    logger.info(f"Added release {release_id} to collection {col.id}.")

    return update_dataclass(
        col,
        num_releases=(
            col.num_releases + 1 if col.num_releases is not None else col.num_releases
        ),
    )


def del_release(col: T, release_id: int, conn: Connection) -> T:
    """
    Remove the provided release from the provided collection.

    :param col: The collection to remove the release from.
    :param release_id: The release to remove.
    :param conn: A connection to the database.
    :return: The collection with the number of tracks (if present) updated.
    :raises NotFound: If no release has the given release ID.
    :raises DoesNotExist: If the release is not in the collection.
    """
    if not release.exists(release_id, conn):
        logger.debug(f"Release {release_id} does not exist.")
        raise NotFound(f"Release {release_id} does not exist.")

    cursor = conn.execute(
        """
        SELECT 1 FROM music__collections_releases
        WHERE collection_id = ? AND release_id = ?
        """,
        (col.id, release_id),
    )
    if not cursor.fetchone():
        logger.debug(f"Release {release_id} not in collection {col.id}.")
        raise DoesNotExist("Release is not in collection.")

    conn.execute(
        """
        DELETE FROM music__collections_releases
        WHERE collection_id = ? AND release_id = ?
        """,
        (col.id, release_id),
    )

    logger.info(f"Deleted release {release_id} from collection {col.id}.")

    return update_dataclass(
        col,
        num_releases=(
            col.num_releases - 1 if col.num_releases is not None else col.num_releases
        ),
    )


def top_genres(col: T, conn: Connection, *, num_genres: int = 5) -> List[Dict]:
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
    :param conn: A connection to the database.
    :param num_genres: The number of top genres to fetch.
    :return: The top genres.
    """
    cursor = conn.execute(
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

    logger.debug(f"Fetched top genres of collection {col.id}.")

    return [
        {
            "genre": from_row(without_key(row, "num_matches")),
            "num_matches": row["num_matches"],
        }
        for row in cursor
    ]


def image(col: T, conn: Connection) -> Optional[libimage.T]:
    """
    Return an image for a collection.

    Since collections do not have images, we return a random cover image from one of the
    releases in the collection, if any exist.

    :param col: The collection whose image to fetch.
    :param conn: A connection to the database.
    :return: The image, if it exists.
    """
    cursor = conn.execute(
        """
        SELECT images.*
        FROM images
            JOIN music__releases AS rls ON rls.image_id = images.id
            JOIN music__collections_releases AS rlscols ON rlscols.release_id = rls.id
        WHERE rlscols.collection_id = ?
        ORDER BY RANDOM()
        LIMIT 1
        """,
        (col.id,),
    )

    if row := cursor.fetchone():
        logger.debug(f"Fetched image for collection {col.id}.")
        return libimage.from_row(row)

    logger.debug(f"Failed to fetch image for collection {col.id}.")
    return None
