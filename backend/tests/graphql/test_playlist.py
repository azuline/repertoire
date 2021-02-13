import pytest

from src.library import playlist
from src.util import database


@pytest.mark.asyncio
async def test_playlist(db, graphql_query, snapshot):
    query = """
        query {
            playlist(id: 2) {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_playlist_not_found(db, graphql_query, snapshot):
    query = """
        query {
            playlist(id: 999999) {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_playlist_from_name_and_type(db, graphql_query, snapshot):
    query = """
        query {
            playlistFromNameAndType(name: "AAAAAA", type: PLAYLIST) {
                ...PlaylistFields
            }
        }
    """

    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_playlist_from_name_and_type_not_found(graphql_query, snapshot):
    query = """
        query {
            playlistFromNameAndType(name: "AAFEFOPAIEFPAJF", type: SYSTEM) {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_playlists(db, graphql_query, snapshot):
    query = """
        query {
            playlists {
                results {
                    ...PlaylistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_playlist_image(db, graphql_query):
    query = """
        query {
            playlist(id: 2) {
                imageId
            }
        }
    """
    _, result = await graphql_query(query)
    assert isinstance(result["data"]["playlist"]["imageId"], int)


@pytest.mark.asyncio
async def test_playlist_image_nonexistent(db, graphql_query):
    query = """
        query {
            playlist(id: 3) {
                imageId
            }
        }
    """
    _, result = await graphql_query(query)
    assert result["data"]["playlist"]["imageId"] is None


@pytest.mark.asyncio
async def test_playlists_type_param(db, graphql_query, snapshot):
    query = """
        query {
            playlists(types: [PLAYLIST, SYSTEM]) {
                results {
                    ...PlaylistFields
                }

            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_create_playlist(db, graphql_query, snapshot):
    query = """
        mutation {
            createPlaylist(name: "NewPlaylist", type: PLAYLIST, starred: true) {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        snapshot.assert_match(playlist.from_id(4, conn.cursor()))


@pytest.mark.asyncio
async def test_create_playlist_duplicate(db, graphql_query, snapshot):
    query = """
        mutation {
            createPlaylist(name: "AAAAAA", type: PLAYLIST, starred: true) {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    assert playlist.from_id(4, db) is None


@pytest.mark.asyncio
async def test_update_playlist(db, graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylist(id: 3, name: "NewPlaylist", starred: true) {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        snapshot.assert_match(playlist.from_id(3, conn.cursor()))


@pytest.mark.asyncio
async def test_update_playlist_duplicate(db, graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylist(id: 2, name: "BBBBBB") {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(playlist.from_id(2, db))


@pytest.mark.asyncio
async def test_update_playlist_not_found(db, graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylist(id: 99999, name: "Hi") {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_update_playlist_immutable(db, graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylist(id: 1, name: "NewPlaylist", starred: true) {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(playlist.from_id(1, db))


@pytest.mark.asyncio
async def test_add_track_to_playlist(db, graphql_query, snapshot):
    query = """
        mutation {
            addTrackToPlaylist(playlistId: 2, trackId: 2) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(playlist.tracks(playlist.from_id(2, cursor), cursor))


@pytest.mark.asyncio
async def test_add_track_to_playlist_bad_playlist(db, graphql_query, snapshot):
    query = """
        mutation {
            addTrackToPlaylist(playlistId: 999, trackId: 2) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_add_track_to_playlist_bad_track(db, graphql_query, snapshot):
    query = """
        mutation {
            addTrackToPlaylist(playlistId: 2, trackId: 9999) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(playlist.tracks(playlist.from_id(2, db), db))


@pytest.mark.asyncio
async def test_add_track_to_playlist_already_exists(db, graphql_query, snapshot):
    query = """
        mutation {
            addTrackToPlaylist(playlistId: 2, trackId: 3) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(playlist.tracks(playlist.from_id(2, db), db))


@pytest.mark.asyncio
async def test_del_track_from_playlist(db, graphql_query, snapshot):
    query = """
        mutation {
            delTrackFromPlaylist(playlistId: 1, trackId: 2) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(playlist.tracks(playlist.from_id(1, cursor), cursor))


@pytest.mark.asyncio
async def test_del_track_from_playlist_bad_playlist(db, graphql_query, snapshot):
    query = """
        mutation {
            delTrackFromPlaylist(playlistId: 999, trackId: 2) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_del_track_from_playlist_bad_track(db, graphql_query, snapshot):
    query = """
        mutation {
            delTrackFromPlaylist(playlistId: 1, trackId: 9999) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(playlist.tracks(playlist.from_id(1, db), db))


@pytest.mark.asyncio
async def test_del_track_from_playlist_doesnt_exist(db, graphql_query, snapshot):
    query = """
        mutation {
            delTrackFromPlaylist(playlistId: 2, trackId: 2) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))