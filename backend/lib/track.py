from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from sqlite3 import Cursor, Row
from typing import List, Optional

from backend.enums import ArtistRole
from backend.util import without_key

from . import artist


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
    #:
    artists: List[artist.T]
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


def from_id(id_: int, cursor: Cursor) -> Optional[T]:
    """
    Return the track with the provided ID.

    :param id_: The ID of the track to fetch.
    :param cursor: A cursor to the database.
    :return: The track with the provided ID, if it exists.
    """
    cursor.execute("""SELECT * FROM music__tracks WHERE id = ?""", (id_,))

    row = cursor.fetchone()
    return from_row(row, cursor) if row else None
