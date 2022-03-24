import logging
import sys

import click

from src.cli import commands
from src.errors import CliError, InvalidConfig

logger = logging.getLogger(__name__)


def run():
    try:
        commands()
    except CliError as e:
        click.echo(str(e))
        sys.exit(1)
    except InvalidConfig as e:
        click.echo(f"Config error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run()
