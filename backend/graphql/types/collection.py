from typing import Any, Dict, List, Optional, Union

from ariadne import ObjectType, UnionType
from graphql.type import GraphQLResolveInfo

from backend.enums import CollectionType, GraphQLError
from backend.errors import AlreadyExists, DoesNotExist, Duplicate
from backend.graphql.mutation import mutation
from backend.graphql.query import query
from backend.graphql.types.error import Error
from backend.graphql.util import require_auth, resolve_result
from backend.library import collection, release
from backend.util import convert_keys_case

gql_collection = ObjectType("Collection")
gql_collection_result = UnionType("CollectionResult", resolve_result("Collection"))

gql_collections = ObjectType("Collections")
gql_collections_result = UnionType("CollectionsResult", resolve_result("Collections"))


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


@query.field("collections")
@require_auth
def resolve_collections(
    obj: Any,
    info: GraphQLResolveInfo,
    type: Optional[CollectionType] = None,
) -> List[collection.T]:
    return {"results": collection.all(info.context.db, type=type)}


@gql_collection.field("releases")
def resolve_releases(obj: collection.T, info: GraphQLResolveInfo) -> List[release.T]:
    return collection.releases(obj, info.context.db)


@gql_collection.field("topGenres")
def resolve_top_genres(obj: collection.T, info: GraphQLResolveInfo) -> List[Dict]:
    return collection.top_genres(obj, info.context.db)


@mutation.field("createCollection")
@require_auth
def resolve_create_collection(
    _,
    info: GraphQLResolveInfo,
    name: str,
    type: CollectionType,
    favorite: bool = False,
) -> Union[collection.T, Error]:
    try:
        return collection.create(name, type, info.context.db, favorite=favorite)
    except Duplicate:
        return Error(
            GraphQLError.DUPLICATE,
            f'Collection "{name}" of type {type} already exists.',
        )


@mutation.field("updateCollection")
@require_auth
def resolve_update_collection(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> Union[collection.T, Error]:
    if not (col := collection.from_id(id, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, f"Collection {id} does not exist.")

    try:
        return collection.update(col, info.context.db, **convert_keys_case(changes))
    except Duplicate:
        return Error(
            GraphQLError.DUPLICATE,
            f'Collection "{changes["name"]}" conflicts with an existing collection.',
        )


@mutation.field("addReleaseToCollection")
@require_auth
def resolve_add_release_to_collection(
    _,
    info: GraphQLResolveInfo,
    collectionId: int,
    releaseId: int,
) -> Union[collection.T, Error]:
    if not (col := collection.from_id(collectionId, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, "Collection does not exist.")
    if not (rls := release.from_id(releaseId, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, "Release does not exist.")

    try:
        collection.add_release(col, rls, info.context.db)
    except AlreadyExists:
        return Error(GraphQLError.ALREADY_EXISTS, "Release is already in collection.")

    return col


@mutation.field("delReleaseFromCollection")
@require_auth
def resolve_del_release_from_collection(
    _,
    info: GraphQLResolveInfo,
    collectionId: int,
    releaseId: int,
) -> Union[collection.T, Error]:
    if not (col := collection.from_id(collectionId, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, "Collection does not exist.")
    if not (rls := release.from_id(releaseId, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, "Release does not exist.")

    try:
        collection.del_release(col, rls, info.context.db)
    except DoesNotExist:
        return Error(GraphQLError.DOES_NOT_EXIST, "Release is not in collection.")

    return col
