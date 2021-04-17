import json
from sqlite3 import Connection

import pytest

from src.library import user
from tests.factory import Factory


@pytest.mark.asyncio
async def test_register_first_user(db: Connection, quart_client):
    response = await quart_client.post("/api/register", json={"nickname": "admin"})
    data = json.loads(await response.get_data())
    assert data["token"] is not None

    usr = user.from_token(bytes.fromhex(data["token"]), db)
    assert usr is not None
    assert usr.id == 1
    assert usr.nickname == "admin"


@pytest.mark.asyncio
async def test_register_first_user_failure(
    factory: Factory,
    db: Connection,
    quart_client,
):
    factory.user(conn=db)
    db.commit()

    response = await quart_client.post("/api/register", json={"nickname": "admin"})
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_has_first_user_true(
    factory: Factory,
    db: Connection,
    quart_client,
):
    factory.user(conn=db)
    db.commit()

    response = await quart_client.get("/api/register/has-first-user")
    data = json.loads(await response.get_data())
    assert data["hasFirstUser"]


@pytest.mark.asyncio
async def test_has_first_user_false(quart_client):
    response = await quart_client.get("/api/register/has-first-user")
    data = json.loads(await response.get_data())
    assert not data["hasFirstUser"]
