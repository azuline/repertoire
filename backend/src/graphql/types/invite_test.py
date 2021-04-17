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

    # Code is nondeterministic.
    assert len(data["data"]["invite"]["code"]) == 64
    del data["data"]["invite"]["code"]

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

    # Code is nondeterministic.
    for inv in data["data"]["invites"]["results"]:
        assert len(inv["code"]) == 64
        del inv["code"]

    snapshot.assert_match(data)


@pytest.mark.asyncio
async def test_invites_filter(graphql_query, snapshot):
    query = """
        query {
            invites(includeExpired: true, createdBy: 1) {
                total
                results {
                    ...InviteFields
                }
            }
        }
    """
    success, data = await graphql_query(query)
    assert success is True

    # Code is nondeterministic.
    for inv in data["data"]["invites"]["results"]:
        assert len(inv["code"]) == 64
        del inv["code"]

    # Include the expired invite.
    assert len(data["data"]["invites"]["results"]) == 2
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

    # Code is nondeterministic.
    for inv in data["data"]["invites"]["results"]:
        assert len(inv["code"]) == 64
        del inv["code"]

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

    code = bytes.fromhex(data["data"]["createInvite"]["code"])
    del data["data"]["createInvite"]["code"]
    snapshot.assert_match(data)

    inv = invite.from_code(code, db)
    assert inv is not None
    assert inv.created_by == 1

    inv_from_id = invite.from_id(data["data"]["createInvite"]["id"], db)
    assert inv == inv_from_id
