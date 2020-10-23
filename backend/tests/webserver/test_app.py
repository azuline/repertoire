import pytest
import quart


@pytest.mark.asyncio
async def test_database_handler(db, quart_app):
    async with quart_app.test_request_context("/", method="GET"):
        await quart_app.preprocess_request()
        quart.g.db.execute("SELECT username FROM system__users WHERE id = 1")
        assert "admin" == quart.g.db.fetchone()[0]


@pytest.mark.asyncio
@pytest.mark.parametrize("path", ["/", "/collections", "/releases"])
async def test_index_root(path, quart_app, quart_client):
    async def fake_send_static_file(_):
        return b"owo"

    quart_app.send_static_file = fake_send_static_file

    response = await quart_client.get(path)
    assert await response.get_data() == b"owo"
