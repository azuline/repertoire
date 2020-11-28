import pytest

from src.library import artist
from src.util import database


@pytest.mark.asyncio
async def test_artist(db, graphql_query, snapshot):
    query = """
        query {
            artist(id: 4) {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artist_not_found(db, graphql_query, snapshot):
    query = """
        query {
            artist(id: 999999) {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artist_from_name(db, graphql_query, snapshot):
    query = """
        query {
            artistFromName(name: "Abakus") {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artist_from_name_not_found(db, graphql_query, snapshot):
    query = """
        query {
            artistFromName(name: "Random Artist name") {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artists(db, graphql_query, snapshot):
    query = """
        query {
            artists {
                results {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artist_image(db, graphql_query, snapshot):
    query = """
        query {
            artist(id: 2) {
                imageId
            }
        }
    """
    _, result = await graphql_query(query)
    assert isinstance(result["data"]["artist"]["imageId"], int)


@pytest.mark.asyncio
async def test_artist_image_nonexistent(db, graphql_query, snapshot):
    query = """
        query {
            artist(id: 1) {
                imageId
            }
        }
    """
    _, result = await graphql_query(query)
    assert result["data"]["artist"]["imageId"] is None


@pytest.mark.asyncio
async def test_create_artist(db, graphql_query, snapshot):
    query = """
        mutation {
            createArtist(name: "New Artist", starred: true) {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        snapshot.assert_match(artist.from_id(6, conn.cursor()))


@pytest.mark.asyncio
async def test_create_artist_duplicate(db, graphql_query, snapshot):
    query = """
        mutation {
            createArtist(name: "Abakus", starred: true) {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    assert artist.from_id(6, db) is None


@pytest.mark.asyncio
async def test_update_artist(db, graphql_query, snapshot):
    query = """
        mutation {
            updateArtist(id: 4, name: "New Name", starred: true) {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        snapshot.assert_match(artist.from_id(4, conn.cursor()))


@pytest.mark.asyncio
async def test_update_artist_doesnt_exist(db, graphql_query, snapshot):
    query = """
        mutation {
            updateArtist(id: 999, name: "New Name", starred: true) {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_update_artist_duplicate(db, graphql_query, snapshot):
    query = """
        mutation {
            updateArtist(id: 4, name: "Bacchus", starred: true) {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(artist.from_id(4, db))
