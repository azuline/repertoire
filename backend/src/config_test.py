from configparser import ConfigParser
from pathlib import Path

import pytest

from src.config import DEFAULT_CONFIG
from src.config import _Config as Config  # We don't want a singleton when we test.
from src.config import initialize_config, write_default_config
from src.errors import InvalidConfig


def test_initialize_config(isolated_dir):
    cfg_path = isolated_dir / "_data" / "config.ini"
    assert not cfg_path.exists()
    initialize_config()
    assert cfg_path.exists()

    with cfg_path.open("r") as fp:
        assert "[repertoire]" in fp.read()


def test_valid_index_crontab():
    config = Config()
    config.parser = {"repertoire": {"index_crontab": "0 0 * * *"}}  # type: ignore
    config.index_crontab  # If it doesn't exception we are good.


@pytest.mark.parametrize(
    "crontab",
    ["* * * *", "* * * * * *", "123 0 * * 0"],
)
def test_invalid_index_crontab(crontab):
    config = Config()
    config.parser = {"repertoire": {"index_crontab": crontab}}  # type: ignore

    with pytest.raises(InvalidConfig):
        config.index_crontab


@pytest.mark.parametrize(
    "directories",
    ['["/path/one", "/path/two"]', '["/path/one"]'],
)
def test_valid_music_directories(directories):
    config = Config()
    config.parser = {"repertoire": {"music_directories": directories}}  # type: ignore
    config.music_directories  # If it doesn't exception we are good.


@pytest.mark.parametrize(
    "directories",
    ['[/path/one", "/path/two"]', "completely wrong lmao!"],
)
def test_invalid_music_directories(directories):
    config = Config()
    config.parser = {"repertoire": {"music_directories": directories}}  # type: ignore

    with pytest.raises(InvalidConfig):
        config.music_directories


def test_write_default_config():
    path = Path("config.ini")
    write_default_config(path)

    parser = ConfigParser()
    parser.read(path)
    assert parser["repertoire"] == DEFAULT_CONFIG["repertoire"]


def test_update_default_config_add_key():
    path = Path("config.ini")

    with path.open("w") as f:
        f.write("[repertoire]\nmusic_directories = []")

    write_default_config(path)

    parser = ConfigParser()
    parser.read(path)
    assert "index_crontab" in parser["repertoire"]


def test_update_default_config_add_section():
    path = Path("config.ini")
    path.touch()
    write_default_config(path)

    parser = ConfigParser()
    parser.read(path)
    assert "repertoire" in parser
