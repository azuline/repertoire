import logging
import sys

from yoyo import get_backend, read_migrations

from src.config import write_default_config
from src.constants import IS_PYTEST, IS_SPHINX, Constants

# Configure logging.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add a logging handler for stdout unless we are testing. Pytest
# captures logging output on its own.
if not IS_PYTEST:
    stream_formatter = logging.Formatter("%(name)s - %(message)s")
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(stream_formatter)
    logger.addHandler(stream_handler)


def run_database_migrations():
    cons = Constants()

    db_backend = get_backend(f"sqlite:///{cons.database_path}")
    db_migrations = read_migrations(str(cons.migrations_path))

    with db_backend.lock():
        db_backend.apply_migrations(db_backend.to_apply(db_migrations))


def initialize_config():
    cons = Constants()

    write_default_config(cons.config_path)


# Don't automatically initialize/update application data when testing.
if not IS_PYTEST and not IS_SPHINX:
    run_database_migrations()
    initialize_config()
