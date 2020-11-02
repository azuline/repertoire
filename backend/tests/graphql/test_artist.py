import pytest

from src.library import artist

ARTIST_RESULT = """
    id
    name
    favorite
    numReleases

    releases {
        id
    }

    topGenres {
        genre {
            id
        }
        numMatches
    }
"""


ARTISTS_RESULT = f"""
    results {{
        {ARTIST_RESULT}
    }}
"""


@pytest.mark.asyncio
async def test_artist(db, graphql_query, snapshot):
    query = f"""
        query {{
            artist(id: 4) {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_artist_not_found(db, graphql_query, snapshot):
    query = f"""
        query {{
            artist(id: 999999) {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_artist_no_auth(db, graphql_query, snapshot):
    query = f"""
        query {{
            artist(id: 4) {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_artist_from_name(db, graphql_query, snapshot):
    query = f"""
        query {{
            artistFromName(name: "Abakus") {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_artist_from_name_not_found(db, graphql_query, snapshot):
    query = f"""
        query {{
            artistFromName(name: "Random Artist name") {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_artist_from_name_no_auth(db, graphql_query, snapshot):
    query = f"""
        query {{
            artistFromName(name: "Abakus") {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_artists(db, graphql_query, snapshot):
    query = f"""
        query {{
            artists {{
                {ARTISTS_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_artists_no_auth(db, graphql_query, snapshot):
    query = f"""
        query {{
            artists {{
                {ARTISTS_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_create_artist(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createArtist(name: "New Artist", favorite: true) {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(artist.from_id(6, db))


@pytest.mark.asyncio
async def test_create_artist_duplicate(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createArtist(name: "Abakus", favorite: true) {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    assert artist.from_id(6, db) is None


@pytest.mark.asyncio
async def test_create_artist_no_auth(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createArtist(name: "New Artist") {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))
    assert artist.from_id(6, db) is None


@pytest.mark.asyncio
async def test_update_artist(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateArtist(id: 4, name: "New Name", favorite: true) {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(artist.from_id(4, db))


@pytest.mark.asyncio
async def test_update_artist_doesnt_exist(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateArtist(id: 999, name: "New Name", favorite: true) {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_update_artist_duplicate(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateArtist(id: 4, name: "Bacchus", favorite: true) {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(artist.from_id(4, db))


@pytest.mark.asyncio
async def test_update_artist_no_auth(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateArtist(id: 4, name: "Bacchus", favorite: true) {{
                {ARTIST_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))
    snapshot.assert_match(artist.from_id(4, db))
