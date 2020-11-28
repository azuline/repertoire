from __future__ import annotations

import logging
from dataclasses import dataclass
from os.path import isfile
from pathlib import Path
from sqlite3 import Cursor, Row
from typing import Dict, List, Optional, Union

from src.enums import ArtistRole
from src.errors import AlreadyExists, DoesNotExist, Duplicate, NotFound
from src.util import update_dataclass, without_key, calculate_sha_256_full

from . import artist, release

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class T:
    """A track dataclass."""

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    filepath: Path
    #: A hash of the beggining of the audio file.
    initial_sha256: bytes
    #: A hash of the audio file.
    full_sha256: Optional[bytes] = None
    #:
    title: str
    #:
    release_id: int
    #:
    duration: int
    #:
    track_number: str
    #:
    disc_number: Optional[str] = None


def exists(id: int, cursor: Cursor) -> bool:
    """
    Return whether a track exists with the given ID.

    :param id: The ID to check.
    :return: Whether a track has the given ID.
    """
    cursor.execute("SELECT 1 FROM music__tracks WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Union[Dict, Row]) -> T:
    """
    Return a track dataclass containing data from a row in the database.

    :param row: A row from the database.
    :return: A track dataclass.
    """
    return T(**dict(row, filepath=Path(row["filepath"])))


def from_id(id: int, cursor: Cursor) -> Optional[T]:
    """
    Return the track with the provided ID.

    :param id: The ID of the track to fetch.
    :param cursor: A cursor to the database.
    :return: The track with the provided ID, if it exists.
    """
    cursor.execute("SELECT * FROM music__tracks WHERE id = ?", (id,))

    if row := cursor.fetchone():
        return from_row(row)

    return None


def from_filepath(filepath: Union[Path, str], cursor: Cursor) -> Optional[T]:
    """
    Return the track with the provided filepath.

    :param filepath: The filepath of the track to fetch.
    :param cursor: A cursor to the database.
    :return: The track with the provided filepath, if it exists.
    """
    cursor.execute("SELECT * FROM music__tracks WHERE filepath = ?", (str(filepath),))

    if row := cursor.fetchone():
        return from_row(row)

    return None


def from_full_sha256(full_sha256: bytes, cursor: Cursor) -> Optional[T]:
    """
    Return the track with the provided sha256 hash.

    :param full_sha256: The sha256 hash of the track to fetch.
    :param cursor: A cursor to the database.
    :return: The track with the provided sha256 hash, if it exists.
    """
    cursor.execute("SELECT * FROM music__tracks WHERE full_sha256 = ?", (full_sha256,))

    if row := cursor.fetchone():
        return from_row(row)

    return None


def from_initial_sha256(initial_sha256: bytes, cursor: Cursor) -> Optional[T]:
    """
    Return the track with the provided sha256 hash.

    :param initial_sha256: The sha256 hash of the track to fetch.
    :param cursor: A cursor to the database.
    :return: The track with the provided sha256 hash, if it exists.
    """
    cursor.execute("SELECT * FROM music__tracks WHERE initial_sha256 = ?", (initial_sha256,))

    if row := cursor.fetchone():
        return from_row(row)

    return None


def create(
    title: str,
    filepath: Path,
    initial_sha256: bytes,
    release_id: int,
    artists: List[Dict],
    duration: int,
    track_number: str,
    disc_number: str,
    cursor: Cursor,
) -> T:
    """
    Create a track with the provided parameters.

    If a track already exists with the same SHA256, the filepath of that track will be
    set to the passed-in filepath and nothing else will be done.

    :param title: The title of the track.
    :param filepath: The filepath of the track.
    :param initial_sha256: The sha256 of the beginning of the track file.
    :param release_id: The ID of the release that this track belongs to.
    :param artists: The artists that contributed to this track. A list of
                    ``{"artist_id": int, "role": ArtistRole}`` mappings.
    :param duration: The duration of this track, in seconds.
    :param track_number: The track number.
    :param disc_number: The disc number.
    :return: The newly created track.
    :raises NotFound: If no release has the given release ID or no artist
                      corresponds with any of the given artist IDs.
    :raises Duplicate: If a track with the same filepath already exists. The duplicate
                       track is passed as the ``entity`` argument.
    """
    if not release.exists(release_id, cursor):
        raise NotFound(f"Release {release_id} does not exist.")

    if bad_ids := [
        d["artist_id"] for d in artists if not artist.exists(d["artist_id"], cursor)
    ]:
        raise NotFound(f"Artist(s) {', '.join(str(i) for i in bad_ids)} do not exist.")

    if trk := _duplicate_track_handle(initial_sha256, filepath, cursor):
        return trk

    # Track is not a duplicate, so we can insert and return.
    cursor.execute(
        """
        INSERT INTO music__tracks (
            title, filepath, initial_sha256, release_id, track_number, disc_number, duration
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (title, str(filepath), initial_sha256, release_id, track_number, disc_number, duration),
    )

    trk = T(
        id=cursor.lastrowid,
        title=title,
        filepath=filepath,
        initial_sha256=initial_sha256,
        release_id=release_id,
        duration=duration,
        track_number=track_number,
        disc_number=disc_number,
    )

    # Insert artists.
    for mapping in artists:
        trk = add_artist(trk, mapping["artist_id"], mapping["role"], cursor)

    logger.info(f'Created track "{filepath}" with ID {trk.id}.')

    return trk


def _duplicate_track_handle(
    initial_sha256: bytes,
    filepath: Path,
    cursor: Cursor
) -> Optional[T]:
    """
    Handles tracking duplicate tracks so that we don't repeat hashing them.
    Returns the original track as it was in the database

    :param initial_sha256: A sha256 of the first 16KB of the file.
    :param filepath: The filepath of the track to check.
    :param cursor: A cursor to the database.
    :return: a reference to the duplicated track or None
    """
    # First, check to see if a track with the same filepath exists.
    if trk := from_filepath(filepath, cursor):
        raise Duplicate("A track with this filepath already exists.", trk)

    # Then check if this duplicate has been found before.
    if trk := _dupe_history_check(initial_sha256, filepath, cursor):
        return trk

    # Now check to see if a track with the same sha256 exists.
    cursor.execute(
        """
        SELECT id, filepath, full_sha256
          FROM music__tracks
         WHERE initial_sha256 = ?
        """,
        (initial_sha256,),
    )
    if row := cursor.fetchone():
        existing_full_sha256 = row["full_sha256"]
        if existing_full_sha256 is None:
            try:
                existing_full_sha256 = calculate_sha_256_full(Path(row["filepath"]))
                cursor.execute(
                    """
                    UPDATE music__tracks
                    SET full_sha256 = ?
                    WHERE id = ?
                    """,
                    (
                        existing_full_sha256,
                        row["id"],
                    ),
                )
            except FileNotFoundError:
                # Need to handle deleting the original track since
                # We can't verify that the track is indeed a duplicate
                return None
        new_full_sha256 = calculate_sha_256_full(Path(filepath))
        if new_full_sha256 != existing_full_sha256:
            return None
        # Since the sha256's match let's check if file still exists
        if isfile(row["filepath"]):
            cursor.execute(
                """
                INSERT INTO music__dupe_tracks (
                    dupe_track_id, filepath, initial_sha256
                ) VALUES (?, ?, ?)
                """,
                (row["id"], str(filepath), initial_sha256),
            )
        else:
            cursor.execute(
                "UPDATE music__tracks SET filepath = ? WHERE id = ?",
                (str(filepath), row["id"]),
            )
        logger.info(f'Duplicate track at "{filepath}" for track ID {row["id"]}.')
        return from_id(row["id"], cursor)

    return None


def _dupe_history_check(
    initial_sha256: bytes,
    filepath: str,
    cursor: Cursor
) -> Optional[T]:
    """
    Return a track if we have found this duplicate before. Else we return None

    :param initial_sha256: A sha256 of the first 16KB of the file.
    :param filepath: The filepath of the track to fetch.
    :return: boolean as to whether the track has been previously found.
    """
    cursor.execute(
        """SELECT dupe_track_id
             FROM music__dupe_tracks
            WHERE initial_sha256 = ?
              AND filepath = ?
        """,
        (
            initial_sha256,
            str(filepath),
        ),
    )

    if row := cursor.fetchone():
        return from_id(row["dupe_track_id"], cursor)

    return None


def update(trk: T, cursor: Cursor, **changes) -> T:
    """
    Update a track and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    :param trk: The track to update.
    :param cursor: A cursor to the database.
    :param title: New track title.
    :type  title: :py:obj:`str`
    :param release_id: ID of the new release.
    :type  release_id: :py:obj:`int`
    :param track_number: New track number.
    :type  track_number: :py:obj:`str`
    :param disc_number: New disc number.
    :type  disc_number: :py:obj:`str`
    :return: The updated track.
    :raise NotFound: If the new release ID does not exist.
    """
    if "release_id" in changes and not release.exists(changes["release_id"], cursor):
        raise NotFound(f"Release {changes['release_id']} does not exist.")

    cursor.execute(
        """
        UPDATE music__tracks
        SET title = ?,
            release_id = ?,
            track_number = ?,
            disc_number = ?
        WHERE id = ?
        """,
        (
            changes.get("title", trk.title),
            changes.get("release_id", trk.release_id),
            changes.get("track_number", trk.track_number),
            changes.get("disc_number", trk.disc_number),
            trk.id,
        ),
    )

    logger.info(f"Updated track {trk.id} with {changes}.")

    return update_dataclass(trk, **changes)


def artists(trk: T, cursor: Cursor) -> List[Dict]:
    """
    Get the artists that contributed to a track and their roles.

    :param trk: The track whose artists to fetch.
    :param cursor: A cursor to the database.
    :return: A list of ``{"artist": artist.T, "role": ArtistRole}`` dicts.
    """
    cursor.execute(
        """
        SELECT
            arts.*,
            COUNT(artsrls.release_id) AS num_releases,
            trksarts.role
        FROM music__tracks_artists AS trksarts
        JOIN music__artists AS arts ON arts.id = trksarts.artist_id
        LEFT JOIN music__releases_artists AS artsrls
            ON artsrls.artist_id = arts.id
        WHERE trksarts.track_id = ?
        GROUP BY arts.id, trksarts.role
        """,
        (trk.id,),
    )

    return [
        {
            "artist": artist.from_row(without_key(row, "role")),
            "role": ArtistRole(row["role"]),
        }
        for row in cursor.fetchall()
    ]


def add_artist(trk: T, artist_id: int, role: ArtistRole, cursor: Cursor) -> T:
    """
    Add the provided artist/role combo to the provided track.

    :param trk: The track to add the artist to.
    :param artist_id: The ID of the artist to add.
    :param role: The role to add the artist with.
    :param cursor: A cursor to the database.
    :return: The track that was passed in.
    :raises NotFound: If no artist has the given artist ID.
    :raises AlreadyExists: If the artist/role combo is already on the track.
    """
    if not artist.exists(artist_id, cursor):
        raise NotFound(f"Artist {artist_id} does not exist.")

    cursor.execute(
        """
        SELECT 1 FROM music__tracks_artists
        WHERE track_id = ? AND artist_id = ? AND role = ?
        """,
        (trk.id, artist_id, role.value),
    )
    if cursor.fetchone():
        raise AlreadyExists("Artist already on track with this role.")

    cursor.execute(
        """
        INSERT INTO music__tracks_artists (track_id, artist_id, role)
        VALUES (?, ?, ?)
        """,
        (trk.id, artist_id, role.value),
    )

    return trk


def del_artist(trk: T, artist_id: int, role: ArtistRole, cursor: Cursor) -> T:
    """
    Delete the provided artist/role combo to the provided track.

    :param trk: The track to delete the artist from.
    :param artist_id: The ID of the artist to delete.
    :param cursor: A cursor to the database.
    :return: The track that was passed in.
    :raises NotFound: If no artist has the given artist ID.
    :raises DoesNotExist: If the artist is not on the track.
    """
    if not artist.exists(artist_id, cursor):
        raise NotFound(f"Artist {artist_id} does not exist.")

    cursor.execute(
        """
        SELECT 1 FROM music__tracks_artists
        WHERE track_id = ? AND artist_id = ? AND role = ?
        """,
        (trk.id, artist_id, role.value),
    )
    if not cursor.fetchone():
        raise DoesNotExist("No artist on track with this role.")

    cursor.execute(
        """
        DELETE FROM music__tracks_artists
        WHERE track_id = ? AND artist_id = ? AND role = ?
        """,
        (trk.id, artist_id, role.value),
    )

    return trk
