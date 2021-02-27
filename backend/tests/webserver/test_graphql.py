import pytest
import json
from src.library import user


@pytest.mark.asyncio
async def test_graphql_endpoint(db, quart_client, snapshot):
    usr, token = user.create("admin", db)
    db.commit()

    query = """
        query {
            user {
                id
                nickname
            }
        }
    """

    response = await quart_client.authed_post(
        "/graphql",
        token=token,
        json={
            "operationName": None,
            "variables": {},
            "query": query,
        },
    )
    data = await response.get_data()
    from pprint import pprint

    pprint(data)
    data = json.loads(data)

    assert data["data"]["user"]["id"] == usr.id
    assert data["data"]["user"]["nickname"] == usr.nickname


@pytest.mark.asyncio
async def test_graphql_endpoint_no_auth(quart_client, snapshot):
    query = """
        query {
            user {
                id
                nickname
            }
        }
    """

    response = await quart_client.post(
        "/graphql", json={"operationName": None, "variables": {}, "query": query}
    )
    assert response.status_code == 401
