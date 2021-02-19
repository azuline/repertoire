from typing import Any, Dict

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.errors import NotFound
from src.graphql.mutation import mutation
from src.graphql.util import commit
from src.library import playlist
from src.library import playlist_entry as pentry
from src.library import track

gql_pentry = ObjectType("PlaylistEntry")


@gql_pentry.field("playlist")
def resolve_playlist(obj: pentry.T, info: GraphQLResolveInfo) -> playlist.T:
    return pentry.playlist(obj, info.context.db)


@gql_pentry.field("track")
def resolve_track(obj: pentry.T, info: GraphQLResolveInfo) -> track.T:
    return pentry.track(obj, info.context.db)


@mutation.field("createPlaylistEntry")
@commit
def create_playlist_entry(
    obj: Any,
    info: GraphQLResolveInfo,
    playlistId: int,
    trackId: int,
) -> pentry.T:
    return pentry.create(playlistId, trackId, info.context.db)


@mutation.field("delPlaylistEntry")
@commit
def delete_playlist_entry(
    obj: Any,
    info: GraphQLResolveInfo,
    id: int,
) -> Dict:
    if ety := pentry.from_id(id, info.context.db):
        pentry.delete(ety, info.context.db)
        return {
            "playlist": playlist.from_id(ety.playlist_id, info.context.db),
            "track": track.from_id(ety.track_id, info.context.db),
        }

    raise NotFound(f"Playlist entry {id} does not exist.")


@mutation.field("delPlaylistEntries")
@commit
def delete_playlist_entries(
    obj: Any,
    info: GraphQLResolveInfo,
    playlistId: int,
    trackId: int,
) -> Dict:
    for ety in pentry.from_playlist_and_track(playlistId, trackId, info.context.db):
        pentry.delete(ety, info.context.db)

    ply = playlist.from_id(playlistId, info.context.db)
    if not ply:
        raise NotFound(f"Playlist {playlistId} does not exist.")

    trk = track.from_id(trackId, info.context.db)
    if not trk:
        raise NotFound(f"Track {trackId} does not exist.")

    return {"playlist": ply, "track": trk}


@mutation.field("updatePlaylistEntry")
@commit
def update_playlist_entry(
    obj: Any,
    info: GraphQLResolveInfo,
    id: int,
    position: int,
) -> pentry.T:
    if ety := pentry.from_id(id, info.context.db):
        return pentry.update(ety, position, info.context.db)

    raise NotFound(f"Playlist entry {id} does not exist.")
