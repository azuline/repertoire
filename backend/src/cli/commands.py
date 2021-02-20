import functools
import logging
from typing import Callable

import click


@click.group()
def commands():  # pragma: no cover
    """A release-oriented music server."""
    pass


def shared_options(func: Callable) -> Callable:
    """
    A decorator to add some shared click options to every command. Currently,
    the ``--log-level`` option is implemented by this decorator.

    This must be applied before the click ``command`` decorator.

    :param Callable func: The function to decorate.

    :return: The decorated function.
    :rtype: Callable
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
