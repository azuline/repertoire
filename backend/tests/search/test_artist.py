from src.library import artist
from tests.conftest import NUM_ARTISTS


def test_query(db):
    cursor = db.execute(
        """
        SELECT rowid FROM music__artists__fts
        WHERE music__artists__fts MATCH '"Aaron"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 2


def test_insert(db):
    artist.create("Name", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__artists__fts
        WHERE music__artists__fts MATCH 'Name'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == NUM_ARTISTS + 1


def test_delete(db):
    # TODO: Dependent on #178.
    pass


def test_update(db):
    col = artist.from_id(3, db)
    assert col is not None

    artist.update(col, name="New Name", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__artists__fts
        WHERE music__artists__fts MATCH '"New Name"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 3
