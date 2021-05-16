from sqlite3 import Connection

import pytest

from src.enums import CollectionType
from src.library import collection


@pytest.mark.asyncio
async def test_collection(graphql_query, snapshot):
    query = """
        query {
            collection(id: 5) {
                ...CollectionFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_collection_not_found(graphql_query, snapshot):
    query = """
        query {
            collection(id: 999999) {
                ...CollectionFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_collection_from_name_type_user(graphql_query, snapshot):
    query = """
        query {
            collectionFromNameTypeUser(name: "Genre1", type: GENRE) {
                ...CollectionFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_collection_from_name_type_user_not_found(graphql_query, snapshot):
    query = """
        query {
            collectionFromNameTypeUser(name: "AAFEFOPAIEFPAJF", type: COLLAGE) {
                ...CollectionFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_collections(graphql_query, snapshot):
    query = """
        query {
            collections {
                total
                results {
                    ...CollectionFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_collections_filter(graphql_query, snapshot):
    query = """
        query {
            collections(search: "genre1", types: [GENRE]) {
                total
                results {
                    ...CollectionFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_collections_pagination(graphql_query, snapshot):
    query = """
        query {
            collections(page: 3, perPage: 2) {
                total
                results {
                    ...CollectionFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_collection_user(graphql_query):
    query = """
        query {
            collection(id: 1) {
                user {
                    id
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    assert data["data"]["collection"]["user"]["id"] == 1


@pytest.mark.asyncio
async def test_collection_image(graphql_query):
    query = """
        query {
            collection(id: 5) {
                imageId
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    assert isinstance(data["data"]["collection"]["imageId"], int)


@pytest.mark.asyncio
async def test_collection_image_nonexistent(graphql_query):
    query = """
        query {
            collection(id: 1) {
                imageId
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    assert data["data"]["collection"]["imageId"] is None


@pytest.mark.asyncio
async def test_collections_type_param(graphql_query, snapshot):
    query = """
        query {
            collections(types: [GENRE, SYSTEM]) {
                results {
                    ...CollectionFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_create_collection(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            createCollection(name: "NewCollection", type: COLLAGE, starred: true) {
                ...CollectionFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    col = collection.from_id(data["data"]["createCollection"]["id"], db)
    assert col is not None
    assert col.name == "NewCollection"
    assert col.type == CollectionType.COLLAGE
    assert col.starred is True


@pytest.mark.asyncio
async def test_create_collection_duplicate(graphql_query, snapshot):
    query = """
        mutation {
            createCollection(name: "Collage1", type: COLLAGE, starred: true) {
                ...CollectionFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_update_collection(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updateCollection(id: 5, name: "NewCollection", starred: true) {
                ...CollectionFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    col = collection.from_id(5, db)
    assert col is not None
    assert col.name == "NewCollection"
    assert col.starred is True


@pytest.mark.asyncio
async def test_update_collection_duplicate(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updateCollection(id: 5, name: "Collage3") {
                ...CollectionFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    col = collection.from_id(5, db)
    assert col is not None
    assert col.name != "Collage3"


@pytest.mark.asyncio
async def test_update_collection_not_found(graphql_query, snapshot):
    query = """
        mutation {
            updateCollection(id: 99999, name: "Hi") {
                ...CollectionFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_update_collection_immutable(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            updateCollection(id: 1, name: "NewCollection") {
                ...CollectionFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    col = collection.from_id(1, db)
    assert col is not None
    assert col.name != "NewCollection"


@pytest.mark.asyncio
async def test_add_release_to_collection(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            addReleaseToCollection(collectionId: 1, releaseId: 2) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    col = collection.from_id(1, db)
    assert col is not None

    assert 2 in [r.id for r in collection.releases(col, db)]


@pytest.mark.asyncio
async def test_add_release_to_collection_bad_collection(graphql_query, snapshot):
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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_add_release_to_collection_bad_release(
    db: Connection,
    graphql_query,
    snapshot,
):
    query = """
        mutation {
            addReleaseToCollection(collectionId: 3, releaseId: 9999) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    col = collection.from_id(3, db)
    assert col is not None

    releases_before = collection.releases(col, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    releases_after = collection.releases(col, db)

    assert releases_before == releases_after


@pytest.mark.asyncio
async def test_add_release_to_collection_already_exists(
    db: Connection,
    graphql_query,
    snapshot,
):
    query = """
        mutation {
            addReleaseToCollection(collectionId: 5, releaseId: 2) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    col = collection.from_id(5, db)
    assert col is not None

    releases_before = collection.releases(col, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    releases_after = collection.releases(col, db)

    assert releases_before == releases_after


@pytest.mark.asyncio
async def test_del_release_from_collection(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            delReleaseFromCollection(collectionId: 5, releaseId: 2) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    col = collection.from_id(5, db)
    assert col is not None
    assert 2 not in [r.id for r in collection.releases(col, db)]


@pytest.mark.asyncio
async def test_del_release_from_collection_bad_collection(graphql_query, snapshot):
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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_del_release_from_collection_bad_release(
    db: Connection,
    graphql_query,
    snapshot,
):
    query = """
        mutation {
            delReleaseFromCollection(collectionId: 3, releaseId: 9999) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    col = collection.from_id(3, db)
    assert col is not None

    releases_before = collection.releases(col, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    releases_after = collection.releases(col, db)

    assert releases_before == releases_after


@pytest.mark.asyncio
async def test_del_release_from_collection_doesnt_exist(
    db: Connection,
    graphql_query,
    snapshot,
):
    query = """
        mutation {
            delReleaseFromCollection(collectionId: 1, releaseId: 1) {
                collection {
                    ...CollectionFields
                }
                release {
                    ...ReleaseFields
                }
            }
        }
    """
    col = collection.from_id(1, db)
    assert col is not None

    releases_before = collection.releases(col, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    releases_after = collection.releases(col, db)

    assert releases_before == releases_after
