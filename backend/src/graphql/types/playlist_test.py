from sqlite3 import Connection

import pytest

from src.enums import PlaylistType
from src.library import playlist


@pytest.mark.asyncio
async def test_playlist(graphql_query, snapshot):
    query = """
        query {
            playlist(id: 3) {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_playlist_not_found(graphql_query, snapshot):
    query = """
        query {
            playlist(id: 999999) {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_playlist_from_name_type_user(graphql_query, snapshot):
    query = """
        query {
            playlistFromNameTypeUser(name: "playlist1", type: PLAYLIST) {
                ...PlaylistFields
            }
        }
    """

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_playlist_from_name_type_user_not_found(graphql_query, snapshot):
    query = """
        query {
            playlistFromNameTypeUser(name: "AAFEFOPAIEFPAJF", type: SYSTEM) {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_playlists_filter(graphql_query, snapshot):
    query = """
        query {
            playlists(search: "Playlist1", types: [PLAYLIST]) {
                total
                results {
                    ...PlaylistFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_playlist_user(graphql_query):
    query = """
        query {
            playlist(id: 1) {
                user {
                    id
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    assert data["data"]["playlist"]["user"]["id"] == 1


@pytest.mark.asyncio
async def test_playlist_image(graphql_query):
    query = """
        query {
            playlist(id: 3) {
                imageId
            }
        }
    """
    _, data = await graphql_query(query)
    assert isinstance(data["data"]["playlist"]["imageId"], int)


@pytest.mark.asyncio
async def test_playlist_image_nonexistent(graphql_query):
    query = """
        query {
            playlist(id: 1) {
                imageId
            }
        }
    """
    _, data = await graphql_query(query)
    assert data["data"]["playlist"]["imageId"] is None


@pytest.mark.asyncio
async def test_playlists_type_param(graphql_query, snapshot):
    query = """
        query {
            playlists(types: [SYSTEM]) {
                results {
                    ...PlaylistFields
                }

            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_create_playlist(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            createPlaylist(name: "NewPlaylist", type: PLAYLIST) {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    ply = playlist.from_id(data["data"]["createPlaylist"]["id"], db)
    assert ply is not None
    assert ply.name == "NewPlaylist"
    assert ply.type == PlaylistType.PLAYLIST


@pytest.mark.asyncio
async def test_create_playlist_duplicate(graphql_query, snapshot):
    query = """
        mutation {
            createPlaylist(name: "Playlist1", type: PLAYLIST) {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_update_playlist(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylist(id: 4, name: "NewPlaylist") {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    ply = playlist.from_id(4, db)
    assert ply is not None
    assert ply.name == "NewPlaylist"


@pytest.mark.asyncio
async def test_update_playlist_duplicate(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylist(id: 3, name: "Playlist3") {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    ply = playlist.from_id(3, db)
    assert ply is not None
    assert ply.name != "Playlist3"


@pytest.mark.asyncio
async def test_update_playlist_not_found(graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylist(id: 99999, name: "Hi") {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_update_playlist_immutable(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylist(id: 1, name: "NewPlaylist") {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    ply = playlist.from_id(1, db)
    assert ply is not None
    assert ply.name != "NewPlaylist"


@pytest.mark.asyncio
async def test_star_playlist(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            starPlaylist(id: 3) {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    ply = playlist.from_id(3, db)
    assert ply is not None
    assert playlist.starred(ply, user_id=1, conn=db)


@pytest.mark.asyncio
async def test_unstar_playlist(db: Connection, graphql_query, snapshot):
    # Playlist 5 should be initially starred.
    ply = playlist.from_id(5, db)
    assert ply is not None
    assert playlist.starred(ply, user_id=1, conn=db)

    query = """
        mutation {
            unstarPlaylist(id: 5) {
                ...PlaylistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    ply = playlist.from_id(5, db)
    assert ply is not None
    assert not playlist.starred(ply, user_id=1, conn=db)
