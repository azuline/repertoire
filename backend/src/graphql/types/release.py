from datetime import date
from typing import Any, Optional

from ariadne import ObjectType

from graphql.type import GraphQLResolveInfo
from src.enums import ArtistRole, CollectionType, ReleaseType
from src.errors import NotFound, ParseError
from src.graphql.mutation import mutation
from src.graphql.query import query
from src.graphql.util import commit
from src.library import artist, collection, release, track
from src.util import convert_keys_case, del_pagination_keys

gql_release = ObjectType("Release")

gql_releases = ObjectType("Releases")


@query.field("release")
def resolve_release(_: Any, info: GraphQLResolveInfo, id: int) -> release.T:
    if rls := release.from_id(id, info.context.db):
        return rls

    raise NotFound(f"Release {id} not found.")


@query.field("releases")
def resolve_releases(_: Any, info: GraphQLResolveInfo, **kwargs) -> dict:
    kwargs = convert_keys_case(kwargs)
    return {
        "results": release.search(info.context.db, **kwargs),
        "total": release.count(info.context.db, **del_pagination_keys(kwargs)),
    }


@gql_release.field("inInbox")
def resolve_in_inbox(obj: release.T, info: GraphQLResolveInfo) -> bool:
    return release.in_inbox(obj, info.context.user.id, info.context.db)


@gql_release.field("inFavorites")
def resolve_in_favorites(obj: release.T, info: GraphQLResolveInfo) -> bool:
    return release.in_favorites(obj, info.context.user.id, info.context.db)


@gql_release.field("artists")
def resolve_artists(obj: release.T, info: GraphQLResolveInfo) -> list[dict]:
    return release.artists(obj, info.context.db)


@gql_release.field("tracks")
def resolve_tracks(obj: release.T, info: GraphQLResolveInfo) -> list[track.T]:
    return release.tracks(obj, info.context.db)


@gql_release.field("genres")
def resolve_genres(obj: release.T, info: GraphQLResolveInfo) -> list[collection.T]:
    return release.collections(obj, info.context.db, type=CollectionType.GENRE)


@gql_release.field("labels")
def resolve_labels(obj: release.T, info: GraphQLResolveInfo) -> list[collection.T]:
    return release.collections(obj, info.context.db, type=CollectionType.LABEL)


@gql_release.field("collages")
def resolve_collages(obj: release.T, info: GraphQLResolveInfo) -> list[collection.T]:
    return release.collections(obj, info.context.db, type=CollectionType.COLLAGE)


@query.field("releaseYears")
def resolve_release_years(_: release.T, info: GraphQLResolveInfo) -> list[int]:
    return release.all_years(info.context.db)


@mutation.field("createRelease")
@commit
def resolve_create_release(
    _,
    info: GraphQLResolveInfo,
    title: str,
    artists: list[dict],
    releaseType: ReleaseType,
    releaseYear: Optional[int],
    releaseDate: Optional[str] = None,
    rating: Optional[int] = None,
) -> release.T:
    # Convert the "releaseDate" field from a string to a `date` object. If it is not in
    # the changes dict, do nothing.
    parsedDate: Optional[date] = None

    if releaseDate is not None:
        try:
            parsedDate = date.fromisoformat(releaseDate)
        except ValueError:
            raise ParseError("Invalid release date.")

    return release.create(
        title=title,
        artists=artists,
        release_type=releaseType,
        release_year=releaseYear,
        release_date=parsedDate,
        rating=rating,
        conn=info.context.db,
    )


@mutation.field("updateRelease")
@commit
def resolve_update_release(
    _,
    info: GraphQLResolveInfo,
    id: int,
    **changes,
) -> release.T:
    rls = release.from_id(id, info.context.db)
    if not rls:
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
@commit
def resolve_add_artist_to_release(
    _,
    info: GraphQLResolveInfo,
    releaseId: int,
    artistId: int,
    role: ArtistRole,
) -> dict:
    rls = release.from_id(releaseId, info.context.db)
    if not rls:
        raise NotFound(f"Release {releaseId} does not exist.")

    rls = release.add_artist(rls, artistId, role, info.context.db)
    art = artist.from_id(artistId, info.context.db)

    return {"release": rls, "artist": art}


@mutation.field("delArtistFromRelease")
@commit
def resolve_del_artist_from_release(
    _,
    info: GraphQLResolveInfo,
    releaseId: int,
    artistId: int,
    role: ArtistRole,
) -> dict:
    rls = release.from_id(releaseId, info.context.db)
    if not rls:
        raise NotFound(f"Release {releaseId} does not exist.")

    rls = release.del_artist(rls, artistId, role, info.context.db)
    art = artist.from_id(artistId, info.context.db)

    return {"release": rls, "artist": art}
