from pathlib import Path
from sqlite3 import Connection

import pytest

from src.fixtures.factory import Factory


@pytest.mark.asyncio
async def test_get_track(factory: Factory, db: Connection, quart_client):
    path = Path.cwd() / "track01.flac"
    with path.open("wb") as f:
        f.write(b"owo")

    trk = factory.track(filepath=path, conn=db)
    _, token = factory.user(conn=db)

    db.commit()

    response = await quart_client.authed_get(
        f"/api/files/tracks/{trk.id}",
        token=token,
    )
    assert b"owo" == await response.get_data()


@pytest.mark.asyncio
async def test_get_track_bad_track_id(factory: Factory, db: Connection, quart_client):
    _, token = factory.user(conn=db)
    db.commit()

    response = await quart_client.authed_get("/api/files/tracks/999999", token=token)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_track_nonexistent_file(
    factory: Factory,
    db: Connection,
    quart_client,
):
    path = Path.cwd() / "nonexistent.flac"
    factory.track(filepath=path, conn=db)
    _, token = factory.user(conn=db)

    db.commit()

    response = await quart_client.authed_get("/api/files/tracks/1", token=token)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_cover(factory: Factory, db: Connection, quart_client):
    path = Path.cwd() / "cover01.png"
    with path.open("wb") as f:
        f.write(b"owo")

    factory.mock_image(path=path, conn=db)
    _, token = factory.user(conn=db)

    db.commit()

    response = await quart_client.authed_get("/api/files/images/1", token=token)
    assert b"owo" == await response.get_data()


@pytest.mark.asyncio
async def test_get_cover_thumbail(factory: Factory, db: Connection, quart_client):
    path = Path.cwd() / "cover01.png"
    with path.with_suffix(".thumbnail").open("wb") as f:
        f.write(b"owo")

    factory.mock_image(path=path, conn=db)
    _, token = factory.user(conn=db)
    db.commit()

    response = await quart_client.authed_get(
        "/api/files/images/1?thumbnail=true",
        token=token,
    )
    assert b"owo" == await response.get_data()


@pytest.mark.asyncio
async def test_get_cover_bad_release_id(factory: Factory, db: Connection, quart_client):
    _, token = factory.user(conn=db)
    db.commit()

    response = await quart_client.authed_get("/api/files/images/999999", token=token)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_cover_nonexistent_file(
    factory: Factory,
    db: Connection,
    quart_client,
):
    path = Path.cwd() / "nonexistent.png"
    factory.mock_image(path=path, conn=db)
    _, token = factory.user(conn=db)

    db.commit()

    response = await quart_client.authed_get("/api/files/images/1", token=token)
    assert response.status_code == 404
