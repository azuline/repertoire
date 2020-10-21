from dataclasses import dataclass
from sqlite3 import Cursor

import flask
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Blueprint, Request, Response

from backend.graphql import schema
from backend.lib import user
from backend.web.util import check_auth

bp = Blueprint("graphql", __name__, url_prefix="/graphql")


@dataclass
class GraphQLContext:
    user: user.T
    db: Cursor
    request: Request


@bp.route("", methods=["GET"])
def graphql_playground() -> Response:
    """
    **Developer endpoint.**

    Return the GraphQL playground if we are in debug mode, otherwise
    raise a 404.
    """
    if not flask.current_app.debug:
        flask.abort(404)

    return PLAYGROUND_HTML, 200


@bp.route("", methods=["POST"])
@check_auth(abort_if_unauthorized=False)
def graphql_server() -> Response:
    """
    Execute and return a GraphQL API request.

    :return: A response to the request.
    """
    success, result = graphql_sync(
        schema=schema,
        data=flask.request.get_json(),
        context_value=GraphQLContext(
            user=getattr(flask.g, "user", None),
            db=flask.g.db,
            request=flask.request,
        ),
        debug=flask.current_app.debug,
    )

    status_code = 200 if success else 400
    return flask.jsonify(result), status_code
