from typing import Dict

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.enums import ArtistRole
from src.library import artist

gql_track_artist = ObjectType("TrackArtist")


@gql_track_artist.field("role")
def resolve_role(obj: Dict, info: GraphQLResolveInfo) -> ArtistRole:
    return obj["role"]


@gql_track_artist.field("artist")
def resolve_artist(obj: Dict, info: GraphQLResolveInfo) -> artist.T:
    return obj["artist"]
