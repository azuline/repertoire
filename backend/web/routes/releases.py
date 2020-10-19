from typing import List

import flask
from voluptuous import Coerce, Required, Schema

from backend.enums import ReleaseSort
from backend.lib import artist, collection, release
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
            Required("limit", default=50): Coerce(int),
            Required("sort", default="recentlyAdded"): SortOption,
            Required("asc", default="true"): StringBool,
        }
    )
)
def get_releases(
    search: str,
    collections: List[collection.T],
    artists: List[artist.T],
    page: int,
    limit: int,
    sort: ReleaseSort,
    asc: bool,
):
    """Returns the stored releases."""
    # Small adjustment to asc... we want recently added ascending to show
    # newest first.
    if sort == "rls.added_on":
        asc = not asc

    with database() as conn:
        cursor = conn.cursor()

        total, releases = release.search(
            search=search,
            collections=collections,
            artists=artists,
            page=page,
            limit=limit,
            sort=sort,
            asc=asc,
            cursor=cursor,
        )

        releases_json = []
        for rls in releases:
            rls_json = rls
            rls_json["tracks"] = release.tracks(rls, cursor)
            rls_json["artists"] = release.artists(rls, cursor)
            rls_json["collections"] = release.collections(rls, cursor)

        cursor.close()

    return flask.jsonify({"total": total, "releases": releases_json})
