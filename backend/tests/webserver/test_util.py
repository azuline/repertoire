import pytest
import quart
from voluptuous import Coerce, Schema

from backend.webserver.util import check_auth, validate_data


@pytest.fixture
def check_auth_app(quart_app):
    @quart_app.route("/testing", methods=["GET"])
    @check_auth()
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
async def test_check_auth_success(check_auth_app, quart_client):
    admin_token = "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"
    response = await quart_client.get(
        "/testing", headers={"Authorization": f"Token {admin_token}"}
    )

    assert b"admin" == await response.get_data()


@pytest.mark.asyncio
async def test_check_auth_failure(check_auth_app, quart_client):
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
