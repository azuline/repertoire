from dataclasses import dataclass
from datetime import datetime
from itertools import chain
from pathlib import Path
from sqlite3 import Cursor, Row
from typing import List, Optional, Tuple

from unidecode import unidecode

from backend.enums import ReleaseSort, ReleaseType
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
    #: The year this release was released.
    release_year: int
    #: The date this release was released.
    release_date: Optional[datetime]
    #: The filepath of the album cover.
    image_path: Optional[Path]
    #: When this release was added to the server.
    added_on: datetime


def from_row(row: Row) -> T:
    """
    Return a release dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: A release dataclass.
    """
    return T(
        **row,
        release_type=ReleaseType(row["release_type"]),
        image_path=Path(row["image_path"]) if row["image_path"] else None,
    )


def search(
    cursor: Cursor,
    search: str = "",
    collections: List[int] = [],
    artists: List[int] = [],
    page: int = 1,
    limit: Optional[int] = None,
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
    :param limit: The maximum amount of releases to return. Pass ``None`` to return all
                  releases.
    :param sort: How to sort the matching releases.
    :param asc: If true, sort in ascending order. If false, descending.
    :param cursor: A cursor to the database.
    :return: The total number of matching releases and the matching releases on the
             current page.
    """
    # Generate the dynamic SQL filters and parameters.
    collection_sql, collection_params = _generate_collection_filter(collections)
    artist_sql, artist_params = _generate_artist_filter(artists)
    search_sql, search_params = _generate_search_filter(search)

    # Combine the dynamically generated SQL and parameters.
    filter_sql = collection_sql + artist_sql + search_sql
    filter_params = tuple(collection_params + artist_params + search_params)

    # Fetch the total number of releases matching this criteria.
    cursor.execute(
        f"""
        SELECT COUNT(1)
        FROM music__releases AS rls
        {"WHERE" + " AND ".join(filter_sql) if filter_sql else ""}
        """,
        filter_params,
    )
    total = cursor.fetchone()[0]

    # Fetch the releases on the current page.
    cursor.execute(
        f"""
        SELECT rls.*
        FROM music__releases AS rls
        {"WHERE" + " and ".join(filter_sql) if filter_sql else ""}
        ORDER BY {sort} {"ASC" if asc else "DESC"}
        LIMIT ? OFFSET ?
        """,
        (*filter_params, limit, (page - 1) * limit),
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
    return sql * len(collections), [c.id for c in collections]


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

    return sql * len(artists), [a.id for a in artists]


def _generate_search_filter(search: str) -> Tuple[str, List[str]]:
    """Generate the SQL and params for filtering on the search words."""
    sql = """
          EXISTS (
              SELECT 1 FROM music__releases_search_index
              WHERE (word = ? OR word = ?) AND release_id = rls.id
          )
          """

    words = [w for w in strip_punctuation(search).split(" ") if w]

    return sql * 2 * words, list(chain(*([word, unidecode(word)] for word in words)))


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
    return [track.from_row(row) for row in cursor.fetchall()]


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
