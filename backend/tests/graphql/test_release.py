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
              hasCover

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


@pytest.mark.asyncio
async def test_releases(graphql_query, snapshot):
    query = """
        query {
          releases {
            __typename

            ... on Releases {
              total
              results {
                id
                title
                releaseType
                addedOn
                inInbox
                releaseYear
                numTracks
                releaseDate
                hasCover

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
async def test_releases_search(graphql_query, snapshot):
    query = """
        query {
          releases(search: "Aaron") {
            __typename

            ... on Releases {
              total
              results {
                id
                title
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
async def test_releases_filter_collections(graphql_query, snapshot):
    query = """
        query {
          releases(collections: [12]) {
            __typename

            ... on Releases {
              total
              results {
                id
                title
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
async def test_releases_filter_artists(graphql_query, snapshot):
    query = """
        query {
          releases(artists: [2]) {
            __typename

            ... on Releases {
              total
              results {
                id
                title
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
async def test_releases_filter_types(graphql_query, snapshot):
    query = """
        query {
          releases(releaseTypes: [ALBUM]) {
            __typename

            ... on Releases {
              total
              results {
                id
                title
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
async def test_releases_pagination(graphql_query, snapshot):
    query = """
        query {
          releases(page: 2, perPage: 2) {
            __typename

            ... on Releases {
              total
              results {
                id
                title
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
async def test_releases_sort(graphql_query, snapshot):
    query = """
        query {
          releases(sort: TITLE) {
            __typename

            ... on Releases {
              total
              results {
                id
                title
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
async def test_releases_sort_desc(graphql_query, snapshot):
    query = """
        query {
          releases(sort: TITLE, asc: false) {
            __typename

            ... on Releases {
              total
              results {
                id
                title
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
async def test_releases_no_auth(graphql_query, snapshot):
    query = """
        query {
          releases {
            __typename

            ... on Releases {
              total
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
