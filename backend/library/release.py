from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from datetime import date, datetime
from itertools import chain, repeat
from pathlib import Path
from sqlite3 import Cursor, Row
from typing import Any, Dict, List, Optional, Tuple

from unidecode import unidecode

from backend.enums import CollectionType, ReleaseSort, ReleaseType
from backend.errors import AlreadyExists, DoesNotExist, Duplicate, NotFound
from backend.util import strip_punctuation

from . import artist, collection, track

logger = logging.getLogger(__name__)


@dataclass
class T:
    """A release dataclass."""

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    title: str
    #: The type of this release.
    release_type: ReleaseType
    #: When this release was added to the server.
    added_on: datetime
    #: The year this release was released.
    release_year: int
    #: The number of tracks that this release has.
    num_tracks: int
    # Whether this release is in the inbox.
    in_inbox: bool
    #: The date this release was released.
    release_date: Optional[date] = None
    #: The filepath of the album cover.
    image_path: Optional[Path] = None


def exists(id: int, cursor: Cursor) -> bool:
    """
    Return whether a release exists with the given ID.

    :param id: The ID to check.
    :return: Whether a release has the given ID.
    """
    cursor.execute("SELECT 1 FROM music__releases WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Row) -> T:
    """
    Return a release dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A release dataclass.
    """
    return T(
        **dict(
            row,
            release_type=ReleaseType(row["release_type"]),
            in_inbox=bool(row["in_inbox"]),
            image_path=Path(row["image_path"]) if row["image_path"] else None,
        )
    )


def from_id(id: int, cursor: Cursor) -> Optional[T]:
    """
    Return the release with the provided ID.

    :param id: The ID of the release to fetch.
    :param cursor: A cursor to the database.
    :return: The release with the provided ID, if it exists.
    """
    cursor.execute(
        """
        SELECT
            rls.*,
            COUNT(trks.id) AS num_tracks,
            (
                SELECT 1
                FROM music__collections_releases
                WHERE release_id = rls.id AND collection_id = 1
            ) AS in_inbox
        FROM music__releases AS rls
            LEFT JOIN music__tracks AS trks ON trks.release_id = rls.id
        WHERE rls.id = ?
        GROUP BY rls.id
        """,
        (id,),
    )

    if row := cursor.fetchone():
        return from_row(row)


def search(
    cursor: Cursor,
    *,
    search: str = "",
    collection_ids: List[int] = [],
    artist_ids: List[int] = [],
    release_types: List[ReleaseType] = [],
    page: int = 1,
    per_page: Optional[int] = None,
    sort: ReleaseSort = ReleaseSort.RECENTLY_ADDED,
    asc: bool = True,
) -> Tuple[int, List[T]]:
    """
    Search for releases matching the passed-in criteria.

    :param search: A search string. We split this up into individual punctuation-less
                   words and return releases that contain each word.
    :param collection_ids: A list of collection IDs. We match releases by the collections
                           in this list. For a release to match, it must be in all
                           collections in this list.
    :param artist_ids: A list of artist IDs. We match releases by the artists in this
                       list. For a release to match, all artists in this list must be
                       included.
    :param release_types: A list of release types. Filter out releases that do not match
                          one of the release types in this list.
    :param page: Which page of releases to return.
    :param per_page: The number of releases per-page. Pass ``None`` to return all
                     releases (this will ignore ``page``).
    :param sort: How to sort the matching releases.
    :param asc: If true, sort in ascending order. If false, descending.
    :param cursor: A cursor to the database.
    :return: The total number of matching releases and the matching releases on the
             current page.
    """
    # Dynamically generate the filter SQL and filter params.
    filter_sql = []
    filter_params = []

    for sql, params in [
        _generate_collection_filter(collection_ids),
        _generate_artist_filter(artist_ids),
        _generate_release_types_filter(release_types),
        _generate_search_filter(search),
    ]:
        filter_sql.extend(sql)
        filter_params.extend(params)

    # Fetch the total number of releases matching this criteria (ignoring pages).
    cursor.execute(
        f"""
        SELECT COUNT(1)
        FROM music__releases AS rls
        {"WHERE " + " AND ".join(filter_sql) if filter_sql else ""}
        """,
        filter_params,
    )
    total = cursor.fetchone()[0]

    # If we have pagination, add the pagination params to the filter SQL.
    if per_page:
        filter_params.extend([per_page, (page - 1) * per_page])

    # Fetch the releases on the current page.
    cursor.execute(
        f"""
        SELECT
            rls.*,
            COUNT(trks.id) AS num_tracks,
            (
                SELECT 1
                FROM music__collections_releases
                WHERE release_id = rls.id AND collection_id = 1
            ) AS in_inbox
        FROM music__releases AS rls
            LEFT JOIN music__tracks AS trks ON trks.release_id = rls.id
        {"WHERE " + " AND ".join(filter_sql) if filter_sql else ""}
        GROUP BY rls.id
        ORDER BY {sort.value} {"ASC" if asc else "DESC"}
        {"LIMIT ? OFFSET ?" if per_page else ""}
        """,
        filter_params,
    )

    return total, [from_row(row) for row in cursor.fetchall()]


def _generate_collection_filter(
    collection_ids: List[int],
) -> Tuple[List[str], List[int]]:
    """
    Generate the SQL and params for filtering on collections.

    :param collection_ids: The collection IDs to filter on.
    :return: The filter SQL and query parameters.
    """
    sql = """
          EXISTS (
              SELECT 1 FROM music__collections_releases
              WHERE release_id = rls.id AND collection_id = ?
          )
          """

    return repeat(sql, len(collection_ids)), collection_ids


def _generate_artist_filter(artist_ids: List[int]) -> Tuple[List[str], List[int]]:
    """
    Generate the SQL and params for filtering on artists.

    :param artist_ids: The artist IDs to filter on.
    :return: The filter SQL and query parameters.
    """
    sql = """
          EXISTS (
              SELECT 1 FROM music__releases_artists
              WHERE release_id = rls.id AND artist_id = ?
          )
          """

    return repeat(sql, len(artist_ids)), artist_ids


def _generate_release_types_filter(
    release_types: List[ReleaseType],
) -> Tuple[List[str], List[int]]:
    """
    Generate the SQL and params for filtering on the release types.

    :param release_types: The release types to filter on.
    :return: The filter SQL and query parameters.
    """
    if not release_types:
        return [], []

    filter_sql = [f"rls.release_type IN ({', '.join('?' * len(release_types))})"]
    filter_params = [rtype.value for rtype in release_types]

    return filter_sql, filter_params


def _generate_search_filter(search: str) -> Tuple[List[str], List[str]]:
    """
    Generate the SQL and params for filtering on the search words.

    :param search: The search words to filter on.
    :return: The filter SQL and query parameters.
    """
    sql = """
          EXISTS (
              SELECT 1 FROM music__releases_search_index
              WHERE (word = ? OR word = ?) AND release_id = rls.id
          )
          """

    words = [w for w in strip_punctuation(search).split(" ") if w]

    filter_sql = repeat(sql, len(words))
    filter_params = chain(*((word, unidecode(word)) for word in words))

    return filter_sql, filter_params


def create(
    title: str,
    artist_ids: List[int],
    release_type: ReleaseType,
    release_year: int,
    cursor: Cursor,
    release_date: Optional[date] = None,
    image_path: Optional[Path] = None,
    allow_duplicate: bool = True,
) -> T:
    """
    Create a release with the provided parameters.

    :param title: The title of the release.
    :param artist_ids: The IDs of the "album artists" on the release.
    :param release_type: The type of the release.
    :param release_year: The year the release came out.
    :param cursor: A cursor to the database.
    :param release_date: The date the release came out.
    :param image_path: A path to the release's cover art.
    :param allow_duplicate: Whether to allow creation of a duplicate release or not. If
                             this is ``False``, then ``Duplicate`` will never be raised.
                             All releases will be created.
    :return: The newly created release.
    :raises NotFound: If the list of artists contains an invalid ID.
    :raises Duplicate: If a release with the same name and artists already exists. The
                       duplicate release is passed as the ``entity`` argument.
    """
    if bad_ids := [str(id) for id in artist_ids if not artist.exists(id, cursor)]:
        raise NotFound(f"Artist(s) {', '.join(bad_ids)} do not exist.")

    if not allow_duplicate and (
        rls := _find_duplicate_release(title, artist_ids, cursor)
    ):
        raise Duplicate(rls)

    # Insert the release into the database.
    cursor.execute(
        """
        INSERT INTO music__releases (
            title, image_path, release_type, release_year, release_date
        ) VALUES (?, ?, ?, ?, ?)
        """,
        (title, image_path, release_type.value, release_year, release_date),
    )
    cursor.connection.commit()
    id = cursor.lastrowid

    # Insert the release artists into the database.
    for artist_id in artist_ids:
        cursor.execute(
            """
            INSERT INTO music__releases_artists (release_id, artist_id) VALUES (?, ?)
            """,
            (id, artist_id),
        )
    cursor.connection.commit()

    logger.info(f'Created release "{title}" with ID {id}.')

    # We fetch it from the database to also get the `added_on` column.
    return from_id(id, cursor)


def _find_duplicate_release(
    title: str,
    artist_ids: List[int],
    cursor: Cursor,
) -> Optional[T]:
    """
    Try to find a duplicate release with the given title and artists. If we find a
    duplicate release, return it.

    :param title: The title of the release.
    :param artist_ids: The IDs of the artists that contributed to the release.
    :param cursor: A cursor to the database.
    :return: The duplicate release, if found.
    """
    # First fetch all releases with the same title.
    cursor.execute(
        """
        SELECT
            rls.*,
            COUNT(trks.id) AS num_tracks,
            (
                SELECT 1
                FROM music__collections_releases
                WHERE release_id = rls.id AND collection_id = 1
            ) AS in_inbox
        FROM music__releases AS rls
            LEFT JOIN music__tracks AS trks ON trks.release_id = rls.id
        WHERE rls.title = ?
        GROUP BY rls.id
        """,
        (title,),
    )
    release_ids = cursor.fetchall()

    # Construct a lowercase set of artists for a future case-insensitive comparison.
    provided_artists = set()
    for id in artist_ids:
        cursor.execute("SELECT name FROM music__artists WHERE id = ?", (id,))
        provided_artists.add(cursor.fetchone()["name"].lower())

    for row in release_ids:
        # For each release with the same title, compare the artists.
        cursor.execute(
            """
            SELECT name
            FROM music__artists AS arts
            INNER JOIN music__releases_artists AS relarts
                ON relarts.artist_id = arts.id
            WHERE relarts.release_id = ?
            """,
            (row["id"],),
        )

        # Compare the artists of this release with our provided artists.
        if provided_artists == {row["name"].lower() for row in cursor.fetchall()}:
            # If they match, return this release, as it is a duplicate.
            return from_row(row)


def update(rls: T, cursor: Cursor, **changes: Dict[str, Any]) -> T:
    """
    Update a release and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    :param rls: The release to update.
    :param cursor: A cursor to the database.
    :param title: New release title.
    :type  title: :py:obj:`str`
    :param release_type: New release type.
    :type  release_type: :py:obj:`backend.enums.ReleaseType`
    :param release_year: New release year.
    :type  release_year: :py:obj:`int`
    :param release_date: New release date.
    :type  release_date: :py:obj:`datetime.date`
    :return: The updated release.
    """
    cursor.execute(
        """
        UPDATE music__releases
        SET title = ?,
            release_type = ?,
            release_year = ?,
            release_date = ?
        WHERE id = ?
        """,
        (
            changes.get("title", rls.title),
            changes.get("release_type", rls.release_type).value,
            changes.get("release_year", rls.release_year),
            changes.get("release_date", rls.release_date),
            rls.id,
        ),
    )
    cursor.connection.commit()

    logger.info(f"Updated release {rls.id} with {changes}.")

    return T(**dict(asdict(rls), **changes))


def tracks(rls: T, cursor: Cursor) -> List[track.T]:
    """
    Get the tracks of the provided release.

    :param rls: The provided release.
    :param cursor: A cursor to the database.
    :return: The tracks of the provided release.
    """
    cursor.execute("SELECT * FROM music__tracks WHERE release_id = ?", (rls.id,))
    return [track.from_row(row) for row in cursor.fetchall()]


def artists(rls: T, cursor: Cursor) -> List[artist.T]:
    """
    Get the "album artists" of the provided release.

    :param rls: The provided release.
    :param cursor: A cursor to the datbase.
    :return: The "album artists" of the provided release.
    """
    cursor.execute(
        """
        SELECT
            artists.*,
            COUNT(rlsarts.release_id) AS num_releases
        FROM (
            SELECT arts.*
            FROM music__releases_artists AS rlsarts
            JOIN music__artists AS arts ON arts.id = rlsarts.artist_id
            WHERE rlsarts.release_id = ?
            GROUP BY arts.id
        ) AS artists
        JOIN music__releases_artists AS rlsarts ON rlsarts.artist_id = artists.id
        GROUP BY artists.id
        """,
        (rls.id,),
    )
    return [artist.from_row(row) for row in cursor.fetchall()]


def add_artist(rls: T, artist_id: int, cursor: Cursor) -> None:
    """
    Add the provided artist to the provided release.

    :param rls: The release to add the artist to.
    :param artist_id: The ID of the artist to add.
    :param cursor: A cursor to the database.
    :raises NotFound: If no artist has the given artist ID.
    :raises AlreadyExists: If the artist is already on the release.
    """
    if not artist.exists(artist_id, cursor):
        raise NotFound(f"Artist {artist_id} does not exist.")

    cursor.execute(
        "SELECT 1 FROM music__releases_artists WHERE release_id = ? AND artist_id = ?",
        (rls.id, artist_id),
    )
    if cursor.fetchone():
        raise AlreadyExists

    cursor.execute(
        "INSERT INTO music__releases_artists (release_id, artist_id) VALUES (?, ?)",
        (rls.id, artist_id),
    )
    cursor.connection.commit()


def del_artist(rls: T, artist_id: int, cursor: Cursor) -> None:
    """
    Delete the provided artist to the provided release.

    :param rls: The release to delete the artist from.
    :param artist_id: The ID of the artist to delete.
    :param cursor: A cursor to the database.
    :raises NotFound: If no artist has the given artist ID.
    :raises DoesNotExist: If the artist is not on the release.
    """
    if not artist.exists(artist_id, cursor):
        raise NotFound(f"Artist {artist_id} does not exist.")

    cursor.execute(
        "SELECT 1 FROM music__releases_artists WHERE release_id = ? AND artist_id = ?",
        (rls.id, artist_id),
    )
    if not cursor.fetchone():
        raise DoesNotExist

    cursor.execute(
        "DELETE FROM music__releases_artists WHERE release_id = ? AND artist_id = ?",
        (rls.id, artist_id),
    )
    cursor.connection.commit()


def collections(
    rls: T, cursor: Cursor, type: Optional[CollectionType] = None
) -> List[collection.T]:
    """
    Get the collections that contain the provided release.

    :param rls: The provided release.
    :param cursor: A cursor to the datbase.
    :param type: The type of collections to fetch. Leave ``None`` to fetch all.
    :return: The collections that contain the provided release.
    """
    cursor.execute(
        f"""
        SELECT
            collections.*,
            COUNT(colsrls.release_id) AS num_releases,
            MAX(colsrls.added_on) AS last_updated_on
        FROM (
            SELECT cols.*
            FROM music__collections AS cols
            JOIN music__collections_releases AS colsrls
                ON colsrls.collection_id = cols.id
            WHERE colsrls.release_id = ?
                {"AND cols.type = ?" if type else ""}
            GROUP BY cols.id
        ) AS collections
        JOIN music__collections_releases AS colsrls
            ON colsrls.collection_id = collections.id
        GROUP BY collections.id
        """,
        (rls.id, *((type.value,) if type else ())),
    )
    return [collection.from_row(row) for row in cursor.fetchall()]
