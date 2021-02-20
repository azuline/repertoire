from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from sqlite3 import Connection, Row
from typing import Dict, List, Optional, Union

from src.enums import ArtistRole
from src.errors import AlreadyExists, DoesNotExist, Duplicate, NotFound
from src.util import update_dataclass, without_key

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


def exists(id: int, conn: Connection) -> bool:
    """
    Return whether a track exists with the given ID.

    :param id: The ID to check.
    :return: Whether a track has the given ID.
    """
    cursor = conn.execute("SELECT 1 FROM music__tracks WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Union[Dict, Row]) -> T:
    """
    Return a track dataclass containing data from a row in the database.

    :param row: A row from the database.
    :return: A track dataclass.
    """
    return T(**dict(row, filepath=Path(row["filepath"])))


def from_id(id: int, conn: Connection) -> Optional[T]:
    """
    Return the track with the provided ID.

    :param id: The ID of the track to fetch.
    :param conn: A connection to the database.
    :return: The track with the provided ID, if it exists.
    """
    cursor = conn.execute("SELECT * FROM music__tracks WHERE id = ?", (id,))

    if row := cursor.fetchone():
        logger.debug("Fetched track {id}.")
        return from_row(row)

    logger.debug("Failed to fetch track {id}.")
    return None


def from_filepath(filepath: Union[Path, str], conn: Connection) -> Optional[T]:
    """
    Return the track with the provided filepath.

    :param filepath: The filepath of the track to fetch.
    :param conn: A connection to the database.
    :return: The track with the provided filepath, if it exists.
    """
    cursor = conn.execute(
        "SELECT * FROM music__tracks WHERE filepath = ?",
        (str(filepath),),
    )

    if row := cursor.fetchone():
        logger.debug("Fetched track {row['id']} from filepath {filepath}.")
        return from_row(row)

    logger.debug("Failed to fetch track from filepath {filepath}.")
    return None


def from_sha256(sha256: bytes, conn: Connection) -> Optional[T]:
    """
    Return the track with the provided sha256 hash.

    :param sha256: The sha256 hash of the track to fetch.
    :param conn: A connection to the database.
    :return: The track with the provided sha256 hash, if it exists.
    """
    cursor = conn.execute("SELECT * FROM music__tracks WHERE sha256 = ?", (sha256,))

    if row := cursor.fetchone():
        logger.debug("Fetched track {row['id']} from SHA256 {sha256.hex()}.")
        return from_row(row)

    logger.debug("Failed to fetch track from SHA256 {sha256.hex()}.")
    return None


def create(
    title: str,
    filepath: Path,
    sha256: bytes,
    release_id: int,
    artists: List[Dict],
    duration: int,
    track_number: str,
    disc_number: str,
    conn: Connection,
) -> T:
    """
    Create a track with the provided parameters.

    If a track already exists with the same SHA256, the filepath of that track will be
    set to the passed-in filepath and nothing else will be done.

    :param title: The title of the track.
    :param filepath: The filepath of the track.
    :param sha256: The sha256 of the track file.
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
    if not release.exists(release_id, conn):
        logger.debug(f"Release {release_id} does not exist.")
        raise NotFound(f"Release {release_id} does not exist.")

    if bad_ids := [
        d["artist_id"] for d in artists if not artist.exists(d["artist_id"], conn)
    ]:
        logger.debug(f"Artist(s) {', '.join(str(i) for i in bad_ids)} do not exist.")
        raise NotFound(f"Artist(s) {', '.join(str(i) for i in bad_ids)} do not exist.")

    # First, check to see if a track with the same filepath exists.
    if trk := from_filepath(filepath, conn):
        logger.debug("A track with this filepath already exists.")
        raise Duplicate("A track with this filepath already exists.", trk)

    # Next, check to see if a track with the same sha256 exists.
    cursor = conn.execute("SELECT id FROM music__tracks WHERE sha256 = ?", (sha256,))
    if row := cursor.fetchone():
        # If a track with the same sha256 exists, update the filepath and return.
        conn.execute(
            "UPDATE music__tracks SET filepath = ? WHERE id = ?",
            (str(filepath), row["id"]),
        )
        logger.debug("Found track with the same SHA256; updated filepath.")
        return from_id(row["id"], conn)  # type: ignore

    # Track is not a duplicate, so we can insert and return.
    cursor.execute(
        """
        INSERT INTO music__tracks (
            title, filepath, sha256, release_id, track_number, disc_number, duration
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (title, str(filepath), sha256, release_id, track_number, disc_number, duration),
    )

    trk = T(
        id=cursor.lastrowid,
        title=title,
        filepath=filepath,
        sha256=sha256,
        release_id=release_id,
        duration=duration,
        track_number=track_number,
        disc_number=disc_number,
    )

    # Insert artists.
    for mapping in artists:
        trk = add_artist(trk, mapping["artist_id"], mapping["role"], conn)

    logger.info(f'Created track "{filepath}" with ID {trk.id}.')

    return trk


def update(trk: T, conn: Connection, **changes) -> T:
    """
    Update a track and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    :param trk: The track to update.
    :param conn: A connection to the database.
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
    if "release_id" in changes and not release.exists(changes["release_id"], conn):
        logger.debug(f"Release {changes['release_id']} does not exist.")
        raise NotFound(f"Release {changes['release_id']} does not exist.")

    conn.execute(
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


def artists(trk: T, conn: Connection) -> List[Dict]:
    """
    Get the artists that contributed to a track and their roles.

    :param trk: The track whose artists to fetch.
    :param conn: A connection to the database.
    :return: A list of ``{"artist": artist.T, "role": ArtistRole}`` dicts.
    """
    cursor = conn.execute(
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

    logger.debug(f"Fetched artists of track {trk.id}.")

    return [
        {
            "artist": artist.from_row(without_key(row, "role")),
            "role": ArtistRole(row["role"]),
        }
        for row in cursor.fetchall()
    ]


def add_artist(trk: T, artist_id: int, role: ArtistRole, conn: Connection) -> T:
    """
    Add the provided artist/role combo to the provided track.

    :param trk: The track to add the artist to.
    :param artist_id: The ID of the artist to add.
    :param role: The role to add the artist with.
    :param conn: A connection to the database.
    :return: The track that was passed in.
    :raises NotFound: If no artist has the given artist ID.
    :raises AlreadyExists: If the artist/role combo is already on the track.
    """
    if not artist.exists(artist_id, conn):
        logger.debug(f"Artist {artist_id} does not exist.")
        raise NotFound(f"Artist {artist_id} does not exist.")

    cursor = conn.execute(
        """
        SELECT 1 FROM music__tracks_artists
        WHERE track_id = ? AND artist_id = ? AND role = ?
        """,
        (trk.id, artist_id, role.value),
    )
    if cursor.fetchone():
        logger.debug(
            f"Artist {artist_id} is already on track {trk.id} with role {role}."
        )
        raise AlreadyExists("Artist already on track with this role.")

    conn.execute(
        """
        INSERT INTO music__tracks_artists (track_id, artist_id, role)
        VALUES (?, ?, ?)
        """,
        (trk.id, artist_id, role.value),
    )

    logger.info(f"Added artist {artist_id} to track {trk.id} with role {role}.")

    return trk


def del_artist(trk: T, artist_id: int, role: ArtistRole, conn: Connection) -> T:
    """
    Delete the provided artist/role combo to the provided track.

    :param trk: The track to delete the artist from.
    :param artist_id: The ID of the artist to delete.
    :param conn: A connection to the database.
    :return: The track that was passed in.
    :raises NotFound: If no artist has the given artist ID.
    :raises DoesNotExist: If the artist is not on the track.
    """
    if not artist.exists(artist_id, conn):
        logger.debug(f"Artist {artist_id} does not exist.")
        raise NotFound(f"Artist {artist_id} does not exist.")

    cursor = conn.execute(
        """
        SELECT 1 FROM music__tracks_artists
        WHERE track_id = ? AND artist_id = ? AND role = ?
        """,
        (trk.id, artist_id, role.value),
    )
    if not cursor.fetchone():
        logger.debug(f"Artist {artist_id} is not on track {trk.id} with role {role}.")
        raise DoesNotExist("No artist on track with this role.")

    conn.execute(
        """
        DELETE FROM music__tracks_artists
        WHERE track_id = ? AND artist_id = ? AND role = ?
        """,
        (trk.id, artist_id, role.value),
    )

    logger.info(f"Deleted artist {artist_id} from track {trk.id} with role {role}.")

    return trk
