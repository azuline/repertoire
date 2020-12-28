from ariadne import EnumType

from src.enums import ArtistRole, CollectionType, PlaylistType, ReleaseSort, ReleaseType

artist_role_enum = EnumType("ArtistRole", ArtistRole)
collection_type_enum = EnumType("CollectionType", CollectionType)
playlist_type_enum = EnumType("PlaylistType", PlaylistType)
release_sort_enum = EnumType("ReleaseSort", ReleaseSort)
release_type_enum = EnumType("ReleaseType", ReleaseType)
