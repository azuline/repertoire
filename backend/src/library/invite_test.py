from sqlite3 import Connection

from src.fixtures.factory import Factory

from . import invite


def test_from_id_success(factory: Factory, db: Connection):
    inv = factory.invite(conn=db)
    new_inv = invite.from_id(inv.id, db)
    assert new_inv == inv


def test_from_id_failure(db: Connection):
    assert invite.from_id(999999, db) is None


def test_from_code_success(factory: Factory, db: Connection):
    inv = factory.invite(conn=db)
    new_inv = invite.from_code(inv.code, db)
    assert new_inv == inv


def test_from_code_failure(db: Connection):
    assert invite.from_code(b"0" * invite.INVITE_LENGTH, db) is None


def test_create(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    inv = invite.create(by_user=usr, conn=db)
    assert inv.created_by == usr.id

    new_inv = invite.from_id(inv.id, db)
    assert new_inv == inv


def test_update(factory: Factory, db: Connection):
    inv = factory.invite(conn=db)

    usr, _ = factory.user(conn=db)
    new_inv = invite.update(inv, used_by=usr, conn=db)

    assert new_inv.used_by == usr.id
    assert new_inv == invite.from_id(inv.id, db)


def test_update_nothing(factory: Factory, db: Connection):
    inv = factory.invite(conn=db)
    new_inv = invite.update(inv, conn=db)
    assert new_inv == inv
