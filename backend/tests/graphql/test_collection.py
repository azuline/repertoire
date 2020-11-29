import pytest

from src.library import collection
from src.util import database


@pytest.mark.asyncio
async def test_collection(db, graphql_query, snapshot):
    query = """
        query {
            collection(id: 3) {
                ...CollectionFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_collection_not_found(db, graphql_query, snapshot):
    query = """
        query {
            collection(id: 999999) {
                ...CollectionFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_collection_from_name_and_type(db, graphql_query, snapshot):
    query = """
        query {
            collectionFromNameAndType(name: "Folk", type: GENRE) {
                ...CollectionFields
            }
        }
    """

    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_collection_from_name_and_type_not_found(graphql_query, snapshot):
    query = """
        query {
            collectionFromNameAndType(name: "AAFEFOPAIEFPAJF", type: COLLAGE) {
                ...CollectionFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_collections(db, graphql_query, snapshot):
    query = """
        query {
            collections {
                results {
                    ...CollectionFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_collection_image(db, graphql_query, snapshot):
    query = """
        query {
            collection(id: 3) {
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
    query = """
        query {
            collections(types: [GENRE, SYSTEM]) {
                results {
                    ...CollectionFields
                }

            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_create_collection(db, graphql_query, snapshot):
    query = """
        mutation {
            createCollection(name: "NewCollection", type: COLLAGE, starred: true) {
                ...CollectionFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        snapshot.assert_match(collection.from_id(12, conn.cursor()))


@pytest.mark.asyncio
async def test_create_collection_duplicate(db, graphql_query, snapshot):
    query = """
        mutation {
            createCollection(name: "Folk", type: GENRE, starred: true) {
                ...CollectionFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    assert collection.from_id(12, db) is None


@pytest.mark.asyncio
async def test_update_collection(db, graphql_query, snapshot):
    query = """
        mutation {
            updateCollection(id: 3, name: "NewCollection", starred: true) {
                ...CollectionFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        snapshot.assert_match(collection.from_id(3, conn.cursor()))


@pytest.mark.asyncio
async def test_update_collection_duplicate(db, graphql_query, snapshot):
    query = """
        mutation {
            updateCollection(id: 7, name: "Folk") {
                ...CollectionFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(collection.from_id(7, db))


@pytest.mark.asyncio
async def test_update_collection_not_found(db, graphql_query, snapshot):
    query = """
        mutation {
            updateCollection(id: 99999, name: "Hi") {
                ...CollectionFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_update_collection_immutable(db, graphql_query, snapshot):
    query = """
        mutation {
            updateCollection(id: 1, name: "NewCollection", starred: true) {
                ...CollectionFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(collection.from_id(1, db))


@pytest.mark.asyncio
async def test_add_release_to_collection(db, graphql_query, snapshot):
    query = """
        mutation {
            addReleaseToCollection(collectionId: 2, releaseId: 2) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(
            collection.releases(collection.from_id(2, cursor), cursor)
        )


@pytest.mark.asyncio
async def test_add_release_to_collection_bad_collection(db, graphql_query, snapshot):
    query = """
        mutation {
            addReleaseToCollection(collectionId: 999, releaseId: 2) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_add_release_to_collection_bad_release(db, graphql_query, snapshot):
    query = """
        mutation {
            addReleaseToCollection(collectionId: 2, releaseId: 9999) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(collection.releases(collection.from_id(2, db), db))


@pytest.mark.asyncio
async def test_add_release_to_collection_already_exists(db, graphql_query, snapshot):
    query = """
        mutation {
            addReleaseToCollection(collectionId: 3, releaseId: 2) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(collection.releases(collection.from_id(3, db), db))


@pytest.mark.asyncio
async def test_del_release_from_collection(db, graphql_query, snapshot):
    query = """
        mutation {
            delReleaseFromCollection(collectionId: 1, releaseId: 2) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(
            collection.releases(collection.from_id(1, cursor), cursor)
        )


@pytest.mark.asyncio
async def test_del_release_from_collection_bad_collection(db, graphql_query, snapshot):
    query = """
        mutation {
            delReleaseFromCollection(collectionId: 999, releaseId: 2) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_del_release_from_collection_bad_release(db, graphql_query, snapshot):
    query = """
        mutation {
            delReleaseFromCollection(collectionId: 2, releaseId: 9999) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(collection.releases(collection.from_id(2, db), db))


@pytest.mark.asyncio
async def test_del_release_from_collection_doesnt_exist(db, graphql_query, snapshot):
    query = """
        mutation {
            delReleaseFromCollection(collectionId: 2, releaseId: 2) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
