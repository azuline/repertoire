from .covers import save_pending_covers
from .scanner import scan_directories


def run_indexer() -> None:
    scan_directories()
