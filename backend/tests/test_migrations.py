from pathlib import Path

from yoyo import get_backend, read_migrations

from src.constants import Constants


def test_migrations(isolated_dir):
    """
    Test that, for each migration, the up -> down -> up path doesn't
    cause an error. Basically, ladder our way up through the migration
    chain.
    """
    cons = Constants()
    backend = get_backend(f"sqlite:///{Path.cwd() / 'db.sqlite3'}")
    migrations = read_migrations(str(cons.migrations_path))

    for mig in migrations:
        backend.apply_one(mig)
        backend.rollback_one(mig)
        backend.apply_one(mig)
