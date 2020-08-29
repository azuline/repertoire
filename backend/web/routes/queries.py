import sqlite3
from typing import Dict

import flask
from voluptuous import Schema

from backend.util import database, to_posix_time
from backend.web.util import check_auth, validate_data

bp = flask.Blueprint("queries", __name__)


@bp.route("/api/queries", methods=["GET"])
@check_auth
def get_queries():
    """Returns the stored queries."""
    with database() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT
                id,
                name,
                favorite,
                added_on,
                query
            FROM music__saved_queries
            """
        )

        queries = [_make_query_dict(row) for row in cursor.fetchall()]

        cursor.close()

    return flask.jsonify(queries)


@bp.route("/api/queries", methods=["POST"])
@check_auth
@validate_data(Schema({"name": str, "query": str}))
def add_query(name, query):
    with database() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO music__saved_queries (name, query) VALUES (?, ?)""",
            (name, query),
        )
        conn.commit()

        cursor.execute(
            """
            SELECT
                id,
                name,
                favorite,
                added_on,
                query
            FROM music__saved_queries
            WHERE id = ?
            """,
            (cursor.lastrowid,),
        )

        query = _make_query_dict(cursor.fetchone())

        cursor.close()

    return flask.jsonify(query)


def _make_query_dict(row: sqlite3.Row) -> Dict:
    return {
        "id": row["id"],
        "name": row["name"],
        "favorite": bool(row["favorite"]),
        "addedOn": to_posix_time(row["added_on"]),
        "query": row["query"],
    }
