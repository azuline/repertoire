from enum import Enum

from tagfiles import ArtistRoles as ArtistRole  # noqa


class ReleaseType(Enum):
    """The available release types."""

    #:
    ALBUM = 1
    #:
    SINGLE = 2
    #:
    EP = 3
    #:
    COMPILATION = 4
    #:
    SOUNDTRACK = 5
    #:
    SPOKENWORD = 6
    #:
    LIVE = 7
    #:
    REMIX = 8
    #:
    DJMIX = 9
    #:
    MIXTAPE = 10
    #:
    OTHER = 11
    #:
    UNKNOWN = 12


class CollectionType(Enum):
    """The available collection types."""

    #:
    SYSTEM = 1
    #:
    COLLAGE = 2
    #:
    LABEL = 3
    #:
    GENRE = 4


class PlaylistType(Enum):
    """The available playlist types."""

    #:
    SYSTEM = 1
    #:
    PLAYLIST = 2


class ReleaseSort(Enum):
    """
    The possible ways to sort releases; used when querying the database for a list of
    releases.
    """

    #:
    RECENTLY_ADDED = "rls.added_on"
    #:
    TITLE = "rls.title"
    #:
    YEAR = "rls.release_year IS NULL, rls.release_year"
    #:
    RATING = "rls.rating IS NULL, rls.rating"
    #:
    RANDOM = "RANDOM()"
