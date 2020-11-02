from src.enums import ArtistRole, ReleaseType
from src.indexer.search import _words_from_string, build_search_index
from src.library import artist, release, track


def test_search_index(db):
    db.execute("DELETE FROM music__releases_search_index")
    db.connection.commit()

    art1 = artist.create("artist1a artist1b", db)
    art2 = artist.create("Artist2a Artist2b", db)

    rls = release.create(
        title="release title",
        artist_ids=[art1.id, art2.id],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        cursor=db,
    )

    art3 = artist.create("artist3a, artist3b", db)

    track.create(
        title="i got a hát title",
        filepath="/1.flac",
        sha256=b"0" * 32,
        release_id=rls.id,
        artists=[
            {"artist_id": art1.id, "role": ArtistRole.MAIN},
            {"artist_id": art3.id, "role": ArtistRole.FEATURE},
        ],
        duration=100,
        track_number="1",
        disc_number="1",
        cursor=db,
    )

    build_search_index()

    words = {
        "artist1a",
        "artist1b",
        "Artist2a",
        "Artist2b",
        "release",
        "title",
        "artist3a",
        "artist3b",
        "i",
        "got",
        "a",
        "hát",
        "hat",
    }

    db.execute(
        "SELECT word FROM music__releases_search_index WHERE release_id = ?",
        (rls.id,),
    )

    assert words == {row[0] for row in db.fetchall()}


def test_words_from_string():
    words = _words_from_string("i got a hát title")
    assert {"i", "got", "a", "hát", "hat", "title"} == words
