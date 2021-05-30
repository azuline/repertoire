from __future__ import annotations

import logging
from dataclasses import dataclass
from itertools import repeat
from pathlib import Path
from sqlite3 import Connection, Row
from typing import Iterable, Optional, Union

from src.enums import ArtistRole, TrackSort
from src.errors import AlreadyExists, DoesNotExist, Duplicate, NotFound
from src.util import (
    calculate_sha_256,
    make_fts_match_query,
    update_dataclass,
    without_key,
)

from . import artist, playlist, playlist_entry
from . import release as librelease

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
    sha256: Optional[bytes]
    #: A hash of the first 1KB of the file.
    sha256_initial: bytes
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


def from_row(row: Union[dict, Row]) -> T:
    """
    Return a track dataclass containing data from a row in the database.

    :param row: A row from the database.
    :return: A track dataclass.
    """
    return T(**dict(row, filepath=Path(row["filepath"])))


def from_id(id_: int, conn: Connection) -> Optional[T]:
    """
    Return the track with the provided ID.

    :param id: The ID of the track to fetch.
    :param conn: A connection to the database.
    :return: The track with the provided ID, if it exists.
    """
    cursor = conn.execute("SELECT * FROM music__tracks WHERE id = ?", (id_,))

    if row := cursor.fetchone():
        logger.debug(f"Fetched track {id_}.")
        return from_row(row)

    logger.debug(f"Failed to fetch track {id_}.")
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
        logger.debug(f"Fetched track {row['id']} from filepath {filepath}.")
        return from_row(row)

    logger.debug(f"Failed to fetch track from filepath {filepath}.")
    return None


def from_sha256_initial(sha256_initial: bytes, conn: Connection) -> Optional[T]:
    """
    Return the track with the provided sha256_initial (hash of the first 1KB) hash.

    :param sha256_initial: The sha256_initial of the track to fetch.
    :param conn: A connection to the database.
    :return: The track with the provided ID, if it exists.
    """
    cursor = conn.execute(
        "SELECT * FROM music__tracks WHERE sha256_initial = ?",
        (sha256_initial,),
    )

    if row := cursor.fetchone():
        logger.debug(
            f"Fetched track {row['id']} from initial SHA256 {sha256_initial.hex()}."
        )
        return from_row(row)

    logger.debug(f"Failed to fetch track from initial SHA256 {sha256_initial.hex()}.")
    return None


def from_sha256(sha256: bytes, conn: Connection) -> Optional[T]:
    """
    Return the track with the provided sha256 hash.

    WARNING: The sha256 attribute is populated lazily. It may not exist. Only use this
    function in a scenario where the sha256 value is guaranteed to exist.

    :param sha256: The sha256 hash of the track to fetch.
    :param conn: A connection to the database.
    :return: The track with the provided sha256 hash, if it exists.
    """
    cursor = conn.execute(
        "SELECT * FROM music__tracks WHERE sha256 = ?",
        (sha256,),
    )

    if row := cursor.fetchone():
        logger.debug(f"Fetched track {row['id']} from SHA256 {sha256.hex()}.")
        return from_row(row)

    logger.debug(f"Failed to fetch track from SHA256 {sha256.hex()}.")
    return None


