import flask

from src.enums import CollectionType
from src.util import database, to_posix_time
from src.web.util import check_auth

bp = flask.Blueprint("collections", __name__)


@bp.route("/collections", methods=["GET"])
@check_auth
def get_collections():
    """Returns the stored collections."""
    with database() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT
                cols.id,
                cols.name,
                cols.favorite,
                cols.type,
                COUNT(colsrls.release_id) AS num_releases,
                MAX(colsrls.added_on) AS last_updated_on
            FROM music__collections AS cols
            LEFT JOIN music__collections_releases AS colsrls
                ON colsrls.collection_id = cols.id
            GROUP BY cols.id
            """
        )

        collections = [
            {
                "id": row["id"],
                "name": row["name"],
                "favorite": row["favorite"],
                "type": row["type"],
                "numReleases": row["num_releases"],
                "lastUpdatedOn": to_posix_time(row["last_updated_on"]),
            }
            for row in cursor.fetchall()
        ]

        # Fetch the top genres for each collection.
        for collection in collections:
            cursor.execute(
                """
                SELECT
                    genres.id,
                    genres.name,
                    COUNT(genresrls.release_id) AS num_matches
                FROM music__collections AS genres
                LEFT JOIN music__collections_releases AS genresrls
                    ON genresrls.collection_id = genres.id
                LEFT JOIN music__collections_releases AS colsrls
                    ON colsrls.release_id = genresrls.release_id
                WHERE colsrls.collection_id = ? AND genres.type = ?
                GROUP BY genres.id
                ORDER BY num_matches DESC
                LIMIT 5
                """,
                (
                    collection["id"],
                    CollectionType.GENRE.value,
                ),
            )

            collection["topGenres"] = [
                {"id": row["id"], "name": row["name"], "numMatches": row["num_matches"]}
                for row in cursor.fetchall()
            ]

        cursor.close()

    return flask.jsonify(collections)
