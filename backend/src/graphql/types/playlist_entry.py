from typing import Any

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
) -> playlist.T:
    if ety := pentry.from_id(id, info.context.db):
        pentry.delete(ety, info.context.db)
        return playlist.from_id(ety.playlist_id, info.context.db)

    raise NotFound(f"Playlist entry {id} does not exist.")


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
