from src.enums import CollectionType
from src.library import collection
from tests.conftest import NUM_COLLECTIONS


def test_query(db):
    cursor = db.execute(
        """
        SELECT rowid FROM music__collections__fts
        WHERE music__collections__fts MATCH '"Country"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 5


def test_insert(db):
    collection.create("Title", type=CollectionType.COLLAGE, conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__collections__fts
        WHERE music__collections__fts MATCH 'Title'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == NUM_COLLECTIONS + 1


def test_delete(db):
    # TODO: Dependent on #178.
    pass


def test_update(db):
    col = collection.from_id(3, db)
    assert col is not None

    collection.update(col, name="New Title", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__collections__fts
        WHERE music__collections__fts MATCH '"New Title"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 3
