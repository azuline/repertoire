# flake8: noqa

from .covers import save_pending_covers
from .scanner import scan_directories


def run_indexer() -> None:
    """Run the two stages of the indexer."""
    scan_directories()
    save_pending_covers()
