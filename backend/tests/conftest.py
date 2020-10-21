import shutil
from pathlib import Path

import pytest
from yoyo import get_backend, read_migrations

from backend.constants import PROJECT_ROOT
from backend.util import database

FAKE_DATA = Path(__file__).parent / "fake_data"
DATABASE_PATH = FAKE_DATA / "db.sqlite3"
DATABASE_JOURNAL_PATH = FAKE_DATA / "db.sqlite3-journal"
TEST_SQL_PATH = Path(__file__).parent / "database.sql"

COVER_ART = FAKE_DATA / "cover_art"
LOGS = FAKE_DATA / "logs"


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
    db_migrations = read_migrations(str(PROJECT_ROOT / "backend" / "migrations"))

    with db_backend.lock():
        db_backend.apply_migrations(db_backend.to_apply(db_migrations))

    with TEST_SQL_PATH.open("r") as f:
        test_sql = f.read()

    with database() as conn:
        conn.executescript(test_sql)
        yield conn.cursor()
