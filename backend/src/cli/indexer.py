from src.cli.commands import commands, shared_options
from src.indexer import index_directories


@commands.command()
@shared_options
def index():
    """Index the music in the music dirs."""
    index_directories()
