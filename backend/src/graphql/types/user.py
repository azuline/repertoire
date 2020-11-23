from typing import Any

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.util import commit
from src.library import user

gql_user = ObjectType("User")
gql_token = ObjectType("Token")


@query.field("user")
def resolve_user(obj: Any, info: GraphQLResolveInfo) -> user.T:
    return info.context.user


@mutation.field("newToken")
@commit
def resolve_new_token(_, info: GraphQLResolveInfo) -> user.T:
    return user.new_token(info.context.user, info.context.db)


@gql_token.field("hex")
def resolve_hex(obj: bytes, info: GraphQLResolveInfo) -> str:
    return obj.hex()
