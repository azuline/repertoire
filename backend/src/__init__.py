import logging
import os
from pathlib import Path

import click
from dotenv import load_dotenv
from yoyo import get_backend, read_migrations

PROJECT_ROOT = Path(__file__).parent.parent.parent
REQUIRED_ENV_KEYS = [
    "DATABASE_PATH",
    "COVER_ART_DIR",
    "LOGS_DIR",
    "PID_PATH",
    "MUSIC_DIRS",
]

# Load up the environment vars and verify that they exist.
load_dotenv(dotenv_path=PROJECT_ROOT / ".env")

if not all(os.getenv(key) for key in REQUIRED_ENV_KEYS):
    click.echo("Make sure all required keys in `.env` exist.")
    exit(1)


LOGS_DIR = Path(os.getenv("LOGS_DIR"))
DATABASE_URL = os.getenv("DATABASE_PATH")

# Configure logging.
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler(str(LOGS_DIR / "backend.log"))
formatter = logging.Formatter("%(asctime)s %(levelname)s:%(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


# Run database migrations.
db_backend = get_backend(f"sqlite:///{DATABASE_URL}")
db_migrations = read_migrations(str(PROJECT_ROOT / "backend" / "migrations"))

with db_backend.lock():
    db_backend.apply_migrations(db_backend.to_apply(db_migrations))
