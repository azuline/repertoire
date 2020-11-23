import pytest
import quart


@pytest.mark.asyncio
async def test_create_session(quart_client, snapshot):
    response = await quart_client.authed_post("/session")
    assert b"success" == await response.get_data()
    snapshot.assert_match(quart.session)


@pytest.mark.asyncio
async def test_create_session_no_auth(quart_client):
    response = await quart_client.post("/session")
    assert 401 == response.status_code
