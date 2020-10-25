import pytest

from backend.library import collection

COLLECTION_RESULT = """
    id
    name
    favorite
    type
    numReleases
    lastUpdatedOn

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

COLLECTIONS_RESULT = f"""
    results {{
        {COLLECTION_RESULT}
    }}
"""


@pytest.mark.asyncio
async def test_collection(db, graphql_query, snapshot):
    query = f"""
        query {{
            collection(id: 12) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_collection_not_found(db, graphql_query, snapshot):
    query = f"""
        query {{
            collection(id: 999999) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_collection_no_auth(db, graphql_query, snapshot):
    query = f"""
        query {{
            collection(id: 12) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_collection_from_name_and_type(db, graphql_query, snapshot):
    query = f"""
        query {{
            collectionFromNameAndType(name: "Folk", type: GENRE) {{
                {COLLECTION_RESULT}
            }}
        }}
    """

    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_collection_from_name_and_type_not_found(graphql_query, snapshot):
    query = f"""
        query {{
            collectionFromNameAndType(name: "AAFEFOPAIEFPAJF", type: COLLAGE) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_collection_from_name_and_type_no_auth(db, graphql_query, snapshot):
    query = f"""
        query {{
            collectionFromNameAndType(name: "Folk", type: GENRE) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_collections(db, graphql_query, snapshot):
    query = f"""
        query {{
            collections {{
                {COLLECTIONS_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_collections_type_param(db, graphql_query, snapshot):
    query = f"""
        query {{
            collections(type: GENRE) {{
                {COLLECTIONS_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_collections_no_auth(db, graphql_query, snapshot):
    query = f"""
        query {{
            collections {{
                {COLLECTIONS_RESULT}
            }}
        }}
    """

    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_create_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createCollection(name: "NewCollection", type: COLLAGE, favorite: true) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(collection.from_id(21, db))


@pytest.mark.asyncio
async def test_create_collection_duplicate(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createCollection(name: "Folk", type: GENRE, favorite: true) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    assert collection.from_id(21, db) is None


@pytest.mark.asyncio
async def test_dreate_collection_no_auth(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createCollection(name: "NewNewNew", type: GENRE) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_update_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateCollection(id: 12, name: "NewCollection", favorite: true) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(collection.from_id(12, db))


@pytest.mark.asyncio
async def test_update_collection_duplicate(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateCollection(id: 16, name: "Folk") {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(collection.from_id(16, db))


@pytest.mark.asyncio
async def test_update_collection_not_found(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateCollection(id: 99999, name: "Hi") {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_update_collection_immutable(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateCollection(id: 1, name: "NewCollection", favorite: true) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(collection.from_id(1, db))


@pytest.mark.asyncio
async def test_update_collection_no_auth(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateCollection(id: 12, name: "NewCollection", favorite: true) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_add_release_to_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addReleaseToCollection(collectionId: 2, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(collection.releases(collection.from_id(2, db), db))


@pytest.mark.asyncio
async def test_add_release_to_collection_bad_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addReleaseToCollection(collectionId: 999, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_add_release_to_collection_bad_release(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addReleaseToCollection(collectionId: 2, releaseId: 9999) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(collection.releases(collection.from_id(2, db), db))


@pytest.mark.asyncio
async def test_add_release_to_collection_already_exists(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addReleaseToCollection(collectionId: 12, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(collection.releases(collection.from_id(12, db), db))


@pytest.mark.asyncio
async def test_add_release_to_collection_no_auth(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addReleaseToCollection(collectionId: 2, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_del_release_from_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delReleaseFromCollection(collectionId: 1, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(collection.releases(collection.from_id(1, db), db))


@pytest.mark.asyncio
async def test_del_release_from_collection_bad_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delReleaseFromCollection(collectionId: 999, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_del_release_from_collection_bad_release(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delReleaseFromCollection(collectionId: 2, releaseId: 9999) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(collection.releases(collection.from_id(2, db), db))


@pytest.mark.asyncio
async def test_del_release_from_collection_doesnt_exist(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delReleaseFromCollection(collectionId: 2, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_del_release_from_collection_no_auth(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delReleaseFromCollection(collectionId: 1, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))
