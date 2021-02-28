import pytest

from src.library import release


@pytest.mark.asyncio
async def test_release(graphql_query, snapshot):
    query = """
        query {
            release(id: 3) {
                ...ReleaseFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_release_not_found(graphql_query, snapshot):
    query = """
        query {
            release(id: 999) {
                ...ReleaseFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_releases(graphql_query, snapshot):
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
async def test_releases_search(graphql_query, snapshot):
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
async def test_releases_filter_collections(graphql_query, snapshot):
    query = """
        query {
            releases(collectionIds: [3]) {
                total
                results {
                    ...ReleaseFields
                }
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))


@pytest.mark.asyncio
async def test_releases_filter_artists(graphql_query, snapshot):
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
async def test_releases_filter_types(graphql_query, snapshot):
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
async def test_releases_pagination(graphql_query, snapshot):
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
async def test_releases_sort(graphql_query, snapshot):
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
async def test_releases_sort_desc(graphql_query, snapshot):
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
    snapshot.assert_match(response)
    assert release.from_id(NEXT_RELEASE_ID, db) is not None


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
    assert release.from_id(NEXT_RELEASE_ID, db) is None


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
    assert release.from_id(NEXT_RELEASE_ID, db) is None


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
                rating: 1
            ) {
                ...ReleaseFields
            }
        }
    """
    snapshot.assert_match(await graphql_query(query))
    snapshot.assert_match(release.from_id(2, db))


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
async def test_update_release_not_found(graphql_query, snapshot):
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
    rls = release.from_id(2, db)
    assert rls is not None
    snapshot.assert_match(release.artists(rls, db))


@pytest.mark.asyncio
async def test_add_artist_to_release_bad_release(graphql_query, snapshot):
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
    rls = release.from_id(2, db)
    assert rls is not None
    snapshot.assert_match(release.artists(rls, db))


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
    rls = release.from_id(2, db)
    assert rls is not None
    snapshot.assert_match(release.artists(rls, db))


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
    rls = release.from_id(2, db)
    assert rls is not None
    snapshot.assert_match(release.artists(rls, db))


@pytest.mark.asyncio
async def test_del_artist_from_release_bad_release(graphql_query, snapshot):
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
    rls = release.from_id(2, db)
    assert rls is not None
    snapshot.assert_match(release.artists(rls, db))


@pytest.mark.asyncio
async def test_del_artist_from_release_doesnt_exist(graphql_query, snapshot):
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


@pytest.mark.asyncio
async def test_release_years(graphql_query, snapshot):
    query = """
        query {
            releaseYears
        }
    """
    snapshot.assert_match(await graphql_query(query))
