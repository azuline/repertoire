import flask

from backend.enums import CollectionType
from backend.util import database
from backend.web.util import check_auth

bp = flask.Blueprint("artists", __name__)


@bp.route("/api/artists", methods=["GET"])
@check_auth
def get_artists():
    """Returns the stored artists."""
    with database() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT
                arts.id,
                arts.name,
                arts.favorite,
                COUNT(artsrls.release_id) AS num_releases
            FROM music__artists AS arts
            LEFT JOIN music__releases_artists AS artsrls
                ON artsrls.artist_id = arts.id
            GROUP BY arts.id
            """
        )

        artists = [
            {
                "id": row["id"],
                "name": row["name"],
                "favorite": bool(row["favorite"]),
                "numReleases": row["num_releases"],
            }
            for row in cursor.fetchall()
            if row["num_releases"] > 0
        ]

        # Fetch the top genres for each collection.
        for artist in artists:
            cursor.execute(
                """
                SELECT
                    genres.id,
                    genres.name,
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
                (
                    artist["id"],
                    CollectionType.GENRE.value,
                ),
            )

            artist["topGenres"] = [
                {"id": row["id"], "name": row["name"], "numMatches": row["num_matches"]}
                for row in cursor.fetchall()
            ]

        cursor.close()

    return flask.jsonify(artists)
