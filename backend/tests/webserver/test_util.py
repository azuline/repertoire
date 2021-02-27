from typing import Optional
from sqlite3 import Connection

import pytest
import quart
from quart import Quart
from voluptuous import Coerce, Schema

from src.webserver.util import check_auth, validate_data
from tests.factory import Factory


@pytest.fixture
def check_auth_app(quart_app: Quart):
    @quart_app.route("/testing", methods=["GET"])
    @check_auth()
    async def testing():
        return quart.g.user.nickname

    return quart_app


@pytest.fixture
def check_csrf_app(quart_app: Quart):
    @quart_app.route("/testing", methods=["POST"])
    @check_auth(csrf=True)
    async def testing():
        return quart.g.user.nickname

    return quart_app


@pytest.fixture
def validate_data_app(quart_app: Quart):
    @quart_app.route("/testing", methods=["GET", "POST"])
    @validate_data(Schema({"a": str, "b": Coerce(int)}))
    async def testing(a, b):
        return f"{a} {b}"

    return quart_app


@pytest.mark.asyncio
async def test_check_auth_token_success(
    factory: Factory,
    db: Connection,
    check_auth_app: Quart,
    quart_client,
):
    _, token = factory.user(nickname="admin", conn=db)
    db.commit()

    response = await quart_client.authed_get("/testing", token=token)

    assert b"admin" == await response.get_data()


@pytest.mark.asyncio
async def test_check_auth_session_success(
    factory: Factory,
    db: Connection,
    check_auth_app: Quart,
    quart_client,
):
    usr, _ = factory.user(nickname="admin", conn=db)
    db.commit()

    async with quart_client.session_transaction() as sess:
        sess["user_id"] = usr.id

    response = await quart_client.get("/testing")
    assert b"admin" == await response.get_data()


@pytest.mark.asyncio
async def test_check_auth_token_failure(check_auth_app: Quart, quart_client):
    response = await quart_client.get(
        "/testing", headers={"Authorization": "Token lol"}
    )

    assert response.status_code == 401


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "headers",
    [
        {"Authorization": "nospace"},
        {"Authorization": "notToken abc"},
        {"Random stuff": "lol"},
        {"Authorization": 42},
        None,
    ],
)
async def test_check_auth_failure_bad_token(
    check_auth_app: Quart,
    quart_client,
    headers: Optional[dict],
):
    response = await quart_client.get("/testing", headers=headers)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_token_csrf_bypass(
    factory: Factory,
    db: Connection,
    check_csrf_app: Quart,
    quart_client,
):
    usr, token = factory.user(nickname="admin", conn=db)
    db.commit()

    response = await quart_client.authed_post("/testing", token=token)
    assert b"admin" == await response.get_data()


@pytest.mark.asyncio
async def test_session_csrf_success(
    factory: Factory,
    db: Connection,
    check_csrf_app: Quart,
    quart_client,
):
    usr, _ = factory.user(nickname="admin", conn=db)
    db.commit()

    async with quart_client.session_transaction() as sess:
        sess["user_id"] = usr.id

    response = await quart_client.post(
        "/testing",
        headers={"X-CSRF-Token": usr.csrf_token.hex()},
    )
    assert b"admin" == await response.get_data()


@pytest.mark.asyncio
async def test_session_csrf_failure(
    factory: Factory,
    db: Connection,
    check_csrf_app: Quart,
    quart_client,
):
    usr, _ = factory.user(conn=db)
    db.commit()

    async with quart_client.session_transaction() as sess:
        sess["user_id"] = usr.id

    response = await quart_client.post("/testing")
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_validate_data_get_success(validate_data_app: Quart, quart_client):
    response = await quart_client.get("/testing?a=abc&b=123")
    assert b"abc 123" == await response.get_data()


@pytest.mark.asyncio
async def test_validate_data_get_failure(validate_data_app: Quart, quart_client):
    response = await quart_client.get("/testing?a=abc&b=bbb")
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_validate_data_post_success(validate_data_app: Quart, quart_client):
    response = await quart_client.post("/testing", json={"a": "abc", "b": 123})
    assert b"abc 123" == await response.get_data()


@pytest.mark.asyncio
async def test_validate_data_post_failure(validate_data_app: Quart, quart_client):
    response = await quart_client.post("/testing", json={"a": "abc", "b": "bbb"})
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_validate_data_post_invalid_json(validate_data_app: Quart, quart_client):
    response = await quart_client.post("/testing", data='{"not json lol"}')
    assert response.status_code == 400
