import json
from configparser import ConfigParser
from pathlib import Path
from typing import List

from huey import crontab

from backend.constants import CONFIG_PATH
from backend.errors import InvalidConfig
from backend.util import parse_crontab

DEFAULT_CONFIG = {
    "repertoire": {"music_directories": "[]", "index_crontab": "0 0 * * *"}
}


def _save_config(parser: ConfigParser, config_path: Path) -> None:
    with config_path.open("w") as f:
        parser.write(f)


def _load_config(config_path: Path) -> ConfigParser:
    parser = ConfigParser()
    parser.read(config_path)
    return parser


def write_default_config(config_path: Path) -> None:
    """
    Write the default config if a config file doesn't exist. And if the
    existing config lacks keys, update it with new default values.
    """
    # If config doesn't exist, write it.
    if not config_path.exists():
        parser = ConfigParser()
        parser.read_dict(DEFAULT_CONFIG)
        _save_config(parser, config_path)
        return

    # Otherwise, update config with default values if keys don't exist.
    parser = _load_config(config_path)
    modified = False

    for section, items in DEFAULT_CONFIG.items():
        if section not in parser:
            modified = True
            parser[section] = {}

        for key, value in items.items():
            if key not in parser[section]:
                modified = True
                parser[section][key] = value

    if modified:
        _save_config(parser, config_path)


class _Config:
    """
    The actual config object that gets loaded as a singleton.
    """

    def __init__(self):
        self.parser = _load_config(CONFIG_PATH)

    @property
    def music_directories(self) -> List[str]:
        try:
            return json.loads(self.parser["repertoire"]["music_directories"])
        except json.decoder.JSONDecodeError:
            raise InvalidConfig(
                "repertoire.music_directories is not a valid JSON-encoded list."
            )

    @property
    def index_crontab(self) -> int:
        try:
            return crontab(**parse_crontab(self.parser["repertoire"]["index_crontab"]))
        except ValueError:
            raise InvalidConfig("repertoire.index_crontab is not a valid crontab.")


class Config:
    """
    A "proxy singleton" that returns the same config instance when instantiated.
    """

    __config: _Config = None

    music_directories: List[str]
    index_crontab: int

    def __new__(cls) -> _Config:
        if cls.__config is None:
            cls.__config = _Config()
        return cls.__config
