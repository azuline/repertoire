import pytest

from src.library import playlist_entry as pentry
from tests.conftest import NEXT_PLAYLIST_ENTRY_ID


@pytest.mark.asyncio
async def test_resolve_playlist_entries(graphql_query, snapshot):
    query = """
        query {
            playlist(id: 1) {
                entries {
                    ...PlaylistEntryFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_create_playlist_entry(db, graphql_query, snapshot):
    query = """
        mutation {
            createPlaylistEntry(playlistId: 1, trackId: 10) {
                ...PlaylistEntryFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    assert pentry.from_id(NEXT_PLAYLIST_ENTRY_ID, db).track_id == 10


@pytest.mark.asyncio
async def test_create_playlist_entry_bad_playlist(graphql_query, snapshot):
    query = """
        mutation {
            createPlaylistEntry(playlistId: 9999, trackId: 10) {
                ...PlaylistEntryFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_create_playlist_entry_bad_track(graphql_query, snapshot):
    query = """
        mutation {
            createPlaylistEntry(playlistId: 1, trackId: 9999) {
                ...PlaylistEntryFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_delete_entry(db, graphql_query, snapshot):
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
    snapshot.assert_match(await graphql_query(query))
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
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_delete_entries(db, graphql_query, snapshot):
    query = """
        mutation {
            delPlaylistEntries(playlistId: 2, trackId: 14) {
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
    assert pentry.from_playlist_and_track(2, 14, db) == []


@pytest.mark.asyncio
async def test_update_playlist_entry(db, graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylistEntry(id: 5, position: 1) {
                ...PlaylistEntryFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    cursor = db.execute(
        """
        SELECT id
        FROM music__playlists_tracks
        WHERE playlist_id = 2
        ORDER BY position ASC
        """
    )

    order = [row["id"] for row in cursor]
    assert order == [5, 3, 4, 6, 7, 8]


@pytest.mark.asyncio
async def test_update_playlist_entry_bad_entry(graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylistEntry(id: 99999, position: 1) {
                ...PlaylistEntryFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_update_playlist_entry_bad_position(db, graphql_query, snapshot):
    query = """
        mutation {
            updatePlaylistEntry(id: 5, position: 9999) {
                ...PlaylistEntryFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    assert pentry.from_id(5, db).position == 3
