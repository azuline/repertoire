from yoyo import get_backend, read_migrations

from src.constants import Constants


def run_database_migrations():
    cons = Constants()

    db_backend = get_backend(f"sqlite:///{cons.database_path}")
    db_migrations = read_migrations(str(cons.migrations_path))

    with db_backend.lock():
        db_backend.apply_migrations(db_backend.to_apply(db_migrations))
