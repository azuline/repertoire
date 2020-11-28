from typing import Any, Dict, List

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.enums import ArtistRole
from src.errors import NotFound
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.util import commit
from src.library import release, track, artist
from src.util import convert_keys_case

gql_track = ObjectType("Track")


@query.field("track")
def resolve_track(obj: Any, info: GraphQLResolveInfo, id: int) -> track.T:
    if trk := track.from_id(id, info.context.db):
        return trk

    raise NotFound(f"Track {id} not found.")


@gql_track.field("release")
def resolve_tracks(obj: track.T, info: GraphQLResolveInfo) -> release.T:
    return release.from_id(obj.release_id, info.context.db)


@gql_track.field("artists")
def resolve_top_genres(obj: track.T, info: GraphQLResolveInfo) -> List[Dict]:
    return track.artists(obj, info.context.db)


@mutation.field("updateTrack")
@commit
def resolve_update_track(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> track.T:
    if not (trk := track.from_id(id, info.context.db)):
        raise NotFound(f"Track {id} does not exist.")

    return track.update(trk, info.context.db, **convert_keys_case(changes))


@mutation.field("addArtistToTrack")
@commit
def resolve_add_artist_to_track(
    _,
    info: GraphQLResolveInfo,
    trackId: int,
    artistId: int,
    role: ArtistRole,
) -> track.T:
    if not (trk := track.from_id(trackId, info.context.db)):
        raise NotFound("Track does not exist.")

    trk = track.add_artist(trk, artistId, role, info.context.db)
    art = artist.from_id(artistId, info.context.db)
    
    return {"track": trk, "trackArtist": {"role": role, "artist": art}}


@mutation.field("delArtistFromTrack")
@commit
def resolve_del_artist_from_track(
    _,
    info: GraphQLResolveInfo,
    trackId: int,
    artistId: int,
    role: ArtistRole,
) -> track.T:
    if not (trk := track.from_id(trackId, info.context.db)):
        raise NotFound("Track does not exist.")

    trk = track.del_artist(trk, artistId, role, info.context.db)
    art = artist.from_id(artistId, info.context.db)
    
    return {"track": trk, "trackArtist": {"role": role, "artist": art}}
