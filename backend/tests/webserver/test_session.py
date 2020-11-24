import json

import pytest
import quart


@pytest.mark.asyncio
async def test_create_session(db, quart_client, snapshot):
    response = await quart_client.authed_post("/session")
    print(await response.get_data())
    assert response.status_code == 201
    data = json.loads(await response.get_data())

    assert (
        data["csrfToken"]
        == "0101010101010101010101010101010101010101010101010101010101010101"
    )
    snapshot.assert_match(quart.session)


@pytest.mark.asyncio
async def test_create_session_no_auth(db, quart_client):
    response = await quart_client.post("/session")
    assert 401 == response.status_code


@pytest.mark.asyncio
async def test_delete_session(db, quart_client):
    async with quart_client.session_transaction() as sess:
        sess["user_id"] = 1

    response = await quart_client.authed_delete(
        "/session", headers={"X-CSRF-Token": "01" * 32}
    )
    assert b"success" == await response.get_data()
    assert quart.session == {}


@pytest.mark.asyncio
async def test_delete_session_invalid_csrf(db, quart_client):
    async with quart_client.session_transaction() as sess:
        sess["user_id"] = 1

    response = await quart_client.authed_delete(
        "/session", headers={"X-CSRF-Token": "99" * 32}
    )
    assert response.status_code == 400
