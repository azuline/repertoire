from __future__ import annotations

from dataclasses import dataclass
from sqlite3 import Connection

import quart
from ariadne import graphql
from ariadne.constants import PLAYGROUND_HTML
from quart import Blueprint, Request, Response

from src.graphql import error_formatter, schema
from src.library import user
from src.webserver.util import check_auth

bp = Blueprint("graphql", __name__, url_prefix="/graphql")


@dataclass
class GraphQLContext:
    user: user.T
    db: Connection
    request: Request


@bp.route("", methods=["GET"])
async def graphql_playground() -> tuple[str, int]:  # pragma: no cover
    """
    **Developer endpoint.**

    Return the GraphQL playground if we are in debug mode, otherwise
    raise a 404.
    """
    if not quart.current_app.debug:
        quart.abort(404)

    return PLAYGROUND_HTML, 200


@bp.route("", methods=["POST"])
@check_auth(csrf=True)
async def graphql_server() -> tuple[Response, int]:
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
            request=quart.request,  # type: ignore
        ),
        error_formatter=error_formatter,
        debug=quart.current_app.debug,
    )

    status_code = 200 if success else 400
    return quart.jsonify(result), status_code
