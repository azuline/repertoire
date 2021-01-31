import shutil
from pathlib import Path

from src.constants import Constants
from src.enums import ReleaseType
from src.indexer.covers import save_pending_covers
from src.library import release, track
from tests.conftest import SEED_DATA

NEW_ALBUM = SEED_DATA / "fake_music" / "New Album"
FAKE_COVER = SEED_DATA / "fake_cover.jpg"


def test_save_pending_covers(db, snapshot):
    cwd = Path.cwd()

    # Create two releases, each with one track. Release 1 has no embedded art but
    # has an external cover; release 2 has embedded art and no cover.
    rls1_path = cwd / "rls1"
    track1_path = rls1_path / "track1.flac"
    rls1_path.mkdir()
    shutil.copyfile(NEW_ALBUM / "track1.flac", track1_path)

    artwork1_path = rls1_path / "cover.jpg"
    shutil.copyfile(FAKE_COVER, artwork1_path)

    rls1 = release.create(
        title="a",
        artist_ids=[],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        cursor=db,
    )

    track.create(
        title="a",
        filepath=track1_path,
        sha256=b"0" * 32,
        release_id=rls1.id,
        artists=[],
        duration=100,
        track_number="1",
        disc_number="1",
        cursor=db,
    )

    rls2_path = cwd / "rls2"
    track2_path = rls2_path / "track2.m4a"
    rls2_path.mkdir()
    shutil.copyfile(NEW_ALBUM / "track2.m4a", track2_path)

    rls2 = release.create(
        title="b",
        artist_ids=[],
        release_type=ReleaseType.ALBUM,
        release_year=2020,
        cursor=db,
    )

    track.create(
        title="b",
        filepath=track2_path,
        sha256=b"1" * 32,
        release_id=rls2.id,
        artists=[],
        duration=100,
        track_number="1",
        disc_number="1",
        cursor=db,
    )

    db.execute(
        """
        INSERT INTO images__music_releases_to_fetch (release_id)
        VALUES (?), (?), (?)
        """,
        (1, rls1.id, rls2.id),
    )
    db.connection.commit()

    save_pending_covers()

    cons = Constants()
    saved_covers = sorted([path.name for path in cons.cover_art_dir.iterdir()])
    assert len(saved_covers) == 4
