from ariadne import EnumType

from backend.enums import (
    ArtistRole,
    CollectionType,
    GraphQLError,
    ReleaseSort,
    ReleaseType,
)

artist_role_enum = EnumType("ArtistRole", ArtistRole)
collection_type_enum = EnumType("CollectionType", CollectionType)
release_sort_enum = EnumType("ReleaseSort", ReleaseSort)
release_type_enum = EnumType("ReleaseType", ReleaseType)
error_type_enum = EnumType("ErrorType", GraphQLError)
