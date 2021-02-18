"""
This module contains the dataclass and associated functions for an entry in a playlist.

Each entry represents a track in the playlist and its location in the playlist.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from sqlite3 import Cursor, Row
from typing import Dict, Optional, Union

from src.errors import NotFound

from . import playlist as libplaylist
from . import track as libtrack

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class T:
    """A playlist track entry."""

    # We have these empty comments so that the attributes and types render in sphinx...
    #: The ID of the entry. Unique across all playlists.
    id: int
    #: The track. Not unique.
    track_id: int
    #: The ID of the playlist this entry belongs to.
    playlist_id: int
    #: The index of the track in the playlist. Unique to the playlist.
    position: int
    #: When the entry was added to the playlist.
    added_on: datetime


def exists(id: int, cursor: Cursor) -> bool:
    """
    Return whether a playlist entry exists with the given ID.

    :param id: The ID to check.
    :param cursor: A cursor to the database.
    :return: Whether a playlist entry has the given ID.
    """
    cursor.execute("SELECT 1 FROM music__playlists_tracks WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Union[Dict, Row]) -> T:
    """
    Return a playlist entry dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A playlist entry dataclass.
    """
    return T(**dict(row))


def from_id(id: int, cursor: Cursor) -> Optional[T]:
    """
    Return the playlist entry with the provided ID.

    :param id: The ID of the playlist entry to fetch.
    :param cursor: A cursor to the database.
    :return: The playlist entry with the provided ID, if it exists.
    """
    cursor.execute(
        """
        SELECT *
        FROM music__playlists_tracks
        WHERE id = ?
        """,
        (id,),
    )

    if row := cursor.fetchone():
        logger.debug(f"Fetched playlist entry {id}.")
        return from_row(row)

    logger.debug(f"Failed to fetch playlist entry {id}.")
    return None


def create(playlist_id: int, track_id: int, cursor: Cursor) -> T:
    """
    Add the provided track to the provided playlist.

    :param playlist_id: The ID of the playlist to add the entry to.
    :param track_id: The ID of the track to insert.
    :param cursor: A cursor to the database.
    :return: The new playlist entry.
    :raises NotFound: If no track has the given track ID.
    """
    if not track.exists(track_id, cursor):
        logger.debug(f"Track {track_id} does not exist.")
        raise NotFound(f"Track {track_id} does not exist.")

    if not playlist.exists(playlist_id, cursor):
        logger.debug(f"Playlist {playlist_id} does not exist.")
        raise NotFound(f"Playlist {playlist_id} does not exist.")

    cursor.execute(
        """
        INSERT INTO music__playlists_tracks (playlist_id, track_id, position)
        VALUES (?, ?, ?)
        """,
        (playlist_id, track_id, _highest_position(playlist_id, cursor) + 1),
    )

    logger.info(
        f"Created entry {cursor.lastrowid} with "
        "track {track_id} and playlist {playlist_id}."
    )
    return from_id(cursor.lastrowid)


def delete(ety: T, cursor: Cursor):
    """
    Remove the provided playlist entry from the provided playlist.

    :param ety: The playlist entry to delete.
    :param cursor: A cursor to the database.
    :raises NotFound: If no entry has the given ID.
    """
    cursor.execute(
        """
        SELECT position, playlist_id FROM music__playlists_tracks WHERE id = ?
        """,
        (ety.id,),
    )
    row = cursor.fetchone()

    if not row:
        logger.debug(f"Entry {ety.id} does not exist.")
        raise NotFound(f"Entry {ety.id} does not exist.")

    cursor.execute(
        """
        DELETE FROM music__playlists_tracks WHERE id = ?
        """,
        (ety.id,),
    )

    cursor.execute(
        """
        UPDATE music__playlists_tracks
        SET position = position - 1
        WHERE playlist_id = ? AND position > ?
        """,
        (row["playlist_id"], row["position"]),
    )

    logger.info(f"Deleted entry {ety.id}.")


def update(ety: T, position: int, cursor: Cursor) -> T:
    """
    Update the index of an entry in a playlist. Shift all other entries accordingly.

    :param ety: The playlist entry to update.
    :param position: The intended new index of the entry.
    :param cursor: A cursor to the database.
    :return: The updated entry.
    :raises IndexError: If the entry is out of bounds.
    """
    max_ = _highest_position(ety.playlist_id, cursor)

    if position < 1 or position > max_:
        raise IndexError(f"Position {position} out of bounds.")

    # Nothing to do here...
    if position == ety.position:
        return ety

    if position > ety.position:
        cursor.execute(
            """
            UPDATE music__playlists_tracks
            SET position = position - 1
            WHERE playlist_id = ? AND position > ? AND position <= ?
            """,
            (ety.playlist_id, ety.position, position),
        )
        cursor.execute(
            """
            UPDATE music__playlists_tracks SET position = ? WHERE id = ?
            """,
            (position, ety.id),
        )
    else:
        cursor.execute(
            """
            UPDATE music__playlists_tracks
            SET position = position + 1
            WHERE playlist_id = ? AND position < ? AND position >= ?
            """,
            (ety.playlist_id, ety.position, position),
        )
        cursor.execute(
            """
            UPDATE music__playlists_tracks SET position = ? WHERE id = ?
            """,
            (position, ety.id),
        )

    logger.info(f"Updated position of entry {id} to {position}.")


def playlist(ety: T, cursor: Cursor) -> libplaylist.T:
    """
    Fetch the playlist that this entry is in.

    :param ety: The playlist entity.
    :param cursor: A cursor to the database.
    :return: The playlist the entry is in.
    """
    return libplaylist.from_id(ety.playlist_id, cursor)


def track(ety: T, cursor: Cursor) -> libtrack.T:
    """
    Fetch the track that this entry represents.

    :param ety: The playlist entity.
    :param cursor: A cursor to the database.
    :return: The track the entry represents.
    """
    return libtrack.from_id(ety.track_id, cursor)


def _highest_position(playlist_id: int, cursor: Cursor) -> int:
    """
    Return the highest position number for a track in a playlist. If there are no
    entries in the playlist, this returns 0.

    :param playlist_id: The playlist ID.
    :param cursor: A cursor to the database.
    :return: The next unused position number in a playlist.
    """
    cursor.execute(
        """
        SELECT MAX(position) FROM music__playlists_tracks WHERE playlist_id = ?
        """,
        (playlist_id,),
    )

    if row := cursor.fetchone():
        logger.debug(
            f"Fetched highest position of {row[0]} for playlist {playlist_id}."
        )
        return row[0]

    logger.debug(f"Fetched highest position of 1 for playlist {playlist_id}.")
    return 0
