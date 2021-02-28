import pytest

from src.library import artist


@pytest.mark.asyncio
async def test_artist(graphql_query, snapshot):
    query = """
        query {
            artist(id: 4) {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artist_not_found(graphql_query, snapshot):
    query = """
        query {
            artist(id: 999999) {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artist_from_name(graphql_query, snapshot):
    query = """
        query {
            artistFromName(name: "Abakus") {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artist_from_name_not_found(graphql_query, snapshot):
    query = """
        query {
            artistFromName(name: "Random Artist name") {
                ...ArtistFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artists(graphql_query, snapshot):
    query = """
        query {
            artists {
                total
                results {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artists_search(graphql_query, snapshot):
    query = """
        query {
            artists(search: "west") {
                total
                results {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artists_pagination(graphql_query, snapshot):
    query = """
        query {
            artists(page: 2, perPage: 1) {
                total
                results {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_artist_image(graphql_query, snapshot):
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
async def test_artist_image_nonexistent(graphql_query, snapshot):
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
    snapshot.assert_match(artist.from_id(NEXT_ARTIST_ID, db))


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
    assert artist.from_id(NEXT_ARTIST_ID, db) is None


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
    snapshot.assert_match(artist.from_id(4, db))


@pytest.mark.asyncio
async def test_update_artist_doesnt_exist(graphql_query, snapshot):
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
