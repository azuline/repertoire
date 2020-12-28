from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from sqlite3 import Cursor, Row
from typing import Dict, List, Optional, Union

from src.enums import CollectionType, PlaylistType
from src.errors import (
    AlreadyExists,
    DoesNotExist,
    Duplicate,
    Immutable,
    InvalidPlaylistType,
    NotFound,
)
from src.util import update_dataclass, without_key

from . import collection
from . import image as libimage
from . import track

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
        return from_row(row)

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
        return from_row(row)

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


def tracks(ply: T, cursor: Cursor) -> List[track.T]:
    """
    Get the tracks in a playlist.

    :param ply: The playlist whose tracks we want to get.
    :param cursor: A cursor to the database.
    :return: A list of tracks in the playlist.
    """
    cursor.execute(
        """
        SELECT
            trks.*
        FROM music__playlists AS plys
            JOIN music__playlists_tracks AS plystrks ON plystrks.playlist_id = plys.id
            JOIN music__tracks AS trks ON trks.id = plystrks.track_id
        WHERE plys.id = ?
        GROUP BY trks.id
        """,
        (ply.id,),
    )

    return [track.from_row(row) for row in cursor.fetchall()]


def add_track(ply: T, track_id: int, cursor: Cursor) -> T:
    """
    Add the provided track to the provided playlist.

    :param ply: The playlist to add the track to.
    :param track_id: The ID of the track to add.
    :param cursor: A cursor to the database.
    :return: The playlist with the number of tracks (if present) updated.
    :raises NotFound: If no track has the given track ID.
    :raises AlreadyExists: If the track is already in the playlist.
    """
    if not track.exists(track_id, cursor):
        raise NotFound(f"Releasse {track_id} does not exist.")

    cursor.execute(
        """
        SELECT 1 FROM music__playlists_tracks
        WHERE playlist_id = ? AND track_id = ?
        """,
        (ply.id, track_id),
    )
    # TODO: Once we add playlist-specific ordering, allow duplicate tracks.
    if cursor.fetchone():
        raise AlreadyExists("Track is already in playlist.")

    cursor.execute(
        """
        INSERT INTO music__playlists_tracks (playlist_id, track_id)
        VALUES (?, ?)
        """,
        (ply.id, track_id),
    )

    return update_dataclass(
        ply,
        num_tracks=(
            ply.num_tracks + 1 if ply.num_tracks is not None else ply.num_tracks
        ),
    )


def del_track(ply: T, track_id: int, cursor: Cursor) -> T:
    """
    Remove the provided track from the provided playlist.

    :param ply: The playlist to remove the track from.
    :param trk: The track to remove.
    :param cursor: A cursor to the database.
    :return: The playlist with the number of tracks (if present) updated.
    :raises NotFound: If no track has the given track ID.
    :raises DoesNotExist: If the track is not in the playlist.
    """
    # TODO: Once we add playlist-specific ordering, perhaps worth switching over to
    # track placement in playlist over track ID, since duplicates may exist.
    if not track.exists(track_id, cursor):
        raise NotFound(f"Track {track_id} does not exist.")

    cursor.execute(
        """
        SELECT 1 FROM music__playlists_tracks
        WHERE playlist_id = ? AND track_id = ?
        """,
        (ply.id, track_id),
    )
    if not cursor.fetchone():
        raise DoesNotExist("Track is not in playlist.")

    cursor.execute(
        """
        DELETE FROM music__playlists_tracks
        WHERE playlist_id = ? AND track_id = ?
        """,
        (ply.id, track_id),
    )

    return update_dataclass(
        ply,
        num_tracks=(
            ply.num_tracks - 1 if ply.num_tracks is not None else ply.num_tracks
        ),
    )


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
        ORDER BY num_matches DESC
        LIMIT ?
        """,
        (ply.id, CollectionType.GENRE.value, num_genres),
    )

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
            JOIN music__playlists_tracks AS trkplys ON trkplys.track_id = trk.id
        WHERE trkplys.playlist_id = ?
        ORDER BY RANDOM()
        LIMIT 1
        """,
        (ply.id,),
    )

    if row := cursor.fetchone():
        return libimage.from_row(row)

    return None
