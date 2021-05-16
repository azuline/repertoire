from yoyo import get_backend, read_migrations

from src.constants import constants


def run_database_migrations():
    db_backend = get_backend(f"sqlite:///{constants.database_path}")
    db_migrations = read_migrations(str(constants.migrations_path))

    with db_backend.lock():
        db_backend.apply_migrations(db_backend.to_apply(db_migrations))
