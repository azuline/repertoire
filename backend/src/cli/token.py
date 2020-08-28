import secrets

import click

from src.cli.commands import commands, shared_options


@commands.command()
@shared_options
def token(username, access):
    """Generate an authentication token."""
    token = "abc"
    click.echo(f"Generated new authentication token: {token}")
