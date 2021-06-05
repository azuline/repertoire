import logging
import sys

import click

from src.cli import commands
from src.errors import CliError, InvalidConfig
from src.initialize import initialize_app

logger = logging.getLogger(__name__)


def run():
    initialize_app()

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
