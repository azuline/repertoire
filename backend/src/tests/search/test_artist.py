from sqlite3 import Connection

from src.library import artist
from tests.factory import Factory


def test_query(factory: Factory, db: Connection):
    art = factory.artist(name="Aaron West and the Roaring Seventies", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__artists__fts
        WHERE music__artists__fts MATCH '"Aaron" AND "Seventies"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == art.id


def test_delete(db: Connection):
    # TODO: Dependent on #178.
    pass


def test_update(factory: Factory, db: Connection):
    art = factory.artist(name="Old Mane", conn=db)
    artist.update(art, name="New Name", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__artists__fts
        WHERE music__artists__fts MATCH '"New Name"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == art.id
