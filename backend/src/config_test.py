import json
from sqlite3 import Connection

import pytest

from src.config import (
    DEFAULT_CONFIG,
    INDEX_CRONTAB,
    MUSIC_DIRECTORIES,
    index_crontab,
    initialize_config,
    music_directories,
    set_index_crontab,
    set_music_directories,
)
from src.errors import InvalidConfig
from src.fixtures.factory import Factory


def test_initialized_config(db: Connection):
    # The config is initialized before the test.
    cursor = db.execute("SELECT key, value FROM system__config")
    cfg = {k: v for k, v in cursor}
    assert cfg == DEFAULT_CONFIG


def test_update_config(db: Connection):
    db.execute(
        "DELETE FROM system__config WHERE key = ?",
        (MUSIC_DIRECTORIES,),
    )
    db.commit()

    initialize_config()

    cursor = db.execute(
        "SELECT value FROM system__config WHERE key = ?",
        (MUSIC_DIRECTORIES,),
    )
    value = cursor.fetchone()["value"]

    assert value == DEFAULT_CONFIG[MUSIC_DIRECTORIES]


def test_valid_index_crontab(db: Connection):
    crontab = "0 0 * * *"
    db.execute(
        "UPDATE system__config SET value = ? WHERE key = ?",
        (crontab, INDEX_CRONTAB),
    )
    db.commit()

    # If it doesn't exception we are good.
    index_crontab()
    set_index_crontab(crontab, db)


@pytest.mark.parametrize(
    "crontab",
    ["* * * *", "* * * * * *", "123 0 * * 0"],
)
def test_invalid_index_crontab(crontab: str, db: Connection):
    db.execute(
        "UPDATE system__config SET value = ? WHERE key = ?",
        (crontab, INDEX_CRONTAB),
    )
    db.commit()

    with pytest.raises(InvalidConfig):
        index_crontab()
    with pytest.raises(InvalidConfig):
        set_index_crontab(crontab, db)


def test_valid_music_directories(db: Connection, factory: Factory):
    p1 = factory.rand_path("")
    p1.mkdir()
    p2 = factory.rand_path("")
    p2.mkdir()

    directories = [str(p1), str(p2)]

    db.execute(
        "UPDATE system__config SET value = ? WHERE key = ?",
        (json.dumps(directories), MUSIC_DIRECTORIES),
    )
    db.commit()

    # If it doesn't exception we are good.
    music_directories()
    set_music_directories(directories, db)


def test_invalid_music_directories_not_even_a_list(db: Connection):
    directories = "completely wrong lmao!"

    db.execute(
        "UPDATE system__config SET value = ? WHERE key = ?",
        (directories, MUSIC_DIRECTORIES),
    )
    db.commit()

    with pytest.raises(InvalidConfig):
        music_directories()
