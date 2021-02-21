import pytest

from src.library import playlist


@pytest.mark.asyncio
async def test_playlist(graphql_query, snapshot):
    query = """
        query {
            playlist(id: 2) {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_playlist_not_found(graphql_query, snapshot):
    query = """
        query {
            playlist(id: 999999) {
                ...PlaylistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_playlist_from_name_and_type(graphql_query, snapshot):
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
async def test_playlists(graphql_query, snapshot):
    query = """
        query {
            playlists {
                total
                results {
                    ...PlaylistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_playlists_filter(graphql_query, snapshot):
    query = """
        query {
            playlists(search: "aaaa", types: [PLAYLIST]) {
                total
                results {
                    ...PlaylistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_playlists_pagination(graphql_query, snapshot):
    query = """
        query {
            playlists(page: 2, perPage: 2) {
                total
                results {
                    ...PlaylistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_playlist_image(graphql_query):
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
async def test_playlist_image_nonexistent(graphql_query):
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
async def test_playlists_type_param(graphql_query, snapshot):
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

    snapshot.assert_match(playlist.from_id(4, db))


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

    snapshot.assert_match(playlist.from_id(3, db))


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
async def test_update_playlist_not_found(graphql_query, snapshot):
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
