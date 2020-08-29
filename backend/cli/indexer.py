from backend.cli.commands import commands, shared_options
from backend.indexer import index_directories


@commands.command()
@shared_options
def index():
    """Index the music in the music dirs."""
    index_directories()
