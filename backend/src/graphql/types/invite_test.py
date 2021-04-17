from sqlite3 import Connection

import pytest

from src.library import invite


@pytest.mark.asyncio
async def test_invite(graphql_query, snapshot):
    query = """
        query {
            invite(id: 1) {
                ...InviteFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_invite_not_found(graphql_query, snapshot):
    query = """
        query {
            invite(id: 999999) {
                ...InviteFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_invites(graphql_query, snapshot):
    query = """
        query {
            invites {
                total
                results {
                    ...InviteFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_invites_filter(graphql_query, snapshot):
    query = """
        query {
            invites(search: "Invite1", createdByUserId: 1) {
                total
                results {
                    ...InviteFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_invites_pagination(graphql_query, snapshot):
    query = """
        query {
            invites(page: 2, perPage: 1) {
                total
                results {
                    ...InviteFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_create_invite(db: Connection, graphql_query, snapshot):
    query = """
        mutation {
            createInvite {
                ...InviteFields
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True
    snapshot.assert_match(data)

    inv = invite.from_id(data["data"]["createInvite"]["id"], db)
    assert inv is not None
    assert inv.created_by == 1
