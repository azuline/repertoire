import pytest

from src.library import release
from src.util import database


@pytest.mark.asyncio
async def test_release(db, graphql_query, snapshot):
    query = """
        query {
            release(id: 3) {
                ...ReleaseFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_release_not_found(db, graphql_query, snapshot):
    query = """
        query {
            release(id: 999) {
                ...ReleaseFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_releases(db, graphql_query, snapshot):
    query = """
        query {
            releases {
                total
                results {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_releases_search(db, graphql_query, snapshot):
    query = """
        query {
            releases(search: "Aaron") {
                total
                results {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_releases_filter_collections(db, graphql_query, snapshot):
    query = """
        query {
            releases(collectionIds: [12]) {
                total
                results {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_releases_filter_artists(db, graphql_query, snapshot):
    query = """
        query {
            releases(artistIds: [2]) {
                total
                results {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_releases_filter_types(db, graphql_query, snapshot):
    query = """
        query {
            releases(releaseTypes: [ALBUM]) {
                total
                results {
                        ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_releases_pagination(db, graphql_query, snapshot):
    query = """
        query {
            releases(page: 2, perPage: 2) {
                total
                results {
                        ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_releases_sort(db, graphql_query, snapshot):
    query = """
        query {
            releases(sort: TITLE) {
                total
                results {
                        ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_releases_sort_desc(db, graphql_query, snapshot):
    query = """
        query {
            releases(sort: TITLE, asc: false) {
                total
                results {
                        ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_create_release(db, graphql_query, snapshot):
    query = """
        mutation {
            createRelease(
                title: "aa"
                artistIds: [2, 3]
                releaseType: ALBUM
                releaseYear: 2020
                releaseDate: "2020-10-23"
            ) {
                ...ReleaseFields
            }
        }
    """
    _, response = await graphql_query(query)
    del response["data"]["createRelease"]["addedOn"]  # It changes every time.

    snapshot.assert_match(response)

    with database() as conn:
        assert release.from_id(4, conn.cursor()) is not None


@pytest.mark.asyncio
async def test_create_release_bad_date(db, graphql_query, snapshot):
    query = """
        mutation {
            createRelease(
                title: "aa"
                artistIds: [2, 3]
                releaseType: ALBUM
                releaseYear: 2020
                releaseDate: "bbbbbb"
            ) {
                ...ReleaseFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    assert release.from_id(4, db) is None


@pytest.mark.asyncio
async def test_create_release_bad_artists(db, graphql_query, snapshot):
    query = """
        mutation {
            createRelease(
                title: "aa"
                artistIds: [2, 3, 9999]
                releaseType: ALBUM
                releaseYear: 2020
                releaseDate: "2020-10-23"
            ) {
                ...ReleaseFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    assert release.from_id(4, db) is None


@pytest.mark.asyncio
async def test_update_release(db, graphql_query, snapshot):
    query = """
        mutation {
            updateRelease(
                id: 2
                title: "aa"
                releaseType: SINGLE
                releaseYear: 2020
                releaseDate: "2020-10-23"
            ) {
                ...ReleaseFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        snapshot.assert_match(release.from_id(2, conn.cursor()))


@pytest.mark.asyncio
async def test_update_release_bad_date(db, graphql_query, snapshot):
    query = """
        mutation {
            updateRelease(
                id: 2
                releaseDate: "bbbbb"
            ) {
                ...ReleaseFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(release.from_id(2, db))


@pytest.mark.asyncio
async def test_update_release_not_found(db, graphql_query, snapshot):
    query = """
        mutation {
            updateRelease(
                id: 99999
                title: "aa"
            ) {
                ...ReleaseFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_add_artist_to_release(db, graphql_query, snapshot):
    query = """
        mutation {
            addArtistToRelease(releaseId: 2, artistId: 3) {
                release {
                    ...ReleaseFields
                }
                artist {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(release.artists(release.from_id(2, cursor), cursor))


@pytest.mark.asyncio
async def test_add_artist_to_release_bad_release(db, graphql_query, snapshot):
    query = """
        mutation {
            addArtistToRelease(releaseId: 999, artistId: 2) {
                release {
                    ...ReleaseFields
                }
                artist {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_add_artist_to_release_bad_artist(db, graphql_query, snapshot):
    query = """
        mutation {
            addArtistToRelease(releaseId: 2, artistId: 9999) {
                release {
                    ...ReleaseFields
                }
                artist {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(release.artists(release.from_id(2, db), db))


@pytest.mark.asyncio
async def test_add_artist_to_release_already_exists(db, graphql_query, snapshot):
    query = """
        mutation {
            addArtistToRelease(releaseId: 2, artistId: 2) {
                release {
                    ...ReleaseFields
                }
                artist {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(release.artists(release.from_id(2, db), db))


@pytest.mark.asyncio
async def test_del_artist_from_release(db, graphql_query, snapshot):
    query = """
        mutation {
            delArtistFromRelease(releaseId: 2, artistId: 2) {
                release {
                    ...ReleaseFields
                }
                artist {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(release.artists(release.from_id(2, cursor), cursor))


@pytest.mark.asyncio
async def test_del_artist_from_release_bad_release(db, graphql_query, snapshot):
    query = """
        mutation {
            delArtistFromRelease(releaseId: 999, artistId: 2) {
                release {
                    ...ReleaseFields
                }
                artist {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_del_artist_from_release_bad_artist(db, graphql_query, snapshot):
    query = """
        mutation {
            delArtistFromRelease(releaseId: 2, artistId: 9999) {
                release {
                    ...ReleaseFields
                }
                artist {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(release.artists(release.from_id(2, db), db))


@pytest.mark.asyncio
async def test_del_artist_from_release_doesnt_exist(db, graphql_query, snapshot):
    query = """
        mutation {
            delArtistFromRelease(releaseId: 3, artistId: 2) {
                release {
                    ...ReleaseFields
                }
                artist {
                    ...ArtistFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
