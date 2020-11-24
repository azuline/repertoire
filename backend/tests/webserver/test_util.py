import pytest
import quart
from voluptuous import Coerce, Schema

from src.webserver.util import check_auth, validate_data


@pytest.fixture
def check_auth_app(db, quart_app):
    @quart_app.route("/testing", methods=["GET"])
    @check_auth()
    async def testing():
        return quart.g.user.username

    return quart_app


@pytest.fixture
def check_csrf_app(db, quart_app):
    @quart_app.route("/testing", methods=["POST"])
    @check_auth(csrf=True)
    async def testing():
        return quart.g.user.username

    return quart_app


@pytest.fixture
def validate_data_app(quart_app):
    @quart_app.route("/testing", methods=["GET", "POST"])
    @validate_data(Schema({"a": str, "b": Coerce(int)}))
    async def testing(a, b):
        return f"{a} {b}"

    return quart_app


@pytest.mark.asyncio
async def test_check_auth_token_success(check_auth_app, quart_client):
    response = await quart_client.authed_get("/testing")

    assert b"admin" == await response.get_data()


@pytest.mark.asyncio
async def test_check_auth_session_success(check_auth_app, quart_client):
    async with quart_client.session_transaction() as sess:
        sess["user_id"] = 1

    response = await quart_client.get("/testing")
    assert b"admin" == await response.get_data()


@pytest.mark.asyncio
async def test_check_auth_token_failure(check_auth_app, quart_client):
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
async def test_check_auth_failure_bad_token(check_auth_app, quart_client, headers):
    response = await quart_client.get("/testing", headers=headers)

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_token_csrf_bypass(check_csrf_app, quart_client):
    response = await quart_client.authed_post("/testing")

    assert b"admin" == await response.get_data()


@pytest.mark.asyncio
async def test_session_csrf_success(check_csrf_app, quart_client):
    async with quart_client.session_transaction() as sess:
        sess["user_id"] = 1

    response = await quart_client.post("/testing", headers={"X-CSRF-Token": "01" * 32})
    assert b"admin" == await response.get_data()


@pytest.mark.asyncio
async def test_session_csrf_failure(check_csrf_app, quart_client):
    async with quart_client.session_transaction() as sess:
        sess["user_id"] = 1

    response = await quart_client.post("/testing")
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_validate_data_get_success(validate_data_app, quart_client):
    response = await quart_client.get("/testing?a=abc&b=123")
    assert b"abc 123" == await response.get_data()


@pytest.mark.asyncio
async def test_validate_data_get_failure(validate_data_app, quart_client):
    response = await quart_client.get("/testing?a=abc&b=bbb")
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_validate_data_post_success(validate_data_app, quart_client):
    response = await quart_client.post("/testing", json={"a": "abc", "b": 123})
    assert b"abc 123" == await response.get_data()


@pytest.mark.asyncio
async def test_validate_data_post_failure(validate_data_app, quart_client):
    response = await quart_client.post("/testing", json={"a": "abc", "b": "bbb"})
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_validate_data_post_invalid_json(validate_data_app, quart_client):
    response = await quart_client.post("/testing", data='{"not json lol"}')
    assert response.status_code == 400
