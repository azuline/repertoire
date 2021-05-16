import click

from src.cli.commands import commands, shared_options
from src.constants import constants


@commands.command()
@shared_options
def config():
    """Edit the application config."""
    with constants.config_path.open("r") as fp:
        config_contents = fp.read()

    config_contents = click.edit(config_contents, extension=".ini")

    if config_contents:
        with constants.config_path.open("w+") as fp:
            fp.write(config_contents)
