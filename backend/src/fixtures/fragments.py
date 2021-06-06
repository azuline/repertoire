FRAGMENTS = {
    "...ArtistFields": """
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
    """,
    "...CollectionFields": """
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
    """,
    "...ConfigFields": """
        fragment ConfigFields on Config {
            musicDirectories
            indexCrontab
        }
    """,
    "...InviteFields": """
        fragment InviteFields on Invite {
            id
            code
            createdBy {
                id
            }
            createdAt
            usedBy {
                id
            }
        }
    """,
    "...PlaylistEntryFields": """
        fragment PlaylistEntryFields on PlaylistEntry {
            id
            position

            track {
                id
                title
            }

            playlist {
                id
                name
            }
        }
    """,
    "...PlaylistFields": """
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
    """,
    "...ReleaseFields": """
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
                role
                artist {
                    id
                    name
                }
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
    """,
    "...TrackFields": """
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
    """,
    "...UserFields": """
        fragment UserFields on User {
            id
            nickname
        }
    """,
}
