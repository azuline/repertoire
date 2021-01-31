import shutil
import sqlite3
from pathlib import Path

import pytest
import quart
from ariadne import graphql
from click.testing import CliRunner
from yoyo import get_backend, read_migrations

from src.constants import BACKEND_ROOT, Constants
from src.graphql import error_formatter, schema
from src.library import user
from src.util import database
from src.webserver.app import create_app
from src.webserver.routes.graphql import GraphQLContext
from tests.fragments import FRAGMENTS

SEED_DATA = Path(__file__).parent / "seed_data"
TEST_SQL_PATH = SEED_DATA / "database.sql"

ADMIN_TOKEN = "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"


@pytest.fixture(scope="session")
def seed_db():
    db_path = SEED_DATA / "db.sqlite3"
    db_path.unlink(missing_ok=True)

    db_backend = get_backend(f"sqlite:///{db_path}")
    db_migrations = read_migrations(str(BACKEND_ROOT / "src" / "migrations"))

    with db_backend.lock():
        db_backend.apply_migrations(db_backend.to_apply(db_migrations))

    with TEST_SQL_PATH.open("r") as f:
        test_sql = f.read()

    with sqlite3.connect(db_path) as conn:
        conn.executescript(test_sql)
        conn.commit()


@pytest.fixture(autouse=True)
def isolated_dir(seed_db):
    with CliRunner().isolated_filesystem():
        cons = Constants()
        cons.data_path = Path.cwd() / "_data"
        shutil.copytree(SEED_DATA, cons.data_path, dirs_exist_ok=True)
        yield


@pytest.fixture
def db(isolated_dir):
    with database() as conn:
        yield conn.cursor()


@pytest.fixture
def quart_app(isolated_dir):
    yield create_app()


@pytest.fixture
async def quart_client(quart_app):
    def update_kwargs(kwargs):
        kwargs["headers"] = {
            **kwargs.get("headers", {}),
            "Authorization": f"Token {ADMIN_TOKEN}",
        }
        return kwargs

    async with quart_app.app_context():
        async with quart_app.test_client() as test_client:

            async def delete(*args, **kwargs):
                return await test_client.open(*args, **dict(kwargs, method="DELETE"))

            async def authed_get(*args, **kwargs):
                return await test_client.get(*args, **update_kwargs(kwargs))

            async def authed_post(*args, **kwargs):
                return await test_client.post(*args, **update_kwargs(kwargs))

            async def authed_delete(*args, **kwargs):
                return await test_client.delete(*args, **update_kwargs(kwargs))

            test_client.delete = delete
            test_client.authed_get = authed_get
            test_client.authed_post = authed_post
            test_client.authed_delete = authed_delete

            yield test_client


@pytest.fixture
def graphql_query(db, quart_app):
    async def executor(query):
        used_fragments = "\n".join(v for k, v in FRAGMENTS.items() if k in query)
        query = f"{query}\n{used_fragments}"

        async with quart_app.test_request_context("/testing", method="GET"):
            return await graphql(
                schema=schema,
                data={"operationName": None, "variables": {}, "query": query},
                context_value=GraphQLContext(
                    user=user.from_id(1, db),
                    db=db,
                    request=quart.request,
                ),
                error_formatter=error_formatter,
                debug=False,
            )

    yield executor
