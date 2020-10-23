from typing import Dict

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.enums import ArtistRole
from backend.library import artist

gql_track_artist = ObjectType("TrackArtist")


@gql_track_artist.field("role")
def resolve_role(obj: Dict, info: GraphQLResolveInfo) -> ArtistRole:
    return obj["role"]


@gql_track_artist.field("artist")
def resolve_artist(obj: Dict, info: GraphQLResolveInfo) -> artist.T:
    return obj["artist"]
