from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from sqlite3 import Connection, Row
from typing import Optional, Union

from src.enums import CollectionType
from src.errors import (
    AlreadyExists,
    DoesNotExist,
    Duplicate,
    Immutable,
    InvalidArgument,
    InvalidCollectionType,
    NotFound,
)
from src.util import make_fts_match_query, update_dataclass, without_key

from . import image as libimage
from . import release
from . import user as libuser

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
    #: The ID of the user that the playlist belongs to. Only set for System and Personal
    #  playlists.
    user_id: Optional[int]
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


def from_row(row: Union[dict, Row]) -> T:
    """
    Return a collection dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A collection dataclass.
    """
    return T(
        **dict(
            row,
            starred=bool(row["starred"]),
            type=CollectionType(row["type"]),
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
            COUNT(colsrls.release_id) AS num_releases
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


def from_name_type_user(
    name: str,
    type: CollectionType,
    conn: Connection,
    user_id: Optional[int] = None,
) -> Optional[T]:
    """
    Return the collection with the given name, type, and user, if it exists.

    :param name: The name of the collection.
    :param type: The type of the collection.
    :param user_id: Who the collection belongs to.
    :param conn: A connection to the database.
    :return: The collection, if it exists.
    """
    cursor = conn.execute(
        """
        SELECT
            cols.*,
            COUNT(colsrls.release_id) AS num_releases
        FROM music__collections AS cols
        LEFT JOIN music__collections_releases AS colsrls
            ON colsrls.collection_id = cols.id
        WHERE cols.name = ?
            AND cols.type = ?
            AND (cols.user_id = ? OR (cols.user_id IS NULL AND ? IS NULL))
        GROUP BY cols.id
        LIMIT 1
        """,
        (name, type.value, user_id, user_id),
    )

    if row := cursor.fetchone():
        logger.debug(
            f'Fetched collection {row["id"]} with '
            f'name "{name}", type {type}, and user {user_id}.'
        )
        return from_row(row)

    logger.debug(
        "Failed to fetch collection with "
        f'name "{name}", type {type}, and user {user_id}.'
    )
    return None


def from_name_and_type(
    name: str,
    type: CollectionType,
    conn: Connection,
) -> list[T]:
    """
    Return all collections with the given name and type.

    :param name: The name of the collection.
    :param type: The type of the collection.
    :param conn: A connection to the database.
    :return: The collection, if it exists.
    """
    cursor = conn.execute(
        """
        SELECT
            cols.*,
            COUNT(colsrls.release_id) AS num_releases
        FROM music__collections AS cols
        LEFT JOIN music__collections_releases AS colsrls
            ON colsrls.collection_id = cols.id
        WHERE cols.name = ? AND cols.type = ?
        GROUP BY cols.id
        """,
        (name, type.value),
    )

    logger.debug(f"Fetched all collections with name {name} and type {type}.")
    return [from_row(row) for row in cursor]


def search(
    conn: Connection,
    *,
    search: str = "",
    types: list[CollectionType] = [],
    user_ids: list[int] = [],
    page: int = 1,
    per_page: Optional[int] = None,
) -> list[T]:
    """
    Search for collections. Parameters are optional; omitted ones are excluded from the
    matching criteria.

    :param conn: A connection to the database.
    :param search: A search string. We split this up into individual punctuation-less
                   tokens and return collections whose titles contain each token. If
                   specified, the returned collections will be sorted by match
                   proximity.
    :param types: Filter by collection types.
    :param user_ids: Filter by collection owners.
    :param page: Which page of collections to return.
    :param per_page: The number of collections per page. Pass ``None`` to return all
                     collections (this will ignore ``page``).
    :return: All matching collections.
    """
    filters, params = _generate_filters(search, types, user_ids)

    if per_page:
        params.extend([per_page, (page - 1) * per_page])

    cursor = conn.execute(
        f"""
        SELECT
            cols.*,
            COUNT(colsrls.release_id) AS num_releases
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
    types: list[CollectionType] = [],
    user_ids: list[int] = [],
) -> int:
    """
    Fetch the number of collections matching the passed-in criteria. Parameters are
    optional; omitted ones are excluded from the matching criteria.

    :param conn: A connection to the database.
    :param search: A search string. We split this up into individual punctuation-less
                   tokens and return collections whose titles contain each token.
    :param types: Filter by collection types.
    :param user_ids: Filter by collection owners.
    :return: The number of matching collections.
    """
    filters, params = _generate_filters(search, types, user_ids)

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
    types: list[CollectionType] = [],
    user_ids: list[int] = [],
) -> tuple[list[str], list[Union[str, int]]]:
    """
    Dynamically generate the SQL filters and parameters from the criteria. See the
    search and total functions for parameter descriptions.

    :return: A tuple of SQL filter strings and parameters. The SQL filter strings can be
    joined with `` AND `` and injected into the where clause.
    """
    filters: list[str] = []
    params: list[Union[str, int]] = []

    if search:
        filters.append("fts.music__collections__fts MATCH ?")
        params.append(make_fts_match_query(search))

    if types:
        filters.append(f"cols.type IN ({','.join('?' * len(types))})")
        params.extend([t.value for t in types])

    if user_ids:
        filters.append(f"cols.user_id IN ({','.join('?' * len(user_ids))})")
        params.extend(user_ids)

    return filters, params


def create(
    name: str,
    type: CollectionType,
    conn: Connection,
    starred: bool = False,
    user_id: Optional[int] = None,
    override_immutable: bool = False,
) -> T:
    """
    Create a collection and persist it to the database.

    :param name: The name of the collection.
    :param type: The type of the collection.
    :param conn: A connection to the database.
    :param starred: Whether the collection is starred or not.
    :param user_id: The ID of the user that this collection belongs to. Should be set
                    for Personal and System collections; unset otherwise.
    :param override_immutable: Whether to allow creation of immutable collections. For
                               internal use.
    :return: The newly created collection.
    :raises Duplicate: If an collection with the same name and type already exists. The
                       duplicate collection is passed as the ``entity`` argument.
    :raises InvalidArgument: If the user_id argument is passed with an non-personal
                             collection type.
    """
    if type == CollectionType.SYSTEM and not override_immutable:
        raise InvalidCollectionType("Cannot create system collections.")

    if type in [CollectionType.PERSONAL, CollectionType.SYSTEM] and user_id is None:
        raise InvalidArgument(
            "Missing user_id argument for personal/system collection."
        )

    if (
        type not in [CollectionType.PERSONAL, CollectionType.SYSTEM]
        and user_id is not None
    ):
        raise InvalidArgument(
            "The user_id argument can only be set for personal/system collections."
        )

    if col := from_name_type_user(name, type, conn, user_id):
        raise Duplicate(f'Collection "{name}" already exists.', col)

    cursor = conn.execute(
        """
        INSERT INTO music__collections (name, type, starred, user_id)
        VALUES (?, ?, ?, ?)
        """,
        (name, type.value, starred, user_id),
    )

    logger.info(
        f'Created collection "{name}" of type {type} with ID {cursor.lastrowid}.'
    )

    col = from_id(cursor.lastrowid, conn)
    assert col is not None
    return col


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
        and (dupl := from_name_type_user(changes["name"], col.type, conn, col.user_id))
        and dupl != col
    ):
        raise Duplicate(f'Collection "{changes["name"]}" already exists.', dupl)

    changes["last_updated_on"] = datetime.utcnow()

    conn.execute(
        """
        UPDATE music__collections
        SET name = ?,
            starred = ?,
            last_updated_on = ?
        WHERE id = ?
        """,
        (
            changes.get("name", col.name),
            changes.get("starred", col.starred),
            changes["last_updated_on"],
            col.id,
        ),
    )

    logger.info(f"Updated collection {col.id} with {changes}.")

    return update_dataclass(col, **changes)


def releases(col: T, conn: Connection) -> list[release.T]:
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

    now = datetime.now()

    conn.execute(
        """
        UPDATE music__collections
        SET last_updated_on = ?
        WHERE id = ?
        """,
        (
            col.id,
            now,
        ),
    )

    logger.info(f"Added release {release_id} to collection {col.id}.")

    return update_dataclass(
        col,
        num_releases=(
            col.num_releases + 1 if col.num_releases is not None else col.num_releases
        ),
        last_updated_on=now,
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

    now = datetime.utcnow()

    conn.execute(
        """
        UPDATE music__collections
        SET last_updated_on = ?
        WHERE id = ?
        """,
        (
            now,
            col.id,
        ),
    )

    logger.info(f"Deleted release {release_id} from collection {col.id}.")

    return update_dataclass(
        col,
        num_releases=(
            col.num_releases - 1 if col.num_releases is not None else col.num_releases
        ),
        last_updated_on=now,
    )


def top_genres(col: T, conn: Connection, *, num_genres: int = 5) -> list[dict]:
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

    The field ``num_releases`` in the genre collections is set to ``None``.

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


def user(col: T, conn: Connection) -> Optional[libuser.T]:
    """
    Returns the user the collection belongs to, if it belongs to a user.

    :param col: The collection whose user to fetch.
    :param conn: A connection to the database.
    :return: The user, if one exists.
    """
    return libuser.from_id(col.user_id, conn) if col.user_id else None


def inbox_of(user_id: int, conn: Connection) -> T:
    """
    Return the inbox collection of the passed-in user.

    :param user_id: The ID of the user whose inbox to fetch.
    :param conn: A connection to the database.
    :return: The user's inbox collection.
    :raises DoesNotExist: If the inbox does not exist.
    """
    col = from_name_type_user(
        "Inbox",
        CollectionType.SYSTEM,
        user_id=user_id,
        conn=conn,
    )
    if col is None:  # pragma: no cover
        raise DoesNotExist(f"No inbox exists for user {user_id}.")
    return col


def favorites_of(user_id: int, conn: Connection) -> T:
    """
    Return the favorites collection of the passed-in user.

    :param user_id: The ID of the user whose favorites to fetch.
    :param conn: A connection to the database.
    :return: The user's favorites collection.
    :raises DoesNotExist: If the inbox does not exist.
    """
    col = from_name_type_user(
        "Favorites",
        CollectionType.SYSTEM,
        user_id=user_id,
        conn=conn,
    )
    if col is None:  # pragma: no cover
        raise DoesNotExist(f"No favorites collection exists for user {user_id}.")
    return col


def has_release(col: T, release_id: int, conn: Connection) -> bool:
    """
    Return whether the collection has a given release.

    :param col: The collection to check membership in.
    :param release_id: The release to check membership for.
    :param conn: A connection to the database.
    :return: Whether the release exists in the collection.
    """
    cursor = conn.execute(
        """
        SELECT 1
        FROM music__collections_releases
        WHERE collection_id = ? AND release_id = ?
        """,
        (col.id, release_id),
    )
    return bool(cursor.fetchone())
