from pathlib import Path

import pytest
from yoyo import get_backend, read_migrations

from backend.constants import PROJECT_ROOT
from backend.util import database

DATA_PATH = Path(__file__).parent / "fake_data"
DATABASE_PATH = DATA_PATH / "db.sqlite3"
TEST_SQL_PATH = Path(__file__).parent / "database.sql"


@pytest.fixture
def data_path():
    return DATA_PATH


@pytest.fixture
def db():
    DATABASE_PATH.unlink(missing_ok=True)

    db_backend = get_backend(f"sqlite:///{DATABASE_PATH}")
    db_migrations = read_migrations(str(PROJECT_ROOT / "backend" / "migrations"))

    with db_backend.lock():
        db_backend.apply_migrations(db_backend.to_apply(db_migrations))

    with TEST_SQL_PATH.open("r") as f:
        test_sql = f.read()

    with database() as conn:
        conn.executescript(test_sql)
        yield conn.cursor()
