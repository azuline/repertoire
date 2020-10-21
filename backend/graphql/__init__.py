"""
This module initializes the GraphQL schema by importing every other module in the
package. The `type_defs` attribute of each module is taken, and together they are
compiled into the schema.
"""

from pathlib import Path

from ariadne import (
    gql,
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)

from backend.graphql.query import query
from backend.graphql.scalars import posix_time_scalar
from backend.graphql.user import user_resolver

SCHEMA_PATH = Path(__file__).parent / "schema.graphql"

type_defs = load_schema_from_path(SCHEMA_PATH)

resolvers = [
    query,
    user_resolver,
    posix_time_scalar,
    snake_case_fallback_resolvers,
]

schema = make_executable_schema(gql(type_defs), *resolvers)
