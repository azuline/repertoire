import json

import pytest
import quart


@pytest.mark.asyncio
async def test_create_session(quart_client, snapshot):
    response = await quart_client.authed_post("/api/session")
    assert response.status_code == 201
    data = json.loads(await response.get_data())

    assert (
        data["csrfToken"]
        == "0101010101010101010101010101010101010101010101010101010101010101"
    )
    snapshot.assert_match(quart.session)


@pytest.mark.asyncio
async def test_create_session_no_auth(quart_client):
    response = await quart_client.post("/api/session")
    assert 401 == response.status_code


@pytest.mark.asyncio
async def test_delete_session(quart_client):
    async with quart_client.session_transaction() as sess:
        sess["user_id"] = 1

    response = await quart_client.authed_delete(
        "/api/session", headers={"X-CSRF-Token": "01" * 32}
    )
    assert b"success" == await response.get_data()
    assert quart.session == {}


@pytest.mark.asyncio
async def test_delete_session_invalid_csrf(quart_client):
    async with quart_client.session_transaction() as sess:
        sess["user_id"] = 1

    response = await quart_client.authed_delete(
        "/api/session", headers={"X-CSRF-Token": "99" * 32}
    )
    assert response.status_code == 400
