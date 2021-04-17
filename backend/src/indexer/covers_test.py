import shutil
from pathlib import Path
from sqlite3 import Connection

from src.conftest import SEED_DATA
from src.constants import Constants
from src.fixtures.factory import Factory

from .covers import save_pending_covers

NEW_ALBUM = SEED_DATA / "fake_music" / "New Album"
FAKE_COVER = SEED_DATA / "fake_cover.jpg"


def test_save_pending_covers(factory: Factory, db: Connection, snapshot):
    cwd = Path.cwd()

    # Create two releases, each with one track. Release 1 has no embedded art but
    # has an external cover; release 2 has embedded art and no cover.
    rls1_path = cwd / "rls1"
    track1_path = rls1_path / "track1.flac"
    rls1_path.mkdir()
    shutil.copyfile(NEW_ALBUM / "track1.flac", track1_path)

    artwork1_path = rls1_path / "cover.jpg"
    shutil.copyfile(FAKE_COVER, artwork1_path)

    rls1 = factory.release(conn=db)
    factory.track(filepath=track1_path, release_id=rls1.id, conn=db)

    rls2_path = cwd / "rls2"
    track2_path = rls2_path / "track2.m4a"
    rls2_path.mkdir()
    shutil.copyfile(NEW_ALBUM / "track2.m4a", track2_path)

    rls2 = factory.release(conn=db)
    factory.track(filepath=track2_path, release_id=rls2.id, conn=db)

    db.execute(
        """
        INSERT INTO music__releases_images_to_fetch (release_id)
        VALUES (?), (?), (?)
        """,
        (1, rls1.id, rls2.id),
    )
    db.commit()

    save_pending_covers()

    cons = Constants()
    saved_covers = sorted([path.name for path in cons.cover_art_dir.iterdir()])
    assert len(saved_covers) == 4
