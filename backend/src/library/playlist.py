"""
This module contains the playlist dataclass and its associated functions.

A playlist is an ordered list of tracks and associated metainfo. We denote a track in a
playlist an "entry." Each entry represents a track and its index in the playlist. The
``playlist_entry`` module contains an entry dataclass and associated functions for
working with playlist entries.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from sqlite3 import Connection, Row
from typing import Optional, Union

from src.enums import CollectionType, PlaylistType
from src.errors import Duplicate, Immutable, InvalidArgument, InvalidPlaylistType
from src.util import make_fts_match_query, update_dataclass, without_key

from . import collection
from . import image as libimage
from . import playlist_entry as pentry
from . import user as libuser

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class T:
    """A playlist dataclass."""

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    name: str
    #:
    starred: bool
    #:
    type: PlaylistType
    #: The ID of the user that the playlist belongs to. Only set for System and Personal
    #  playlists.
    user_id: Optional[int]
    #:
    num_tracks: Optional[int] = None
    #:
    last_updated_on: Optional[datetime] = None


def exists(id: int, conn: Connection) -> bool:
    """
    Return whether a playlist exists with the given ID.

    :param id: The ID to check.
    :param conn: A connection to the database.
    :return: Whether a playlist has the given ID.
    """
    cursor = conn.execute("SELECT 1 FROM music__playlists WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Union[dict, Row]) -> T:
    """
    Return a playlist dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A playlist dataclass.
    """
    return T(
        **dict(
            row,
            starred=bool(row["starred"]),
            type=PlaylistType(row["type"]),
        )
    )


def from_id(id: int, conn: Connection) -> Optional[T]:
    """
    Return the playlist with the provided ID.

    :param id: The ID of the playlist to fetch.
    :param conn: A connection to the database.
    :return: The playlist with the provided ID, if it exists.
    """
    cursor = conn.execute(
        """
        SELECT
            plys.*,
            COUNT(plystrks.track_id) AS num_tracks
        FROM music__playlists AS plys
        LEFT JOIN music__playlists_tracks AS plystrks
            ON plystrks.playlist_id = plys.id
        WHERE plys.id = ?
        GROUP BY plys.id
        """,
        (id,),
    )

    if row := cursor.fetchone():
        logger.debug(f"Fetched playlist {id}.")
        return from_row(row)

    logger.debug(f"Failed to fetch playlist {id}.")
    return None


def from_name_type_user(
    name: str,
    type: PlaylistType,
    conn: Connection,
    user_id: int = None,
) -> Optional[T]:
    """
    Return the playlist with the given name, type, and user, if it exists.

    :param name: The name of the playlist.
    :param type: The type of the playlist.
    :param user_id: Who the playlist belongs to.
    :param conn: A connection to the database.
    :return: The playlist, if it exists.
    """
    cursor = conn.execute(
        """
        SELECT
            plys.*,
            COUNT(plystrks.track_id) AS num_tracks
        FROM music__playlists AS plys
        LEFT JOIN music__playlists_tracks AS plystrks
            ON plystrks.playlist_id = plys.id
        WHERE plys.name = ?
            AND plys.type = ?
            AND (plys.user_id = ? OR (plys.user_id IS NULL AND ? IS NULL))
        GROUP BY plys.id
        """,
        (name, type.value, user_id, user_id),
    )

    if row := cursor.fetchone():
        logger.debug(
            f'Fetch playlist {row["id"]} with '
            f'name "{name}", type {type}, and user {user_id}.'
        )
        return from_row(row)

    logger.debug(
        f"Failed to fetch playlist with "
        f'name "{name}", type {type}, and user {user_id}.'
    )
    return None


def search(
    conn: Connection,
    *,
    search: str = "",
    types: list[PlaylistType] = [],
    user_ids: list[int] = [],
    page: int = 1,
    per_page: Optional[int] = None,
) -> list[T]:
    """
    Search for playlists. Parameters are optional; omitted ones are excluded from the
    matching criteria.

    :param conn: A connection to the database.
    :param search: A search string. We split this up into individual punctuation-less
                   tokens and return playlists whose titles contain each token. If
                   specified, the returned playlists will be sorted by match proximity.
    :param types: Filter by playlist types.
    :param user_ids: Filter by collection owners.
    :param page: Which page of playlists to return.
    :param per_page: The number of playlists per page. Pass ``None`` to return all
                     playlists (this will ignore ``page``).
    :return: All matching playlists.
    """
    filters, params = _generate_filters(search, types, user_ids)

    if per_page:
        params.extend([per_page, (page - 1) * per_page])

    cursor = conn.execute(
        f"""
        SELECT
            plys.*,
            COUNT(plystrks.track_id) AS num_tracks
        FROM music__playlists AS plys
        JOIN music__playlists__fts AS fts ON fts.rowid = plys.id
        LEFT JOIN music__playlists_tracks AS plystrks
            ON plystrks.playlist_id = plys.id
        {"WHERE " + " AND ".join(filters) if filters else ""}
        GROUP BY plys.id
        ORDER BY
            {"fts.rank" if search else "plys.type, plys.starred DESC, plys.name"}
        {"LIMIT ? OFFSET ?" if per_page else ""}
        """,
        params,
    )

    logger.debug(f"Searched playlists with {cursor.rowcount} results.")
    return [from_row(row) for row in cursor]


def count(
    conn: Connection,
    *,
    search: str = "",
    types: list[PlaylistType] = [],
    user_ids: list[int] = [],
) -> int:
    """
    Fetch the number of playlists matching the passed-in criteria. Parameters are
    optional; omitted ones are excluded from the matching criteria.

    :param conn: A connection to the database.
    :param search: A search string. We split this up into individual punctuation-less
                   tokens and return playlists whose titles contain each token.
    :param types: Filter by playlist types.
    :param user_ids: Filter by collection owners.
    :return: The number of matching playlists.
    """
    filters, params = _generate_filters(search, types, user_ids)

    cursor = conn.execute(
        f"""
        SELECT COUNT(1)
        FROM music__playlists AS plys
        JOIN music__playlists__fts AS fts ON fts.rowid = plys.id
        {"WHERE " + " AND ".join(filters) if filters else ""}
        """,
        params,
    )

    count = cursor.fetchone()[0]
    logger.debug(f"Counted {count} playlists that matched the filters.")
    return count


def _generate_filters(
    search: str = "",
    types: list[PlaylistType] = [],
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
        filters.append("fts.music__playlists__fts MATCH ?")
        params.append(make_fts_match_query(search))

    if types:
        filters.append(f"plys.type IN ({','.join('?' * len(types))})")
        params.extend([t.value for t in types])

    if user_ids:
        filters.append(f"plys.user_id IN ({','.join('?' * len(user_ids))})")
        params.extend(user_ids)

    return filters, params


def create(
    name: str,
    type: PlaylistType,
    conn: Connection,
    starred: bool = False,
    user_id: Optional[int] = None,
    override_immutable: bool = False,
) -> T:
    """
    Create a playlist and persist it to the database.

    :param name: The name of the playlist.
    :param type: The type of the playlist.
    :param conn: A connection to the database.
    :param starred: Whether the playlist is starred or not.
    :param user_id: The ID of the user that this playlist belongs to. Should be set for
                    Personal and System playlists; unset otherwise.
    :param override_immutable: Whether to allow creation of immutable playlists. For
                               internal use.
    :return: The newly created playlist.
    :raises Duplicate: If an playlist with the same name and type already exists. The
                       duplicate playlist is passed as the ``entity`` argument.
    :raises InvalidArgument: If the user_id argument is passed with a non-personal
                             playlist type.
    """
    if type == PlaylistType.SYSTEM and not override_immutable:
        raise InvalidPlaylistType("Cannot create system playlists.")

    if type in [PlaylistType.PERSONAL, PlaylistType.SYSTEM] and user_id is None:
        raise InvalidArgument(
            "Missing user_id argument for personal/system collection."
        )

    if type not in [PlaylistType.PERSONAL, PlaylistType.SYSTEM] and user_id is not None:
        raise InvalidArgument(
            "The user_id argument can only be set for personal/system collections."
        )

    if ply := from_name_type_user(name, type, conn, user_id):
        raise Duplicate(f'Playlist "{name}" already exists.', ply)

    cursor = conn.execute(
        """
        INSERT INTO music__playlists (name, type, starred, user_id)
        VALUES (?, ?, ?, ?)
        """,
        (name, type.value, starred, user_id),
    )

    logger.info(f'Created playlist "{name}" of type {type} with ID {cursor.lastrowid}.')

    ply = from_id(cursor.lastrowid, conn)
    assert ply is not None
    return ply


def update(ply: T, conn: Connection, **changes) -> T:
    """
    Update a playlist and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    **Note: The type and user_id of a playlist cannot be changed.**

    :param ply: The playlist to update.
    :param conn: A connection to the database.
    :param name: New playlist name.
    :type  name: :py:obj:`str`
    :param starred: Whether ew playlist is starred.
    :type  starred: :py:obj:`bool`
    :return: The updated playlist.
    :raises Immutable: If the playlist cannot be updated.
    :raises Duplicate: If the new name conflicts with another playlist.
    """
    if ply.type == PlaylistType.SYSTEM:
        raise Immutable("System playlists cannot be modified.")

    if (
        "name" in changes
        and (dupl := from_name_type_user(changes["name"], ply.type, conn, ply.user_id))
        and dupl != ply
    ):
        raise Duplicate(f'Playlist "{changes["name"]}" already exists.', dupl)

    changes["last_updated_on"] = datetime.utcnow()

    conn.execute(
        """
        UPDATE music__playlists
        SET name = ?,
            starred = ?,
            last_updated_on = ?
        WHERE id = ?
        """,
        (
            changes.get("name", ply.name),
            changes.get("starred", ply.starred),
            changes["last_updated_on"],
            ply.id,
        ),
    )

    logger.info(f"Updated playlist {ply.id} with {changes}.")

    return update_dataclass(ply, **changes)


def entries(ply: T, conn: Connection) -> list[pentry.T]:
    """
    Get the tracks in a playlist.

    :param ply: The playlist whose tracks we want to get.
    :param conn: A connection to the database.
    :return: A list of tracks in the playlist.
    """
    cursor = conn.execute(
        """
        SELECT
            plystrks.*
        FROM music__playlists AS plys
        JOIN music__playlists_tracks AS plystrks ON plystrks.playlist_id = plys.id
        WHERE plys.id = ?
        ORDER BY plystrks.position ASC
        """,
        (ply.id,),
    )

    logger.debug(f"Fetched tracks of playlist {ply}.")
    return [pentry.from_row(row) for row in cursor]


def top_genres(ply: T, conn: Connection, *, num_genres: int = 5) -> list[dict]:
    """
    Get the top genre collections of the tracks in a playlist.

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

    :param ply: The playlist whose top genres to fetch.
    :param conn: A connection to the database.
    :param num_genres: The number of top genres to fetch.
    :return: The top genres.
    """
    cursor = conn.execute(
        """
        SELECT
            genres.*,
            COUNT(plystrks.track_id) AS num_matches
        FROM music__collections AS genres
        LEFT JOIN music__collections_releases AS colsrls
            ON colsrls.collection_id = genres.id
        LEFT JOIN music__tracks AS trks
            ON trks.release_id = colsrls.release_id
        LEFT JOIN music__playlists_tracks AS plystrks
            ON plystrks.track_id = trks.id
        WHERE plystrks.playlist_id = ? AND genres.type = ?
        GROUP BY genres.id
        ORDER BY num_matches DESC, genres.id ASC
        LIMIT ?
        """,
        (ply.id, CollectionType.GENRE.value, num_genres),
    )

    logger.debug(f"Fetched top genres of playlist {ply.id}.")
    return [
        {
            "genre": collection.from_row(without_key(row, "num_matches")),
            "num_matches": row["num_matches"],
        }
        for row in cursor
    ]


def image(ply: T, conn: Connection) -> Optional[libimage.T]:
    """
    Return an image for a playlist.

    Since playlists do not have images, we return a random cover image from one of the
    tracks in the playlist, if any exist.

    :param ply: The playlist whose image to fetch.
    :param conn: A connection to the database.
    :return: The image, if it exists.
    """
    cursor = conn.execute(
        """
        SELECT images.*
        FROM images
        JOIN music__releases AS rls ON rls.image_id = images.id
        JOIN music__tracks AS trk ON trk.release_id = rls.id
        JOIN music__playlists_tracks AS plystrks ON plystrks.track_id = trk.id
        WHERE plystrks.playlist_id = ?
        ORDER BY RANDOM()
        LIMIT 1
        """,
        (ply.id,),
    )

    if row := cursor.fetchone():
        logger.debug(f"Fetched image for playlist {ply.id}.")
        return libimage.from_row(row)

    logger.debug(f"Failed to fetch image for playlist {ply.id}.")
    return None


def user(ply: T, conn: Connection) -> Optional[libuser.T]:
    """
    Returns the user the playlist belongs to, if it belongs to a user.

    :param ply: The playlist whose user to fetch.
    :param conn: A connection to the database.
    :return: The user, if one exists.
    """
    return libuser.from_id(ply.user_id, conn) if ply.user_id else None
