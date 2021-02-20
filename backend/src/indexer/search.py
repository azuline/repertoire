import logging
from sqlite3 import Connection, Row
from typing import List, Optional, Set

from unidecode import unidecode

from src.util import database, strip_punctuation

logger = logging.getLogger(__name__)


def build_search_index() -> None:
    """
    Build the (shoddy) search index for releases.

    Fetch the words associated with the release, its artists, and its tracks. Associate
    a normalized and non-normalized form of each word with the release in the database.
    """
    logger.info("Rebuilding search index...")

    with database() as conn:
        # Clear the pre-existing search indx.
        conn.execute("DELETE FROM music__releases_search_index")

        for rls in _get_releases_to_index(conn):
            # Accumulate the strings whose words we will enter for this release.
            strings_to_use = [rls["title"], rls["artists"]]

            # For each track, extend our list of words with its words.
            for trk in _get_tracks_of_release(rls["id"], conn):
                strings_to_use.extend([trk["title"], trk["artists"]])

            # Compile the words we need (as the union of words of all our strings).
            words = set.union(*[_words_from_string(s) for s in strings_to_use])

            # Insert each word into the database with the release id.
            for word in words:
                conn.execute(
                    """
                    INSERT INTO music__releases_search_index (release_id, word)
                    VALUES (?, ?)
                    """,
                    (rls["id"], word),
                )

        conn.commit()


def _get_releases_to_index(conn: Connection) -> List[Row]:
    """
    Get a list of releases in the database along with a space-delimited list of artist
    names that are associated with the release.

    :param conn: A connection to the database.
    :return: A list of queried database rows.
    """
    cursor = conn.execute(
        """
            SELECT
                rls.id,
                rls.title,
                (
                    SELECT GROUP_CONCAT(arts.name, " ")
                    FROM music__artists AS arts
                    JOIN music__releases_artists AS rlsarts
                        ON rlsarts.artist_id = arts.id
                    WHERE rlsarts.release_id = rls.id
                ) AS artists
            FROM music__releases AS rls
            """
    )
    return cursor.fetchall()


def _get_tracks_of_release(rls_id: int, conn: Connection) -> List[Row]:
    """
    For a given release, get a list of its tracks along with a space-delimited list of
    artist names that are associated with the track.

    :param rls_id: The release id whose tracks we are fetching.
    :param conn: A connection to the database.
    :return: A list of queried database rows.
    """
    cursor = conn.execute(
        """
        SELECT
            trks.title,
            (
                SELECT GROUP_CONCAT(arts.name, " ")
                FROM music__artists AS arts
                JOIN music__tracks_artists AS trksarts
                    ON trksarts.artist_id = arts.id
                WHERE trksarts.track_id = trks.id
            ) AS artists
        FROM music__tracks AS trks
        WHERE trks.release_id = ?
        """,
        (rls_id,),
    )
    return cursor.fetchall()


def _words_from_string(string: Optional[str]) -> Set[str]:
    """
    Return a set containing the normalized and unnormalized form of each word in
    ``string``. Ignores punctuation.

    :param string: The string to fetch words from.
    :return: Set of normalized and unnormalized forms of each word in ``string``.
    """
    if not string:
        return set()

    raw_words = {w for w in strip_punctuation(string).split(" ") if w}
    return raw_words | {unidecode(w) for w in raw_words}
