from typing import Any

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.graphql.mutation import mutation
from backend.graphql.query import query
from backend.graphql.util import require_auth
from backend.library import user

gql_user = ObjectType("User")
gql_token = ObjectType("Token")


@query.field("user")
@require_auth
def resolve_user(obj: Any, info: GraphQLResolveInfo) -> user.T:
    return info.context.user


@mutation.field("newToken")
@require_auth
def resolve_new_token(_, info: GraphQLResolveInfo) -> user.T:
    return user.new_token(info.context.user, info.context.db)


@gql_token.field("hex")
@require_auth
def resolve_hex(obj: bytes, info: GraphQLResolveInfo) -> str:
    return obj.hex()
