import pytest

USER_QUERY = """
    query {
        user {
            __typename

            ... on User {
                id
            }

            ... on Error {
                error
                message
            }
        }
    }
"""

TOKEN_QUERY = """
    mutation {
        newToken {
            __typename

            ... on Token {
                hex
            }

            ... on Error {
                error
                message
            }
        }
    }
"""


@pytest.mark.asyncio
async def test_user(db, graphql_query, snapshot):
    snapshot.assert_match(await graphql_query(USER_QUERY, authed=True))


@pytest.mark.asyncio
async def test_user_no_auth(db, graphql_query, snapshot):
    snapshot.assert_match(await graphql_query(USER_QUERY, authed=False))


@pytest.mark.asyncio
async def test_new_token(db, graphql_query):
    _, result = await graphql_query(TOKEN_QUERY, authed=True)
    assert result["data"]["newToken"]["__typename"] == "Token"
    assert "hex" in result["data"]["newToken"]


@pytest.mark.asyncio
async def test_new_token_no_auth(db, graphql_query, snapshot):
    snapshot.assert_match(await graphql_query(TOKEN_QUERY, authed=False))
