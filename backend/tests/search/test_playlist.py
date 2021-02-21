from src.enums import PlaylistType
from src.library import playlist
from tests.conftest import NUM_PLAYLISTS


def test_query(db):
    cursor = db.execute(
        """
        SELECT rowid FROM music__playlists__fts
        WHERE music__playlists__fts MATCH '"AAAAAA"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 2


def test_insert(db):
    playlist.create("Title", type=PlaylistType.PLAYLIST, conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__playlists__fts
        WHERE music__playlists__fts MATCH 'Title'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == NUM_PLAYLISTS + 1


def test_delete(db):
    # TODO: Dependent on #178.
    pass


def test_update(db):
    ply = playlist.from_id(2, db)
    assert ply is not None

    playlist.update(ply, name="New Title", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__playlists__fts
        WHERE music__playlists__fts MATCH '"New Title"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 2
