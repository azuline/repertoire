from src.library import playlist
from tests.conftest import NEXT_PLAYLIST_ID


def test_query(db):
    cursor = db.execute(
        """
        SELECT rowid FROM music__playlists__fts
        WHERE music__playlists__fts MATCH '"AAAAAA"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 1


def test_insert(db):
    playlist.create(
        conn=db,
    )

    cursor = db.execute(
        """
        SELECT rowid FROM music__playlists__fts
        WHERE music__playlists__fts MATCH 'Title AND Abakus'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == NEXT_playlist_ID


def test_delete(db):
    # TODO: Dependent on #178.
    pass


def test_update(db):
    trk = playlist.from_id(1, db)
    assert trk is not None

    playlist.update(trk, title="New Title", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__playlists__fts
        WHERE music__playlists__fts MATCH '"New Title"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 1
