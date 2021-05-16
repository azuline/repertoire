from sqlite3 import Connection

import pytest

from src.library import playlist
from src.library import playlist_entry as pentry


@pytest.mark.asyncio
async def test_resolve_playlist_entries(graphql_query, snapshot):
    query = """
        query {
            playlist(id: 3) {
                entries {
                    ...PlaylistEntryFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_create_playlist_entry(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            createPlaylistEntry(playlistId: 1, trackId: 1) {
                ...PlaylistEntryFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_create_playlist_entry_bad_playlist(graphql_query, snapshot):
    query = """
        mutation {
            createPlaylistEntry(playlistId: 9999, trackId: 10) {
                ...PlaylistEntryFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_create_playlist_entry_bad_track(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            createPlaylistEntry(playlistId: 1, trackId: 9999) {
                ...PlaylistEntryFields
            }
        }
    """
    ply = playlist.from_id(1, db)
    assert ply is not None

    before_tracks = playlist.entries(ply, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    after_tracks = playlist.entries(ply, db)

    assert before_tracks == after_tracks


@pytest.mark.asyncio
async def test_delete_entry(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            delPlaylistEntry(id: 1) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    assert pentry.from_id(1, db) is None


@pytest.mark.asyncio
async def test_delete_entry_invalid(graphql_query, snapshot):
    query = """
        mutation {
            delPlaylistEntry(id: 99999) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_delete_entries(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            delPlaylistEntries(playlistId: 3, trackId: 1) {
                playlist {
                    ...PlaylistFields
                }
                track {
                    ...TrackFields
                }
            }
        }
    """
    assert pentry.from_playlist_and_track(3, 1, db) != []

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    assert pentry.from_playlist_and_track(3, 1, db) == []


@pytest.mark.asyncio
async def test_update_playlist_entry(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylistEntry(id: 3, position: 1) {
                ...PlaylistEntryFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    cursor = db.execute(
        """
        SELECT id
        FROM music__playlists_tracks
        WHERE playlist_id = 3
        ORDER BY position ASC
        """
    )

    order = [row["id"] for row in cursor]
    assert order == [3, 1, 2, 4, 5]


@pytest.mark.asyncio
async def test_update_playlist_entry_bad_entry(graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylistEntry(id: 99999, position: 1) {
                ...PlaylistEntryFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_update_playlist_entry_bad_position(
    db: Connection,
    graphql_query,
    snapshot,
):
    query = """
        mutation {
            updatePlaylistEntry(id: 3, position: 9999) {
                ...PlaylistEntryFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    ety = pentry.from_id(3, db)
    assert ety is not None
    assert ety.position == 3
