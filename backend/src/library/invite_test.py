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


def test_search_all(factory: Factory, db: Connection):
    invs = {factory.invite(conn=db) for _ in range(5)}
    # Remove the favorites invite for an easy comparison.
    out = set(invite.search(db))
    assert invs == out


def test_search_created_by(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    invs_from_user = [factory.invite(by_user=usr, conn=db) for _ in range(2)]

    for _ in range(3):
        factory.invite(conn=db)

    invs = invite.search(db, created_by=usr.id)
    assert set(invs) == set(invs_from_user)


def test_search_expired(factory: Factory, db: Connection):
    invs = [factory.invite(conn=db) for _ in range(3)]

    # Expire the third invite.
    db.execute(
        """
        UPDATE system__invites
        SET created_at = DATETIME(CURRENT_TIMESTAMP, '-2 DAYS')
        WHERE id = ?
        """,
        (invs[2].id,),
    )

    out = invite.search(db, include_expired=True)
    assert set(i.id for i in out) == set(i.id for i in invs)

    out = invite.search(db, include_expired=False)
    assert set(out) == set(invs[:2])


def test_search_page(factory: Factory, db: Connection):
    for _ in range(5):
        factory.invite(conn=db)

    i1 = invite.search(db, page=1, per_page=1)[0]
    i2 = invite.search(db, page=2, per_page=1)[0]
    assert i1 != i2


def test_search_per_page(factory: Factory, db: Connection):
    invs = [factory.invite(conn=db) for _ in range(5)]
    invs = invite.search(db, page=1, per_page=2)
    assert len(invs) == 2


def test_count_all(factory: Factory, db: Connection):
    invs = [factory.invite(conn=db) for _ in range(5)]
    count = invite.count(db)
    assert count == len(invs)


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
