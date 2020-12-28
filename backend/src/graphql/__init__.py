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
from src.graphql.enums import (
    artist_role_enum,
    collection_type_enum,
    playlist_type_enum,
    release_sort_enum,
    release_type_enum,
)
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.scalars import posix_time_scalar
from src.graphql.types.artist import gql_artist, gql_artists  # type: ignore
from src.graphql.types.collection import gql_collection, gql_collections  # type: ignore
from src.graphql.types.playlist import gql_playlist, gql_playlists  # type: ignore
from src.graphql.types.release import gql_release, gql_releases  # type: ignore
from src.graphql.types.top_genre import gql_top_genre  # type: ignore
from src.graphql.types.track import gql_track  # type: ignore
from src.graphql.types.track_artist import gql_track_artist  # type: ignore
from src.graphql.types.user import gql_token, gql_user  # type: ignore

SCHEMA_PATH = Path(__file__).parent / "schema.graphql"

type_defs = load_schema_from_path(str(SCHEMA_PATH))

resolvers = [
    query,
    mutation,
    gql_artist,
    gql_artists,
    gql_collection,
    gql_collections,
    gql_playlist,
    gql_playlists,
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
    playlist_type_enum,
    snake_case_fallback_resolvers,
]

schema = make_executable_schema(gql(type_defs), *resolvers)


def error_formatter(error: GraphQLError, debug: bool = False) -> Dict:
    lib_error = unwrap_graphql_error(error)

    def enhance_error(error):
        try:
            return dict(
                error,
                message=lib_error.message,
                type=lib_error.__class__.__name__,
            )
        except AttributeError:  # This isn't a lib error but a real error.
            return error

    if debug:  # pragma: no cover
        return enhance_error(format_error(error, debug))

    return enhance_error(error.formatted)
