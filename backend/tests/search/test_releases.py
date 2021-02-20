def test_query_release_title(db):
    cursor = db.execute(
        """
        SELECT rowid FROM music__releases__fts
        WHERE music__releases__fts MATCH '"Have Each Other"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 2


def test_query_release_artist(db):
    cursor = db.execute(
        """
        SELECT rowid FROM music__releases__fts
        WHERE music__releases__fts MATCH '"Aaron West"'
        ORDER BY rank
        """
    )
    assert cursor.fetchone()[0] == 2
