from __future__ import annotations

from dataclasses import dataclass
from sqlite3 import Cursor, Row
from typing import Dict, List, Optional

from backend.enums import CollectionType

from . import release


@dataclass
class T:
    """
    An artist dataclass. This dataclass is frozen (immutable).
    """

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    name: str
    #:
    favorite: bool
    #: The number of releases attributed to the artist.
    num_releases: Optional[int]


def from_row(row: Row) -> T:
    """
    Return an artist dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: An artist dataclass.
    """
    return T(**row)


def from_id(id_: int, cursor: Cursor) -> Optional[T]:
    """
    Return the artist with the provided ID.

    :param id_: The ID of the artist to fetch.
    :param cursor: A cursor to the database.
    :return: The artist with the provided ID, if it exists.
    """
    cursor.execute(
        """
        SELECT
            arts.*,
            COUNT(artsrls.release_id) AS num_releases
        FROM music__artists AS arts
        LEFT JOIN music__releases_artists AS artsrls
            ON artsrls.artist_id = arts.id
        WHERE arts.id = ?
        """,
        (id_,),
    )

    row = cursor.fetchone()
    return from_row(row) if row else None


def all(cursor: Cursor) -> List[T]:
    """
    Get all artists with one-or-more releases.

    :param cursor: A cursor to the database.
    :return: All artists with releases stored on the backend.
    """
    cursor.execute(
        """
        SELECT
            arts.*,
            COUNT(artsrls.release_id) AS num_releases
        FROM music__artists AS arts
        LEFT JOIN music__releases_artists AS artsrls
            ON artsrls.artist_id = arts.id
        GROUP BY arts.id
        """
    )
    return [from_row(row) for row in cursor.fetchall() if row["num_releases"]]


def releases(artist: T, cursor: Cursor) -> List[release.T]:
    """
    Get the releases of an artist.

    :param collection: The artist whose releases we want to get.
    :param cursor: A cursor to the database.
    :return: A list of releases of the artist.
    """
    _, releases = release.search(artists=[artist], cursor=cursor)
    return releases


def top_genres(artist: T, cursor: Cursor, *, num_genres: int = 5) -> List[Dict]:
    """
    Get the top genre collections of the releases of an artist.

    The returned genres are in the following format:

    .. code-block:: python

       [
         {
           "genre": genre.T,
           "num_matches": int,
         },
         ...
       ]

    :param artist: The artist whose top genres to fetch.
    :param cursor: A cursor to the database.
    :param num_genres: The number of top genres to fetch.
    :return: The top genres.
    """
    cursor.execute(
        """
        SELECT
            genres.*,
            COUNT(genresrls.release_id) AS num_matches
        FROM music__collections AS genres
        LEFT JOIN music__collections_releases AS genresrls
            ON genresrls.collection_id = genres.id
        LEFT JOIN music__releases_artists AS artsrls
            ON artsrls.release_id = genresrls.release_id
        WHERE artsrls.artist_id = ? AND genres.type = ?
        GROUP BY genres.id
        ORDER BY num_matches DESC
        LIMIT 5
        """,
        (artist.id, CollectionType.GENRE.value, num_genres),
    )

    top_genres = []

    for row in cursor.fetchall():
        matches = row["num_matches"]
        del row["num_matches"]
        top_genres.append({"genre": from_row(row), "num_matches": matches})

    return top_genres
