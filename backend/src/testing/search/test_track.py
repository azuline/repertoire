from sqlite3 import Connection

from src.enums import ArtistRole
from src.library import track
from src.testing.factory import Factory


def test_insert_and_query(factory: Factory, db: Connection):
    art = factory.artist(name="Aaron West", conn=db)
    trk = factory.track(
        title="Our Apartment",
        artists=[{"artist_id": art.id, "role": ArtistRole.MAIN}],
        conn=db,
    )

    cursor = db.execute(
        """
        SELECT rowid FROM music__tracks__fts
        WHERE music__tracks__fts MATCH '"Aaron" AND "Our Apartment"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == trk.id


def test_delete(db: Connection):
    # TODO: Dependent on #178.
    pass


def test_update(factory: Factory, db: Connection):
    trk = factory.track(title="Old Name", conn=db)

    track.update(trk, title="New Title", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__tracks__fts
        WHERE music__tracks__fts MATCH '"New Title"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == trk.id
