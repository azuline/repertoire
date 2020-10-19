import logging

import click
from unidecode import unidecode

from backend.util import database, strip_punctuation

logger = logging.getLogger(__name__)


def build_search_index():
    """
    Build the (shoddy) search index for releases.

    Insert a normalized and non-normalized form of each word into the database.
    """
    with database() as conn:
        logger.info("Rebuilding search index...")
        click.echo("Rebuilding search index...")

        cursor = conn.cursor()
        cursor.execute("""DELETE FROM music__releases_search_index""")

        cursor.execute(
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

        releases = cursor.fetchall()

        logger.debug(f"Found {len(releases)} releases to index.")

        for rls in releases:
            words = set()

            # Add the words from the release information.
            for string in [rls["title"], rls["artists"]]:
                if string:
                    string = strip_punctuation(string)
                    words |= {w for w in string.split(" ") if w}
                    words |= {unidecode(w) for w in string.split(" ") if w}

            # Add the words from the track information.
            cursor.execute(
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
                (rls["id"],),
            )

            for trk in cursor.fetchall():
                for string in [trk["title"], trk["artists"]]:
                    if string:
                        string = strip_punctuation(string)
                        words |= {w for w in string.split(" ") if w}
                        words |= {unidecode(w) for w in string.split(" ") if w}

            for word in words:
                cursor.execute(
                    """
                    INSERT INTO music__releases_search_index (release_id, word)
                    VALUES (?, ?)
                    """,
                    (rls["id"], word),
                )
            conn.commit()
