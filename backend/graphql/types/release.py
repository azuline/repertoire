from typing import Any, Dict, List, Optional

from ariadne import ObjectType, UnionType
from graphql.type import GraphQLResolveInfo

from backend.enums import CollectionType, GraphQLError, ReleaseType
from backend.graphql.query import query
from backend.graphql.types.error import Error
from backend.graphql.util import require_auth, resolve_result
from backend.library import artist, release

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
def resolve_releases(
    obj: Any,
    info: GraphQLResolveInfo,
    releaseTypes: List[ReleaseType] = [],
    perPage: Optional[int] = None,
    **kwargs,
) -> List[release.T]:
    # For some of the parameters, we have to convert camelCase to snake_case manually.
    total, releases = release.search(
        cursor=info.context.db,
        per_page=perPage,
        release_types=releaseTypes,
        **kwargs,
    )
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
