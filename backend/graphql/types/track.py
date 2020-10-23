from typing import Any, Dict, List, Union

from ariadne import ObjectType, UnionType
from graphql.type import GraphQLResolveInfo

from backend.enums import ArtistRole, GraphQLError
from backend.errors import AlreadyExists, DoesNotExist
from backend.graphql.mutation import mutation
from backend.graphql.query import query
from backend.graphql.types.error import Error
from backend.graphql.util import require_auth, resolve_result
from backend.library import artist, release, track
from backend.util import convert_keys_case

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


@mutation.field("updateTrack")
@require_auth
def resolve_update_track(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> Union[track.T, Error]:
    if not (trk := track.from_id(id, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, f"Track {id} does not exist.")

    if "releaseId" in changes:
        changes["release"] = release.from_id(changes["releaseId"], info.context.db)
        if not changes["release"]:
            return Error(GraphQLError.NOT_FOUND, "Release does not exist.")

        del changes["releaseId"]

    return track.update(trk, info.context.db, **convert_keys_case(changes))


@mutation.field("addArtistToTrack")
@require_auth
def resolve_add_artist_to_track(
    _,
    info: GraphQLResolveInfo,
    trackId: int,
    artistId: int,
    role: ArtistRole,
) -> Union[track.T, Error]:
    if not (trk := track.from_id(trackId, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, "Track does not exist.")
    if not (art := artist.from_id(artistId, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, "Artist does not exist.")

    try:
        track.add_artist(trk, art, role, info.context.db)
    except AlreadyExists:
        return Error(GraphQLError.ALREADY_EXISTS, "Artist is already on track.")

    return trk


@mutation.field("delArtistFromTrack")
@require_auth
def resolve_del_artist_from_track(
    _,
    info: GraphQLResolveInfo,
    trackId: int,
    artistId: int,
    role: ArtistRole,
) -> Union[track.T, Error]:
    if not (trk := track.from_id(trackId, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, "Track does not exist.")
    if not (art := artist.from_id(artistId, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, "Artist does not exist.")

    try:
        track.del_artist(trk, art, role, info.context.db)
    except DoesNotExist:
        return Error(GraphQLError.DOES_NOT_EXIST, "Artist is not on track.")

    return trk
