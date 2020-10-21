from typing import Any, Dict, List

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.enums import CollectionType
from backend.graphql.query import query
from backend.library import release

release_resolver = ObjectType("Release")


@query.field("release")
def resolve_release(obj: Any, info: GraphQLResolveInfo, id: int) -> release.T:
    return release.from_id(id, info.context.db)


@release_resolver.field("artists")
def resolve_releases(obj: release.T, info: GraphQLResolveInfo) -> List[release.T]:
    return release.artists(obj, info.context.db)


@release_resolver.field("tracks")
def resolve_top_genres(obj: release.T, info: GraphQLResolveInfo) -> List[Dict]:
    return release.tracks(obj, info.context.db)


@release_resolver.field("genres")
def resolve_genres(obj: release.T, info: GraphQLResolveInfo) -> List[Dict]:
    return release.collections(obj, info.context.db, type=CollectionType.GENRE)


@release_resolver.field("labels")
def resolve_labels(obj: release.T, info: GraphQLResolveInfo) -> List[Dict]:
    return release.collections(obj, info.context.db, type=CollectionType.LABEL)


@release_resolver.field("collages")
def resolve_collages(obj: release.T, info: GraphQLResolveInfo) -> List[Dict]:
    return release.collections(obj, info.context.db, type=CollectionType.COLLAGE)
