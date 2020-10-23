import pytest


@pytest.mark.asyncio
async def test_user(graphql_query, snapshot):
    query = """
        query {
          user {
            __typename

            ... on User {
              id
              username
            }

            ... on Error {
              error
              message
            }
          }
        }
    """

    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_user_no_auth(graphql_query, snapshot):
    query = """
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

    snapshot.assert_match(await graphql_query(query, authed=False))
