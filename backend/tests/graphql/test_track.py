import pytest

from src.library import track


@pytest.mark.asyncio
async def test_track(graphql_query, snapshot):
    query = """
        query {
            track(id: 10) {
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
async def test_track_favorited(graphql_query, snapshot):
    query = """
        query {
            track(id: 1) {
                favorited
            }
        }
    """
    _, res = await graphql_query(query)
    assert res["data"]["track"]["favorited"]


@pytest.mark.asyncio
async def test_track_favorited_false(graphql_query, snapshot):
    query = """
        query {
            track(id: 6) {
                favorited
            }
        }
    """
    _, res = await graphql_query(query)
    assert not res["data"]["track"]["favorited"]


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
            tracks(search: "Aaron") {
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
            tracks(playlistIds: [1]) {
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
async def test_update_track(db, graphql_query, snapshot):
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
    snapshot.assert_match(track.from_id(2, db))


@pytest.mark.asyncio
async def test_update_track_bad_release_id(db, graphql_query, snapshot):
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
    snapshot.assert_match(track.from_id(2, db))


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
async def test_add_artist_to_track(db, graphql_query, snapshot):
    query = """
        mutation {
            addArtistToTrack(trackId: 1, artistId: 3, role: MAIN) {
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
    snapshot.assert_match(track.artists(trk, db))


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
async def test_add_artist_to_track_bad_artist(db, graphql_query, snapshot):
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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)
    trk = track.from_id(1, db)
    assert trk is not None
    snapshot.assert_match(track.artists(trk, db))


@pytest.mark.asyncio
async def test_add_artist_to_track_already_exists(db, graphql_query, snapshot):
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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)
    trk = track.from_id(1, db)
    assert trk is not None
    snapshot.assert_match(track.artists(trk, db))


@pytest.mark.asyncio
async def test_del_artist_from_track(db, graphql_query, snapshot):
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
    snapshot.assert_match(track.artists(trk, db))


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
async def test_del_artist_from_track_bad_artist(db, graphql_query, snapshot):
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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)
    trk = track.from_id(2, db)
    assert trk is not None
    snapshot.assert_match(track.artists(trk, db))


@pytest.mark.asyncio
async def test_del_artist_from_track_doesnt_exist(graphql_query, snapshot):
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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)
