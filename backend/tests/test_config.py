from configparser import ConfigParser
from pathlib import Path

import pytest
from click.testing import CliRunner

from src.config import DEFAULT_CONFIG
from src.config import Config as SingletonConfig
from src.config import _Config as Config  # We don't want a singleton when we test.
from src.config import write_default_config
from src.errors import InvalidConfig


def test_valid_index_crontab():
    config = Config()
    config.index_crontab  # If it doesn't exception we are good.


@pytest.mark.parametrize(
    "crontab",
    ["* * * *", "* * * * * *", "123 0 * * 0"],
)
def test_invalid_index_crontab(crontab):
    config = Config()
    config.parser = {"repertoire": {"index_crontab": crontab}}

    with pytest.raises(InvalidConfig):
        config.index_crontab


@pytest.mark.parametrize(
    "directories",
    ['["/path/one", "/path/two"]', '["/path/one"]'],
)
def test_valid_music_directories(directories):
    config = Config()
    config.parser = {"repertoire": {"music_directories": directories}}
    config.music_directories  # If it doesn't exception we are good.


@pytest.mark.parametrize(
    "directories",
    ['[/path/one", "/path/two"]', "completely wrong lmao!"],
)
def test_invalid_music_directories(directories):
    config = Config()
    config.parser = {"repertoire": {"music_directories": directories}}

    with pytest.raises(InvalidConfig):
        config.music_directories


def test_write_default_config():
    path = Path("config.ini")

    with CliRunner().isolated_filesystem():
        write_default_config(path)

        parser = ConfigParser()
        parser.read(path)
        assert parser["repertoire"] == DEFAULT_CONFIG["repertoire"]


def test_update_default_config_add_key():
    path = Path("config.ini")

    with CliRunner().isolated_filesystem():
        with path.open("w") as f:
            f.write("[repertoire]\nmusic_directories = []")

        write_default_config(path)

        parser = ConfigParser()
        parser.read(path)
        assert "index_crontab" in parser["repertoire"]


def test_update_default_config_add_section():
    path = Path("config.ini")

    with CliRunner().isolated_filesystem():
        path.touch()

        write_default_config(path)

        parser = ConfigParser()
        parser.read(path)
        assert "repertoire" in parser


def test_singleton():
    c1 = SingletonConfig()
    c2 = SingletonConfig()
    assert c1 is c2
