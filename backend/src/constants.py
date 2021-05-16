import logging
import os
import sys
from functools import cached_property
from pathlib import Path

import click
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

BACKEND_ROOT = Path(__file__).parent.parent
load_dotenv(dotenv_path=BACKEND_ROOT / ".env")

# If pytest/sphinx is running the program, do a few things differently:
# - Set DATA_PATH to the tests' data directory rather than the real one.
# - Don't autoinitialize the database and config file.
IS_PYTEST = "pytest" in sys.modules
IS_SPHINX = "sphinx" in sys.modules
TEST_DATA_PATH = BACKEND_ROOT / "test_data"


def _get_data_path() -> Path:
    """
    Fetch the data path from `.env` and ensure that it exists and is writeable.
    """
    logger.debug("Ensuring that DATA_PATH exists and is writeable.")

    try:
        data_path = Path(os.getenv("DATA_PATH"))  # type: ignore
    except TypeError:
        click.echo("Make sure `DATA_PATH` is correctly set in `.env`.")
        exit(1)

    try:
        data_path.mkdir(exist_ok=True)
    except (FileNotFoundError, OSError):
        click.echo(
            f"Make sure that `{data_path.parent}` is a directory and is writeable."
        )
        exit(1)

    if not os.path.isdir(data_path) or not os.access(data_path, os.W_OK):
        click.echo(f"Make sure that `{data_path}` is a directory and is writeable.")
        exit(1)

    return data_path


class __Constants:
    """
    The "real" constants object that gets loaded as a singleton in ``Constants``.
    """

    def __init__(self):
        if IS_PYTEST:
            self.data_path = Path.cwd() / "_data"
        elif IS_SPHINX:  # pragma: no cover
            self.data_path = TEST_DATA_PATH
        else:  # pragma: no cover
            self.data_path = _get_data_path()

        self._cover_art_mkdir = False

    @property
    def cover_art_dir(self) -> Path:
        dir_ = self.data_path / "cover_art"
        if not self._cover_art_mkdir:
            logger.debug("Ensuring that cover art path exists.")
            dir_.mkdir(exist_ok=True)
            self._cover_art_mkdir = True
        return dir_

    @property
    def database_path(self) -> Path:
        return self.data_path / "db.sqlite3"

    @property
    def huey_path(self) -> Path:
        return self.data_path / "huey.sqlite3"

    @property
    def config_path(self) -> Path:
        return self.data_path / "config.ini"

    @property
    def pid_path(self) -> Path:
        return self.data_path / "src.pid"

    @cached_property
    def migrations_path(_) -> Path:
        return BACKEND_ROOT / "src" / "migrations" / "sql"

    @cached_property
    def built_frontend_dir(_) -> Path:
        try:
            return Path(os.getenv("BUILT_FRONTEND_DIR"))  # type: ignore
        except TypeError:
            return BACKEND_ROOT.parent / "frontend" / "build"


constants = __Constants()
