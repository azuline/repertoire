"""
This module contains the dataclass and associated functions for an entry in a playlist.

Each entry represents a track in the playlist and its location in the playlist.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from sqlite3 import Connection, Row
from typing import Optional, Union

from src.errors import NotFound
from src.util import update_dataclass

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


def exists(id: int, conn: Connection) -> bool:
    """
    Return whether a playlist entry exists with the given ID.

    :param id: The ID to check.
    :param conn: A connection to the database.
    :return: Whether a playlist entry has the given ID.
    """
    cursor = conn.execute("SELECT 1 FROM music__playlists_tracks WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def exists_playlist_and_track(
    playlist_id: int, track_id: int, conn: Connection
) -> bool:
    """
    Check whether the given track is in the given playlist.

    :param playlist_id: The ID of the playlist.
    :param track_id: The ID of the track.
    :param conn: A connection to the database.
    :return: Whether the track is in the playlist.
    """
    cursor = conn.execute(
        """
        SELECT 1 FROM music__playlists_tracks
        WHERE playlist_id = ? AND track_id = ?
        """,
        (playlist_id, track_id),
    )
    return bool(cursor.fetchone())


def from_row(row: Union[dict, Row]) -> T:
    """
    Return a playlist entry dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A playlist entry dataclass.
    """
    return T(**dict(row))


def from_id(id: int, conn: Connection) -> Optional[T]:
    """
    Return the playlist entry with the provided ID.

    :param id: The ID of the playlist entry to fetch.
    :param conn: A connection to the database.
    :return: The playlist entry with the provided ID, if it exists.
    """
    cursor = conn.execute(
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


def from_playlist_and_track(
    playlist_id: int, track_id: int, conn: Connection
) -> list[T]:
    """
    Return the playlist entries with the provided playlist and track IDs.

    :param playlist_id: The ID of the playlist.
    :param track_id: The ID of the track.
    :param conn: A connection to the database.
    :return: The playlist entries with the provided playlist and track.
    """
    cursor = conn.execute(
        """
        SELECT *
        FROM music__playlists_tracks
        WHERE playlist_id = ? AND track_id = ?
        """,
        (playlist_id, track_id),
    )

    logger.debug(
        f"Fetched playlist entries for playlist {playlist_id} and track {track_id}."
    )
    return [from_row(row) for row in cursor]


def create(playlist_id: int, track_id: int, conn: Connection) -> T:
    """
    Add the provided track to the provided playlist.

    :param playlist_id: The ID of the playlist to add the entry to.
    :param track_id: The ID of the track to insert.
    :param conn: A connection to the database.
    :return: The new playlist entry.
    :raises NotFound: If no track has the given track ID.
    """
    if not libtrack.exists(track_id, conn):
        logger.debug(f"Track {track_id} does not exist.")
        raise NotFound(f"Track {track_id} does not exist.")

    if not libplaylist.exists(playlist_id, conn):
        logger.debug(f"Playlist {playlist_id} does not exist.")
        raise NotFound(f"Playlist {playlist_id} does not exist.")

    cursor = conn.execute(
        """
        INSERT INTO music__playlists_tracks (playlist_id, track_id, position)
        VALUES (?, ?, ?)
        """,
        (playlist_id, track_id, _highest_position(playlist_id, conn) + 1),
    )

    conn.execute(
        """
        UPDATE music__playlists
        SET last_updated_on = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (playlist_id,),
    )

    logger.info(
        f"Created entry {cursor.lastrowid} with "
        "track {track_id} and playlist {playlist_id}."
    )
    pety = from_id(cursor.lastrowid, conn)
    assert pety is not None
    return pety


def delete(ety: T, conn: Connection):
    """
    Remove the provided playlist entry from the provided playlist.

    :param ety: The playlist entry to delete.
    :param conn: A connection to the database.
    """
    conn.execute(
        """
        DELETE FROM music__playlists_tracks WHERE id = ?
        """,
        (ety.id,),
    )

    conn.execute(
        """
        UPDATE music__playlists_tracks
        SET position = position - 1
        WHERE playlist_id = ? AND position > ?
        """,
        (ety.playlist_id, ety.position),
    )

    conn.execute(
        """
        UPDATE music__playlists
        SET last_updated_on = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (ety.playlist_id,),
    )

    logger.info(f"Deleted entry {ety.id}.")


def update(ety: T, position: int, conn: Connection) -> T:
    """
    Update the index of an entry in a playlist. Shift all other entries accordingly.

    :param ety: The playlist entry to update.
    :param position: The intended new index of the entry.
    :param conn: A connection to the database.
    :return: The updated entry.
    :raises IndexError: If the entry is out of bounds.
    """
    max_ = _highest_position(ety.playlist_id, conn)

    if position < 1 or position > max_:
        raise IndexError(f"Position {position} out of bounds.")

    # Nothing to do here...
    if position == ety.position:
        return ety

    # I believe Python surrounds these with an implicit transaction.
    if position > ety.position:
        conn.execute(
            """
            UPDATE music__playlists_tracks
            SET position = position - 1
            WHERE playlist_id = ? AND position > ? AND position <= ?
            """,
            (ety.playlist_id, ety.position, position),
        )
        conn.execute(
            """
            UPDATE music__playlists_tracks SET position = ? WHERE id = ?
            """,
            (position, ety.id),
        )
    else:
        conn.execute(
            """
            UPDATE music__playlists_tracks
            SET position = position + 1
            WHERE playlist_id = ? AND position < ? AND position >= ?
            """,
            (ety.playlist_id, ety.position, position),
        )
        conn.execute(
            """
            UPDATE music__playlists_tracks SET position = ? WHERE id = ?
            """,
            (position, ety.id),
        )

    conn.execute(
        """
        UPDATE music__playlists
        SET last_updated_on = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (ety.playlist_id,),
    )

    logger.info(f"Updated position of entry {id} to {position}.")
    return update_dataclass(ety, position=position)


def playlist(ety: T, conn: Connection) -> libplaylist.T:
    """
    Fetch the playlist that this entry is in.

    :param ety: The playlist entity.
    :param conn: A connection to the database.
    :return: The playlist the entry is in.
    """
    ply = libplaylist.from_id(ety.playlist_id, conn)
    assert ply is not None
    return ply


def track(ety: T, conn: Connection) -> libtrack.T:
    """
    Fetch the track that this entry represents.

    :param ety: The playlist entity.
    :param conn: A connection to the database.
    :return: The track the entry represents.
    """
    trk = libtrack.from_id(ety.track_id, conn)
    assert trk is not None
    return trk


def _highest_position(playlist_id: int, conn: Connection) -> int:
    """
    Return the highest position number for a track in a playlist. If there are no
    entries in the playlist, this returns 0.

    :param playlist_id: The playlist ID.
    :param conn: A connection to the database.
    :return: The next unused position number in a playlist.
    """
    cursor = conn.execute(
        """
        SELECT MAX(position) FROM music__playlists_tracks WHERE playlist_id = ?
        """,
        (playlist_id,),
    )

    return cursor.fetchone()[0] or 0
