from typing import Any, Dict, List

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.enums import CollectionType
from backend.graphql.query import query
from backend.library import collection, release

collection_resolver = ObjectType("Collection")


@query.field("collection")
def resolve_collection(obj: Any, info: GraphQLResolveInfo, id: int) -> collection.T:
    return collection.from_id(id, info.context.db)


@query.field("collectionFromNameAndType")
def resolve_collection_from_name_and_type(
    obj: Any,
    info: GraphQLResolveInfo,
    name: str,
    type: CollectionType,
) -> collection.T:
    return collection.from_name_and_type(name, type, info.context.db)


@collection_resolver.field("releases")
def resolve_releases(obj: collection.T, info: GraphQLResolveInfo) -> List[release.T]:
    return collection.releases(obj, info.context.db)


@collection_resolver.field("topGenres")
def resolve_top_genres(obj: collection.T, info: GraphQLResolveInfo) -> List[Dict]:
    return collection.top_genres(obj, info.context.db)
