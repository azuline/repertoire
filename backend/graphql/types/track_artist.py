from typing import Dict

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.enums import ArtistRole
from backend.library import artist

track_artist_resolver = ObjectType("TrackArtist")


@track_artist_resolver.field("role")
def resolve_role(obj: Dict, info: GraphQLResolveInfo) -> ArtistRole:
    return obj["role"]


@track_artist_resolver.field("artist")
def resolve_artist(obj: Dict, info: GraphQLResolveInfo) -> artist.T:
    return obj["artist"]
