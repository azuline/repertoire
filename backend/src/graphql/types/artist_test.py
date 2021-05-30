from sqlite3 import Connection

import pytest

from src.library import artist


@pytest.mark.asyncio
async def test_artist(graphql_query, snapshot):
    query = """
        query {
            artist(id: 2) {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_artist_not_found(graphql_query, snapshot):
    query = """
        query {
            artist(id: 999999) {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_artist_from_name(graphql_query, snapshot):
    query = """
        query {
            artistFromName(name: "Artist1") {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_artist_from_name_not_found(graphql_query, snapshot):
    query = """
        query {
            artistFromName(name: "Bad Name") {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_artists_search(graphql_query, snapshot):
    query = """
        query {
            artists(search: "Artist1") {
                total
                results {
                    ...ArtistFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_artist_image(graphql_query, snapshot):
    query = """
        query {
            artist(id: 2) {
                imageId
            }
        }
    """
    success, result = await graphql_query(query)
    assert success is True
    assert isinstance(result["data"]["artist"]["imageId"], int)


@pytest.mark.asyncio
async def test_artist_image_nonexistent(graphql_query, snapshot):
    query = """
        query {
            artist(id: 6) {
                imageId
            }
        }
    """
    success, result = await graphql_query(query)
    assert success is True
    assert result["data"]["artist"]["imageId"] is None


@pytest.mark.asyncio
async def test_create_artist(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            createArtist(name: "New Artist") {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    art = artist.from_id(data["data"]["createArtist"]["id"], db)
    assert art is not None
    assert art.name == "New Artist"


@pytest.mark.asyncio
async def test_create_artist_duplicate(graphql_query, snapshot):
    query = """
        mutation {
            createArtist(name: "Artist1") {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_update_artist(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updateArtist(id: 4, name: "New Name") {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    art = artist.from_id(4, db)
    assert art is not None
    assert art.name == "New Name"


@pytest.mark.asyncio
async def test_update_artist_doesnt_exist(graphql_query, snapshot):
    query = """
        mutation {
            updateArtist(id: 999, name: "New Name") {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_update_artist_duplicate(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updateArtist(id: 4, name: "Artist1") {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    art = artist.from_id(4, db)
    assert art is not None
    assert art.name != "Artist1"


@pytest.mark.asyncio
async def test_star_artist(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            starArtist(id: 3) {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    art = artist.from_id(3, db)
    assert art is not None
    assert artist.starred(art, user_id=1, conn=db)


@pytest.mark.asyncio
async def test_unstar_artist(db: Connection, graphql_query, snapshot):
    # Artist 4 should be initially starred.
    art = artist.from_id(4, db)
    assert art is not None
    assert artist.starred(art, user_id=1, conn=db)

    query = """
        mutation {
            unstarArtist(id: 4) {
                ...ArtistFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    art = artist.from_id(4, db)
    assert art is not None
    assert not artist.starred(art, user_id=1, conn=db)
