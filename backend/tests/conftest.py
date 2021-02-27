import shutil
import sqlite3
from pathlib import Path

import pytest
import quart
from ariadne import graphql
from click.testing import CliRunner
from freezegun import freeze_time
from quart.testing import QuartClient
from yoyo import get_backend, read_migrations

from src.config import Config, _Config
from src.constants import Constants
from src.graphql import error_formatter, schema
from src.library import user
from src.util import database, freeze_database_time
from src.webserver.app import create_app
from src.webserver.routes.graphql import GraphQLContext
from tests.factory import Factory
from tests.fragments import FRAGMENTS

SEED_DATA = Path(__file__).parent / "seed_data"

ADMIN_TOKEN = "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"

NUM_RELEASES = 3
NUM_ARTISTS = 5
NUM_TRACKS = 21
NUM_COLLECTIONS = 11
NUM_PLAYLISTS = 3
NUM_PLAYLIST_ENTRIES = 8
NUM_IMAGES = 2
NUM_USERS = 2

# These are the next autoincremented DB primary key IDs for each model.
NEXT_RELEASE_ID = NUM_RELEASES + 1
NEXT_ARTIST_ID = NUM_ARTISTS + 1
NEXT_TRACK_ID = NUM_TRACKS + 1
NEXT_COLLECTION_ID = NUM_COLLECTIONS + 1
NEXT_PLAYLIST_ID = NUM_PLAYLISTS + 1
NEXT_PLAYLIST_ENTRY_ID = NUM_PLAYLIST_ENTRIES + 1
NEXT_IMAGE_ID = NUM_IMAGES + 1
NEXT_USER_ID = NUM_USERS + 1


@pytest.fixture(scope="session")
def seed_db():
    db_path = SEED_DATA / "db.sqlite3"
    db_path.unlink(missing_ok=True)

    cons = Constants()
    db_backend = get_backend(f"sqlite:///{db_path}")
    db_migrations = read_migrations(str(cons.migrations_path))

    freeze_database_time(db_backend._connection)

    with db_backend.lock():
        db_backend.apply_migrations(db_backend.to_apply(db_migrations))


@pytest.fixture(autouse=True)
def isolated_dir():
    with CliRunner().isolated_filesystem():
        cons = Constants()
        cons.data_path = Path.cwd() / "_data"
        cons.data_path.mkdir()
        yield Path.cwd()


@pytest.fixture(autouse=True)
def stop_the_clock():
    with freeze_time("2020-01-01 01:01:01"):
        yield


@pytest.fixture
def seed_data(seed_db, isolated_dir):
    cons = Constants()
    shutil.copytree(SEED_DATA, cons.data_path, dirs_exist_ok=True)
    # Update config cache with a new config.
    Config._local.config = _Config()


@pytest.fixture
def db(seed_data):
    with database() as conn:
        yield conn


@pytest.fixture
def factory() -> Factory:
    return Factory()


@pytest.fixture
def quart_app(seed_data):
    yield create_app()


@pytest.fixture
async def quart_client(quart_app):
    def update_kwargs(token: bytes, **kwargs):
        print(f"{token=}")
        kwargs["headers"] = {
            **kwargs.get("headers", {}),
            "Authorization": f"Token {token.hex()}",
        }
        return kwargs

    async with quart_app.app_context():
        async with quart_app.test_client() as test_client:

            async def authed_get(*args, token, **kwargs):
                return await test_client.get(*args, **update_kwargs(token, **kwargs))

            async def authed_post(*args, token, **kwargs):
                return await test_client.post(*args, **update_kwargs(token, **kwargs))

            async def authed_delete(*args, token, **kwargs):
                return await test_client.delete(*args, **update_kwargs(token, **kwargs))

            test_client.authed_get = authed_get
            test_client.authed_post = authed_post
            test_client.authed_delete = authed_delete

            yield test_client


@pytest.fixture
def graphql_query(seed_data, quart_app):
    async def executor(query):
        used_fragments = "\n".join(v for k, v in FRAGMENTS.items() if k in query)
        query = f"{query}\n{used_fragments}"

        async with quart_app.test_request_context("/testing", method="GET"):
            with database() as conn:
                return await graphql(
                    schema=schema,
                    data={"operationName": None, "variables": {}, "query": query},
                    context_value=GraphQLContext(
                        user=user.from_id(1, conn),  # type: ignore
                        db=conn,
                        request=quart.request,
                    ),
                    error_formatter=error_formatter,
                    debug=False,
                )

    yield executor
