from typing import Any, Optional

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.enums import CollectionType
from src.errors import NotFound
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.util import commit
from src.library import collection, release
from src.library import user as libuser
from src.util import convert_keys_case, del_pagination_keys

gql_collection = ObjectType("Collection")
gql_collections = ObjectType("Collections")


@query.field("collection")
def resolve_collection(obj: Any, info: GraphQLResolveInfo, id: int) -> collection.T:
    if col := collection.from_id(id, info.context.db):
        return col

    raise NotFound(f"Collection {id} not found.")


@query.field("collectionFromNameTypeUser")
def resolve_collection_from_name_type_user(
    obj: Any,
    info: GraphQLResolveInfo,
    name: str,
    type: CollectionType,
    user: Optional[int] = None,
) -> collection.T:
    if col := collection.from_name_type_user(name, type, info.context.db, user_id=user):
        return col

    raise NotFound(
        f'Collection "{name}" of type {type.name} and user {user} not found.'
    )


@query.field("collections")
def resolve_collections(obj: Any, info: GraphQLResolveInfo, **kwargs) -> dict:
    kwargs = convert_keys_case(kwargs)
    return {
        "results": collection.search(info.context.db, **kwargs),
        "total": collection.count(info.context.db, **del_pagination_keys(kwargs)),
    }


@gql_collection.field("starred")
def resolve_starred(obj: collection.T, info: GraphQLResolveInfo) -> bool:
    return collection.starred(obj, info.context.user.id, info.context.db)


@gql_collection.field("releases")
def resolve_releases(obj: collection.T, info: GraphQLResolveInfo) -> list[release.T]:
    return collection.releases(obj, info.context.db)


@gql_collection.field("topGenres")
def resolve_top_genres(obj: collection.T, info: GraphQLResolveInfo) -> list[dict]:
    return collection.top_genres(obj, info.context.db)


@gql_collection.field("imageId")
def resolve_image_id(obj: collection.T, info: GraphQLResolveInfo) -> Optional[int]:
    if img := collection.image(obj, info.context.db):
        return img.id

    return None


@gql_collection.field("user")
def resolve_user(obj: collection.T, info: GraphQLResolveInfo) -> Optional[libuser.T]:
    if obj.user_id is None:
        return None

    return libuser.from_id(obj.user_id, info.context.db)


@mutation.field("createCollection")
@commit
def resolve_create_collection(
    _,
    info: GraphQLResolveInfo,
    name: str,
    type: CollectionType,
) -> collection.T:
    return collection.create(name, type, info.context.db)


@mutation.field("updateCollection")
@commit
def resolve_update_collection(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> collection.T:
    col = collection.from_id(id, info.context.db)
    if not col:
        raise NotFound(f"Collection {id} does not exist.")

    return collection.update(col, info.context.db, **convert_keys_case(changes))


@mutation.field("starCollection")
@commit
def resolve_star_collection(_, info: GraphQLResolveInfo, id: int) -> collection.T:
    col = collection.from_id(id, info.context.db)
    if not col:
        raise NotFound(f"Collection {id} does not exist.")

    collection.star(col, info.context.user.id, info.context.db)
    return col


@mutation.field("unstarCollection")
@commit
def resolve_unstar_collection(_, info: GraphQLResolveInfo, id: int) -> collection.T:
    col = collection.from_id(id, info.context.db)
    if not col:
        raise NotFound(f"Collection {id} does not exist.")

    collection.unstar(col, info.context.user.id, info.context.db)
    return col


@mutation.field("addReleaseToCollection")
@commit
def resolve_add_release_to_collection(
    _,
    info: GraphQLResolveInfo,
    collectionId: int,
    releaseId: int,
) -> dict:
    col = collection.from_id(collectionId, info.context.db)
    if not col:
        raise NotFound(f"Collection {collectionId} does not exist.")

    col = collection.add_release(col, releaseId, info.context.db)
    rls = release.from_id(releaseId, info.context.db)

    return {"collection": col, "release": rls}


@mutation.field("delReleaseFromCollection")
@commit
def resolve_del_release_from_collection(
    _,
    info: GraphQLResolveInfo,
    collectionId: int,
    releaseId: int,
) -> dict:
    col = collection.from_id(collectionId, info.context.db)
    if not col:
        raise NotFound(f"Collection {collectionId} does not exist.")

    col = collection.del_release(col, releaseId, info.context.db)
    rls = release.from_id(releaseId, info.context.db)

    return {"collection": col, "release": rls}
