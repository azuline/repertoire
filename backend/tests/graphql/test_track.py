import pytest

from src.library import track
from src.util import database

TRACK_RESULT = """
    id
    title
    duration
    trackNumber
    discNumber

    release {
      id
    }

    artists {
      role
      artist {
        id
      }
    }
"""


@pytest.mark.asyncio
async def test_track(db, graphql_query, snapshot):
    query = f"""
        query {{
            track(id: 10) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_track_not_found(db, graphql_query, snapshot):
    query = f"""
        query {{
            track(id: 999) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_update_track(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateTrack(
                id: 2
                title: "aa"
                releaseId: 3
                trackNumber: "999"
                discNumber: "899"
            ) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        snapshot.assert_match(track.from_id(2, conn.cursor()))


@pytest.mark.asyncio
async def test_update_track_bad_release_id(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateTrack(
                id: 2
                releaseId: 999
            ) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(track.from_id(2, db))


@pytest.mark.asyncio
async def test_update_track_not_found(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateTrack(
                id: 99999
                title: "aa"
            ) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_add_artist_to_track(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addArtistToTrack(trackId: 1, artistId: 3, role: MAIN) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(track.artists(track.from_id(1, cursor), cursor))


@pytest.mark.asyncio
async def test_add_artist_to_track_bad_track(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addArtistToTrack(trackId: 999, artistId: 2, role: MAIN) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_add_artist_to_track_bad_artist(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addArtistToTrack(trackId: 1, artistId: 9999, role: MAIN) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(track.artists(track.from_id(1, db), db))


@pytest.mark.asyncio
async def test_add_artist_to_track_already_exists(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addArtistToTrack(trackId: 1, artistId: 2, role: MAIN) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(track.artists(track.from_id(1, db), db))


@pytest.mark.asyncio
async def test_del_artist_from_track(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delArtistFromTrack(trackId: 1, artistId: 2, role: MAIN) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(track.artists(track.from_id(1, cursor), cursor))


@pytest.mark.asyncio
async def test_del_artist_from_track_bad_track(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delArtistFromTrack(trackId: 999, artistId: 2, role: MAIN) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_del_artist_from_track_bad_artist(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delArtistFromTrack(trackId: 2, artistId: 9999, role: MAIN) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(track.artists(track.from_id(2, db), db))


@pytest.mark.asyncio
async def test_del_artist_from_track_doesnt_exist(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delArtistFromTrack(trackId: 1, artistId: 2, role: FEATURE) {{
                {TRACK_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))
