import json
import logging
from configparser import ConfigParser
from pathlib import Path
from typing import Callable

from huey import crontab

from src.constants import constants
from src.errors import InvalidConfig
from src.util import parse_crontab

logger = logging.getLogger(__name__)

DEFAULT_CONFIG = {
    "repertoire": {
        "music_directories": '["/music"]',
        "index_crontab": "0 0 * * *",
    }
}


def initialize_config():
    """
    Write the default config to the constant `config_path` location.
    """
    write_default_config(constants.config_path)


def write_default_config(config_path: Path) -> None:
    """
    Write the default config if a config file doesn't exist. And if the
    existing config lacks keys, update it with new default values.

    :param config_path: The filepath of the configuration file. Typically
                        ``CONFIG_PATH``.
    """
    # If config doesn't exist, write it.
    if not config_path.exists():
        logger.debug("Writing a new default config.")
        parser = ConfigParser()
        parser.read_dict(DEFAULT_CONFIG)
        _save_config(parser, config_path)
        return

    logger.debug("Adding missing config keys to existing config.")

    # Otherwise, update config with default values if keys don't exist.
    parser = _load_config(config_path)
    modified = False

    for section, items in DEFAULT_CONFIG.items():
        if section not in parser:
            logger.debug(f"Adding section {section} to config.")
            modified = True
            parser[section] = {}

        for key, value in items.items():
            if key not in parser[section]:
                logger.debug(f"Adding key {key} to config with default value {value}.")
                modified = True
                parser[section][key] = value

    if modified:
        _save_config(parser, config_path)


class _Config:
    def __init__(self):
        self.parser = _load_config(constants.config_path)

    @property
    def music_directories(self) -> list[str]:
        try:
            return json.loads(self.parser["repertoire"]["music_directories"])
        except json.decoder.JSONDecodeError:
            raise InvalidConfig(
                "repertoire.music_directories is not a valid JSON-encoded list."
            )

    @property
    def index_crontab(self) -> Callable:
        try:
            return crontab(**parse_crontab(self.parser["repertoire"]["index_crontab"]))
        except ValueError:
            raise InvalidConfig("repertoire.index_crontab is not a valid crontab.")


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
    logger.debug(f"Reading config from {config_path}.")
    parser = ConfigParser()
    parser.read(config_path)
    return parser


config = _Config()
