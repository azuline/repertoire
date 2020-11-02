import click

from src.cli.commands import commands, shared_options
from src.constants import CONFIG_PATH


@commands.command()
@shared_options
def config():
    """Edit the application config."""
    with CONFIG_PATH.open("r") as fp:
        config_contents = fp.read()

    config_contents = click.edit(config_contents, extension=".ini")

    if config_contents:
        with CONFIG_PATH.open("w+") as fp:
            fp.write(config_contents)
