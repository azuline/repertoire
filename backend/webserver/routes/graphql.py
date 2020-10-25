from dataclasses import dataclass
from sqlite3 import Cursor

import quart
from ariadne import graphql
from ariadne.constants import PLAYGROUND_HTML
from quart import Blueprint, Request, Response

from backend.graphql import error_formatter, schema
from backend.library import user
from backend.webserver.util import check_auth

bp = Blueprint("graphql", __name__, url_prefix="/graphql")


@dataclass
class GraphQLContext:
    user: user.T
    db: Cursor
    request: Request


@bp.route("", methods=["GET"])
async def graphql_playground() -> Response:
    """
    **Developer endpoint.**

    Return the GraphQL playground if we are in debug mode, otherwise
    raise a 404.
    """
    if not quart.current_app.debug:
        quart.abort(404)

    return PLAYGROUND_HTML, 200


@bp.route("", methods=["POST"])
@check_auth(abort_if_unauthorized=False)
async def graphql_server() -> Response:
    """
    Execute and return a GraphQL API request.

    :return: A response to the request.
    """
    success, result = await graphql(
        schema=schema,
        data=await quart.request.get_json(),
        context_value=GraphQLContext(
            user=getattr(quart.g, "user", None),
            db=quart.g.db,
            request=quart.request,
        ),
        error_formatter=error_formatter,
        debug=quart.current_app.debug,
    )

    status_code = 200 if success else 400
    return quart.jsonify(result), status_code
