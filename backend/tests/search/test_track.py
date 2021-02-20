from pathlib import Path

from src.enums import ArtistRole
from src.library import track
from tests.conftest import NEXT_TRACK_ID


def test_query(db):
    cursor = db.execute(
        """
        SELECT rowid FROM music__tracks__fts
        WHERE music__tracks__fts MATCH '"Aaron" AND "Our Apartment"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 1


def test_insert(db):
    track.create(
        "Title",
        filepath=Path("/tmp/hello.m4a"),
        sha256=b"0" * 32,
        release_id=1,
        artists=[{"artist_id": 4, "role": ArtistRole.MAIN}],
        duration=100,
        track_number="1",
        disc_number="1",
        conn=db,
    )

    cursor = db.execute(
        """
        SELECT rowid FROM music__tracks__fts
        WHERE music__tracks__fts MATCH 'Title AND Abakus'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == NEXT_TRACK_ID


def test_delete(db):
    # TODO: Dependent on #178.
    pass


def test_update(db):
    trk = track.from_id(1, db)
    assert trk is not None

    track.update(trk, title="New Title", conn=db)

    cursor = db.execute(
        """
        SELECT rowid FROM music__tracks__fts
        WHERE music__tracks__fts MATCH '"New Title"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 1
