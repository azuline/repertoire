import random
import shutil
import string
from datetime import date
from pathlib import Path
from sqlite3 import Connection
from typing import Optional

from src.constants import TEST_DATA_PATH
from src.enums import ArtistRole, CollectionType, PlaylistType, ReleaseType
from src.library import artist as libartist
from src.library import collection as libcollection
from src.library import image as libimage
from src.library import invite as libinvite
from src.library import playlist as libplaylist
from src.library import playlist_entry as libpentry
from src.library import release as librelease
from src.library import track as libtrack
from src.library import user as libuser

FAKE_COVER = TEST_DATA_PATH / "fake_cover.jpg"


class Factory:
    """
    This factory is a helper class that generates test data.

    It is a class to present a type interface as a pytest fixture, but the methods are
    stateless.
    """

    def artist(
        self,
        *,
        conn: Connection,
        name: Optional[str] = None,
    ) -> libartist.T:
        return libartist.create(
            name=name or self.rand_string(12),
            conn=conn,
        )

    def collection(
        self,
        *,
        conn: Connection,
        name: Optional[str] = None,
        type: Optional[CollectionType] = None,
        user: Optional[libuser.T] = None,
    ) -> libcollection.T:
        return libcollection.create(
            name=name or self.rand_string(12),
            type=type or CollectionType.COLLAGE,
            user_id=user.id if user else None,
            conn=conn,
            override_immutable=True,
        )

    def image(
        self,
        *,
        conn: Connection,
        path: Optional[Path] = None,
    ) -> libimage.T:
        if path is None:
            path = Path.cwd() / f"{self.rand_string(12)}.png"
            shutil.copyfile(FAKE_COVER, path)

        return libimage.create(path=path, conn=conn)

    def invite(
        self,
        *,
        conn: Connection,
        by_user: Optional[libuser.T] = None,
        expired: bool = False,
        used_by: Optional[libuser.T] = None,
    ) -> libinvite.T:
        if by_user is None:
            by_user, _ = self.user(conn=conn)

        inv = libinvite.create(by_user=by_user, conn=conn)

        if expired:
            conn.execute(
                """
                UPDATE system__invites
                SET created_at = DATETIME(CURRENT_TIMESTAMP, '-2 DAYS')
                WHERE id = ?
                """,
                (inv.id,),
            )

        if used_by:
            conn.execute(
                """
                UPDATE system__invites
                SET used_by = ?
                WHERE id = ?
                """,
                (used_by.id, inv.id),
            )

        return inv

    def mock_image(
        self,
        *,
        conn: Connection,
        path: Optional[Path] = None,
    ) -> libimage.T:
        """This creates an dummy image in the database. No actual image files."""
        if path is None:
            path = Path.cwd() / f"{self.rand_string(12)}.png"

        cursor = conn.execute("INSERT INTO images(path) VALUES (?)", (str(path),))
        img = libimage.from_id(cursor.lastrowid, conn=conn)
        assert img is not None
        return img

    def playlist(
        self,
        *,
        conn: Connection,
        name: Optional[str] = None,
        user: Optional[libuser.T] = None,
        type: Optional[PlaylistType] = None,
    ) -> libplaylist.T:
        return libplaylist.create(
            name=name or self.rand_string(12),
            type=type or PlaylistType.PLAYLIST,
            user_id=user.id if user else None,
            conn=conn,
            override_immutable=True,
        )

    def playlist_entry(
        self,
        *,
        conn: Connection,
        playlist_id: Optional[int] = None,
        track_id: Optional[int] = None,
    ) -> libpentry.T:
        if playlist_id is None:
            playlist_id = self.playlist(conn=conn).id

        if track_id is None:
            track_id = self.track(conn=conn).id

        return libpentry.create(playlist_id, track_id, conn)

    def release(
        self,
        *,
        title: Optional[str] = None,
        artists: Optional[list[dict]] = None,
        release_type: Optional[ReleaseType] = None,
        release_year: Optional[int] = None,
        release_date: Optional[date] = None,
        rating: Optional[int] = None,
        image_id: Optional[int] = None,
        conn: Connection,
    ) -> librelease.T:
        if artists is None:
            artists = [
                {"artist_id": self.artist(conn=conn).id, "role": ArtistRole.MAIN}
            ]

        return librelease.create(
            title=title or self.rand_string(12),
            artists=artists,
            release_type=release_type or ReleaseType.ALBUM,
            release_year=release_year,
            release_date=release_date,
            rating=rating,
            image_id=image_id,
            conn=conn,
        )

    def track(
        self,
        *,
        conn: Connection,
        title: Optional[str] = None,
        filepath: Optional[Path] = None,
        sha256_initial: Optional[bytes] = None,
        sha256: Optional[bytes] = None,
        release_id: Optional[int] = None,
        artists: Optional[list[dict]] = None,
        duration: Optional[int] = None,
        track_number: Optional[str] = None,
        disc_number: Optional[str] = None,
    ) -> libtrack.T:
        release: Optional[librelease.T] = None

        if release_id is None:
            release = self.release(conn=conn)
            release_id = release.id

        if artists is None:
            if release:
                artists = [
                    {
                        "artist_id": artist["artist"].id,
                        "role": ArtistRole.MAIN,
                    }
                    for artist in librelease.artists(release, conn)
                ]
            else:
                artists = [
                    {
                        "artist_id": self.artist(conn=conn).id,
                        "role": ArtistRole.MAIN,
                    }
                ]

        return libtrack.create(
            title=title or self.rand_string(12),
            filepath=filepath or self.rand_path(".m4a"),
            sha256_initial=sha256_initial or random.randbytes(32),
            sha256=sha256,
            release_id=release_id,
            artists=artists,
            duration=duration or random.randint(100, 400),
            track_number=track_number or "1",
            disc_number=disc_number or "1",
            conn=conn,
        )

    def user(
        self,
        *,
        conn: Connection,
        nickname: Optional[str] = None,
    ) -> tuple[libuser.T, bytes]:
        return libuser.create(
            nickname=nickname or self.rand_string(12),
            conn=conn,
        )

    def rand_string(self, length: int) -> str:
        return "".join(random.choice(string.ascii_letters) for _ in range(length))

    def rand_path(self, ext: str) -> Path:
        return Path.cwd() / f"{self.rand_string(12)}{ext}"

    def rand_year(self) -> int:
        return random.randint(0, 2022)
