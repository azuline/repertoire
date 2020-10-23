import pytest


@pytest.mark.asyncio
async def test_release(graphql_query, snapshot):
    query = """
        query {
          release(id: 3) {
            __typename

            ... on Release {
              id
              title
              releaseType
              addedOn
              inInbox
              releaseYear
              numTracks
              releaseDate
              imagePath

              artists {
                id
              }

              tracks {
                id
              }

              genres {
                id
              }

              labels {
                id
              }

              collages {
                id
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
async def test_release_not_found(graphql_query, snapshot):
    query = """
        query {
          release(id: 999) {
            __typename

            ... on Release {
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
async def test_release_no_auth(graphql_query, snapshot):
    query = """
        query {
          release(id: 3) {
            __typename

            ... on Release {
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
