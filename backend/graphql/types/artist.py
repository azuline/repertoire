from typing import Any, Dict, List

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.graphql.query import query
from backend.library import artist, release

artist_resolver = ObjectType("Artist")


@query.field("artist")
def resolve_artist(obj: Any, info: GraphQLResolveInfo, id: int) -> artist.T:
    return artist.from_id(id, info.context.db)


@query.field("artistFromName")
def resolve_artist_from_name(obj: Any, info: GraphQLResolveInfo, name: str) -> artist.T:
    return artist.from_name(name, info.context.db)


@artist_resolver.field("releases")
def resolve_releases(obj: artist.T, info: GraphQLResolveInfo) -> List[release.T]:
    return artist.releases(obj, info.context.db)


@artist_resolver.field("topGenres")
def resolve_top_genres(obj: artist.T, info: GraphQLResolveInfo) -> List[Dict]:
    return artist.top_genres(obj, info.context.db)
