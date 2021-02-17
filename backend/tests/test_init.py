import sqlite3

from src import initialize_config, run_database_migrations


def test_run_database_migrations(isolated_dir):
    db_path = isolated_dir / "_data" / "db.sqlite3"
    assert not db_path.exists()
    run_database_migrations()
    assert db_path.exists()

    with sqlite3.connect(str(db_path)) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM _yoyo_version")
        assert len(cursor.fetchall()) > 0


def test_initialize_config(isolated_dir):
    cfg_path = isolated_dir / "_data" / "config.ini"
    assert not cfg_path.exists()
    initialize_config()
    assert cfg_path.exists()

    with cfg_path.open("r") as fp:
        assert "[repertoire]" in fp.read()
