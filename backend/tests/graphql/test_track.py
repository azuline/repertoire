import pytest


@pytest.mark.asyncio
async def test_track(graphql_query, snapshot):
    query = """
        query {
          track(id: 10) {
            __typename

            ... on Track {
              id
              title
              duration
              trackNumber
              discNumber

              release {
                id
              }

              artists {
                role
                artist {
                  id
                }
              }
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
async def test_track_not_found(graphql_query, snapshot):
    query = """
        query {
          track(id: 999) {
            __typename

            ... on Track {
              id
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
async def test_track_no_auth(graphql_query, snapshot):
    query = """
        query {
          track(id: 10) {
            __typename

            ... on Track {
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
