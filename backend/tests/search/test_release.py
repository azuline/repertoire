from src.enums import ReleaseType
from src.library import release
from tests.conftest import NUM_RELEASES


def test_query(db):
    cursor = db.execute(
        """
        SELECT rowid FROM music__releases__fts
        WHERE music__releases__fts MATCH '"Have Each Other" AND "Aaron West"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 2


def test_insert(db):
    release.create(
        "Title",
        artist_ids=[4],
        release_type=ReleaseType.ALBUM,
        release_year=2000,
        conn=db,
    )

    cursor = db.execute(
        """
        SELECT rowid FROM music__releases__fts
        WHERE music__releases__fts MATCH 'Title AND Abakus'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == NUM_RELEASES + 1


def test_delete(db):
    # TODO: Dependent on #178.
    pass


def test_update(db):
    rls = release.from_id(2, db)
    assert rls is not None

    release.update(rls, title="New Title", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__releases__fts
        WHERE music__releases__fts MATCH '"New Title"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 2
