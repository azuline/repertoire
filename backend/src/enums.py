from enum import Enum

from tagfiles import ArtistRoles
from string import Template

ArtistRole = ArtistRoles


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
    releases.  The enum values are templates with an ``$order`` key--this key should be
    ASC or DESC.
    """

    #:
    RECENTLY_ADDED = Template("rls.added_on $order")
    #:
    TITLE = Template("rls.title $order")
    #:
    YEAR = Template("rls.release_year IS NULL, rls.release_year $order")
    #:
    RATING = Template("rls.rating IS NULL, rls.rating $order")
    #:
    RANDOM = Template("RANDOM() $order")
    #:
    SEARCH_RANK = Template("fts.rank $order")


class TrackSort(Enum):
    """
    The possible ways to sort tracks; used when querying the database for a list of
    tracks. The enum values are templates with an ``$order`` key--this key should be ASC
    or DESC.

    The RECENTLY_ADDED, YEAR, AND RATING methods sort on the release fields and then on
    the track's disc and track numbers.
    """

    #:
    RECENTLY_ADDED = Template(
        """
        rls.added_on $order,
        rls.id,
        trks.disc_number,
        trks.track_number
        """
    )
    #:
    TITLE = Template("trks.title $order")
    #:
    YEAR = Template(
        """
        rls.release_year IS NULL,
        rls.release_year $order,
        trks.disc_number,
        trks.track_number
        """
    )
    #:
    RATING = Template(
        """
        rls.rating IS NULL,
        rls.rating $order,
        trks.disc_number,
        trks.track_number
        """
    )
    #:
    RANDOM = Template("RANDOM() $order")
    #:
    SEARCH_RANK = Template("fts.rank $order")
