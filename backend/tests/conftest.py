import shutil
from pathlib import Path

import pytest
import quart
from ariadne import graphql
from yoyo import get_backend, read_migrations

from src.constants import PROJECT_ROOT
from src.graphql import error_formatter, schema
from src.library import user
from src.util import database
from src.webserver.app import create_app
from src.webserver.routes.graphql import GraphQLContext

FAKE_DATA = Path(__file__).parent / "fake_data"
DATABASE_PATH = FAKE_DATA / "db.sqlite3"
DATABASE_JOURNAL_PATH = FAKE_DATA / "db.sqlite3-journal"
TEST_SQL_PATH = Path(__file__).parent / "database.sql"

COVER_ART = FAKE_DATA / "cover_art"
LOGS = FAKE_DATA / "logs"

ADMIN_TOKEN = "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"


@pytest.fixture(autouse=True)
def clear_fake_data_logs_and_covers():
    shutil.rmtree(COVER_ART, ignore_errors=True)
    shutil.rmtree(LOGS, ignore_errors=True)

    COVER_ART.mkdir()
    LOGS.mkdir()


@pytest.fixture
def db():
    DATABASE_PATH.unlink(missing_ok=True)
    DATABASE_JOURNAL_PATH.unlink(missing_ok=True)

    db_backend = get_backend(f"sqlite:///{DATABASE_PATH}")
    db_migrations = read_migrations(
        str(PROJECT_ROOT / "backend" / "src" / "migrations")
    )

    with db_backend.lock():
        db_backend.apply_migrations(db_backend.to_apply(db_migrations))

    with TEST_SQL_PATH.open("r") as f:
        test_sql = f.read()

    with database() as conn:
        conn.executescript(test_sql)
        conn.commit()
        yield conn.cursor()


@pytest.fixture
def quart_app():
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

            async def authed_get(*args, **kwargs):
                return await test_client.get(*args, **update_kwargs(kwargs))

            async def authed_post(*args, **kwargs):
                return await test_client.post(*args, **update_kwargs(kwargs))

            test_client.authed_get = authed_get
            test_client.authed_post = authed_post

            yield test_client


@pytest.fixture
def graphql_query(db, quart_app):
    async def executor(query):
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
