import json
from configparser import ConfigParser
from typing import List

from huey import crontab

from backend.constants import CONFIG_PATH
from backend.errors import InvalidConfig
from backend.util import parse_crontab

DEFAULT_CONFIG = {
    "repertoire": {"music_directories": "[]", "index_crontab": "0 0 * * *"}
}


def _save_config(parser: ConfigParser) -> None:
    with CONFIG_PATH.open("w") as f:
        parser.write(f)


def _load_config() -> ConfigParser:
    parser = ConfigParser()
    parser.read(CONFIG_PATH)
    return parser


ConfigParser.save = _save_config


def write_default_config() -> None:
    """
    Write the default config if a config file doesn't exist. And if the
    existing config lacks keys, update it with new default values.
    """
    # If config doesn't exist, write it.
    if not CONFIG_PATH.exists():
        parser = ConfigParser()
        parser.read_dict(DEFAULT_CONFIG)
        parser.save()
        return

    # Otherwise, update config with default values if keys don't exist.
    parser = _load_config()
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
        parser.save()


class Config:
    """
    A "proxy singleton" that returns the same config instance when instantiated.
    """

    __config = None

    def __new__(cls):
        if cls.__config is None:
            cls.__config = super().__new__(cls)
        return cls.__config

    def __init__(self):
        self.parser = _load_config()

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
