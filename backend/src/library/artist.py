from __future__ import annotations

import logging
from dataclasses import dataclass
from sqlite3 import Connection, Row
from typing import Optional, Union

from src.enums import CollectionType
from src.errors import Duplicate
from src.util import make_fts_match_query, update_dataclass, without_key

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


def from_row(row: Union[dict, Row]) -> T:
    """
    Return an artist dataclass containing data from a row from the database.

    :param row: A row from the database.
    :return: An artist dataclass.
    """
    return T(**dict(row))


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


def search(
    conn: Connection,
    search: str = "",
    page: int = 1,
    per_page: Optional[int] = None,
) -> list[T]:
    """
    Search for artists. Parameters are optional; omitted ones are excluded from the
    matching criteria.

    :param conn: A connection to the database.
    :param search: A search string. We split this up into individual punctuation-less
                   tokens and return artists whose names contain each token. If
                   specified, the returned artists will be sorted by match proximity.
    :param page: Which page of artists to return.
    :param per_page: The number of artists per page. Pass ``None`` to return all
                     artists (this will ignore ``page``).
    :return: All matching artists.
    """
    filters, params = _generate_filters(search)

    if per_page:
        params.extend([per_page, (page - 1) * per_page])

    cursor = conn.execute(
        f"""
        SELECT
            arts.*,
            COUNT(artsrls.release_id) AS num_releases
        FROM music__artists AS arts
        JOIN music__artists__fts AS fts ON fts.rowid = arts.id
        LEFT JOIN music__releases_artists AS artsrls
            ON artsrls.artist_id = arts.id
        {"WHERE " + " AND ".join(filters) if filters else ""}
        GROUP BY arts.id
        ORDER BY {"fts.rank" if search else "arts.name"}
        {"LIMIT ? OFFSET ?" if per_page else ""}
        """,
        params,
    )

    logger.debug(f"Searched artists with {cursor.rowcount} results.")
    return [from_row(row) for row in cursor]


def count(
    conn: Connection,
    search: str = "",
) -> int:
    """
    Fetch the number of artists matching the passed-in criteria. Parameters are
    optional; omitted ones are excluded from the matching criteria.

    :param conn: A connection to the database.
    :param search: A search string. We split this up into individual punctuation-less
                   tokens and return artists whose names contain each token.
    :return: The number of matching artists.
    """
    filters, params = _generate_filters(search)

    cursor = conn.execute(
        f"""
        SELECT COUNT(1)
        FROM music__artists AS arts
        JOIN music__artists__fts AS fts ON fts.rowid = arts.id
        {"WHERE " + " AND ".join(filters) if filters else ""}
        """,
        params,
    )

    count = cursor.fetchone()[0]
    logger.debug(f"Counted {count} artists that matched the filters.")
    return count


def _generate_filters(search: str = "") -> tuple[list[str], list[Union[str, int]]]:
    """
    Dynamically generate the SQL filters and parameters from the criteria. See the
    search and total functions for parameter descriptions.

    :return: A tuple of SQL filter strings and parameters. The SQL filter strings can be
    joined with `` AND `` and injected into the where clause.
    """
    filters: list[str] = []
    params: list[Union[str, int]] = []

    if search:
        filters.append("fts.music__artists__fts MATCH ?")
        params.append(make_fts_match_query(search))

    return filters, params


def create(name: str, conn: Connection) -> T:
    """
    Create an artist and persist it to the database.

    :param name: The name of the artist.
    :param conn: A connection to the database.
    :return: The newly created artist.
    :raises Duplicate: If an artist with the same name already exists. The duplicate
                       artist is passed as the ``entity`` argument.
    """
    if art := from_name(name, conn):
        raise Duplicate(f'Artist "{name}" already exists.', art)

    cursor = conn.execute(
        "INSERT INTO music__artists (name) VALUES (?)",
        (name,),
    )

    logger.info(f'Created artist "{name}" with ID {cursor.lastrowid}')

    art = from_id(cursor.lastrowid, conn)
    assert art is not None
    return art


def update(art: T, conn: Connection, **changes) -> T:
    """
    Update an artist and persist changes to the database. To update a value, pass it
    in as a keyword argument. To keep the original value, do not pass in a keyword
    argument.

    :param art: The artist to update.
    :param conn: A connection to the database.
    :param name: New artist name.
    :type  name: :py:obj:`str`
    :return: The updated artist.
    :raises Duplicate: If an artist already exists with the new name.
    """
    if "name" in changes and (dupl := from_name(changes["name"], conn)) and dupl != art:
        raise Duplicate(f'Artist "{changes["name"]}" already exists.', dupl)

    conn.execute(
        """
        UPDATE music__artists
        SET name = ?
        WHERE id = ?
        """,
        (
            changes.get("name", art.name),
            art.id,
        ),
    )

    logger.info(f"Updated artist {art.id} with {changes}.")

    return update_dataclass(art, **changes)


def starred(art: T, user_id: int, conn: Connection) -> bool:
    """
    Return whether this artist is starred by the passed-in user.

    :param art: The provided artist.
    :param user_id: The passed-in user's ID.
    :param conn: A connection to the database.
    :return: Whether the artist is starred by the user.
    """
    cursor = conn.execute(
        """
        SELECT 1 FROM music__artists_starred
        WHERE user_id = ? AND artist_id = ?
        """,
        (user_id, art.id),
    )

    return cursor.fetchone() is not None


def star(art: T, user_id: int, conn: Connection) -> None:
    """
    Star the artist for the passed-in user.

    :param art:
    :param user_id:
    :param conn:
    """
    # If already starred, do nothing.
    if starred(art, user_id, conn):
        return

    conn.execute(
        "INSERT INTO music__artists_starred (user_id, artist_id) VALUES (?, ?)",
        (user_id, art.id),
    )


def unstar(art: T, user_id: int, conn: Connection) -> None:
    """
    Unstar the artist for the passed-in user.

    :param art:
    :param user_id:
    :param conn:
    """
    # If not starred, do nothing.
    if not starred(art, user_id, conn):
        return

    conn.execute(
        """
        DELETE FROM music__artists_starred
        WHERE user_id = ? AND artist_id = ?
        """,
        (user_id, art.id),
    )


def releases(art: T, conn: Connection) -> list[release.T]:
    """
    Get the releases of an artist.

    :param art: The artist whose releases we want to get.
    :param conn: A connection to the database.
    :return: A list of releases of the artist.
    """
    releases = release.search(artist_ids=[art.id], conn=conn)
    logger.debug(f"Fetched the releases of artist {art.id}.")
    return releases


def top_genres(art: T, conn: Connection, *, num_genres: int = 5) -> list[dict]:
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

    The field ``num_releases`` in the genre collections is set to ``None``.

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
