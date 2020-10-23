from typing import Any, Dict, List

from ariadne import ObjectType, UnionType
from graphql.type import GraphQLResolveInfo

from backend.enums import GraphQLError
from backend.graphql.query import query
from backend.graphql.types.error import Error
from backend.graphql.util import require_auth, resolve_result
from backend.library import artist, release

gql_artist = ObjectType("Artist")
gql_artist_result = UnionType("ArtistResult", resolve_result("Artist"))


@query.field("artist")
@require_auth
def resolve_artist(obj: Any, info: GraphQLResolveInfo, id: int) -> artist.T:
    if art := artist.from_id(id, info.context.db):
        return art

    return Error(GraphQLError.NOT_FOUND, f"Artist {id} does not exist.")


@query.field("artistFromName")
@require_auth
def resolve_artist_from_name(obj: Any, info: GraphQLResolveInfo, name: str) -> artist.T:
    if art := artist.from_name(name, info.context.db):
        return art

    return Error(GraphQLError.NOT_FOUND, f'Artist "{name}" does not exist.')


@gql_artist.field("releases")
def resolve_releases(obj: artist.T, info: GraphQLResolveInfo) -> List[release.T]:
    return artist.releases(obj, info.context.db)


@gql_artist.field("topGenres")
def resolve_top_genres(obj: artist.T, info: GraphQLResolveInfo) -> List[Dict]:
    return artist.top_genres(obj, info.context.db)
