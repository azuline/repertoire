from typing import Any, Dict, List

from ariadne import ObjectType
from graphql.type import GraphQLResolveInfo

from backend.graphql.query import query
from backend.library import release, track

track_resolver = ObjectType("Track")


@query.field("track")
def resolve_track(obj: Any, info: GraphQLResolveInfo, id: int) -> track.T:
    return track.from_id(id, info.context.db)


@track_resolver.field("release")
def resolve_tracks(obj: track.T, info: GraphQLResolveInfo) -> release.T:
    return release.from_id(obj.release_id, info.context.db)


@track_resolver.field("artists")
def resolve_top_genres(obj: track.T, info: GraphQLResolveInfo) -> List[Dict]:
    return track.artists(obj, info.context.db)
