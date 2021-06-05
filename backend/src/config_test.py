from sqlite3 import Connection

import pytest

from src.config import (
    DEFAULT_CONFIG,
    INDEX_CRONTAB,
    MUSIC_DIRECTORIES,
    index_crontab,
    initialize_config,
    music_directories,
)
from src.errors import InvalidConfig


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
    db.execute(
        "UPDATE system__config SET value = '0 0 * * *' WHERE key = ?",
        (INDEX_CRONTAB,),
    )
    db.commit()

    # If it doesn't exception we are good.
    index_crontab()


@pytest.mark.parametrize(
    "crontab",
    ["* * * *", "* * * * * *", "123 0 * * 0"],
)
def test_invalid_index_crontab(crontab, db: Connection):
    db.execute(
        "UPDATE system__config SET value = ? WHERE key = ?",
        (crontab, INDEX_CRONTAB),
    )
    db.commit()

    with pytest.raises(InvalidConfig):
        index_crontab()


@pytest.mark.parametrize(
    "directories",
    ['["/path/one", "/path/two"]', '["/path/one"]'],
)
def test_valid_music_directories(directories: str, db: Connection):
    db.execute(
        "UPDATE system__config SET value = ? WHERE key = ?",
        (directories, MUSIC_DIRECTORIES),
    )
    db.commit()

    # If it doesn't exception we are good.
    music_directories()


@pytest.mark.parametrize(
    "directories",
    ['[/path/one", "/path/two"]', "completely wrong lmao!"],
)
def test_invalid_music_directories(directories: str, db: Connection):
    db.execute(
        "UPDATE system__config SET value = ? WHERE key = ?",
        (directories, MUSIC_DIRECTORIES),
    )
    db.commit()

    with pytest.raises(InvalidConfig):
        music_directories()
