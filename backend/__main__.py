from gevent import monkey  # isort:skip

monkey.patch_all()  # noqa

import logging
import sys

import click

from src.cli import commands
from src.cli.errors import CliError

logger = logging.getLogger(__name__)


def run():
    try:
        commands()
    except CliError as e:
        click.echo(str(e))
        sys.exit(1)


if __name__ == "__main__":
    run()
