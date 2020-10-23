from typing import Any, Dict, List, Union

from ariadne import ObjectType, UnionType
from graphql.type import GraphQLResolveInfo

from backend.enums import GraphQLError
from backend.errors import Duplicate
from backend.graphql.mutation import mutation
from backend.graphql.query import query
from backend.graphql.types.error import Error
from backend.graphql.util import require_auth, resolve_result
from backend.library import artist, release
from backend.util import convert_keys_case

gql_artist = ObjectType("Artist")
gql_artist_result = UnionType("ArtistResult", resolve_result("Artist"))

gql_artists = ObjectType("Artists")
gql_artists_result = UnionType("ArtistsResult", resolve_result("Artists"))


@query.field("artist")
@require_auth
def resolve_artist(obj: Any, info: GraphQLResolveInfo, id: int) -> artist.T:
    if art := artist.from_id(id, info.context.db):
        return art

    return Error(GraphQLError.NOT_FOUND, f"Artist {id} does not exist.")


@query.field("artistFromName")
@require_auth
def resolve_artist_from_name(obj: Any, info: GraphQLResolveInfo, name: str) -> artist.T:
    if art := artist.from_name(name, info.context.db):
        return art

    return Error(GraphQLError.NOT_FOUND, f'Artist "{name}" does not exist.')


@query.field("artists")
@require_auth
def resolve_artists(obj: Any, info: GraphQLResolveInfo) -> List[artist.T]:
    return {"results": artist.all(info.context.db)}


@gql_artist.field("releases")
def resolve_releases(obj: artist.T, info: GraphQLResolveInfo) -> List[release.T]:
    return artist.releases(obj, info.context.db)


@gql_artist.field("topGenres")
def resolve_top_genres(obj: artist.T, info: GraphQLResolveInfo) -> List[Dict]:
    return artist.top_genres(obj, info.context.db)


@mutation.field("createArtist")
@require_auth
def resolve_create_artist(
    _,
    info: GraphQLResolveInfo,
    name: str,
    favorite: bool = False,
) -> Union[artist.T, Error]:
    try:
        return artist.create(name, info.context.db, favorite=favorite)
    except Duplicate:
        return Error(GraphQLError.DUPLICATE, f'Artist "{name}" already exists.')


@mutation.field("updateArtist")
@require_auth
def resolve_update_artist(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> Union[artist.T, Error]:
    if not (art := artist.from_id(id, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, f"Artist {id} does not exist.")

    try:
        return artist.update(art, info.context.db, **convert_keys_case(changes))
    except Duplicate:
        return Error(
            GraphQLError.DUPLICATE, f'Artist "{changes["name"]}" already exists.'
        )
