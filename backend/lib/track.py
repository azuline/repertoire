from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from sqlite3 import Cursor, Row
from typing import Any, Dict, List, Optional, Union

from backend.enums import ArtistRole
from backend.errors import AlreadyExists, DoesNotExist, Duplicate
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
    #:
    track_number: str
    #:
    disc_number: Optional[str] = None


def from_row(row: Row) -> T:
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


def from_sha256(sha256: bytes, cursor: Cursor) -> Optional[T]:
    """
    Return the track with the provided sha256 hash.

    :param sha256: The sha256 hash of the track to fetch.
    :param cursor: A cursor to the database.
    :return: The track with the provided sha256 hash, if it exists.
    """
    cursor.execute("SELECT * FROM music__tracks WHERE sha256 = ?", (sha256,))

    if row := cursor.fetchone():
        return from_row(row)


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
    :raises Duplicate: If a track with the same filepath already exists. The duplicate
                       track is passed as the ``entity`` argument.
    """
    # First, check to see if a track with the same filepath exists.
    if trk := from_filepath(filepath, cursor):
        raise Duplicate(trk)

    # Next, check to see if a track with the same sha256 exists.
    cursor.execute("SELECT id FROM music__tracks WHERE sha256 = ?", (sha256,))
    if row := cursor.fetchone():
        # If a track with the same sha256 exists, update the filepath and return.
        cursor.execute(
            """UPDATE music__tracks SET filepath = ? WHERE id = ?""",
            (str(filepath), row["id"]),
        )
        cursor.connection.commit()
        return from_id(row["id"], cursor)

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

    return from_id(id, cursor)


def update(trk: T, cursor: Cursor, **changes: Dict[str, Any]) -> T:
    """
    Update a track and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    :param trk: The track to update.
    :param cursor: A cursor to the database.
    :param title: New track title.
    :type  title: :py:obj:`str`
    :param release: New release.
    :type  release: :py:obj:`backend.lib.release.T`
    :param track_number: New track number.
    :type  track_number: :py:obj:`str`
    :param disc_number: New disc number.
    :type  disc_number: :py:obj:`str`
    :return: The updated track.
    """
    # Adjust the exposed `release` to the internally used `release_id`.
    if "release" in changes:
        changes["release_id"] = changes["release"].id
        del changes["release"]

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
    cursor.connection.commit()

    return T(**dict(asdict(trk), **changes))


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


def add_artist(trk: T, art: artist.T, role: ArtistRole, cursor: Cursor) -> None:
    """
    Add the provided artist/role combo to the provided track.

    :param trk: The track to add the artist to.
    :param art: The artist to add.
    :param role: The role to add the artist with.
    :param cursor: A cursor to the database.
    :raises AlreadyExists: If the artist/role combo is already on the track.
    """
    cursor.execute(
        """
        SELECT 1 FROM music__tracks_artists
        WHERE track_id = ? AND artist_id = ? AND role = ?
        """,
        (trk.id, art.id, role.value),
    )
    if cursor.fetchone():
        raise AlreadyExists

    cursor.execute(
        """
        INSERT INTO music__tracks_artists (track_id, artist_id, role)
        VALUES (?, ?, ?)
        """,
        (trk.id, art.id, role.value),
    )
    cursor.connection.commit()


def del_artist(trk: T, art: artist.T, role: ArtistRole, cursor: Cursor) -> None:
    """
    Delete the provided artist/role combo to the provided track.

    :param trk: The track to delete the artist from.
    :param art: The artist to delete.
    :param cursor: A cursor to the database.
    :raises DoesNotExist: If the artist is not on the track.
    """
    cursor.execute(
        """
        SELECT 1 FROM music__tracks_artists
        WHERE track_id = ? AND artist_id = ? AND role = ?
        """,
        (trk.id, art.id, role.value),
    )
    if not cursor.fetchone():
        raise DoesNotExist

    cursor.execute(
        """
        DELETE FROM music__tracks_artists
        WHERE track_id = ? AND artist_id = ? AND role = ?
        """,
        (trk.id, art.id, role.value),
    )
    cursor.connection.commit()
