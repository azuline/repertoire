from typing import Any, Optional

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.enums import PlaylistType
from src.errors import NotFound
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.util import commit
from src.library import playlist
from src.library import playlist_entry as pentry
from src.library import user as libuser
from src.util import convert_keys_case, del_pagination_keys

gql_playlist = ObjectType("Playlist")
gql_playlists = ObjectType("Playlists")


@query.field("playlist")
def resolve_playlist(obj: Any, info: GraphQLResolveInfo, id: int) -> playlist.T:
    if ply := playlist.from_id(id, info.context.db):
        return ply

    raise NotFound(f"Playlist {id} not found.")


@query.field("playlistFromNameTypeUser")
def resolve_playlist_from_name_type_user(
    obj: Any,
    info: GraphQLResolveInfo,
    name: str,
    type: PlaylistType,
    user: int,
) -> playlist.T:
    if ply := playlist.from_name_type_user(name, type, info.context.db, user_id=user):
        return ply

    raise NotFound(f'Playlist "{name}" of type {type.name} and user {user} not found.')


@query.field("playlists")
def resolve_playlists(obj: Any, info: GraphQLResolveInfo, **kwargs) -> dict:
    kwargs = convert_keys_case(kwargs)
    return {
        "results": playlist.search(info.context.db, **kwargs),
        "total": playlist.count(info.context.db, **del_pagination_keys(kwargs)),
    }


@gql_playlist.field("entries")
def resolve_entries(obj: playlist.T, info: GraphQLResolveInfo) -> list[pentry.T]:
    return playlist.entries(obj, info.context.db)


@gql_playlist.field("topGenres")
def resolve_top_genres(obj: playlist.T, info: GraphQLResolveInfo) -> list[dict]:
    return playlist.top_genres(obj, info.context.db)


@gql_playlist.field("imageId")
def resolve_image_id(obj: playlist.T, info: GraphQLResolveInfo) -> Optional[int]:
    if img := playlist.image(obj, info.context.db):
        return img.id

    return None


@gql_playlist.field("user")
def resolve_user(obj: playlist.T, info: GraphQLResolveInfo) -> Optional[libuser.T]:
    if obj.user_id is None:
        return None

    return libuser.from_id(obj.user_id, info.context.db)


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
