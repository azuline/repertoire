import pytest

from src.library import release
from src.util import database

RELEASE_RESULT = """
    id
    title
    releaseType
    addedOn
    inInbox
    releaseYear
    numTracks
    runtime
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
"""

RELEASES_RESULT = f"""
    total
    results {{
        {RELEASE_RESULT}
    }}
"""


@pytest.mark.asyncio
async def test_release(db, graphql_query, snapshot):
    query = f"""
        query {{
            release(id: 3) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_release_not_found(db, graphql_query, snapshot):
    query = f"""
        query {{
            release(id: 999) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_release_no_auth(db, graphql_query, snapshot):
    query = f"""
        query {{
            release(id: 3) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_releases(db, graphql_query, snapshot):
    query = f"""
        query {{
            releases {{
                {RELEASES_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_releases_search(db, graphql_query, snapshot):
    query = f"""
        query {{
            releases(search: "Aaron") {{
                {RELEASES_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_releases_filter_collections(db, graphql_query, snapshot):
    query = f"""
        query {{
            releases(collectionIds: [12]) {{
                {RELEASES_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_releases_filter_artists(db, graphql_query, snapshot):
    query = f"""
        query {{
            releases(artistIds: [2]) {{
                {RELEASES_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_releases_filter_types(db, graphql_query, snapshot):
    query = f"""
        query {{
            releases(releaseTypes: [ALBUM]) {{
                {RELEASES_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_releases_pagination(db, graphql_query, snapshot):
    query = f"""
        query {{
            releases(page: 2, perPage: 2) {{
                {RELEASES_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_releases_sort(db, graphql_query, snapshot):
    query = f"""
        query {{
            releases(sort: TITLE) {{
                {RELEASES_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_releases_sort_desc(db, graphql_query, snapshot):
    query = f"""
        query {{
            releases(sort: TITLE, asc: false) {{
                {RELEASES_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_releases_no_auth(db, graphql_query, snapshot):
    query = f"""
        query {{
            releases {{
                {RELEASES_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_create_release(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createRelease(
                title: "aa"
                artistIds: [2, 3]
                releaseType: ALBUM
                releaseYear: 2020
                releaseDate: "2020-10-23"
            ) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    _, response = await graphql_query(query, authed=True)
    del response["data"]["createRelease"]["addedOn"]  # It changes every time.

    snapshot.assert_match(response)

    with database() as conn:
        assert release.from_id(4, conn.cursor()) is not None


@pytest.mark.asyncio
async def test_create_release_bad_date(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createRelease(
                title: "aa"
                artistIds: [2, 3]
                releaseType: ALBUM
                releaseYear: 2020
                releaseDate: "bbbbbb"
            ) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    assert release.from_id(4, db) is None


@pytest.mark.asyncio
async def test_create_release_bad_artists(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createRelease(
                title: "aa"
                artistIds: [2, 3, 9999]
                releaseType: ALBUM
                releaseYear: 2020
                releaseDate: "2020-10-23"
            ) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    assert release.from_id(4, db) is None


@pytest.mark.asyncio
async def test_create_release_no_auth(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            createRelease(
                title: "aa"
                artistIds: [2, 3]
                releaseType: ALBUM
                releaseYear: 2020
                releaseDate: "2020-10-23"
            ) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_update_release(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateRelease(
                id: 2
                title: "aa"
                releaseType: SINGLE
                releaseYear: 2020
                releaseDate: "2020-10-23"
            ) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))

    with database() as conn:
        snapshot.assert_match(release.from_id(2, conn.cursor()))


@pytest.mark.asyncio
async def test_update_release_bad_date(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateRelease(
                id: 2
                releaseDate: "bbbbb"
            ) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(release.from_id(2, db))


@pytest.mark.asyncio
async def test_update_release_not_found(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateRelease(
                id: 99999
                title: "aa"
            ) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_update_release_no_auth(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            updateRelease(
                id: 2
                title: "aa"
            ) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_add_artist_to_release(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addArtistToRelease(releaseId: 2, artistId: 3) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(release.artists(release.from_id(2, cursor), cursor))


@pytest.mark.asyncio
async def test_add_artist_to_release_bad_release(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addArtistToRelease(releaseId: 999, artistId: 2) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_add_artist_to_release_bad_artist(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addArtistToRelease(releaseId: 2, artistId: 9999) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(release.artists(release.from_id(2, db), db))


@pytest.mark.asyncio
async def test_add_artist_to_release_already_exists(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addArtistToRelease(releaseId: 2, artistId: 2) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(release.artists(release.from_id(2, db), db))


@pytest.mark.asyncio
async def test_add_artist_to_release_no_auth(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            addArtistToRelease(releaseId: 2, artistId: 2) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))


@pytest.mark.asyncio
async def test_del_artist_from_release(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delArtistFromRelease(releaseId: 2, artistId: 2) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))

    with database() as conn:
        cursor = conn.cursor()
        snapshot.assert_match(release.artists(release.from_id(2, cursor), cursor))


@pytest.mark.asyncio
async def test_del_artist_from_release_bad_release(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delArtistFromRelease(releaseId: 999, artistId: 2) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_del_artist_from_release_bad_artist(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delArtistFromRelease(releaseId: 2, artistId: 9999) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))
    snapshot.assert_match(release.artists(release.from_id(2, db), db))


@pytest.mark.asyncio
async def test_del_artist_from_release_doesnt_exist(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delArtistFromRelease(releaseId: 3, artistId: 2) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=True))


@pytest.mark.asyncio
async def test_del_artist_from_release_no_auth(db, graphql_query, snapshot):
    query = f"""
        mutation {{
            delArtistFromRelease(releaseId: 2, artistId: 2) {{
                {RELEASE_RESULT}
            }}
        }}
    """
    snapshot.assert_match(await graphql_query(query, authed=False))
