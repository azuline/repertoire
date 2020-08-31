from backend.cli.commands import commands, shared_options
from backend.lib import build_search_index, index_directories, save_pending_images


@commands.command()
@shared_options
def index():
    """Index the music in the music dirs."""
    index_directories()
    build_search_index()
    save_pending_images()
