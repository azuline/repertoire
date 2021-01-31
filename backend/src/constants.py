import os
import sys
from pathlib import Path
from functools import cached_property
from typing import Callable, List, Optional

import click
from dotenv import load_dotenv

BACKEND_ROOT = Path(__file__).parent.parent

# If pytest/sphinx is running the program, do a few things differently:
# - Set DATA_PATH to the tests' data directory rather than the real one.
# - Don't autoinitialize the database and config file.
TESTING = "pytest" in sys.modules or "sphinx" in sys.modules
TEST_DATA_PATH = BACKEND_ROOT / "tests" / "fake_data"


def _get_data_path() -> Path:
    """
    Fetch the data path from `.env` and ensure that it exists and is writeable.
    """

    try:
        data_path = Path(os.getenv("DATA_PATH"))  # type: ignore
    except TypeError:
        click.echo("Make sure `DATA_PATH` is correctly set in `.env`.")
        exit(1)

    try:
        data_path.mkdir(exist_ok=True)
    except (FileNotFoundError, OSError):
        click.echo(
            "Make sure that `{data_path.parent}` is a directory and is writeable."
        )
        exit(1)

    if not os.path.isdir(data_path) or not os.access(data_path, os.W_OK):
        click.echo("Make sure that `{data_path}` is a directory and is writeable.")
        exit(1)

    return data_path


class _Constants:
    """
    The "real" config object that gets loaded as a singleton in ``Config``.
    """

    def __init__(self):
        load_dotenv(dotenv_path=BACKEND_ROOT / ".env")

        self.data_path = _get_data_path() if not TESTING else TEST_DATA_PATH

    @cached_property
    def cover_art_dir(self):
        dir_ = self.data_path / "cover_art"
        dir_.mkdir(exist_ok=True)
        return dir_

    @cached_property
    def database_path(self):
        return self.data_path / "db.sqlite3"

    @cached_property
    def huey_path(self):
        return self.data_path / "huey.sqlite3"

    @cached_property
    def config_path(self):
        return self.data_path / "config.ini"

    @cached_property
    def pid_path(self):
        return self.data_path / "src.pid"

    @cached_property
    def migrations_path(_):
        return BACKEND_ROOT / "src" / "migrations"

    @cached_property
    def built_frontend_dir(_):
        try:
            return Path(os.getenv("BUILT_FRONTEND_DIR"))  # type: ignore
        except TypeError:
            return BACKEND_ROOT.parent / "frontend" / "build"


class Constants:
    """
    A "proxy singleton" that returns the same config instance when instantiated.

    Other modules should only work with this singleton. This allows for code to fetch
    the global configuration object when needed.
    """

    __constants: Optional[_Constants] = None

    #: Data storage location.
    data_path: Path
    #: Storage location of cover art.
    cover_art_dir: Path
    #: Path to SQLite3 database.
    database_path: Path
    #: Path to Huey database.
    huey_path: Path
    #: Path to config ini file.
    config_path: Path
    #: Path to backend PID file.
    pid_path: Path
    #: Path to the database migrations.
    migrations_path: Path
    #: Path to the built Typescript frontend.
    built_frontend_dir: Path

    def __new__(cls) -> _Constants:  # type: ignore
        if cls.__constants is None:
            cls.__constants = _Constants()
        return cls.__constants
