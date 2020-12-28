from typing import Any, Dict, List, Optional

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.enums import PlaylistType
from src.errors import NotFound
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.util import commit
from src.library import playlist, track
from src.util import convert_keys_case

gql_playlist = ObjectType("Playlist")
gql_playlists = ObjectType("Playlists")


@query.field("playlist")
def resolve_playlist(obj: Any, info: GraphQLResolveInfo, id: int) -> playlist.T:
    if ply := playlist.from_id(id, info.context.db):
        return ply

    raise NotFound(f"Playlist {id} not found.")


@query.field("playlistFromNameAndType")
def resolve_playlist_from_name_and_type(
    obj: Any,
    info: GraphQLResolveInfo,
    name: str,
    type: PlaylistType,
) -> playlist.T:
    if ply := playlist.from_name_and_type(name, type, info.context.db):
        return ply

    raise NotFound(f'Playlist "{name}" of type {type.name} not found.')


@query.field("playlists")
def resolve_playlists(
    obj: Any,
    info: GraphQLResolveInfo,
    types: List[PlaylistType] = [],
) -> Dict:
    return {"results": playlist.all(info.context.db, types=types)}


@gql_playlist.field("tracks")
def resolve_tracks(obj: playlist.T, info: GraphQLResolveInfo) -> List[track.T]:
    return playlist.tracks(obj, info.context.db)


@gql_playlist.field("topGenres")
def resolve_top_genres(obj: playlist.T, info: GraphQLResolveInfo) -> List[Dict]:
    return playlist.top_genres(obj, info.context.db)


@gql_playlist.field("imageId")
def resolve_image_id(obj: playlist.T, info: GraphQLResolveInfo) -> Optional[int]:
    if img := playlist.image(obj, info.context.db):
        return img.id

    return None


@mutation.field("createPlaylist")
@commit
def resolve_create_playlist(
    _,
    info: GraphQLResolveInfo,
    name: str,
    type: PlaylistType,
    starred: bool = False,
) -> playlist.T:
    return playlist.create(name, type, info.context.db, starred=starred)


@mutation.field("updatePlaylist")
@commit
def resolve_update_playlist(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> playlist.T:
    if not (ply := playlist.from_id(id, info.context.db)):
        raise NotFound(f"Playlist {id} does not exist.")

    return playlist.update(ply, info.context.db, **convert_keys_case(changes))


@mutation.field("addTrackToPlaylist")
@commit
def resolve_add_track_to_playlist(
    _,
    info: GraphQLResolveInfo,
    playlistId: int,
    trackId: int,
) -> Dict:
    if not (ply := playlist.from_id(playlistId, info.context.db)):
        raise NotFound(f"Playlist {playlistId} does not exist.")

    ply = playlist.add_track(ply, trackId, info.context.db)
    trk = track.from_id(trackId, info.context.db)

    return {"playlist": ply, "track": trk}


@mutation.field("delTrackFromPlaylist")
@commit
def resolve_del_track_from_playlist(
    _,
    info: GraphQLResolveInfo,
    playlistId: int,
    trackId: int,
) -> Dict:
    if not (ply := playlist.from_id(playlistId, info.context.db)):
        raise NotFound(f"Playlist {playlistId} does not exist.")

    ply = playlist.del_track(ply, trackId, info.context.db)
    trk = track.from_id(trackId, info.context.db)

    return {"playlist": ply, "track": trk}