def search(
    conn: Connection,
    *,
    search: str = "",
    playlist_ids: list[int] = [],
    artist_ids: list[int] = [],
    years: list[int] = [],
    page: int = 1,
    per_page: Optional[int] = None,
    sort: Optional[TrackSort] = None,
    asc: bool = True,
) -> list[T]:
    """
    Search for tracks matching the passed-in criteria. Parameters are optional;
    omitted ones are excluded from the matching criteria.

    :param search: A search string. We split this up into individual punctuation-less
                   tokens and return tracks whose titles and artists contain each
                   token.
    :param playlist_ids: A list of playlist IDs. We match tracks by the playlists in
                         this list. For a track to match, it must be in all playlists in
                         this list.
    :param artist_ids: A list of artist IDs. We match tracks by the artists in this
                       list. For a track to match, all artists in this list must be
                       included.
    :param years: A list of years. Filter out tracks that were not released in one of
                  the years in this list.
    :param page: Which page of tracks to return.
    :param per_page: The number of tracks per page. Pass ``None`` to return all releases
                     (this will ignore ``page``).
    :param sort: How to sort the matching releases. If not explicitly passed, this
                 defaults to ``SEARCH_RANK`` if ``search`` is not ``None`` and
                 ``RECENTLY_ADDED`` otherwise.
    :param asc: If true, sort in ascending order. If false, descending.
    :param conn: A connection to the database.
    :return: The matching tracks on the current page.
    """
    filters, params = _generate_filters(search, playlist_ids, artist_ids, years)

    # set the default sort if it's not specified
    if not sort:
        sort = TrackSort.SEARCH_RANK if search else TrackSort.RECENTLY_ADDED

    if per_page:
        params.extend([per_page, (page - 1) * per_page])

    cursor = conn.execute(
        f"""
        SELECT trks.*
        FROM music__tracks AS trks
        JOIN music__tracks__fts AS fts on fts.rowid = trks.id
        JOIN music__releases AS rls ON rls.id = trks.release_id
        {"WHERE " + " AND ".join(filters) if filters else ""}
        GROUP BY trks.id
        ORDER BY {sort.value.substitute(order="ASC" if asc else "DESC")}
        {"LIMIT ? OFFSET ?" if per_page else ""}
        """,
        params,
    )

    logger.debug(f"Searched tracks with {cursor.rowcount} paged results.")
    return [from_row(row) for row in cursor]


def count(
    conn: Connection,
    *,
    search: str = "",
    playlist_ids: list[int] = [],
    artist_ids: list[int] = [],
    years: list[int] = [],
) -> int:
    """
    Fetch the number of tracks matching the passed-in criteria. Parameters are
    optional; omitted ones are excluded from the matching criteria.

    :param search: A search string. We split this up into individual punctuation-less
                   tokens and return tracks whose titles and artists contain each
                   token.
    :param playlist_ids: A list of playlist IDs. We match tracks by the playlists in
                         this list. For a track to match, it must be in all playlists in
                         this list.
    :param artist_ids: A list of artist IDs. We match tracks by the artists in this
                       list. For a track to match, all artists in this list must be
                       included.
    :param years: A list of years. Filter out tracks that were not released in one of
                  the years in this list.
    :param conn: A connection to the database.
    :return: The number of matching releases.
    """
    filters, params = _generate_filters(search, playlist_ids, artist_ids, years)

    cursor = conn.execute(
        f"""
        SELECT COUNT(1)
        FROM music__tracks AS trks
        JOIN music__tracks__fts AS fts ON fts.rowid = trks.id
        JOIN music__releases AS rls ON rls.id = trks.release_id
        {"WHERE " + " AND ".join(filters) if filters else ""}
        """,
        params,
    )

    count = cursor.fetchone()[0]
    logger.debug(f"Counted {count} tracks that matched the filters.")
    return count


def _generate_filters(
    search: str,
    collection_ids: list[int],
    artist_ids: list[int],
    years: list[int],
) -> tuple[list[str], list[Union[str, int]]]:
    """
    Dynamically generate the SQL filters and parameters from the criteria. See the
    search and total functions for parameter descriptions.

    :return: A tuple of SQL filter strings and parameters. The SQL filter strings can be
    joined with `` AND `` and injected into the where clause.
    """
    filters: list[str] = []
    params: list[Union[str, int]] = []

    for sql, sql_args in [
        _generate_search_filter(search),
        _generate_collection_filter(collection_ids),
        _generate_artist_filter(artist_ids),
        _generate_year_filter(years),
    ]:
        filters.extend(sql)
        params.extend(sql_args)  # type: ignore

    return filters, params


def _generate_search_filter(search: str) -> tuple[Iterable[str], Iterable[str]]:
    """
    Generate the SQL and params for filtering on the search words.

    :param search: The search words to filter on.
    :return: The filter SQL and query parameters.
    """
    if not search:
        return [], []

    filter_sql = ["fts.music__tracks__fts MATCH ?"]
    filter_params = [make_fts_match_query(search)]

    return filter_sql, filter_params


