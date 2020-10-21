from click.testing import CliRunner

from backend.indexer.covers import (
    _get_possible_cover_paths,
    generate_thumbnail,
    save_image,
    save_pending_covers,
)


def test_save_pending_covers(db):
    with CliRunner().isolated_filesystem():
        pass
