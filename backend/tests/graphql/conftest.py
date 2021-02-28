"""
This file inserts the data we use to seed the API for the GraphQL tests.

The GraphQL tests are simple snapshot tests over the API responses containing sample
data.
"""

import shutil
import sqlite3
from datetime import date
from pathlib import Path
from sqlite3 import Connection

import pytest

from src.constants import Constants
from src.enums import ArtistRole, CollectionType, PlaylistType, ReleaseType
from src.library import collection
from src.library import playlist_entry as pentry
from src.util import freeze_database_time
from tests.conftest import SEED_DATA
from tests.factory import Factory

GQL_DB_PATH = SEED_DATA / "gql_db.sqlite3"


@pytest.fixture(scope="session")
def seed_gql_db(seed_db):
    """
    This fixture augments the existing migrated seed database with test data.
    """
    GQL_DB_PATH.unlink(missing_ok=True)

    seed_db_path = SEED_DATA / "db.sqlite3"
    shutil.copyfile(seed_db_path, GQL_DB_PATH)

    with sqlite3.connect(
        GQL_DB_PATH,
        detect_types=sqlite3.PARSE_DECLTYPES,
    ) as conn:
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        freeze_database_time(conn)
        _add_test_data(conn)


@pytest.fixture(autouse=True)
def seed_gql_data(seed_data, seed_gql_db):
    """
    This fixture replaces the seeded database in the isolated test directory with the
    database containing test data.
    """
    cons = Constants()
    cons.database_path.unlink(missing_ok=True)
    shutil.copyfile(GQL_DB_PATH, cons.database_path)


