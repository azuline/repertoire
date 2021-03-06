import os
from sqlite3 import Connection

import pytest

from src.library import user
from tests.factory import Factory


@pytest.mark.asyncio
async def test_create_dev_user(db: Connection, quart_app, quart_client):
    quart_app.debug = True

    response = await quart_client.post("/api/dev/testuser")
    assert response.status_code == 200

    usr = user.from_nickname("tester", db)
    assert usr is not None
    assert user.check_token(usr, b"\x00" * 32, db)


@pytest.mark.asyncio
async def test_create_dev_user_404(db: Connection, quart_app, quart_client):
    quart_app.debug = False
    response = await quart_client.post("/api/dev/testuser")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_dev_index_library(db: Connection, quart_app, quart_client):
    quart_app.debug = True
    response = await quart_client.post("/api/dev/indexlib")
    # It just calls run_indexer, I'm not going to bother with a real test.
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_dev_index_library_404(quart_app, quart_client):
    quart_app.debug = False
    response = await quart_client.post("/api/dev/indexlib")
    assert response.status_code == 404
