# flake8: noqa

from .covers import save_pending_covers
from .scanner import scan_directories
from src.tasks import huey
from src.config import config


def run_indexer() -> None:
    """Run the two stages of the indexer."""
    scan_directories()
    save_pending_covers()


@huey.periodic_task(config.index_crontab)
def indexer():
    run_indexer()
