from datetime import date
from typing import Any, Dict, List, Optional, Union

from ariadne import ObjectType, UnionType
from graphql.type import GraphQLResolveInfo

from backend.enums import CollectionType, GraphQLError, ReleaseType
from backend.errors import AlreadyExists, DoesNotExist, NotFound
from backend.graphql.mutation import mutation
from backend.graphql.query import query
from backend.graphql.types.error import Error
from backend.graphql.util import require_auth, resolve_result
from backend.library import artist, release
from backend.util import convert_keys_case

gql_release = ObjectType("Release")
gql_release_result = UnionType("ReleaseResult", resolve_result("Release"))

gql_releases = ObjectType("Releases")
gql_releases_result = UnionType("ReleasesResult", resolve_result("Releases"))


@query.field("release")
@require_auth
def resolve_release(obj: Any, info: GraphQLResolveInfo, id: int) -> release.T:
    if rls := release.from_id(id, info.context.db):
        return rls

    return Error(GraphQLError.NOT_FOUND, f"Release {id} not found.")


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
) -> Union[release.T, Error]:
    if releaseDate:
        try:
            releaseDate = date.fromisoformat(releaseDate)
        except ValueError:
            return Error(GraphQLError.PARSE_ERROR, "Invalid release date.")

    try:
        return release.create(
            title=title,
            artist_ids=artistIds,
            release_type=releaseType,
            release_year=releaseYear,
            cursor=info.context.db,
            release_date=releaseDate,
        )
    except NotFound as e:
        return Error(GraphQLError.NOT_FOUND, e.message)


@mutation.field("updateRelease")
@require_auth
def resolve_update_release(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> Union[release.T, Error]:
    if not (rls := release.from_id(id, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, f"Release {id} does not exist.")

    # TODO: Comment these resolvers up a bit, they've gotten non-trivial...
    if "releaseDate" in changes:
        try:
            changes["releaseDate"] = date.fromisoformat(changes["releaseDate"])
        except ValueError:
            return Error(GraphQLError.PARSE_ERROR, "Invalid release date.")

    return release.update(rls, info.context.db, **convert_keys_case(changes))


@mutation.field("addArtistToRelease")
@require_auth
def resolve_add_artist_to_release(
    _,
    info: GraphQLResolveInfo,
    releaseId: int,
    artistId: int,
) -> Union[release.T, Error]:
    if not (rls := release.from_id(releaseId, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, "Release does not exist.")

    try:
        release.add_artist(rls, artistId, info.context.db)
    except NotFound as e:
        return Error(GraphQLError.NOT_FOUND, e.message)
    except AlreadyExists:
        return Error(GraphQLError.ALREADY_EXISTS, "Artist is already in release.")

    return rls


@mutation.field("delArtistFromRelease")
@require_auth
def resolve_del_artist_from_release(
    _,
    info: GraphQLResolveInfo,
    releaseId: int,
    artistId: int,
) -> Union[release.T, Error]:
    if not (rls := release.from_id(releaseId, info.context.db)):
        return Error(GraphQLError.NOT_FOUND, "Release does not exist.")

    try:
        release.del_artist(rls, artistId, info.context.db)
    except NotFound as e:
        return Error(GraphQLError.NOT_FOUND, e.message)
    except DoesNotExist:
        return Error(GraphQLError.DOES_NOT_EXIST, "Artist is not in release.")

    return rls
