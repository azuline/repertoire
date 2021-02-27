import random
import shutil
import string
from datetime import date
from pathlib import Path
from sqlite3 import Connection
from typing import Optional

from src.enums import ArtistRole, CollectionType, PlaylistType, ReleaseType
from src.library import artist as libartist
from src.library import collection as libcollection
from src.library import image as libimage
from src.library import playlist as libplaylist
from src.library import release as librelease
from src.library import track as libtrack
from src.library import user as libuser

FAKE_COVER = Path(__file__).parent / "seed_data" / "fake_cover.jpg"


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
            name=name if name is not None else _rand_string(12),
            conn=conn,
        )

    def collection(
        self,
        *,
        conn: Connection,
        name: Optional[str] = None,
        type: Optional[CollectionType] = None,
    ) -> libcollection.T:
        return libcollection.create(
            name=name if name is not None else _rand_string(12),
            type=type if type is not None else CollectionType.COLLAGE,
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
            path = Path.cwd() / f"{_rand_string(12)}.png"
            shutil.copyfile(FAKE_COVER, path)

        return libimage.create(path=path, conn=conn)

    def mock_image(
        self,
        *,
        conn: Connection,
        path: Optional[Path] = None,
    ) -> libimage.T:
        """This creates an dummy image in the database. No actual image files."""
        if path is None:
            path = Path.cwd() / f"{_rand_string(12)}.png"

        cursor = conn.execute("INSERT INTO images(path) VALUES (?)", (str(path),))
        img = libimage.from_id(cursor.lastrowid, conn=conn)
        assert img is not None
        return img

    def playlist(
        self,
        *,
        conn: Connection,
        name: Optional[str] = None,
        type: Optional[PlaylistType] = None,
    ) -> libplaylist.T:
        return libplaylist.create(
            name=name if name is not None else _rand_string(12),
            type=type if type is not None else PlaylistType.PLAYLIST,
            conn=conn,
            override_immutable=True,
        )

    def release(
        self,
        *,
        title: Optional[str] = None,
        artist_ids: Optional[list[int]] = None,
        release_type: Optional[ReleaseType] = None,
        release_year: Optional[int] = None,
        release_date: Optional[date] = None,
        rating: Optional[int] = None,
        image_id: Optional[int] = None,
        conn: Connection,
    ) -> librelease.T:
        if artist_ids is None:
            artist_ids = [self.artist(conn=conn).id]

        return librelease.create(
            title=title if title is not None else _rand_string(12),
            artist_ids=artist_ids,
            release_type=(
                release_type if release_type is not None else ReleaseType.ALBUM
            ),
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
                        "artist_id": artist.id,
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
            title=title if title is not None else _rand_string(12),
            filepath=filepath if filepath is not None else _rand_path(".m4a"),
            sha256=sha256 if sha256 is not None else random.randbytes(12),
            release_id=release_id,
            artists=artists,
            duration=duration if duration is not None else random.randint(100, 400),
            track_number=track_number if track_number is not None else "1",
            disc_number=disc_number if disc_number is not None else "1",
            conn=conn,
        )

    def user(
        self,
        *,
        conn: Connection,
        nickname: Optional[str] = None,
    ) -> tuple[libuser.T, bytes]:
        return libuser.create(
            nickname=nickname if nickname is not None else _rand_string(12),
            conn=conn,
        )


def _rand_string(length: int) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def _rand_path(ext: str) -> Path:
    return Path.cwd() / f"{_rand_string(12)}{ext}"
