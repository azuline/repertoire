import functools
import logging

import click


@click.group()
def commands():
    """A release-oriented music server."""
    pass


def shared_options(func):
    """
    A decorator to add some shared click options to every command. Currently,
    the --log-level option is implemented by this decorator.

    :param Callable func: The function to decorate.

    :return: The decorated function.
    :rtype: Callable
    """

    @click.option(
        "--log-level",
        type=click.Choice(["DEBUG", "INFO"]),
        default="INFO",
        help="Logging level",
    )
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger()
        logger.setLevel(kwargs.get("log_level"))
        del kwargs["log_level"]
        return func(*args, **kwargs)

    return wrapper
