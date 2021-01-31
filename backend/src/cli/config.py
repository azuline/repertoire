import click

from src.cli.commands import commands, shared_options
from src.constants import Constants


@commands.command()
@shared_options
def config():
    """Edit the application config."""
    cons = Constants()
    with cons.config_path.open("r") as fp:
        config_contents = fp.read()

    config_contents = click.edit(config_contents, extension=".ini")

    if config_contents:
        with cons.config_path.open("w+") as fp:
            fp.write(config_contents)
