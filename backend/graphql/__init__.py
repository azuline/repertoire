from pathlib import Path
from typing import Dict

from ariadne import (
    format_error,
    gql,
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
    unwrap_graphql_error,
)
from graphql import GraphQLError

from backend.graphql.enums import (
    artist_role_enum,
    collection_type_enum,
    release_sort_enum,
    release_type_enum,
)
from backend.graphql.mutation import mutation
from backend.graphql.query import query
from backend.graphql.scalars import posix_time_scalar
from backend.graphql.types.artist import gql_artist, gql_artists
from backend.graphql.types.collection import gql_collection, gql_collections
from backend.graphql.types.release import gql_release, gql_releases
from backend.graphql.types.top_genre import gql_top_genre
from backend.graphql.types.track import gql_track
from backend.graphql.types.track_artist import gql_track_artist
from backend.graphql.types.user import gql_token, gql_user

SCHEMA_PATH = Path(__file__).parent / "schema.graphql"

type_defs = load_schema_from_path(SCHEMA_PATH)

resolvers = [
    query,
    mutation,
    gql_artist,
    gql_artists,
    gql_collection,
    gql_collections,
    gql_release,
    gql_releases,
    gql_token,
    gql_top_genre,
    gql_track,
    gql_track_artist,
    gql_user,
    posix_time_scalar,
    artist_role_enum,
    collection_type_enum,
    release_sort_enum,
    release_type_enum,
    snake_case_fallback_resolvers,
]

schema = make_executable_schema(gql(type_defs), *resolvers)


def error_formatter(error: GraphQLError, debug: bool = False) -> Dict:
    if debug:
        return format_error(error, debug)

    lib_error = unwrap_graphql_error(error)

    return dict(
        error.formatted,
        message=lib_error.message,
        type=lib_error.__class__.__name__,
    )
