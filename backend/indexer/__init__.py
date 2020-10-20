# flake8: noqa

from .covers import save_pending_covers
from .scanner import scan_directories
from .search import build_search_index


def run_indexer() -> None:
    """Run the three stages of the indexer."""
    scan_directories()
    build_search_index()
    save_pending_covers()
