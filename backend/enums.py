from enum import Enum

from tagfiles import ArtistRoles  # noqa


class CollectionType(Enum):
    SYSTEM = 1
    COLLAGE = 2
    LABEL = 3
    GENRE = 4


class ReleaseType(Enum):
    ALBUM = 1
    SINGLE = 2
    EP = 3
    COMPILATION = 4
    SOUNDTRACK = 5
    SPOKENWORD = 6
    LIVE = 7
    REMIX = 8
    DJMIX = 9
    MIXTAPE = 10
    OTHER = 11
    UNKNOWN = 12
