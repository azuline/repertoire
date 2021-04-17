import json
from sqlite3 import Connection

import pytest
import quart

from src.fixtures.factory import Factory


@pytest.mark.asyncio
async def test_create_session(factory: Factory, db: Connection, quart_client):
    usr, token = factory.user(conn=db)
    db.commit()

    response = await quart_client.authed_post("/api/session", token=token)
    assert response.status_code == 201
    data = json.loads(await response.get_data())

    assert data["csrfToken"] == usr.csrf_token.hex()
    assert quart.session["user_id"] == usr.id


@pytest.mark.asyncio
async def test_create_session_no_auth(quart_client):
    response = await quart_client.post("/api/session")
    assert 401 == response.status_code


@pytest.mark.asyncio
async def test_delete_session(factory: Factory, db: Connection, quart_client):
    usr, token = factory.user(conn=db)
    db.commit()

    async with quart_client.session_transaction() as sess:
        sess["user_id"] = usr.id

    response = await quart_client.authed_delete(
        "/api/session",
        token=token,
        headers={"X-CSRF-Token": usr.csrf_token.hex()},
    )
    assert b"success" == await response.get_data()
    assert quart.session == {}


@pytest.mark.asyncio
async def test_delete_session_invalid_csrf(
    factory: Factory,
    db: Connection,
    quart_client,
):
    usr, token = factory.user(conn=db)
    db.commit()

    async with quart_client.session_transaction() as sess:
        sess["user_id"] = usr.id

    response = await quart_client.authed_delete(
        "/api/session",
        token=token,
        headers={"X-CSRF-Token": "99" * 32},
    )
    assert response.status_code == 400
