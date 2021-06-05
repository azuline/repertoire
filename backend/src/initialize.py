from src.config import initialize_config
from src.migrations.database import run_database_migrations


def initialize_app():
    """
    Initialize repertoire. This function needs to be invoked before other functions in
    the application are invoked, preferably in the application entry point.

    This function:

    - Runs database migrations.
    - Updates the configuration if it is outdated.
    """
    # if not IS_PYTEST and not IS_SPHINX:  # pragma: no cover
    run_database_migrations()
    initialize_config()
