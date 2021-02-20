from __future__ import annotations

import logging
from dataclasses import dataclass
from sqlite3 import Connection, Row
from typing import Dict, List, Optional, Union

from src.enums import CollectionType
from src.errors import Duplicate
from src.util import update_dataclass, without_key

from . import collection
from . import image as libimage
from . import release

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class T:
    """An artist dataclass."""

    # We have these empty comments so that the attributes and types render in sphinx...
    #:
    id: int
    #:
    name: str
    #:
    starred: bool
    #: The number of releases attributed to the artist.
    num_releases: int


def exists(id: int, conn: Connection) -> bool:
    """
    Return whether an artist exists with the given ID.

    :param id: The ID to check.
    :return: Whether an artist has the given ID.
    """
    cursor = conn.execute("SELECT 1 FROM music__artists WHERE id = ?", (id,))
    return bool(cursor.fetchone())


def from_row(row: Union[Dict, Row]) -> T:
    """
    Return an artist dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: An artist dataclass.
    """
    return T(**dict(row, starred=bool(row["starred"])))


def from_id(id: int, conn: Connection) -> Optional[T]:
    """
    Return the artist with the provided ID.

    :param id: The ID of the artist to fetch.
    :param conn: A connection to the database.
    :return: The artist with the provided ID, if it exists.
    """
    cursor = conn.execute(
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
        logger.debug(f"Fetched artist {id}.")
        return from_row(row)

    logger.debug(f"Failed to fetch artist {id}.")
    return None


def from_name(name: str, conn: Connection) -> Optional[T]:
    """
    Return the artist with the given name, if they exist.

    :param name: The name of the artist.
    :param conn: A connection to the database.
    :return: The artist, if they exist.
    """
    cursor = conn.execute(
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
        logger.debug(f"Fetched artist {row['id']} with name {name}.")
        return from_row(row)

    logger.debug(f"Failed to fetch artist with name {name}.")
    return None


def all(conn: Connection) -> List[T]:
    """
    Get all artists with one-or-more releases.

    :param conn: A connection to the database.
    :return: All artists with releases stored on the src.
    """
    cursor = conn.execute(
        """
        SELECT
            arts.*,
            COUNT(artsrls.release_id) AS num_releases
        FROM music__artists AS arts
        LEFT JOIN music__releases_artists AS artsrls
            ON artsrls.artist_id = arts.id
        GROUP BY arts.id
        ORDER BY
            arts.starred DESC,
            arts.name
        """
    )

    logger.debug("Fetched all artists.")
    return [from_row(row) for row in cursor if row["num_releases"]]


def create(name: str, conn: Connection, starred: bool = False) -> T:
    """
    Create an artist and persist it to the database.

    :param name: The name of the artist.
    :param conn: A connection to the database.
    :param starred: Whether the artist is starred or not.
    :return: The newly created artist.
    :raises Duplicate: If an artist with the same name already exists. The duplicate
                       artist is passed as the ``entity`` argument.
    """
    if art := from_name(name, conn):
        raise Duplicate(f'Artist "{name}" already exists.', art)

    cursor = conn.execute(
        "INSERT INTO music__artists (name, starred) VALUES (?, ?)", (name, starred)
    )

    logger.info(f'Created artist "{name}" with ID {cursor.lastrowid}')

    return T(id=cursor.lastrowid, name=name, starred=starred, num_releases=0)


def update(art: T, conn: Connection, **changes) -> T:
    """
    Update an artist and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    :param art: The artist to update.
    :param conn: A connection to the database.
    :param name: New artist name.
    :type  name: :py:obj:`str`
    :param starred: Whether new artist is starred.
    :type  starred: :py:obj:`bool`
    :return: The updated artist.
    :raises Duplicate: If an artist already exists with the new name.
    """
    if "name" in changes and (dupl := from_name(changes["name"], conn)) and dupl != art:
        raise Duplicate(f'Artist "{changes["name"]}" already exists.', dupl)

    conn.execute(
        """
        UPDATE music__artists
        SET name = ?,
            starred = ?
        WHERE id = ?
        """,
        (changes.get("name", art.name), changes.get("starred", art.starred), art.id),
    )

    logger.info(f"Updated artist {art.id} with {changes}.")

    return update_dataclass(art, **changes)


def releases(art: T, conn: Connection) -> List[release.T]:
    """
    Get the releases of an artist.

    :param art: The artist whose releases we want to get.
    :param conn: A connection to the database.
    :return: A list of releases of the artist.
    """
    _, releases = release.search(artist_ids=[art.id], conn=conn)
    logger.debug(f"Fetched the releases of artist {art.id}.")
    return releases


def top_genres(art: T, conn: Connection, *, num_genres: int = 5) -> List[Dict]:
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
    :param conn: A connection to the database.
    :param num_genres: The number of top genres to fetch.
    :return: The top genres.
    """
    cursor = conn.execute(
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

    logger.debug(f"Fetched the top genres of artist {art.id}.")

    return [
        {
            "genre": collection.from_row(without_key(row, "num_matches")),
            "num_matches": row["num_matches"],
        }
        for row in cursor
    ]


def image(art: T, conn: Connection) -> Optional[libimage.T]:
    """
    Return an image for an artist.

    At the moment, artists do not have images, so we return a random cover image from
    one of the artists' releases, if any exist.

    :param art: The artist whose image to fetch.
    :param conn: A connection to the database.
    :return: The image, if it exists.
    """
    cursor = conn.execute(
        """
        SELECT images.*
        FROM images
            JOIN music__releases AS rls ON rls.image_id = images.id
            JOIN music__releases_artists AS rlsarts ON rlsarts.release_id = rls.id
        WHERE rlsarts.artist_id = ?
        ORDER BY RANDOM()
        LIMIT 1
        """,
        (art.id,),
    )

    if row := cursor.fetchone():
        logger.debug(f"Fetched the image of artist {art.id}.")
        return libimage.from_row(row)

    logger.debug(f"Failed to fetch the image of artist {art.id}.")
    return None
