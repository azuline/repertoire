from sqlite3 import Connection

from src.library import playlist
from src.fixtures.factory import Factory


def test_query(factory: Factory, db: Connection):
    ply = factory.playlist(name="AAAAAA", conn=db)
    cursor = db.execute(
        """
        SELECT rowid FROM music__playlists__fts
        WHERE music__playlists__fts MATCH '"AAAAAA"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == ply.id


def test_delete(db: Connection):
    # TODO: Dependent on #178.
    pass


def test_update(factory: Factory, db: Connection):
    ply = factory.playlist(name="AAAAAA", conn=db)
    playlist.update(ply, name="New Title", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__playlists__fts
        WHERE music__playlists__fts MATCH '"New Title"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == ply.id
