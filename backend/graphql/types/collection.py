from typing import Any, Dict, List, Optional

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.enums import CollectionType
from backend.errors import NotFound
from backend.graphql.mutation import mutation
from backend.graphql.query import query
from backend.graphql.util import require_auth
from backend.library import collection, release
from backend.util import convert_keys_case

gql_collection = ObjectType("Collection")
gql_collections = ObjectType("Collections")


@query.field("collection")
@require_auth
def resolve_collection(obj: Any, info: GraphQLResolveInfo, id: int) -> collection.T:
    if col := collection.from_id(id, info.context.db):
        return col

    raise NotFound(f"Collection {id} not found.")


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

    raise NotFound(f'Collection "{name}" of type {type.name} not found.')


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
) -> collection.T:
    return collection.create(name, type, info.context.db, favorite=favorite)


@mutation.field("updateCollection")
@require_auth
def resolve_update_collection(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> collection.T:
    if not (col := collection.from_id(id, info.context.db)):
        raise NotFound(f"Collection {id} does not exist.")

    return collection.update(col, info.context.db, **convert_keys_case(changes))


@mutation.field("addReleaseToCollection")
@require_auth
def resolve_add_release_to_collection(
    _,
    info: GraphQLResolveInfo,
    collectionId: int,
    releaseId: int,
) -> collection.T:
    if not (col := collection.from_id(collectionId, info.context.db)):
        raise NotFound(f"Collection {collectionId} does not exist.")

    collection.add_release(col, releaseId, info.context.db)
    col.num_releases += 1
    return col


@mutation.field("delReleaseFromCollection")
@require_auth
def resolve_del_release_from_collection(
    _,
    info: GraphQLResolveInfo,
    collectionId: int,
    releaseId: int,
) -> collection.T:
    if not (col := collection.from_id(collectionId, info.context.db)):
        raise NotFound(f"Collection {collectionId} does not exist.")

    collection.del_release(col, releaseId, info.context.db)
    col.num_releases -= 1
    return col
