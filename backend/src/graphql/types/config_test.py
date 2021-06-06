import pytest

from src import config
from src.fixtures.factory import Factory


@pytest.mark.asyncio
async def test_config(graphql_query):
    query = """
        query {
            config {
                ...ConfigFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True

    assert data["data"]["config"]["musicDirectories"] == ["/music"]
    assert data["data"]["config"]["indexCrontab"] == "0 0 * * *"


@pytest.mark.asyncio
async def test_update_config(factory: Factory, graphql_query):
    pathObj = factory.rand_path("")
    pathObj.mkdir()
    path = str(pathObj)

    query = f"""
        mutation {{
            updateConfig(
                musicDirectories: ["{path}"],
                indexCrontab: "1 1 * 2 *",
            ) {{
                ...ConfigFields
            }}
        }}
    """
    success, data = await graphql_query(query)
    assert success is True

    assert data["data"]["updateConfig"]["musicDirectories"] == [f"{path}"]
    assert data["data"]["updateConfig"]["indexCrontab"] == "1 1 * 2 *"

    assert config.music_directories() == [f"{path}"]
    assert config.index_crontab_str() == "1 1 * 2 *"


@pytest.mark.asyncio
async def test_update_config_bad_directory(graphql_query, snapshot):
    # This directory doesn't exist.
    path = "/not_a_directory_lol"

    query = f"""
        mutation {{
            updateConfig(
                musicDirectories: ["{path}"],
            ) {{
                ...ConfigFields
            }}
        }}
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_update_config_bad_crontab(graphql_query, snapshot):
    query = """
        mutation {
            updateConfig(
                indexCrontab: "1 1 * 2 * 7 3",
            ) {
                ...ConfigFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)