def _generate_collection_filter(
    collection_ids: list[int],
) -> tuple[Iterable[str], Iterable[int]]:
    """
    Generate the SQL and params for filtering on collections.

    :param collection_ids: The collection IDs to filter on.
    :return: The filter SQL and query parameters.
    """
    sql = """
          EXISTS (
              SELECT 1 FROM music__playlists_tracks
              WHERE track_id = trks.id AND playlist_id = ?
          )
          """

    return repeat(sql, len(collection_ids)), collection_ids


def _generate_artist_filter(
    artist_ids: list[int],
) -> tuple[Iterable[str], Iterable[int]]:
    """
    Generate the SQL and params for filtering on artists.

    :param artist_ids: The artist IDs to filter on.
    :return: The filter SQL and query parameters.
    """
    sql = """
          EXISTS (
              SELECT 1 FROM music__tracks_artists
              WHERE track_id = trks.id AND artist_id = ?
          )
          """

    return repeat(sql, len(artist_ids)), artist_ids


def _generate_year_filter(years: list[int]) -> tuple[Iterable[str], Iterable[int]]:
    """
    Generate the SQL and params for filtering on the years.

    :param years: The years to filter on.
    :return: The filter SQL and query parameters.
    """
    if not years:
        return [], []

    return [f"rls.release_year IN ({', '.join('?' * len(years))})"], years


