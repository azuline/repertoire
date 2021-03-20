import json
from sqlite3 import Connection

import pytest

from tests.factory import Factory


@pytest.mark.asyncio
async def test_has_first_user_successful(
    factory: Factory,
    db: Connection,
    quart_client,
):
    factory.user(conn=db)
    db.commit()

    response = await quart_client.get("/api/has_first_user")
    data = json.loads(await response.get_data())
    assert data["hasFirstUser"]


@pytest.mark.asyncio
async def test_has_first_user_(quart_client):
    response = await quart_client.get("/api/has_first_user")
    data = json.loads(await response.get_data())
    assert not data["hasFirstUser"]
