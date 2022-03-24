import click

from src.cli.commands import commands, shared_options
from src.library import user
from src.util import database, transaction


@commands.command()
@shared_options
def token():
    """Generate an authorization token."""
    # Currently, we only support a single user.
    with transaction() as conn:
        if usr := user.from_id(1, conn):
            token = user.new_token(usr, conn)
        else:
            _, token = user.create("admin", conn)

    click.echo(f"Generated new authorization token: {token.hex()}")
