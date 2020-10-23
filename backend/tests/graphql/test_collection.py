import pytest


@pytest.mark.asyncio
async def test_collection(graphql_query, snapshot):
    query = """
        query {
          collection(id: 12) {
            __typename

            ... on Collection {
              id
              name
              favorite
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
async def test_collection_not_found(graphql_query, snapshot):
    query = """
        query {
          collection(id: 999999) {
            __typename

            ... on Collection {
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
async def test_collection_no_auth(graphql_query, snapshot):
    query = """
        query {
          collection(id: 12) {
            __typename

            ... on Collection {
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
async def test_collection_from_name_and_type(graphql_query, snapshot):
    query = """
        query {
          collectionFromNameAndType(name: "Folk", type: GENRE) {
            __typename

            ... on Collection {
              id
              name
              favorite
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
async def test_collection_from_name_and_type_not_found(graphql_query, snapshot):
    query = """
        query {
          collectionFromNameAndType(name: "AAFEFOPAIEFPAJF", type: COLLAGE) {
            __typename

            ... on Collection {
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
async def test_collection_from_name_and_type_no_auth(graphql_query, snapshot):
    query = """
        query {
          collectionFromNameAndType(name: "Folk", type: GENRE) {
            __typename

            ... on Collection {
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
async def test_collections(graphql_query, snapshot):
    query = """
        query {
          collections {
            __typename

            ... on Collections {
              results {
                id
                name
                favorite
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
async def test_collections_type_param(graphql_query, snapshot):
    query = """
        query {
          collections(type: GENRE) {
            __typename

            ... on Collections {
              results {
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
async def test_collections_no_auth(graphql_query, snapshot):
    query = """
        query {
          collections {
            __typename

            ... on Collections {
              results {
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

    snapshot.assert_match(await graphql_query(query, authed=False))
