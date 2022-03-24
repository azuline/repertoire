import functools
import logging
from typing import Callable

import click

from src.config import initialize_config
from src.migrations.database import run_database_migrations


@click.group()
def commands():  # pragma: no cover
    """A release-oriented music server."""
    pass


def shared_options(func: Callable) -> Callable:
    """
    A decorator to add some shared click options to every command. Currently,
    the ``--log-level`` option is implemented by this decorator.

    This must be applied before the click ``command`` decorator.
    """

    @click.option(
        "--log-level",
        type=click.Choice(["DEBUG", "INFO", "WARNING"]),
        default="INFO",
        help="Logging level",
    )
    @functools.wraps(func)
    def wrapper(*args, log_level: str, **kwargs):
        logger = logging.getLogger()
        logger.setLevel(log_level)
        return func(*args, **kwargs)

    return wrapper


def migrate(func: Callable) -> Callable:
    """
    A decorator to run initial migrations before the command is run.

    This function:

    - Runs database migrations.
    - Updates the configuration if it is outdated.

    This must be applied before the click ``command`` decorator.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        run_database_migrations()
        initialize_config()
        return func(*args, **kwargs)

    return wrapper