def _add_test_data(conn: Connection):
    factory = Factory()

    usr_admin, _ = factory.user(nickname="admin", conn=conn)
    usr_blissful, _ = factory.user(nickname="blissful", conn=conn)

    # These start at ID 2.

    artists = [
        factory.artist(name="Artist1", conn=conn),
        factory.artist(name="Artist2", conn=conn),
        factory.artist(name="Artist3", conn=conn),
        factory.artist(name="Artist4", conn=conn),
        factory.artist(name="Artist5", conn=conn),
    ]

    # These start at ID 3.

    collages = [
        factory.collection(name="Collage1", type=CollectionType.COLLAGE, conn=conn),
        factory.collection(name="Collage2", type=CollectionType.COLLAGE, conn=conn),
        factory.collection(name="Collage3", type=CollectionType.COLLAGE, conn=conn),
    ]

    labels = [
        factory.collection(name="Label1", type=CollectionType.LABEL, conn=conn),
        factory.collection(name="Label2", type=CollectionType.LABEL, conn=conn),
        factory.collection(name="Label3", type=CollectionType.LABEL, conn=conn),
    ]

    genres = [
        factory.collection(name="Genre1", type=CollectionType.GENRE, conn=conn),
        factory.collection(name="Genre2", type=CollectionType.GENRE, conn=conn),
        factory.collection(name="Genre3", type=CollectionType.GENRE, conn=conn),
    ]

    # These start at ID 1.

    images = [
        factory.mock_image(path=Path.cwd() / "image1.png", conn=conn),
        factory.mock_image(path=Path.cwd() / "image2.png", conn=conn),
        factory.mock_image(path=Path.cwd() / "image3.png", conn=conn),
    ]

    # These start at ID 2.

    playlists = [
        factory.playlist(name="Playlist1", type=PlaylistType.PLAYLIST, conn=conn),
        factory.playlist(name="Playlist2", type=PlaylistType.PLAYLIST, conn=conn),
        factory.playlist(name="Playlist3", type=PlaylistType.PLAYLIST, conn=conn),
    ]

    # These start at ID 2.

    releases = [
        factory.release(
            title="Release1",
            artist_ids=[artists[0].id, artists[1].id],
            release_type=ReleaseType.ALBUM,
            release_year=1970,
            release_date=date(1970, 2, 5),
            rating=8,
            image_id=images[0].id,
            conn=conn,
        ),
        factory.release(
            title="Release2",
            artist_ids=[artists[1].id, artists[2].id],
            release_type=ReleaseType.ALBUM,
            release_year=1980,
            release_date=None,
            rating=None,
            image_id=None,
            conn=conn,
        ),
        factory.release(
            title="Release3",
            artist_ids=[artists[3].id],
            release_type=ReleaseType.COMPILATION,
            release_year=1990,
            release_date=date(1970, 2, 5),
            rating=None,
            image_id=images[1].id,
            conn=conn,
        ),
        factory.release(
            title="Release4",
            artist_ids=[artists[0].id, artists[2].id, artists[4].id],
            release_type=ReleaseType.UNKNOWN,
            release_year=2000,
            release_date=None,
            rating=2,
            image_id=None,
            conn=conn,
        ),
        factory.release(
            title="Release5",
            artist_ids=[],
            release_type=ReleaseType.EP,
            release_year=2010,
            release_date=None,
            rating=5,
            image_id=images[2].id,
            conn=conn,
        ),
    ]

    collection.add_release(collages[0], releases[0].id, conn)
    collection.add_release(collages[0], releases[1].id, conn)
    collection.add_release(collages[0], releases[2].id, conn)
    collection.add_release(collages[1], releases[0].id, conn)

    collection.add_release(labels[0], releases[0].id, conn)
    collection.add_release(labels[0], releases[1].id, conn)
    collection.add_release(labels[1], releases[2].id, conn)
    collection.add_release(labels[1], releases[3].id, conn)

    collection.add_release(genres[0], releases[0].id, conn)
    collection.add_release(genres[0], releases[1].id, conn)
    collection.add_release(genres[0], releases[2].id, conn)
    collection.add_release(genres[1], releases[0].id, conn)
    collection.add_release(genres[1], releases[1].id, conn)
    collection.add_release(genres[1], releases[2].id, conn)
    collection.add_release(genres[2], releases[3].id, conn)
    collection.add_release(genres[2], releases[4].id, conn)

    # These start at ID 0.

    r1tracks = [
        factory.track(
            title=f"Track{i}",
            filepath=Path.cwd() / "music" / f"track{i}.flac",
            sha256=bytes([i] * 32),
            release_id=releases[0].id,
            artists=[
                {"artist_id": artists[0].id, "role": ArtistRole.MAIN},
                {"artist_id": artists[1].id, "role": ArtistRole.PRODUCER},
            ],
            duration=i,
            track_number=str(i),
            disc_number="1",
            conn=conn,
        )
        for i in range(3)
    ]
    r2tracks = [
        factory.track(
            title=f"Track{i}",
            filepath=Path.cwd() / "music" / f"track{i}.flac",
            sha256=bytes([i] * 32),
            release_id=releases[1].id,
            artists=[
                {"artist_id": artists[1].id, "role": ArtistRole.MAIN},
                {"artist_id": artists[2].id, "role": ArtistRole.FEATURE},
            ],
            duration=i,
            track_number=str(i),
            disc_number=str(i),
            conn=conn,
        )
        for i in range(3, 5)
    ]
    r3tracks = [
        factory.track(
            title=f"Track{i}",
            filepath=Path.cwd() / "music" / f"track{i}.flac",
            sha256=bytes([i] * 32),
            release_id=releases[2].id,
            artists=[{"artist_id": artists[3].id, "role": ArtistRole.MAIN}],
            duration=i,
            track_number=str(i),
            disc_number="1",
            conn=conn,
        )
        for i in range(5, 8)
    ]
    r4tracks = [
        factory.track(
            title=f"Track{i}",
            filepath=Path.cwd() / "music" / f"track{i}.flac",
            sha256=bytes([i] * 32),
            release_id=releases[3].id,
            artists=[
                {"artist_id": artists[0].id, "role": ArtistRole.MAIN},
                {"artist_id": artists[2].id, "role": ArtistRole.FEATURE},
                {"artist_id": artists[4].id, "role": ArtistRole.REMIXER},
            ],
            duration=i,
            track_number=str(i),
            disc_number="1",
            conn=conn,
        )
        for i in range(8, 13)
    ]
    r5tracks = [
        factory.track(
            title=f"Track{i}",
            filepath=Path.cwd() / "music" / f"track{i}.flac",
            sha256=bytes([i] * 32),
            release_id=releases[4].id,
            artists=[],
            duration=i,
            track_number=str(i),
            disc_number=str(i),
            conn=conn,
        )
        for i in range(13, 15)
    ]

    tracks = r1tracks + r2tracks + r3tracks + r4tracks + r5tracks

    # These start at ID 1.

    for trk in tracks[:5]:
        pentry.create(playlists[0].id, trk.id, conn)
    for trk in tracks[5:8]:
        pentry.create(playlists[1].id, trk.id, conn)
    for trk in tracks[5:10]:
        pentry.create(playlists[2].id, trk.id, conn)
