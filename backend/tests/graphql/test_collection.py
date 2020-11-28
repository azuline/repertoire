import pytest

from src.library import collection
from src.util import database

COLLECTION_RESULT = """
    id
    name
    starred
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
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_collection_not_found(db, graphql_query, snapshot):
    query = f"""
        query {{
            collection(id: 999999) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_collection_from_name_and_type(db, graphql_query, snapshot):
    query = f"""
        query {{
            collectionFromNameAndType(name: "Folk", type: GENRE) {{
                {COLLECTION_RESULT}
            }}
        }}
    """

    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_collection_from_name_and_type_not_found(graphql_query, snapshot):
    query = f"""
        query {{
            collectionFromNameAndType(name: "AAFEFOPAIEFPAJF", type: COLLAGE) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_collections(db, graphql_query, snapshot):
    query = f"""
        query {{
            collections {{
                {COLLECTIONS_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_collection_image(db, graphql_query, snapshot):
    query = """
        query {
            collection(id: 12) {
                imageId
            }
        }
    """
    _, result = await graphql_query(query)
    assert isinstance(result["data"]["collection"]["imageId"], int)


@pytest.mark.asyncio
async def test_collection_image_nonexistent(db, graphql_query, snapshot):
    query = """
        query {
            collection(id: 2) {
                imageId
            }
        }
    """
    _, result = await graphql_query(query)
    assert result["data"]["collection"]["imageId"] is None


@pytest.mark.asyncio
async def test_collections_type_param(db, graphql_query, snapshot):
    query = f"""
        query {{
            collections(types: [GENRE, SYSTEM]) {{
                {COLLECTIONS_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_create_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createCollection(name: "NewCollection", type: COLLAGE, starred: true) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        snapshot.assert_match(collection.from_id(21, conn.cursor()))


@pytest.mark.asyncio
async def test_create_collection_duplicate(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createCollection(name: "Folk", type: GENRE, starred: true) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))
    assert collection.from_id(21, db) is None


@pytest.mark.asyncio
async def test_update_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateCollection(id: 12, name: "NewCollection", starred: true) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        snapshot.assert_match(collection.from_id(12, conn.cursor()))


@pytest.mark.asyncio
async def test_update_collection_duplicate(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateCollection(id: 16, name: "Folk") {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))
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
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_update_collection_immutable(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateCollection(id: 1, name: "NewCollection", starred: true) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(collection.from_id(1, db))


@pytest.mark.asyncio
async def test_add_release_to_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addReleaseToCollection(collectionId: 2, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(
            collection.releases(collection.from_id(2, cursor), cursor)
        )


@pytest.mark.asyncio
async def test_add_release_to_collection_bad_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addReleaseToCollection(collectionId: 999, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_add_release_to_collection_bad_release(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addReleaseToCollection(collectionId: 2, releaseId: 9999) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))
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
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(collection.releases(collection.from_id(12, db), db))


@pytest.mark.asyncio
async def test_del_release_from_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delReleaseFromCollection(collectionId: 1, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(
            collection.releases(collection.from_id(1, cursor), cursor)
        )


@pytest.mark.asyncio
async def test_del_release_from_collection_bad_collection(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delReleaseFromCollection(collectionId: 999, releaseId: 2) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_del_release_from_collection_bad_release(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delReleaseFromCollection(collectionId: 2, releaseId: 9999) {{
                {COLLECTION_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query))
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
    snapshot.assert_match(await graphql_query(query))
