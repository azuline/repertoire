from sqlite3 import Cursor

import pytest
from werkzeug.security import check_password_hash

from backend.errors import InvalidUsername
from backend.lib import user


def test_from_id_success(db: Cursor):
    assert user.T(id=1, username="admin") == user.from_id(1, db)


def test_from_id_failure(db: Cursor):
    assert user.from_id(3, db) is None


def test_from_username_success(db: Cursor):
    assert user.T(id=1, username="admin") == user.from_username("admin", db)


def test_from_username_failure(db: Cursor):
    assert user.from_username("garbage", db) is None


def test_from_token_success(db: Cursor):
    token = bytes.fromhex(
        "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"
    )
    assert user.T(id=1, username="admin") == user.from_token(token, db)


def test_from_token_failure(db: Cursor):
    assert user.from_token(b"0" * 32, db) is None


def test_from_token_bad_length(db: Cursor):
    assert user.from_token(b"0" * 100, db) is None


def test_create_user_success(db: Cursor):
    new_user, _token = user.create("neW1", db)
    assert user.T(id=3, username="neW1") == new_user


def test_create_user_invalid_username(db: Cursor):
    with pytest.raises(InvalidUsername):
        assert user.create("a bc", db)


def test_create_user_duplicate_username(db: Cursor):
    with pytest.raises(InvalidUsername):
        assert user.create("admin", db)


def test_generate_new_token(db: Cursor):
    db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    old_hash = db.fetchone()["token_hash"]

    usr = user.T(id=1, username="admin")
    token = user.new_token(usr, db)

    db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    new_hash = db.fetchone()["token_hash"]

    assert not check_password_hash(old_hash, token)
    assert check_password_hash(new_hash, token)


def test_check_token_success(db: Cursor):
    token = bytes.fromhex(
        "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"
    )
    usr = user.T(id=1, username="admin")

    assert user.check_token(usr, token, db)


def test_check_token_failure(db: Cursor):
    usr = user.T(id=1, username="admin")

    assert not user.check_token(usr, b"0" * 32, db)


def test_check_token_bad_user(db: Cursor):
    token = bytes.fromhex(
        "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"
    )
    usr = user.T(id=3, username="lol")

    assert not user.check_token(usr, token, db)
