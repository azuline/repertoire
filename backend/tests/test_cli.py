from sqlite3 import Cursor

from click.testing import CliRunner
from werkzeug.security import check_password_hash

from src.cli.token import token


def test_update_token(db: Cursor):
    db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    old_token_hash = db.fetchone()["token_hash"]

    output = CliRunner().invoke(token).output
    tkn = bytes.fromhex(output.split(": ")[1])

    db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    new_token_hash = db.fetchone()["token_hash"]

    assert not check_password_hash(old_token_hash, tkn)
    assert check_password_hash(new_token_hash, tkn)


def test_create_admin(db: Cursor):
    db.execute("DELETE FROM system__users")
    db.connection.commit()

    db.execute("SELECT 1 FROM system__users WHERE id = 1")
    assert not db.fetchone()

    output = CliRunner().invoke(token).output
    tkn = bytes.fromhex(output.split(": ")[1])

    db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    token_hash = db.fetchone()["token_hash"]

    assert check_password_hash(token_hash, tkn)
