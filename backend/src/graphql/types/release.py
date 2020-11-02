from datetime import date
from typing import Any, Dict, List, Optional

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.enums import CollectionType, ReleaseType
from src.errors import NotFound, ParseError
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.util import require_auth
from src.library import artist, release
from src.util import convert_keys_case

gql_release = ObjectType("Release")

gql_releases = ObjectType("Releases")


@query.field("release")
@require_auth
def resolve_release(obj: Any, info: GraphQLResolveInfo, id: int) -> release.T:
    if rls := release.from_id(id, info.context.db):
        return rls

    raise NotFound(f"Release {id} not found.")


@query.field("releases")
@require_auth
def resolve_releases(obj: Any, info: GraphQLResolveInfo, **kwargs) -> List[release.T]:
    total, releases = release.search(info.context.db, **convert_keys_case(kwargs))
    return {"total": total, "results": releases}


@gql_release.field("hasCover")
def resolve_has_cover(obj: release.T, info: GraphQLResolveInfo) -> bool:
    return bool(obj.image_path)


@gql_release.field("artists")
def resolve_artists(obj: release.T, info: GraphQLResolveInfo) -> List[artist.T]:
    return release.artists(obj, info.context.db)


@gql_release.field("tracks")
def resolve_top_genres(obj: release.T, info: GraphQLResolveInfo) -> List[Dict]:
    return release.tracks(obj, info.context.db)


@gql_release.field("genres")
def resolve_genres(obj: release.T, info: GraphQLResolveInfo) -> List[Dict]:
    return release.collections(obj, info.context.db, type=CollectionType.GENRE)


@gql_release.field("labels")
def resolve_labels(obj: release.T, info: GraphQLResolveInfo) -> List[Dict]:
    return release.collections(obj, info.context.db, type=CollectionType.LABEL)


@gql_release.field("collages")
def resolve_collages(obj: release.T, info: GraphQLResolveInfo) -> List[Dict]:
    return release.collections(obj, info.context.db, type=CollectionType.COLLAGE)


@mutation.field("createRelease")
@require_auth
def resolve_create_release(
    _,
    info: GraphQLResolveInfo,
    title: str,
    artistIds: List[int],
    releaseType: ReleaseType,
    releaseYear: int,
    releaseDate: Optional[str] = None,
) -> release.T:
    # Convert the "releaseDate" field from a string to a `dat` object. If it is not in
    # the changes dict, do nothing.
    try:
        releaseDate = date.fromisoformat(releaseDate)
    except ValueError:
        raise ParseError("Invalid release date.")
    except TypeError:
        pass

    return release.create(
        title=title,
        artist_ids=artistIds,
        release_type=releaseType,
        release_year=releaseYear,
        cursor=info.context.db,
        release_date=releaseDate,
    )


@mutation.field("updateRelease")
@require_auth
def resolve_update_release(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> release.T:
    if not (rls := release.from_id(id, info.context.db)):
        raise NotFound(f"Release {id} does not exist.")

    # Convert the "releaseDate" update from a string to a `date` object. If it is not in
    # the changes dict, do nothing.
    try:
        changes["releaseDate"] = date.fromisoformat(changes["releaseDate"])
    except ValueError:
        raise ParseError("Invalid release date.")
    except KeyError:
        pass

    return release.update(rls, info.context.db, **convert_keys_case(changes))


@mutation.field("addArtistToRelease")
@require_auth
def resolve_add_artist_to_release(
    _,
    info: GraphQLResolveInfo,
    releaseId: int,
    artistId: int,
) -> release.T:
    if not (rls := release.from_id(releaseId, info.context.db)):
        raise NotFound(f"Release {releaseId} does not exist.")

    release.add_artist(rls, artistId, info.context.db)
    return rls


@mutation.field("delArtistFromRelease")
@require_auth
def resolve_del_artist_from_release(
    _,
    info: GraphQLResolveInfo,
    releaseId: int,
    artistId: int,
) -> release.T:
    if not (rls := release.from_id(releaseId, info.context.db)):
        raise NotFound(f"Release {releaseId} does not exist.")

    release.del_artist(rls, artistId, info.context.db)
    return rls
