import shutil
from pathlib import Path

import pytest
from click.testing import CliRunner
from freezegun import freeze_time
from yoyo import get_backend, read_migrations

from src.config import Config, _Config
from src.constants import Constants
from src.util import database, freeze_database_time
from src.webserver.app import create_app
from tests.factory import Factory

SEED_DATA = Path(__file__).parent / "seed_data"


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
