from datetime import date

import pytest

from src.enums import ReleaseType
from src.library import release


@pytest.mark.asyncio
async def test_release(graphql_query, snapshot):
    query = """
        query {
            release(id: 2) {
                ...ReleaseFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_release_not_found(graphql_query, snapshot):
    query = """
        query {
            release(id: 999) {
                ...ReleaseFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_releases_search(graphql_query, snapshot):
    query = """
        query {
            releases(search: "Release1") {
                total
                results {
                    ...ReleaseFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_releases_filter_collections(graphql_query, snapshot):
    query = """
        query {
            releases(collectionIds: [5]) {
                total
                results {
                    ...ReleaseFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_create_release(db, graphql_query, snapshot):
    query = """
        mutation {
            createRelease(
                title: "NewRelease"
                artistIds: [2, 3]
                releaseType: ALBUM
                releaseYear: 2020
                releaseDate: "2020-10-23"
            ) {
                ...ReleaseFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    rls = release.from_id(data["data"]["createRelease"]["id"], db)
    assert rls is not None
    assert rls.title == "NewRelease"
    assert rls.release_type == ReleaseType.ALBUM
    assert rls.release_year == 2020
    assert rls.release_date == date(2020, 10, 23)

    assert {2, 3} == {a.id for a in release.artists(rls, db)}


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    rls = release.from_id(2, db)
    assert rls.title == "aa"
    assert rls.release_type == ReleaseType.SINGLE
    assert rls.release_year == 2020
    assert rls.release_date == date(2020, 10, 23)
    assert rls.rating == 1


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    rls = release.from_id(2, db)
    assert rls.release_date == date(1970, 2, 5)


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_add_artist_to_release(db, graphql_query, snapshot):
    query = """
        mutation {
            addArtistToRelease(releaseId: 2, artistId: 5) {
                release {
                    ...ReleaseFields
                }
                artist {
                    ...ArtistFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    rls = release.from_id(2, db)
    assert rls is not None
    assert 5 in [a.id for a in release.artists(rls, db)]


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    rls = release.from_id(2, db)
    assert rls is not None

    before_artists = release.artists(rls, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    after_artists = release.artists(rls, db)

    assert before_artists == after_artists


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
    rls = release.from_id(2, db)
    assert rls is not None

    before_artists = release.artists(rls, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    after_artists = release.artists(rls, db)

    assert before_artists == after_artists


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
    rls = release.from_id(2, db)
    assert rls is not None

    assert 2 in [a.id for a in release.artists(rls, db)]

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    assert 2 not in [a.id for a in release.artists(rls, db)]


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
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


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
    rls = release.from_id(2, db)
    assert rls is not None

    before_artists = release.artists(rls, db)

    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    after_artists = release.artists(rls, db)

    assert before_artists == after_artists


@pytest.mark.asyncio
async def test_del_artist_from_release_doesnt_exist(graphql_query, snapshot):
    query = """
        mutation {
            delArtistFromRelease(releaseId: 3, artistId: 1) {
                release {
                    ...ReleaseFields
                }
                artist {
                    ...ArtistFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_release_years(graphql_query, snapshot):
    query = """
        query {
            releaseYears
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)
