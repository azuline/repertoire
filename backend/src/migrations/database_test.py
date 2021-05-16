import sqlite3

from yoyo import get_backend, read_migrations

from src.constants import constants
from src.util import freeze_database_time

from .database import run_database_migrations


def test_run_database_migrations(isolated_dir):
    db_path = isolated_dir / "_data" / "db.sqlite3"
    assert not db_path.exists()
    run_database_migrations()
    assert db_path.exists()

    with sqlite3.connect(str(db_path)) as conn:
        freeze_database_time(conn)
        cursor = conn.execute("SELECT 1 FROM _yoyo_version")
        assert len(cursor.fetchall()) > 0


def test_migrations(isolated_dir):
    """
    Test that, for each migration, the up -> down -> up path doesn't
    cause an error. Basically, ladder our way up through the migration
    chain.
    """
    backend = get_backend(f"sqlite:///{isolated_dir / 'db.sqlite3'}")
    migrations = read_migrations(str(constants.migrations_path))

    for mig in migrations:
        backend.apply_one(mig)
        backend.rollback_one(mig)
        backend.apply_one(mig)
