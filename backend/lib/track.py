from dataclasses import dataclass
from pathlib import Path
from sqlite3 import Cursor, Row
from typing import List

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
    track_number: str
    #:
    disc_number: str
    #:
    duration: int
    #:
    artists: List[artist.T]


def from_row(row: Row, cursor: Cursor) -> T:
    cursor.execute(
        """
        SELECT
            arts.id,
            arts.name,
            trksarts.role
        FROM music__tracks_artists AS trksarts
        JOIN music__artists AS arts ON arts.id = trksarts.artist_id
        WHERE trksarts.track_id = ?
        """,
        (row["id"],),
    )

    return T(
        **row,
        filepath=Path(row["filepath"]),
        artists=[artist.from_row(row) for row in cursor.fetchall()],
    )
