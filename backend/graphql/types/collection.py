from typing import Any, Dict, List

from ariadne import ObjectType, UnionType
from graphql.type import GraphQLResolveInfo

from backend.enums import CollectionType, GraphQLError
from backend.graphql.query import query
from backend.graphql.types.error import Error
from backend.graphql.util import require_auth, resolve_result
from backend.library import collection, release

gql_collection = ObjectType("Collection")
gql_collection_result = UnionType("CollectionResult", resolve_result("Collection"))


@query.field("collection")
@require_auth
def resolve_collection(obj: Any, info: GraphQLResolveInfo, id: int) -> collection.T:
    if col := collection.from_id(id, info.context.db):
        return col

    return Error(GraphQLError.NOT_FOUND, f"Collection {id} not found.")


@query.field("collectionFromNameAndType")
@require_auth
def resolve_collection_from_name_and_type(
    obj: Any,
    info: GraphQLResolveInfo,
    name: str,
    type: CollectionType,
) -> collection.T:
    if col := collection.from_name_and_type(name, type, info.context.db):
        return col

    return Error(
        GraphQLError.NOT_FOUND, f'Collection "{name}" of type {type.name} not found.'
    )


@gql_collection.field("releases")
def resolve_releases(obj: collection.T, info: GraphQLResolveInfo) -> List[release.T]:
    return collection.releases(obj, info.context.db)


@gql_collection.field("topGenres")
def resolve_top_genres(obj: collection.T, info: GraphQLResolveInfo) -> List[Dict]:
    return collection.top_genres(obj, info.context.db)
