from sqlite3 import Connection

from src.library import release
from src.testing.factory import Factory


def test_query(factory: Factory, db: Connection):
    art = factory.artist(name="Aaron West", conn=db)
    rls = factory.release(
        title="We Will Always Have a Paris",
        artist_ids=[art.id],
        conn=db,
    )

    cursor = db.execute(
        """
        SELECT rowid FROM music__releases__fts
        WHERE music__releases__fts MATCH '"Have a Paris" AND "Aaron West"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == rls.id


def test_delete(db: Connection):
    # TODO: Dependent on #178.
    pass


def test_update(factory: Factory, db: Connection):
    rls = factory.release(title="Old Bible", conn=db)
    release.update(rls, title="New Title", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__releases__fts
        WHERE music__releases__fts MATCH '"New Title"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == rls.id
