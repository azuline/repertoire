# flake8: noqa

from .images import save_pending_images
from .indexer import index_directories
from .search import build_search_index


def run_indexer():
    index_directories()
    build_search_index()
    save_pending_images()