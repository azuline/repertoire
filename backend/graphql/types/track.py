from typing import Any, Dict, List

from ariadne import ObjectType, UnionType
from graphql.type import GraphQLResolveInfo

from backend.enums import GraphQLError
from backend.graphql.query import query
from backend.graphql.types.error import Error
from backend.graphql.util import require_auth, resolve_result
from backend.library import release, track

gql_track = ObjectType("Track")
gql_track_result = UnionType("TrackResult", resolve_result("Track"))


@query.field("track")
@require_auth
def resolve_track(obj: Any, info: GraphQLResolveInfo, id: int) -> track.T:
    if trk := track.from_id(id, info.context.db):
        return trk

    return Error(GraphQLError.NOT_FOUND, f"Track {id} not found.")


@gql_track.field("release")
def resolve_tracks(obj: track.T, info: GraphQLResolveInfo) -> release.T:
    return release.from_id(obj.release_id, info.context.db)


@gql_track.field("artists")
def resolve_top_genres(obj: track.T, info: GraphQLResolveInfo) -> List[Dict]:
    return track.artists(obj, info.context.db)
