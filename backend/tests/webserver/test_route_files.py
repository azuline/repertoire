from pathlib import Path

import pytest
from click.testing import CliRunner


@pytest.mark.asyncio
async def test_get_track(db, quart_client):
    with CliRunner().isolated_filesystem():
        path = Path.cwd() / "track01.flac"

        with path.open("wb") as f:
            f.write(b"owo")

        db.execute("UPDATE music__tracks SET filepath = ? WHERE id = 1", (str(path),))
        db.connection.commit()

        response = await quart_client.authed_get("/files/tracks/1")
        assert b"owo" == await response.get_data()


@pytest.mark.asyncio
async def test_get_track_bad_track_id(quart_client):
    with CliRunner().isolated_filesystem():
        response = await quart_client.authed_get("/files/tracks/999999")
        assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_track_nonexistent_file(db, quart_client):
    with CliRunner().isolated_filesystem():
        path = Path.cwd() / "nonexistent.flac"

        db.execute("UPDATE music__tracks SET filepath = ? WHERE id = 1", (str(path),))
        db.connection.commit()

        response = await quart_client.authed_get("/files/tracks/1")
        assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_cover(db, quart_client):
    with CliRunner().isolated_filesystem():
        path = Path.cwd() / "cover01.png"

        with path.open("wb") as f:
            f.write(b"owo")

        db.execute(
            "UPDATE music__releases SET image_path = ? WHERE id = 1", (str(path),)
        )
        db.connection.commit()

        response = await quart_client.authed_get("/files/covers/1")
        assert b"owo" == await response.get_data()


@pytest.mark.asyncio
async def test_get_cover_thumbail(db, quart_client):
    with CliRunner().isolated_filesystem():
        path = Path.cwd() / "cover01.png"

        with path.with_suffix(".thumbnail").open("wb") as f:
            f.write(b"owo")

        db.execute(
            "UPDATE music__releases SET image_path = ? WHERE id = 1", (str(path),)
        )
        db.connection.commit()

        response = await quart_client.authed_get("/files/covers/1?thumbnail=true")
        assert b"owo" == await response.get_data()


@pytest.mark.asyncio
async def test_get_cover_bad_release_id(quart_client):
    with CliRunner().isolated_filesystem():
        response = await quart_client.authed_get("/files/covers/999999")
        assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_cover_nonexistent_file(db, quart_client):
    with CliRunner().isolated_filesystem():
        path = Path.cwd() / "nonexistent.png"

        db.execute(
            "UPDATE music__releases SET image_path = ? WHERE id = 1", (str(path),)
        )
        db.connection.commit()

        response = await quart_client.authed_get("/files/covers/1")
        assert response.status_code == 404
