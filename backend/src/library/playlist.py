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
from sqlite3 import Cursor, Row
from typing import Dict, List, Optional, Union

from src.enums import CollectionType, PlaylistType
from src.errors import Duplicate, Immutable, InvalidPlaylistType
from src.util import update_dataclass, without_key

from . import collection
from . import image as libimage
from . import playlist_entry as pentry

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
    #:
    num_tracks: Optional[int] = None
    #:
    last_updated_on: Optional[datetime] = None


def exists(id: int, cursor: Cursor) -> bool:
    """
    Return whether a playlist exists with the given ID.

    :param id: The ID to check.
    :param cursor: A cursor to the database.
    :return: Whether a playlist has the given ID.
    """
    cursor.execute("SELECT 1 FROM music__playlists WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Union[Dict, Row]) -> T:
    """
    Return a playlist dataclass containing data from a row from the database.

    _Note: For some reason, SQLite doesn't parse the ``last_updated_on`` row as a
    ``datetime`` object, instead parsing it as a string. So we do the manual conversion
    here to a datetime object.

    :param row: A row from the database.
    :return: A playlist dataclass.
    """
    try:
        last_updated_on = datetime.fromisoformat(row["last_updated_on"])
    except (KeyError, TypeError):
        last_updated_on = None  # type: ignore

    return T(
        **dict(
            row,
            starred=bool(row["starred"]),
            type=PlaylistType(row["type"]),
            last_updated_on=last_updated_on,
        )
    )


def from_id(id: int, cursor: Cursor) -> Optional[T]:
    """
    Return the playlist with the provided ID.

    :param id: The ID of the playlist to fetch.
    :param cursor: A cursor to the database.
    :return: The playlist with the provided ID, if it exists.
    """
    cursor.execute(
        """
        SELECT
            plys.*,
            COUNT(plystrks.track_id) AS num_tracks,
            MAX(plystrks.added_on) AS last_updated_on
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


def from_name_and_type(name: str, type: PlaylistType, cursor: Cursor) -> Optional[T]:
    """
    Return the playlist with the given name and type, if it exists.

    :param name: The name of the playlist.
    :param type: The type of the playlist.
    :param cursor: A cursor to the database.
    :return: The playlist, if it exists.
    """
    cursor.execute(
        """
        SELECT
            plys.*,
            COUNT(plystrks.track_id) AS num_tracks,
            MAX(plystrks.added_on) AS last_updated_on
        FROM music__playlists AS plys
        LEFT JOIN music__playlists_tracks AS plystrks
            ON plystrks.playlist_id = plys.id
        WHERE plys.name = ? AND plys.type = ?
        GROUP BY plys.id
        """,
        (name, type.value),
    )

    if row := cursor.fetchone():
        logger.debug(f'Fetch playlist {row["id"]} with name "{name}" and type {type}.')
        return from_row(row)

    logger.debug(f'Failed to fetch playlist with name "{name}" and type {type}.')
    return None


def all(cursor: Cursor, types: List[PlaylistType] = []) -> List[T]:
    """
    Get all playlists.

    :param cursor: A cursor to the database.
    :param types: Filter by playlist types. Pass an empty list to fetch all types.
    :return: All playlists stored on the src.
    """
    filter_ = f"WHERE plys.type IN ({','.join('?' * len(types))})" if types else ""

    cursor.execute(
        f"""
        SELECT
            plys.*,
            COUNT(plystrks.track_id) AS num_tracks,
            MAX(plystrks.added_on) AS last_updated_on
        FROM music__playlists AS plys
        LEFT JOIN music__playlists_tracks AS plystrks
            ON plystrks.playlist_id = plys.id
        {filter_}
        GROUP BY plys.id
        ORDER BY
            plys.type,
            plys.starred DESC,
            plys.name
        """,
        tuple(type_.value for type_ in types),
    )

    logger.debug("Fetched all playlists.")
    return [from_row(row) for row in cursor.fetchall()]


def create(name: str, type: PlaylistType, cursor: Cursor, starred: bool = False) -> T:
    """
    Create a playlist and persist it to the database.

    :param name: The name of the playlist.
    :param type: The type of the playlist.
    :cursor: A cursor to the database.
    :param starred: Whether the playlist is starred or not.
    :return: The newly created playlist.
    :raises Duplicate: If an playlist with the same name and type already exists. The
                       duplicate playlist is passed as the ``entity`` argument.
    """
    if type == PlaylistType.SYSTEM:
        raise InvalidPlaylistType("Cannot create system playlists.")

    if ply := from_name_and_type(name, type, cursor):
        raise Duplicate(f'Playlist "{name}" already exists.', ply)

    cursor.execute(
        "INSERT INTO music__playlists (name, type, starred) VALUES (?, ?, ?)",
        (name, type.value, starred),
    )

    logger.info(f'Created playlist "{name}" of type {type} with ID {cursor.lastrowid}.')

    return T(
        id=cursor.lastrowid,
        name=name,
        type=type,
        starred=starred,
        num_tracks=0,
    )


def update(ply: T, cursor: Cursor, **changes) -> T:
    """
    Update a playlist and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    **Note: The type of a playlist cannot be changed.**

    :param ply: The playlist to update.
    :param cursor: A cursor to the database.
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
        and (dupl := from_name_and_type(changes["name"], ply.type, cursor))
        and dupl != ply
    ):
        raise Duplicate(f'Playlist "{changes["name"]}" already exists.', dupl)

    cursor.execute(
        """
        UPDATE music__playlists
        SET name = ?,
            starred = ?
        WHERE id = ?
        """,
        (
            changes.get("name", ply.name),
            changes.get("starred", ply.starred),
            ply.id,
        ),
    )

    logger.info(f"Updated playlist {ply.id} with {changes}.")

    return update_dataclass(ply, **changes)


def entries(ply: T, cursor: Cursor) -> List[pentry.T]:
    """
    Get the tracks in a playlist.

    :param ply: The playlist whose tracks we want to get.
    :param cursor: A cursor to the database.
    :return: A list of tracks in the playlist.
    """
    cursor.execute(
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
    return [pentry.from_row(row) for row in cursor.fetchall()]


def top_genres(ply: T, cursor: Cursor, *, num_genres: int = 5) -> List[Dict]:
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

    The fields ``num_tracks`` and ``last_updated_on`` in the genre playlists are set
    to ``None``.

    :param ply: The playlist whose top genres to fetch.
    :param cursor: A cursor to the database.
    :param num_genres: The number of top genres to fetch.
    :return: The top genres.
    """
    cursor.execute(
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
        for row in cursor.fetchall()
    ]


def image(ply: T, cursor: Cursor) -> Optional[libimage.T]:
    """
    Return an image for a playlist.

    Since playlists do not have images, we return a random cover image from one of the
    tracks in the playlist, if any exist.

    :param ply: The playlist whose image to fetch.
    :param cursor: A cursor to the database.
    :return: The image, if it exists.
    """
    cursor.execute(
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
