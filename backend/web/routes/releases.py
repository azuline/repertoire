from typing import List

import flask
from voluptuous import Coerce, Required, Schema

from backend.util import database
from backend.web.util import check_auth, validate_data
from backend.web.validators import JSONList, SortOption, StringBool

bp = flask.Blueprint("releases", __name__)


@bp.route("/api/releases", methods=["GET"])
@check_auth
@validate_data(
    Schema(
        {
            Required("search", default=""): str,
            Required("collections", default="[]"): JSONList(int),
            Required("artists", default="[]"): JSONList(int),
            Required("page", default=1): Coerce(int),
            Required("perPage", default=50): Coerce(int),
            Required("sort", default="recentlyAdded"): SortOption,
            Required("asc", default="true"): StringBool,
        }
    )
)
def get_releases(
    search: str,
    collections: List[int],
    artists: List[int],
    page: int,
    perPage: int,
    sort: int,
    asc: bool,
):
    """Returns the stored releases."""
    # Small adjustment to asc... we want recently added ascending to show
    # newest first.
    if sort == "rls.added_on":
        asc = not asc

    with database() as conn:
        cursor = conn.cursor()

        # releases = _query_releases(
        #     search, collections, artists, page, perPage, sort, asc, cursor
        # )

        # for release in releases["releases"]:
        #     release["tracks"] = _fetch_tracks(release, cursor)
        #     release["artists"] = _fetch_artists(release, cursor)
        #     release["collections"] = _fetch_collections(release, cursor)

        cursor.close()

    # return flask.jsonify(releases)
