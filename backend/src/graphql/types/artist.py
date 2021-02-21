from typing import Any, Dict, List, Optional

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.errors import NotFound
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.util import commit
from src.library import artist, release
from src.util import convert_keys_case, del_pagination_keys

gql_artist = ObjectType("Artist")
gql_artists = ObjectType("Artists")


@query.field("artist")
def resolve_artist(obj: Any, info: GraphQLResolveInfo, id: int) -> artist.T:
    if art := artist.from_id(id, info.context.db):
        return art

    raise NotFound(f"Artist {id} does not exist.")


@query.field("artistFromName")
def resolve_artist_from_name(obj: Any, info: GraphQLResolveInfo, name: str) -> artist.T:
    if art := artist.from_name(name, info.context.db):
        return art

    raise NotFound(f'Artist "{name}" does not exist.')


@query.field("artists")
def resolve_artists(obj: Any, info: GraphQLResolveInfo, **kwargs) -> Dict:
    kwargs = convert_keys_case(kwargs)
    return {
        "results": artist.search(info.context.db, **kwargs),
        "total": artist.count(info.context.db, **del_pagination_keys(kwargs)),
    }


@gql_artist.field("releases")
def resolve_releases(obj: artist.T, info: GraphQLResolveInfo) -> List[release.T]:
    return artist.releases(obj, info.context.db)


@gql_artist.field("topGenres")
def resolve_top_genres(obj: artist.T, info: GraphQLResolveInfo) -> List[Dict]:
    return artist.top_genres(obj, info.context.db)


@gql_artist.field("imageId")
def resolve_image_id(obj: artist.T, info: GraphQLResolveInfo) -> Optional[int]:
    if img := artist.image(obj, info.context.db):
        return img.id

    return None


@mutation.field("createArtist")
@commit
def resolve_create_artist(
    _,
    info: GraphQLResolveInfo,
    name: str,
    starred: bool = False,
) -> artist.T:
    return artist.create(name, info.context.db, starred=starred)


@mutation.field("updateArtist")
@commit
def resolve_update_artist(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> artist.T:
    if not (art := artist.from_id(id, info.context.db)):
        raise NotFound(f"Artist {id} does not exist.")

    return artist.update(art, info.context.db, **convert_keys_case(changes))
