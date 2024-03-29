import pytest

from src.library import user
from src.util import database

USER_QUERY = """
    query {
        user {
            ...UserFields
        }
    }
"""

TOKEN_QUERY = """
    mutation {
        newToken {
            hex
        }
    }
"""


@pytest.mark.asyncio
async def test_user(graphql_query, snapshot):
    success, data = await graphql_query(USER_QUERY)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_user_collection_ids(graphql_query, snapshot):
    success, data = await graphql_query(
        """
        query {
            user {
               inboxCollectionId
               favoritesCollectionId
               favoritesPlaylistId
           }
       }
       """
    )
    assert success is True
    assert data["data"]["user"]["inboxCollectionId"] == 1
    assert data["data"]["user"]["favoritesCollectionId"] == 2
    assert data["data"]["user"]["favoritesPlaylistId"] == 1


@pytest.mark.asyncio
async def test_update_user(db, graphql_query, snapshot):
    query = """
        mutation {
            updateUser(nickname: "not admin") {
                ...UserFields
            }
        }
    """

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)
    assert user.from_id(1, db).nickname == "not admin"


@pytest.mark.asyncio
async def test_new_token(db, graphql_query):
    cursor = db.execute("SELECT token_prefix FROM system__users WHERE id = 1")
    old_prefix = cursor.fetchone()[0]

    _, result = await graphql_query(TOKEN_QUERY)
    assert result["data"]["newToken"]["hex"]

    with database() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT token_prefix FROM system__users WHERE id = 1")
        new_prefix = cursor.fetchone()[0]

    assert old_prefix != new_prefix
