from sqlite3 import Connection

import pytest
import quart

from src.webserver.app import _get_secret_key
from tests.factory import Factory


@pytest.mark.asyncio
async def test_database_handler(factory: Factory, db: Connection, quart_app):
    usr, _ = factory.user(nickname="admin", conn=db)
    db.commit()

    async with quart_app.test_request_context("/", method="GET"):
        await quart_app.preprocess_request()
        cursor = quart.g.db.execute(
            "SELECT nickname FROM system__users WHERE id = ?",
            (usr.id,),
        )
        assert "admin" == cursor.fetchone()[0]


def test_get_secret_key_new(db):
    key = _get_secret_key()
    assert len(key) == 32
    cursor = db.execute("SELECT key FROM system__secret_key")
    assert key == cursor.fetchone()[0]


def test_get_secret_key_exists(db):
    db.execute("INSERT INTO system__secret_key (key) VALUES (X'0000')")
    db.commit()
    assert b"\x00\x00" == _get_secret_key()


@pytest.mark.asyncio
@pytest.mark.parametrize("path", ["/", "/collections", "/releases"])
async def test_index_root(path, quart_app, quart_client):
    async def fake_send_static_file(_):
        return b"owo"

    quart_app.send_static_file = fake_send_static_file

    response = await quart_client.get(path)
    assert await response.get_data() == b"owo"
