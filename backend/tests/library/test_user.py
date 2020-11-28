from sqlite3 import Cursor

import pytest
from werkzeug.security import check_password_hash

from src.errors import InvalidNickname
from src.library import user


def test_exists(db: Cursor):
    assert user.exists(1, db)


def test_does_not_exist(db: Cursor):
    assert not user.exists(9999999, db)


def test_from_id_success(db: Cursor, snapshot):
    snapshot.assert_match(user.from_id(1, db))


def test_from_id_failure(db: Cursor):
    assert user.from_id(3, db) is None


def test_from_nickname_success(db: Cursor, snapshot):
    snapshot.assert_match(user.from_nickname("admin", db))


def test_from_nickname_failure(db: Cursor):
    assert user.from_nickname("garbage", db) is None


def test_from_token_success(db: Cursor, snapshot):
    token = bytes.fromhex(
        "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"
    )
    snapshot.assert_match(user.from_token(token, db))


def test_from_token_failure_but_correct_prefix(db: Cursor, snapshot):
    token = bytes.fromhex(
        "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc0"
    )
    snapshot.assert_match(user.from_token(token, db))


def test_from_token_failure(db: Cursor):
    assert user.from_token(b"0" * 32, db) is None


def test_from_token_bad_length(db: Cursor):
    assert user.from_token(b"0" * 100, db) is None


def test_create_user_success(db: Cursor, snapshot):
    new_user, token = user.create("neW1", db)
    snapshot.assert_match(new_user)
    db.execute("SELECT token_hash FROM system__users WHERE id = ?", (new_user.id,))
    token_hash = db.fetchone()["token_hash"]
    assert check_password_hash(token_hash, token)


def test_create_user_invalid_nickname(db: Cursor):
    with pytest.raises(InvalidNickname):
        assert user.create("a" * 24, db)


def test_update_user(db: Cursor):
    usr = user.from_id(1, db)
    usr = user.update(usr, db, nickname="not admin")  # type: ignore
    db.connection.commit()
    assert usr.nickname == "not admin"
    assert usr == user.from_id(1, db)


def test_update_user_bad_nickname(db: Cursor):
    usr = user.from_id(1, db)
    with pytest.raises(InvalidNickname):
        user.update(usr, db, nickname="not admin" * 24)  # type: ignore


def test_generate_new_token(db: Cursor):
    db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    old_hash = db.fetchone()["token_hash"]

    token = user.new_token(user.from_id(1, db), db)  # type: ignore

    db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    new_hash = db.fetchone()["token_hash"]

    assert not check_password_hash(old_hash, token)
    assert check_password_hash(new_hash, token)


def test_check_token_success(db: Cursor):
    token = bytes.fromhex(
        "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"
    )
    assert user.check_token(user.from_id(1, db), token, db)  # type: ignore


def test_check_token_failure(db: Cursor):
    assert not user.check_token(user.from_id(1, db), b"0" * 32, db)  # type: ignore


def test_check_token_bad_user(db: Cursor):
    token = bytes.fromhex(
        "62ec24e7d70d3a55dfd823b8006ad8c6dda26aec9193efc0c83e35ce8a968bc8"
    )
    usr = user.T(id=3, nickname="lol")

    assert not user.check_token(usr, token, db)
