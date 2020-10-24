from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from sqlite3 import Cursor, Row
from typing import Any, Dict, List, Optional

from backend.enums import CollectionType
from backend.errors import Duplicate
from backend.util import without_key

from . import collection, release

logger = logging.getLogger(__name__)


@dataclass
class T:
    """An artist dataclass."""

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    name: str
    #:
    favorite: bool
    #: The number of releases attributed to the artist.
    num_releases: int


def from_row(row: Row) -> T:
    """
    Return an artist dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: An artist dataclass.
    """
    return T(**dict(row, favorite=bool(row["favorite"])))


def from_id(id: int, cursor: Cursor) -> Optional[T]:
    """
    Return the artist with the provided ID.

    :param id: The ID of the artist to fetch.
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
        GROUP BY arts.id
        """,
        (id,),
    )

    if row := cursor.fetchone():
        return from_row(row)


def from_name(name: str, cursor: Cursor) -> Optional[T]:
    """
    Return the artist with the given name, if they exist.

    :param name: The name of the artist.
    :param cursor: A cursor to the database.
    :return: The artist, if they exist.
    """
    cursor.execute(
        """
        SELECT
            arts.*,
            COUNT(artsrls.release_id) AS num_releases
        FROM music__artists AS arts
        LEFT JOIN music__releases_artists AS artsrls
            ON artsrls.artist_id = arts.id
        WHERE arts.name = ?
        GROUP BY arts.id
        """,
        (name,),
    )

    if row := cursor.fetchone():
        return from_row(row)


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


def create(name: str, cursor: Cursor, favorite: bool = False) -> T:
    """
    Create an artist and persist it to the database.

    :param name: The name of the artist.
    :cursor: A cursor to the database.
    :param favorite: Whether the artist is a favorite or not.
    :return: The newly created artist.
    :raises Duplicate: If an artist with the same name already exists. The duplicate
                       artist is passed as the ``entity`` argument.
    """
    if art := from_name(name, cursor):
        raise Duplicate(art)

    cursor.execute(
        "INSERT INTO music__artists (name, favorite) VALUES (?, ?)", (name, favorite)
    )
    cursor.connection.commit()

    logger.info(f'Created artist "{name}" with ID {cursor.lastrowid}')

    return T(id=cursor.lastrowid, name=name, favorite=favorite, num_releases=0)


def update(art: T, cursor: Cursor, **changes: Dict[str, Any]) -> T:
    """
    Update an artist and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    :param art: The artist to update.
    :param cursor: A cursor to the database.
    :param name: New artist name.
    :type  name: :py:obj:`str`
    :param favorite: New artist favorite.
    :type  favorite: :py:obj:`bool`
    :return: The updated artist.
    :raises Duplicate: If an artist already exists with the new name.
    """
    if (
        "name" in changes
        and (dupl := from_name(changes["name"], cursor))
        and dupl != art
    ):
        raise Duplicate(dupl)

    cursor.execute(
        """
        UPDATE music__artists
        SET name = ?,
            favorite = ?
        WHERE id = ?
        """,
        (changes.get("name", art.name), changes.get("favorite", art.favorite), art.id),
    )
    cursor.connection.commit()

    logger.info(f"Updated artist {art.id} with {changes}.")

    return T(**dict(asdict(art), **changes))


def releases(art: T, cursor: Cursor) -> List[release.T]:
    """
    Get the releases of an artist.

    :param art: The artist whose releases we want to get.
    :param cursor: A cursor to the database.
    :return: A list of releases of the artist.
    """
    _, releases = release.search(artists=[art.id], cursor=cursor)
    return releases


def top_genres(art: T, cursor: Cursor, *, num_genres: int = 5) -> List[Dict]:
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

    :param art: The artist whose top genres to fetch.
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
        LIMIT ?
        """,
        (art.id, CollectionType.GENRE.value, num_genres),
    )

    return [
        {
            "genre": collection.from_row(without_key(row, "num_matches")),
            "num_matches": row["num_matches"],
        }
        for row in cursor.fetchall()
    ]
