from sqlite3 import Connection

from src.library import collection
from src.testing.factory import Factory


def test_query(factory: Factory, db: Connection):
    col = factory.collection(name="Country", conn=db)
    cursor = db.execute(
        """
        SELECT rowid FROM music__collections__fts
        WHERE music__collections__fts MATCH '"Country"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == col.id


def test_delete(db: Connection):
    # TODO: Dependent on #178.
    pass


def test_update(factory: Factory, db: Connection):
    col = factory.collection(name="Country", conn=db)
    collection.update(col, name="New Title", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__collections__fts
        WHERE music__collections__fts MATCH '"New Title"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == col.id
