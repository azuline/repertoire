from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from itertools import chain, repeat
from pathlib import Path
from sqlite3 import Cursor, Row
from typing import List, Optional, Tuple

from unidecode import unidecode

from backend.enums import ReleaseSort, ReleaseType
from backend.errors import Duplicate
from backend.util import strip_punctuation

from . import artist, collection, track


@dataclass(frozen=True)
class T:
    """
    A release dataclass. This dataclass is frozen (immutable).
    """

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
    #: The date this release was released.
    release_date: Optional[date] = None
    #: The filepath of the album cover.
    image_path: Optional[Path] = None


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
    cursor.execute("""SELECT * FROM music__releases WHERE id = ?""", (id,))

    if row := cursor.fetchone():
        return from_row(row)


def search(
    cursor: Cursor,
    *,
    search: str = "",
    collections: List[collection.T] = [],
    artists: List[artist.T] = [],
    page: int = 1,
    per_page: Optional[int] = None,
    sort: ReleaseSort = ReleaseSort.RECENTLY_ADDED,
    asc: bool = True,
) -> Tuple[int, List[T]]:
    """
    Search for releases matching the passed-in criteria.

    :param search: A search string. We split this up into individual punctuation-less
                   words and return releases that contain each word.
    :param collections: A list of collections. We match releases by the collections in
                        this list. For a release to match, it must be in all collections
                        in this list.
    :param artists: A list of artists. We match releases by the artists in this list. For
                    a release to match, all artists in this list must be included.
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
        _generate_collection_filter(collections),
        _generate_artist_filter(artists),
        _generate_search_filter(search),
    ]:
        filter_sql.extend(sql)
        filter_params.extend(params)

    # Fetch the total number of releases matching this criteria (ignoring pages).
    cursor.execute(
        f"""
        SELECT COUNT(1)
        FROM music__releases AS rls
        {"WHERE" + " AND ".join(filter_sql) if filter_sql else ""}
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
        SELECT rls.*
        FROM music__releases AS rls
        {"WHERE" + " AND ".join(filter_sql) if filter_sql else ""}
        ORDER BY {sort.value} {"ASC" if asc else "DESC"}
        {"LIMIT ? OFFSET ?" if per_page else ""}
        """,
        filter_params,
    )

    return total, [from_row(row) for row in cursor.fetchall()]


def _generate_collection_filter(
    collections: List[collection.T],
) -> Tuple[str, List[int]]:
    """Generate the SQL and params for filtering on collections."""
    sql = """
          EXISTS (
              SELECT 1 FROM music__collections_releases
              WHERE release_id = rls.id AND collection_id = ?
          )
          """

    filter_sql = repeat(sql, len(collections))
    filter_params = [c.id for c in collections]

    return filter_sql, filter_params


def _generate_artist_filter(
    artists: List[artist.T],
) -> Tuple[str, List[int]]:
    """Generate the SQL and params for filtering on artists."""
    sql = """
          EXISTS (
              SELECT 1 FROM music__releases_artists
              WHERE release_id = rls.id AND artist_id = ?
          )
          """

    filter_sql = repeat(sql, len(artists))
    filter_params = [a.id for a in artists]

    return filter_sql, filter_params


def _generate_search_filter(search: str) -> Tuple[str, List[str]]:
    """Generate the SQL and params for filtering on the search words."""
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
    artists: List[artist.T],
    release_type: ReleaseType,
    release_year: int,
    cursor: Cursor,
    release_date: date = None,
    image_path: Path = None,
) -> T:
    """
    Create a release with the provided parameters.

    :param title: The title of the release.
    :param artists: The "album artists" on the release.
    :param release_type: The type of the release.
    :param release_year: The year the release came out.
    :param cursor: A cursor to the database.
    :param release_date: The date the release came out.
    :param image_path: A path to the release's cover art.
    :return: The newly created release.
    :raises Duplicate: If a release with the same name and artists already exists.
    """
    if _find_duplicate_release(title, artists):
        raise Duplicate

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
    for art in artists:
        cursor.execute(
            """
            INSERT INTO music__releases_artists (release_id, artist_id) VALUES (?, ?)
            """,
            (id, art.id),
        )
    cursor.connection.commit()

    # We fetch it from the database to also get the `added_on` column.
    return from_id(id, cursor)


def _find_duplicate_release(
    title: str, artists: List[artist.T], cursor: Cursor
) -> bool:
    """
    Try to find a duplicate release with the given title and artists. Return whether we
    find one or not.

    :param title: The title of the release.
    :param artists: The artists that contributed to the release.
    """
    # We run a search on the title, limiting it to releases with all the artists, and
    # then see if any have an exact match with the title.
    matches = search(search=title, artists=artists, cursor=cursor)
    return any(rls.title == title for rls in matches)


def tracks(release: T, cursor: Cursor) -> List[track.T]:
    """
    Get the tracks of the provided release.

    :param release: The provided release.
    :param cursor: A cursor to the database.
    :return: The tracks of the provided release.
    """
    cursor.execute(
        """SELECT * FROM music__tracks WHERE release_id = ?""",
        (release.id,),
    )
    return [track.from_row(row, cursor) for row in cursor.fetchall()]


def artists(release: T, cursor: Cursor) -> List[artist.T]:
    """
    Get the "album artists" of the provided release.

    :param release: The provided release.
    :param cursor: A cursor to the datbase.
    :return: The "album artists" of the provided release.
    """
    cursor.execute(
        """
        SELECT arts.*
        FROM music__releases_artists AS rlsarts
        JOIN music__artists AS arts ON arts.id = rlsarts.artist_id
        WHERE rlsarts.release_id = ?
        """,
        (release.id,),
    )
    return [artist.from_row(row) for row in cursor.fetchall()]


def collections(release: T, cursor: Cursor) -> List[collection.T]:
    """
    Get the collections that contain the provided release.

    :param release: The provided release.
    :param cursor: A cursor to the datbase.
    :return: The collections that contain the provided release.
    """
    cursor.execute(
        """
        SELECT cols.*
        FROM music__collections AS cols
        JOIN music__collections_releases AS colsrls
            ON colsrls.collection_id = cols.id
        WHERE colsrls.release_id = ?
        """,
        (release.id,),
    )
    return [collection.from_row(row) for row in cursor.fetchall()]
