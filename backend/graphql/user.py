from typing import Any

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.graphql.query import query

user_resolver = ObjectType("User")


@query.field("user")
def resolve_user(obj: Any, info: GraphQLResolveInfo):
    return info.context.user
