from sqlite3 import Connection

import pytest
from werkzeug.security import check_password_hash

from src.errors import InvalidNickname
from src.fixtures.factory import Factory
from . import user


def test_exists(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    assert user.exists(usr.id, db)


def test_does_not_exist(db: Connection):
    assert not user.exists(9999999, db)


def test_from_id_success(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    new_usr = user.from_id(usr.id, db)
    assert new_usr == usr


def test_from_id_failure(db: Connection):
    assert user.from_id(999999, db) is None


def test_from_nickname_success(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    new_usr = user.from_nickname(usr.nickname, db)
    assert new_usr == usr


def test_from_nickname_failure(db: Connection):
    assert user.from_nickname("garbage", db) is None


def test_from_token_success(factory: Factory, db: Connection):
    usr, token = factory.user(conn=db)
    new_usr = user.from_token(token, db)
    assert new_usr == usr


def test_from_token_failure_but_correct_prefix(factory: Factory, db: Connection):
    usr, token = factory.user(conn=db)
    new_token = token[: user.PREFIX_LENGTH] + b"0" * (
        user.TOKEN_LENGTH - user.PREFIX_LENGTH
    )
    assert user.from_token(new_token, db) is None


def test_from_token_failure(db: Connection):
    assert user.from_token(b"0" * user.TOKEN_LENGTH, db) is None


def test_from_token_bad_length(db: Connection):
    assert user.from_token(b"0" * 100, db) is None


def test_create_user_success(db: Connection):
    new_user, token = user.create("neW1", db)
    cursor = db.execute(
        "SELECT token_hash FROM system__users WHERE id = ?",
        (new_user.id,),
    )
    token_hash = cursor.fetchone()["token_hash"]
    assert check_password_hash(token_hash, token)


def test_create_user_invalid_nickname(db: Connection):
    with pytest.raises(InvalidNickname):
        user.create("a" * 24, db)


def test_update_user(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)

    new_usr = user.update(usr, nickname="not admin", conn=db)

    assert new_usr.nickname == "not admin"
    assert new_usr == user.from_id(usr.id, db)


def test_update_user_bad_nickname(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)

    with pytest.raises(InvalidNickname):
        user.update(usr, db, nickname="not admin" * 24)


def test_generate_new_token(factory: Factory, db: Connection):
    usr, old_token = factory.user(conn=db)

    cursor = db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    old_hash = cursor.fetchone()["token_hash"]

    new_token = user.new_token(usr, db)

    cursor = db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    new_hash = cursor.fetchone()["token_hash"]

    assert not check_password_hash(old_hash, new_token)
    assert not check_password_hash(new_hash, old_token)
    assert check_password_hash(new_hash, new_token)


def test_check_token_success(factory: Factory, db: Connection):
    usr, token = factory.user(conn=db)
    assert user.check_token(usr, token, db)


def test_check_token_failure(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    assert not user.check_token(usr, b"0" * 32, db)


def test_check_token_bad_user(factory: Factory, db: Connection):
    token = bytes.fromhex(
        "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"
    )
    usr = user.T(id=3, nickname="lol", csrf_token=b"0" * 32)

    assert not user.check_token(usr, token, db)
