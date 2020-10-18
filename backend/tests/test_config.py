from configparser import ConfigParser
from pathlib import Path

import pytest
from click.testing import CliRunner

from backend.config import DEFAULT_CONFIG
from backend.config import __Config as Config  # We don't want a singleton when we test.
from backend.config import write_default_config
from backend.errors import InvalidConfig


def test_valid_index_crontab():
    config = Config()
    config.index_crontab  # If it doesn't exception we are good.


@pytest.mark.parametrize(
    "crontab",
    [
        "* * * *",
        "* * * * * *",
        "123 0 * * 0",
    ],
)
def test_invalid_index_crontab(crontab):
    config = Config()
    config.parser = {"repertoire": {"index_crontab": crontab}}

    with pytest.raises(InvalidConfig):
        config.index_crontab


@pytest.mark.parametrize(
    "directories",
    [
        '["/path/one", "/path/two"]',
        '["/path/one"]',
    ],
)
def test_valid_music_directories(directories):
    config = Config()
    config.parser = {"repertoire": {"music_directories": directories}}
    config.music_directories  # If it doesn't exception we are good.


@pytest.mark.parametrize(
    "directories",
    [
        '[/path/one", "/path/two"]',
        "completely wrong lmao!",
    ],
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
        print(dict(parser))
        assert parser["repertoire"] == DEFAULT_CONFIG["repertoire"]


def test_update_default_config():
    path = Path("config.ini")

    with CliRunner().isolated_filesystem():
        with path.open("w") as f:
            f.write("[repertoire]\nmusic_directories = []")

        write_default_config(path)

        parser = ConfigParser()
        parser.read(path)
        assert "index_crontab" in parser["repertoire"]
