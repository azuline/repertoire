USER_FIELDS = """
    fragment UserFields on User {
        id
        nickname
    }
"""

RELEASE_FIELDS = """
    fragment ReleaseFields on Release {
        id
        title
        releaseType
        addedOn
        inInbox
        inFavorites
        releaseYear
        releaseDate
        numTracks
        runtime
        imageId

        artists {
            id
            name
        }
        collages {
            id
            name
        }
        labels {
            id
            name
        }
        genres {
            id
            name
        }
        tracks {
            id
            title
        }
    }
"""

ARTIST_FIELDS = """
    fragment ArtistFields on Artist {
        id
        name
        starred
        numReleases

        releases {
            id
            title
        }

        topGenres {
            genre {
                id
            }
            numMatches
        }
    }
"""

COLLECTION_FIELDS = """
    fragment CollectionFields on Collection {
        id
        name
        starred
        type
        numReleases
        lastUpdatedOn

        releases {
            id
            title
        }

        topGenres {
            genre {
                id
            }
            numMatches
        }
    }
"""

PLAYLIST_FIELDS = """
    fragment PlaylistFields on Playlist {
        id
        name
        starred
        type
        numTracks
        lastUpdatedOn

        entries {
            id
            track {
                id
                title
            }
        }

        topGenres {
            genre {
                id
            }
            numMatches
        }
    }
"""

TRACK_FIELDS = """
    fragment TrackFields on Track {
        id
        title
        duration
        trackNumber
        discNumber

        release {
            id
            title
        }

        artists {
            role
            artist {
                id
                name
            }
        }
    }
"""

FRAGMENTS = {
    "...UserFields": USER_FIELDS,
    "...ReleaseFields": RELEASE_FIELDS,
    "...ArtistFields": ARTIST_FIELDS,
    "...CollectionFields": COLLECTION_FIELDS,
    "...PlaylistFields": PLAYLIST_FIELDS,
    "...TrackFields": TRACK_FIELDS,
}
