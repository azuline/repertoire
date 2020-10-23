import pytest


@pytest.mark.asyncio
async def test_artist(graphql_query, snapshot):
    query = """
        query {
          artist(id: 4) {
            __typename

            ... on Artist {
              id
              name
              favorite
              numReleases

              releases {
                id
              }

              topGenres {
                genre {
                  id
                }
                numMatches
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
async def test_artist_no_auth_not_found(graphql_query, snapshot):
    query = """
        query {
          artist(id: 999999) {
            __typename

            ... on Artist {
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
async def test_artist_no_auth(graphql_query, snapshot):
    query = """
        query {
          artist(id: 4) {
            __typename

            ... on Artist {
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


@pytest.mark.asyncio
async def test_artist_from_name(graphql_query, snapshot):
    query = """
        query {
          artistFromName(name: "Abakus") {
            __typename

            ... on Artist {
              id
              name
              favorite
              numReleases

              releases {
                id
              }

              topGenres {
                genre {
                  id
                }
                numMatches
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
async def test_artist_from_name_not_found(graphql_query, snapshot):
    query = """
        query {
          artistFromName(name: "Random Artist name") {
            __typename

            ... on Artist {
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
async def test_artist_from_name_no_auth(graphql_query, snapshot):
    query = """
        query {
          artistFromName(name: "Abakus") {
            __typename

            ... on Artist {
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
