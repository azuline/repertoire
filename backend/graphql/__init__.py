from pathlib import Path

from ariadne import (
    gql,
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)

from backend.graphql.enums import (
    artist_role_enum,
    collection_type_enum,
    error_type_enum,
    release_sort_enum,
    release_type_enum,
)
from backend.graphql.mutation import mutation
from backend.graphql.query import query
from backend.graphql.scalars import posix_time_scalar
from backend.graphql.types.artist import (
    gql_artist,
    gql_artist_result,
    gql_artists,
    gql_artists_result,
)
from backend.graphql.types.collection import (
    gql_collection,
    gql_collection_result,
    gql_collections,
    gql_collections_result,
)
from backend.graphql.types.error import gql_error
from backend.graphql.types.release import (
    gql_release,
    gql_release_result,
    gql_releases,
    gql_releases_result,
)
from backend.graphql.types.top_genre import gql_top_genre
from backend.graphql.types.track import gql_track, gql_track_result
from backend.graphql.types.track_artist import gql_track_artist
from backend.graphql.types.user import gql_user, gql_user_result

SCHEMA_PATH = Path(__file__).parent / "schema.graphql"

type_defs = load_schema_from_path(SCHEMA_PATH)

resolvers = [
    query,
    mutation,
    gql_artist,
    gql_artist_result,
    gql_artists,
    gql_artists_result,
    gql_collection,
    gql_collection_result,
    gql_collections,
    gql_collections_result,
    gql_error,
    gql_release,
    gql_release_result,
    gql_releases,
    gql_releases_result,
    gql_top_genre,
    gql_track,
    gql_track_artist,
    gql_track_result,
    gql_user,
    gql_user_result,
    posix_time_scalar,
    artist_role_enum,
    collection_type_enum,
    error_type_enum,
    release_sort_enum,
    release_type_enum,
    snake_case_fallback_resolvers,
]

schema = make_executable_schema(gql(type_defs), *resolvers)
