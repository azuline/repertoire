import sqlite3

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