def create(
    title: str,
    filepath: Path,
    sha256_initial: bytes,
    release_id: int,
    artists: list[dict],
    duration: int,
    track_number: str,
    disc_number: str,
    conn: Connection,
    sha256: Optional[bytes] = None,
) -> T:
    """
    Create a track with the provided parameters.

    If a track already exists with the same SHA256, the filepath of that track will be
    set to the passed-in filepath and nothing else will be done.

    :param title: The title of the track.
    :param filepath: The filepath of the track.
    :param sha256_initial: The SHA256 of the first 1KB of the track file.
    :param release_id: The ID of the release that this track belongs to.
    :param artists: The artists that contributed to this track. A list of
                    ``{"artist_id": int, "role": ArtistRole}`` mappings.
    :param duration: The duration of this track, in seconds.
    :param track_number: The track number.
    :param disc_number: The disc number.
    :param sha256: The full SHA256 of the track file. This should generally not be
                   passed in--calculating a SHA256 requires a filesystem read of several
                   MB, and we want to do that lazily. But we allow it to be passed in
                   for testing and cases where efficiency doesn't matter.
    :return: The newly created track.
    :raises NotFound: If no release has the given release ID or no artist
                      corresponds with any of the given artist IDs.
    :raises Duplicate: If a track with the same filepath already exists. The duplicate
                       track is passed as the ``entity`` argument.
    """
    if not librelease.exists(release_id, conn):
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
    if trk := _check_for_duplicate_sha256(sha256_initial, filepath, conn):
        return trk

    # Track is not a duplicate, so we can insert and return.
    cursor = conn.execute(
        """
        INSERT INTO music__tracks (
            title,
            filepath,
            sha256_initial,
            release_id,
            track_number,
            disc_number,
            duration,
            sha256
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            title,
            str(filepath),
            sha256_initial,
            release_id,
            track_number,
            disc_number,
            duration,
            sha256,
        ),
    )

    trk = from_id(cursor.lastrowid, conn)
    assert trk is not None

    # Insert artists.
    for mapping in artists:
        trk = add_artist(trk, mapping["artist_id"], mapping["role"], conn)

    logger.info(f'Created track "{filepath}" with ID {trk.id}.')

    return trk


def _check_for_duplicate_sha256(
    sha256_initial: bytes,
    filepath: Path,
    conn: Connection,
) -> Optional[T]:
    """
    Check to see whether the current track shares a SHA256 with another track. If so,
    update the existing track to point to the new filepath and return the existing
    track. Otherwise, return None.

    This function takes in the sha256 of the first 1KB of the track. If we find that
    another track has the same first 1KB hash, we proceed to compare the full hashes of
    both files. We do this for efficiency reasons--see the scanner for more details.
    """
    trk = from_sha256_initial(sha256_initial, conn)
    if not trk:
        return None

    # At this point, we know that the sha256 of the first bytes exist.

    new_sha256 = calculate_sha_256(filepath)
    # This value is calculated lazily. Since we demand it here,
    # we must calculate it if it doesn't exist.
    trk = _ensure_track_has_full_sha256(trk, conn)

    if not trk.sha256 or new_sha256 != trk.sha256:
        return None

    # At this point, we know that the tracks have the same SHA256.

    conn.execute(
        "UPDATE music__tracks SET filepath = ? WHERE id = ?",
        (str(filepath), trk.id),
    )
    logger.debug(f"Found track {trk.id} with the same SHA256; updated filepath.")

    return from_id(trk.id, conn)


def _ensure_track_has_full_sha256(trk: T, conn: Connection) -> T:
    """
    Ensure that a track has a sha256 for the full track. If the track's file is no
    longer on disk, trk's sha256 will remain unmodified.

    :param trk: The track to update.
    :param conn: A connection to the database.
    :return: The updated track.
    """
    if trk.sha256:
        logger.debug(f"Track {trk.id} already has a full sha256, not calculating.")
        return trk

    logger.debug(f"Calculating sha256 for track {trk.id}.")
    try:
        try:
            calculate_track_full_sha256(trk, conn)
        except Duplicate as e:
            return e.entity

        # Reload track.
        refreshed_trk = from_id(trk.id, conn)
        assert refreshed_trk is not None
        return refreshed_trk
    except FileNotFoundError:
        logger.debug(f"File for track {trk.id} not on disk.")
        # TODO: Flag the file missing when we add the missing files feature?
        return trk


def calculate_track_full_sha256(trk: T, conn: Connection) -> bytes:
    """
    Given a track, calculate its full SHA256. If the newly calculated SHA256 is
    equivalent to an existing track's SHA256, delete the passed-in track and raise a
    Duplicate error with the existing track.

    :param trk: The track.
    :param conn: A connection to the DB.
    :return: The calculated SHA256.
    :raises FileNotFoundError: If the track no longer exists.
    :raises Duplicate: If the calculated sha256 is the same as an existing track. The
                       existing track is attached to the error.
    """
    logger.debug(f"Calculating SHA256 for {trk.filepath}.")
    sha256sum = calculate_sha_256(trk.filepath)

    # The newly calculated sha256 is a duplicate of another track...
    # To deduplicate, delete the new track.
    if dup := from_sha256(sha256sum, conn):
        logger.info(
            f"Track {trk.id} is a hash-duplicate of {dup.id}. Deleting {trk.id}."
        )
        delete(trk, conn)
        raise Duplicate("Duplicate SHA256 detected.", dup)

    conn.execute(
        "UPDATE music__tracks SET sha256 = ? WHERE id = ?",
        (sha256sum, trk.id),
    )
    return sha256sum


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
    if "release_id" in changes and not librelease.exists(changes["release_id"], conn):
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


def delete(trk: T, conn: Connection) -> None:
    """
    Delete a track.

    :param trk: The track to delete.
    :param conn: A connection to the database.
    """
    conn.execute(
        "DELETE FROM music__tracks WHERE id = ?",
        (trk.id,),
    )

    logger.info(f"Deleted track {trk.id}.")


def in_favorites(trk: T, user_id: int, conn: Connection) -> bool:
    """
    Return whether this track is in the favorites of the passed-in user.

    :param trk: The provided track.
    :param user_id: The ID of the user whose favorites to check.
    :param conn: A connection to the database.
    :return: Whether the track is in the user's favorites.
    :raises DoesNotExist: If the user's favorites does not exist.
    """
    favorites = playlist.favorites_of(user_id, conn)
    return playlist_entry.exists_playlist_and_track(favorites.id, trk.id, conn)


def release(trk: T, conn: Connection) -> librelease.T:
    """
    Get the release that this track belongs to.

    :param trk: The track whose artists to fetch.
    :param conn: A connection to the database.
    :return: A list of ``{"artist": artist.T, "role": ArtistRole}`` dicts.
    """
    rls = librelease.from_id(trk.release_id, conn)
    assert rls is not None
    logger.debug(f"Fetched release of track {trk.id}.")
    return rls


def artists(trk: T, conn: Connection) -> list[dict]:
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
        for row in cursor
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
