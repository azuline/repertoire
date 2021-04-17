from sqlite3 import Connection

from click.testing import CliRunner
from werkzeug.security import check_password_hash

from src.fixtures.factory import Factory

from .token import token


def test_update_token(factory: Factory, db: Connection):
    usr, _ = factory.user(conn=db)
    db.commit()

    cursor = db.execute(
        "SELECT token_hash FROM system__users WHERE id = ?",
        (usr.id,),
    )
    old_token_hash = cursor.fetchone()["token_hash"]

    output = CliRunner().invoke(token).output
    tkn = bytes.fromhex(output.split(": ")[1])

    cursor = db.execute(
        "SELECT token_hash FROM system__users WHERE id = ?",
        (usr.id,),
    )
    new_token_hash = cursor.fetchone()["token_hash"]

    assert not check_password_hash(old_token_hash, tkn)
    assert check_password_hash(new_token_hash, tkn)


def test_create_admin(db: Connection):
    cursor = db.execute("SELECT 1 FROM system__users WHERE id = 1")
    assert not cursor.fetchone()

    output = CliRunner().invoke(token).output
    tkn = bytes.fromhex(output.split(": ")[1])

    cursor = db.execute("SELECT token_hash FROM system__users WHERE id = 1")
    token_hash = cursor.fetchone()["token_hash"]

    assert check_password_hash(token_hash, tkn)
