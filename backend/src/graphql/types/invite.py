from typing import Any, Optional

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.errors import NotFound
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.util import commit
from src.library import invite, user
from src.util import convert_keys_case, del_pagination_keys

gql_invite = ObjectType("Invite")
gql_invites = ObjectType("Invites")


@query.field("invite")
def resolve_invite(_: Any, info: GraphQLResolveInfo, id: int) -> invite.T:
    if inv := invite.from_id(id, info.context.db):
        return inv

    raise NotFound(f"Invite {id} does not exist.")


@query.field("invites")
def resolve_invites(_: Any, info: GraphQLResolveInfo, **kwargs) -> dict:
    kwargs = convert_keys_case(kwargs)
    return {
        "results": invite.search(info.context.db, **kwargs),
        "total": invite.count(info.context.db, **del_pagination_keys(kwargs)),
    }


@gql_invite.field("code")
def resolve_releases(obj: invite.T, _: GraphQLResolveInfo) -> str:
    return obj.code.hex()


@gql_invite.field("createdBy")
def resolve_created_by(obj: invite.T, info: GraphQLResolveInfo) -> user.T:
    usr = user.from_id(obj.created_by, info.context.db)
    assert usr is not None
    return usr


@gql_invite.field("usedBy")
def resolve_used_by(obj: invite.T, info: GraphQLResolveInfo) -> Optional[user.T]:
    return user.from_id(obj.used_by, info.context.db) if obj.used_by else None


@mutation.field("createInvite")
@commit
def resolve_create_invite(_, info: GraphQLResolveInfo) -> invite.T:
    return invite.create(info.context.user, info.context.db)
