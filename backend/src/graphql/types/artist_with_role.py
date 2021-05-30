from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.enums import ArtistRole
from src.library import artist

gql_artist_with_role = ObjectType("ArtistWithRole")


@gql_artist_with_role.field("role")
def resolve_role(obj: dict, info: GraphQLResolveInfo) -> ArtistRole:
    return obj["role"]


@gql_artist_with_role.field("artist")
def resolve_artist(obj: dict, info: GraphQLResolveInfo) -> artist.T:
    return obj["artist"]
