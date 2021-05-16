# flake8: noqa

from src.config import config
from src.tasks import huey

from .covers import save_pending_covers
from .scanner import scan_directories


def run_indexer() -> None:
    """Run the two stages of the indexer."""
    scan_directories()
    save_pending_covers()


@huey.periodic_task(config.index_crontab)
def indexer():
    run_indexer()
