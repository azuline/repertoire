from src.cli.commands import commands, migrate, shared_options
from src.indexer import run_indexer


@commands.command()
@migrate
@shared_options
def index():
    """Index the music in the music dirs."""
    run_indexer()
