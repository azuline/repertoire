from typing import Any

from ariadne import ObjectType, UnionType
from graphql.type import GraphQLResolveInfo

from backend.graphql.query import query
from backend.graphql.util import require_auth, resolve_result
from backend.library import user

gql_user = ObjectType("User")
gql_user_result = UnionType("UserResult", resolve_result("User"))


@query.field("user")
@require_auth
def resolve_user(obj: Any, info: GraphQLResolveInfo) -> user.T:
    return info.context.user
