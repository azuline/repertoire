import os
import sys
from pathlib import Path

import click
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent.parent

# If pytest is running, set DATA_PATH to the tests' data directory rather than the real
# one.

if "pytest" not in sys.modules:
    load_dotenv(dotenv_path=PROJECT_ROOT / ".env")
else:
    os.environ["DATA_PATH"] = str(PROJECT_ROOT / "backend" / "tests" / "data")

# Fetch the data path from `.env` and ensure that it exists and is writeable.
try:
    DATA_PATH = Path(os.getenv("DATA_PATH"))
except TypeError:
    click.echo("Make sure `DATA_PATH` is correctly set in `.env`.")
    exit(1)

try:
    DATA_PATH.mkdir(exist_ok=True)
except (FileNotFoundError, OSError):
    click.echo("Make sure that `{DATA_PATH.parent}` is a directory and is writeable.")
    exit(1)

if not os.path.isdir(DATA_PATH) or not os.access(DATA_PATH, os.W_OK):
    click.echo("Make sure that `{DATA_PATH}` is a directory and is writeable.")
    exit(1)

LOGS_DIR = DATA_PATH / "logs"
COVER_ART_DIR = DATA_PATH / "cover_art"

LOGS_DIR.mkdir(exist_ok=True)
COVER_ART_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATA_PATH / "db.sqlite3"
CONFIG_PATH = DATA_PATH / "config.ini"
PID_PATH = DATA_PATH / "backend.pid"
