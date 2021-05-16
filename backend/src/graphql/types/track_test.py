from sqlite3 import Connection

import pytest

from src.library import playlist_entry as pentry
from src.library import track


@pytest.mark.asyncio
async def test_track(graphql_query, snapshot):
    query = """
        query {
            track(id: 1) {
                ...TrackFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_track_not_found(graphql_query, snapshot):
    query = """
        query {
            track(id: 999) {
                ...TrackFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_track_in_favorites(db: Connection, graphql_query):
    query = """
        query {
            track(id: 1) {
                inFavorites
            }
        }
    """

    # Setup
    pentry.create(1, 1, db)
    db.commit()

    success, data = await graphql_query(query)
    assert success is True
    assert data["data"]["track"]["inFavorites"]


@pytest.mark.asyncio
async def test_track_in_favorites_false(graphql_query):
    query = """
        query {
            track(id: 1) {
                inFavorites
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    assert not data["data"]["track"]["inFavorites"]


@pytest.mark.asyncio
async def test_tracks(graphql_query, snapshot):
    query = """
        query {
            tracks {
                total
                results {
                    ...TrackFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_tracks_search(graphql_query, snapshot):
    query = """
        query {
            tracks(search: "Track1") {
                total
                results {
                    ...TrackFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_tracks_filter_playlists(graphql_query, snapshot):
    query = """
        query {
            tracks(playlistIds: [2]) {
                total
                results {
                    ...TrackFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_tracks_filter_artists(graphql_query, snapshot):
    query = """
        query {
            tracks(artistIds: [2]) {
                total
                results {
                    ...TrackFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_tracks_pagination(graphql_query, snapshot):
    query = """
        query {
            tracks(page: 2, perPage: 2) {
                total
                results {
                    ...TrackFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_tracks_sort(graphql_query, snapshot):
    query = """
        query {
            tracks(sort: TITLE) {
                total
                results {
                    ...TrackFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_tracks_sort_desc(graphql_query, snapshot):
    query = """
        query {
            tracks(sort: TITLE, asc: false) {
                total
                results {
                    ...TrackFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_update_track(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updateTrack(
                id: 2
                title: "aa"
                releaseId: 3
                trackNumber: "999"
                discNumber: "899"
            ) {
                ...TrackFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    trk = track.from_id(2, db)
    assert trk is not None
    assert trk.title == "aa"
    assert trk.release_id == 3
    assert trk.track_number == "999"
    assert trk.disc_number == "899"


@pytest.mark.asyncio
async def test_update_track_bad_release_id(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updateTrack(
                id: 2
                releaseId: 999
            ) {
                ...TrackFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    trk = track.from_id(2, db)
    assert trk is not None
    assert trk.release_id != 999


@pytest.mark.asyncio
async def test_update_track_not_found(graphql_query, snapshot):
    query = """
        mutation {
            updateTrack(
                id: 99999
                title: "aa"
            ) {
                ...TrackFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_add_artist_to_track(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            addArtistToTrack(trackId: 1, artistId: 5, role: MAIN) {
                track {
                    ...TrackFields
                }
                trackArtist {
                    role
                    artist {
                        ...ArtistFields
                    }
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    trk = track.from_id(1, db)
    assert trk is not None
    assert 5 in [a["artist"].id for a in track.artists(trk, db)]


@pytest.mark.asyncio
async def test_add_artist_to_track_bad_track(graphql_query, snapshot):
    query = """
        mutation {
            addArtistToTrack(trackId: 999, artistId: 2, role: MAIN) {
                track {
                    ...TrackFields
                }
                trackArtist {
                    role
                    artist {
                        ...ArtistFields
                    }
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_add_artist_to_track_bad_artist(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            addArtistToTrack(trackId: 1, artistId: 9999, role: MAIN) {
                track {
                    ...TrackFields
                }
                trackArtist {
                    role
                    artist {
                        ...ArtistFields
                    }
                }
            }
        }
    """
    trk = track.from_id(1, db)
    assert trk is not None

    before_artists = track.artists(trk, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    after_artists = track.artists(trk, db)

    assert before_artists == after_artists


@pytest.mark.asyncio
async def test_add_artist_to_track_already_exists(
    db: Connection,
    graphql_query,
    snapshot,
):
    query = """
        mutation {
            addArtistToTrack(trackId: 1, artistId: 2, role: MAIN) {
                track {
                    ...TrackFields
                }
                trackArtist {
                    role
                    artist {
                        ...ArtistFields
                    }
                }
            }
        }
    """
    trk = track.from_id(1, db)
    assert trk is not None

    before_artists = track.artists(trk, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    after_artists = track.artists(trk, db)

    assert before_artists == after_artists


@pytest.mark.asyncio
async def test_del_artist_from_track(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            delArtistFromTrack(trackId: 1, artistId: 2, role: MAIN) {
                track {
                    ...TrackFields
                }
                trackArtist {
                    role
                    artist {
                        ...ArtistFields
                    }
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    trk = track.from_id(1, db)
    assert trk is not None
    assert 2 not in [a["artist"].id for a in track.artists(trk, db)]


@pytest.mark.asyncio
async def test_del_artist_from_track_bad_track(graphql_query, snapshot):
    query = """
        mutation {
            delArtistFromTrack(trackId: 999, artistId: 2, role: MAIN) {
                track {
                    ...TrackFields
                }
                trackArtist {
                    role
                    artist {
                        ...ArtistFields
                    }
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_del_artist_from_track_bad_artist(
    db: Connection,
    graphql_query,
    snapshot,
):
    query = """
        mutation {
            delArtistFromTrack(trackId: 2, artistId: 9999, role: MAIN) {
                track {
                    ...TrackFields
                }
                trackArtist {
                    role
                    artist {
                        ...ArtistFields
                    }
                }
            }
        }
    """
    trk = track.from_id(2, db)
    assert trk is not None

    before_artists = track.artists(trk, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    after_artists = track.artists(trk, db)

    assert before_artists == after_artists


@pytest.mark.asyncio
async def test_del_artist_from_track_doesnt_exist(
    db: Connection,
    graphql_query,
    snapshot,
):
    query = """
        mutation {
            delArtistFromTrack(trackId: 1, artistId: 2, role: FEATURE) {
                track {
                    ...TrackFields
                }
                trackArtist {
                    role
                    artist {
                        ...ArtistFields
                    }
                }
            }
        }
    """
    trk = track.from_id(1, db)
    assert trk is not None

    before_artists = track.artists(trk, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    after_artists = track.artists(trk, db)

    assert before_artists == after_artists
