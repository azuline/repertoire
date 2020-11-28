import pytest

from src.library import user
from src.util import database

USER_QUERY = """
    query {
        user {
            id
            nickname
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
async def test_user(db, graphql_query, snapshot):
    snapshot.assert_match(await graphql_query(USER_QUERY))


@pytest.mark.asyncio
async def test_update_user(db, graphql_query, snapshot):
    query = """
        mutation {
            updateUser(nickname: "not admin") {
                id
                nickname
            }
        }
    """

    snapshot.assert_match(await graphql_query(query))
    assert user.from_id(1, db).nickname == "not admin"


@pytest.mark.asyncio
async def test_new_token(db, graphql_query):
    db.execute("SELECT token_prefix FROM system__users WHERE id = 1")
    old_prefix = db.fetchone()[0]

    _, result = await graphql_query(TOKEN_QUERY)
    assert result["data"]["newToken"]["hex"]

    with database() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT token_prefix FROM system__users WHERE id = 1")
        new_prefix = cursor.fetchone()[0]

    assert old_prefix != new_prefix
