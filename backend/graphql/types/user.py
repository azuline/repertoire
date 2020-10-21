from typing import Any

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.graphql.query import query
from backend.library import user

user_resolver = ObjectType("User")


@query.field("user")
def resolve_user(obj: Any, info: GraphQLResolveInfo) -> user.T:
    return info.context.user
