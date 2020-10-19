from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from sqlite3 import Cursor, Row
from typing import Dict, List, Optional

from backend.enums import ArtistRole
from backend.errors import Duplicate
from backend.util import without_key

from . import artist, release


@dataclass
class T:
    """
    A track dataclass. This dataclass is frozen (immutable).
    """

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    filepath: Path
    #: A hash of the audio file.
    sha256: bytes
    #:
    title: str
    #:
    release_id: int
    #:
    duration: int
    #: The mapping ``{"artist": artist.T, "role": ArtistRole}``.
    artists: Dict
    #:
    track_number: str
    #:
    disc_number: Optional[str] = None


def from_row(row: Row, cursor: Cursor) -> T:
    cursor.execute(
        """
        SELECT
            arts.*,
            trksarts.role
        FROM music__tracks_artists AS trksarts
        JOIN music__artists AS arts ON arts.id = trksarts.artist_id
        WHERE trksarts.track_id = ?
        """,
        (row["id"],),
    )

    artists = [
        {
            "artist": artist.from_row(without_key(row, "role")),
            "role": ArtistRole(row["role"]),
        }
        for row in cursor.fetchall()
    ]

    return T(**dict(row, filepath=Path(row["filepath"]), artists=artists))


def from_id(id: int, cursor: Cursor) -> Optional[T]:
    """
    Return the track with the provided ID.

    :param id: The ID of the track to fetch.
    :param cursor: A cursor to the database.
    :return: The track with the provided ID, if it exists.
    """
    cursor.execute("SELECT * FROM music__tracks WHERE id = ?", (id,))

    if row := cursor.fetchone():
        return from_row(row, cursor)


def from_filepath(filepath: str, cursor: Cursor) -> Optional[T]:
    """
    Return the track with the provided filepath.

    :param filepath: The filepath of the track to fetch.
    :param cursor: A cursor to the database.
    :return: The track with the provided filepath, if it exists.
    """
    cursor.execute("SELECT * FROM music__tracks WHERE filepath = ?", (filepath,))

    if row := cursor.fetchone():
        return from_row(row, cursor)


def from_sha256(sha256: bytes, cursor: Cursor) -> Optional[T]:
    """
    Return the track with the provided sha256 hash.

    :param sha256: The sha256 hash of the track to fetch.
    :param cursor: A cursor to the database.
    :return: The track with the provided sha256 hash, if it exists.
    """
    cursor.execute("SELECT * FROM music__tracks WHERE sha256 = ?", (sha256,))

    if row := cursor.fetchone():
        return from_row(row, cursor)


def create(
    title: str,
    filepath: Path,
    sha256: bytes,
    release: release.T,
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
    :param sha256: The sha256 of the track file.
    :param release: The release that this track belongs to.
    :param artists: The artists that contributed to this track. A list of
                    ``{"artist": artist.T, "role": ArtistRole}`` mappings.
    :param duration: The duration of this track, in seconds.
    :param track_number: The track number.
    :param disc_number: The disc number.
    :return: The newly created track.
    :raises Duplicate: If a track with the same filepath already exists.
    """
    # First, check to see if a track with the same filepath exists.
    cursor.execute("SELECT 1 FROM music__tracks WHERE filepath = ?", (str(filepath),))
    if cursor.fetchone():
        raise Duplicate

    # Next, check to see if a track with the same sha256 exists.
    cursor.execute("SELECT id FROM music__tracks WHERE sha256 = ?", (sha256,))
    if row := cursor.fetchone():
        # If a track with the same sha256 exists, update the filepath and return.
        cursor.execute(
            """UPDATE music__tracks SET filepath = ? WHERE id = ?""",
            (filepath, row["id"]),
        )
        cursor.connection.commit()
        return

    # Track is not a duplicate, so we can insert and return.
    cursor.execute(
        """
        INSERT INTO music__tracks (
            title, filepath, sha256, release_id, track_number, disc_number, duration
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (title, str(filepath), sha256, release.id, track_number, disc_number, duration),
    )
    cursor.connection.commit()
    id = cursor.lastrowid

    # Insert artists.
    for mapping in artists:
        cursor.execute(
            """
            INSERT INTO music__tracks_artists (track_id, artist_id, role)
            VALUES (?, ?, ?)
            """,
            (id, mapping["artist"].id, mapping["role"].value),
        )
    cursor.connection.commit()

    return T(
        id=id,
        title=title,
        filepath=filepath,
        sha256=sha256,
        release=release,
        artists=artists,
        duration=duration,
        track_number=track_number,
        disc_number=disc_number,
    )
