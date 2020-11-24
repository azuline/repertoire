import pytest


@pytest.mark.asyncio
async def test_graphql_endpoint(quart_client, snapshot):
    query = """
        query {
            user {
                id
                username
            }
        }
    """

    response = await quart_client.authed_post(
        "/graphql", json={"operationName": None, "variables": {}, "query": query}
    )
    snapshot.assert_match(await response.get_data())


@pytest.mark.asyncio
async def test_graphql_endpoint_no_auth(quart_client, snapshot):
    query = """
        query {
            user {
                id
                username
            }
        }
    """

    response = await quart_client.post(
        "/graphql", json={"operationName": None, "variables": {}, "query": query}
    )
    snapshot.assert_match(await response.get_data())
