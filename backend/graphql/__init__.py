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
    release_sort_enum,
    release_type_enum,
)
from backend.graphql.query import query
from backend.graphql.scalars import posix_time_scalar
from backend.graphql.types.artist import artist_resolver
from backend.graphql.types.collection import collection_resolver
from backend.graphql.types.release import release_resolver
from backend.graphql.types.top_genre import top_genre_resolver
from backend.graphql.types.track import track_resolver
from backend.graphql.types.track_artist import track_artist_resolver
from backend.graphql.types.user import user_resolver

SCHEMA_PATH = Path(__file__).parent / "schema.graphql"

type_defs = load_schema_from_path(SCHEMA_PATH)

resolvers = [
    query,
    artist_resolver,
    collection_resolver,
    release_resolver,
    top_genre_resolver,
    track_resolver,
    track_artist_resolver,
    user_resolver,
    posix_time_scalar,
    artist_role_enum,
    collection_type_enum,
    release_sort_enum,
    release_type_enum,
    snake_case_fallback_resolvers,
]

schema = make_executable_schema(gql(type_defs), *resolvers)
