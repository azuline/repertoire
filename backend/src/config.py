import json
from configparser import ConfigParser
from pathlib import Path
from typing import Callable, List, Optional

from huey import crontab

from src.constants import Constants
from src.errors import InvalidConfig
from src.util import parse_crontab

DEFAULT_CONFIG = {
    "repertoire": {"music_directories": "[]", "index_crontab": "0 0 * * *"}
}


def _save_config(parser: ConfigParser, config_path: Path) -> None:
    """
    This function saves a ConfigParser instance to the provided ``config_path``.

    :param parser: The ConfigParser instance to save.
    :param config_path: The filepath of the file to save to.
    """
    with config_path.open("w") as f:
        parser.write(f)


def _load_config(config_path: Path) -> ConfigParser:
    """
    This function loads a ConfigParser instance from the provided ``config_path``.

    :param config_path: The filepath of the config file to load.
    :return: The loaded ConfigParser instance.
    """
    parser = ConfigParser()
    parser.read(config_path)
    return parser


def write_default_config(config_path: Path) -> None:
    """
    Write the default config if a config file doesn't exist. And if the
    existing config lacks keys, update it with new default values.

    :param config_path: The filepath of the configuration file. Typically
                        ``CONFIG_PATH``.
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
    The "real" config object that gets loaded as a singleton in ``Config``.
    """

    def __init__(self):
        cons = Constants()

        self.parser = _load_config(cons.config_path)

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

    Other modules should only work with this singleton. This allows for code to fetch
    the global configuration object when needed.
    """

    __config: Optional[_Config] = None

    #: Music directories to index.
    music_directories: List[str]
    #: Crontab to schedule library indexing. Its type is a Huey ``crontab``.
    index_crontab: Callable

    def __new__(cls) -> _Config:  # type: ignore
        if cls.__config is None:
            cls.__config = _Config()
        return cls.__config
