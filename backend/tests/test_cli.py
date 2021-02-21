from click.testing import CliRunner
from pysqlite3 import Connection
from werkzeug.security import check_password_hash

from src.cli.token import token


def test_update_token(db: Connection):
    cursor = db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    old_token_hash = cursor.fetchone()["token_hash"]

    output = CliRunner().invoke(token).output
    tkn = bytes.fromhex(output.split(": ")[1])

    cursor = db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    new_token_hash = cursor.fetchone()["token_hash"]

    assert not check_password_hash(old_token_hash, tkn)
    assert check_password_hash(new_token_hash, tkn)


def test_create_admin(db: Connection):
    db.execute("DELETE FROM system__users")
    db.commit()

    cursor = db.execute("SELECT 1 FROM system__users WHERE id = 1")
    assert not cursor.fetchone()

    output = CliRunner().invoke(token).output
    tkn = bytes.fromhex(output.split(": ")[1])

    cursor = db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    token_hash = cursor.fetchone()["token_hash"]

    assert check_password_hash(token_hash, tkn)
