from typing import Any, Optional

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.util import commit
from src.library import user, collection, playlist

gql_user = ObjectType("User")
gql_token = ObjectType("Token")


@query.field("user")
def resolve_user(_: Any, info: GraphQLResolveInfo) -> user.T:
    return info.context.user


@gql_user.field("inboxCollectionId")
def resolve_inbox_col_id(_: Any, info: GraphQLResolveInfo) -> int:
    return collection.inbox_of(info.context.user.id, info.context.db).id


@gql_user.field("favoritesCollectionId")
def resolve_favorites_col_id(_: Any, info: GraphQLResolveInfo) -> int:
    return collection.favorites_of(info.context.user.id, info.context.db).id


@gql_user.field("favoritesPlaylistId")
def resolve_favorites_ply_id(_: Any, info: GraphQLResolveInfo) -> int:
    return playlist.favorites_of(info.context.user.id, info.context.db).id


@mutation.field("updateUser")
@commit
def resolve_update_user(
    _,
    info: GraphQLResolveInfo,
    nickname: Optional[str],
) -> user.T:
    return user.update(
        info.context.user,
        info.context.db,
        nickname=nickname,
    )


@mutation.field("newToken")
@commit
def resolve_new_token(_, info: GraphQLResolveInfo) -> bytes:
    return user.new_token(info.context.user, info.context.db)


@gql_token.field("hex")
def resolve_hex(obj: bytes, _: GraphQLResolveInfo) -> str:
    return obj.hex()
