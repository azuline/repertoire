from enum import Enum

from tagfiles import ArtistRoles as ArtistRole  # noqa


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


class CollectionType(Enum):
    SYSTEM = 1
    COLLAGE = 2
    LABEL = 3
    GENRE = 4
    RATING = 5


class ReleaseSort(Enum):
    RECENTLY_ADDED = "rls.added_on"
    TITLE = "rls.title"
    YEAR = "rls.release_year"
    RANDOM = "RANDOM()"
