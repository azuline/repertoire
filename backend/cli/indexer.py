from backend.cli.commands import commands, shared_options
from backend.indexer import run_indexer


@commands.command()
@shared_options
def index():
    """Index the music in the music dirs."""
    run_indexer()
