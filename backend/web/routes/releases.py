import sqlite3
from typing import Dict, List

import flask
from unidecode import unidecode
from voluptuous import Required, Schema

from backend.util import database, strip_punctuation, to_posix_time
from backend.web.util import check_auth, validate_data

bp = flask.Blueprint("releases", __name__)

SORT_OPTIONS = {
    "recentlyAdded": "rls.added_on",
    "title": "rls.title",
    "year": "rls.release_year",
    "random": "RANDOM()",
}


def SortOption(value):
    """Voluptuous custom schema validator."""
    try:
        return SORT_OPTIONS[value]
    except KeyError:
        raise ValueError


@bp.route("/api/releases", methods=["GET"])
@check_auth
@validate_data(
    Schema(
        {
            "search": str,
            "collections": [int],
            "page": int,
            "limit": int,
            Required("sort", default="recentlyAdded"): SortOption,
        }
    )
)
def get_releases(
    search: str = "", collections: List[int] = [], page: int = 1, offset: int = 40
):
    """Returns the stored releases."""
    with database() as conn:
        cursor = conn.cursor()

        releases = _query_releases(search, collections, page, offset, cursor)

        for release in releases["releases"]:
            release["tracks"] = _fetch_tracks(release, cursor)
            release["artists"] = _fetch_artists(release, cursor)
            release["collections"] = _fetch_collections(release, cursor)

        cursor.close()

    return flask.jsonify(releases)


def _query_releases(
    search: str,
    collections: List[int],
    page: int,
    offset: int,
    sort: str,
    cursor: sqlite3.Cursor,
) -> List[Dict]:
    """
    We query the releases with a search string and a list of collections to
    filter by. To do so, we construct the SQL query and parameter list
    dynamically based on the number of words in the search string and number of
    collections in the collection list.

    Our search string is split up into individual punctuation-less words and
    then used to filter the releases.
    """
    # Variables to hold the filter SQL and params.
    filter_sql = []
    filter_params = []

    # Add the collections to the filter SQL.
    for collection in collections:
        filter_sql.append(
            """
            EXISTS (
                SELECT 1 FROM music__collections_releases
                WHERE release_id = rls.id AND collection_id = ?
            )
            """
        )
        filter_params.append(collection.id)

    # Add the search str to the filter SQL.
    for word in strip_punctuation(search).split(" "):
        if not word:
            continue

        filter_sql.append(
            """
            EXISTS (
                SELECT 1 FROM music__releases_search_index
                WHERE word = ? OR word = ? AND release_id = rls.id
            )
            """
        )
        filter_params.append(word, unidecode(word))

    cursor.execute(
        f"""
        SELECT
            COUNT(1)
        FROM music__releases AS rls
        {"WHERE" + " and ".join(filter_sql) if filter_sql else ""}
        """,
        tuple(filter_params),
    )

    total = cursor.fetchone()[0]

    cursor.execute(
        f"""
        SELECT
            rls.id,
            rls.title,
            rls.release_type,
            rls.release_year,
            rls.added_on
        FROM music__releases AS rls
        {"WHERE" + " and ".join(filter_sql) if filter_sql else ""}
        ORDER BY {sort}
        LIMIT ?
        OFFSET ?
        """,
        (*filter_params, offset, (page - 1) * offset),
    )

    return {
        "total": total,
        "releases": [
            {
                "id": row["id"],
                "title": row["title"],
                "releaseType": row["release_type"],
                "year": row["release_year"],
                "addedOn": to_posix_time(row["added_on"]),
            }
            for row in cursor.fetchall()
        ],
    }


def _fetch_tracks(release: Dict, cursor: sqlite3.Cursor) -> List[Dict]:
    """
    Fetch all tracks of a release from the database and arrange them in a
    hierarchical disc -> track dictionary structure.
    """
    discs = {}

    cursor.execute(
        """
        SELECT id, title, track_number, disc_number, duration
        FROM music__tracks WHERE release_id = ?
        """,
        (release["id"],),
    )
    tracks = cursor.fetchall()

    for row in tracks:
        disc = discs.setdefault(row["disc_number"], {})

        cursor.execute(
            """
            SELECT
                arts.id,
                arts.name,
                trksarts.role
            FROM music__tracks_artists AS trksarts
            JOIN music__artists AS arts ON arts.id = trksarts.artist_id
            WHERE trksarts.track_id = ?
            """,
            (row["id"],),
        )

        disc[row["track_number"]] = {
            "id": row["id"],
            "title": row["title"],
            "duration": row["duration"],
            "artists": [
                {"id": art_row["id"], "name": art_row["name"], "role": art_row["role"]}
                for art_row in cursor.fetchall()
            ],
        }

    return discs


def _fetch_artists(release: Dict, cursor: sqlite3.Cursor) -> List[Dict]:
    cursor.execute(
        """
        SELECT
            arts.id,
            arts.name
        FROM music__releases_artists AS rlsarts
        JOIN music__artists AS arts ON arts.id = rlsarts.artist_id
        WHERE rlsarts.release_id = ?
        """,
        (release["id"],),
    )

    return [{"id": row["id"], "name": row["name"]} for row in cursor.fetchall()]


def _fetch_collections(release: Dict, cursor: sqlite3.Cursor) -> List[Dict]:
    cursor.execute(
        """
        SELECT
            cols.id,
            cols.name,
            cols.type
        FROM music__collections AS cols
        JOIN music__collections_releases AS colsrls
            ON colsrls.collection_id = cols.id
        WHERE colsrls.release_id = ?
        """,
        (release["id"],),
    )

    return [
        {"id": row["id"], "name": row["name"], "type": row["type"]}
        for row in cursor.fetchall()
    ]
