import click

from backend.cli.commands import commands, shared_options
from backend.library import user
from backend.util import database


@commands.command()
@shared_options
def token():
    """Generate an authentication token."""
    # Currently, we only support a single user.
    with database() as conn:
        cursor = conn.cursor()

        if usr := user.from_id(1, cursor):
            token = user.new_token(usr, cursor)
        else:
            _, token = user.create("admin", cursor)

    click.echo(f"Generated new authentication token: {token.hex()}")
