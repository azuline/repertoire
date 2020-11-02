import logging
import sys

from yoyo import get_backend, read_migrations

from src.config import write_default_config
from src.constants import CONFIG_PATH, DATABASE_PATH, LOGS_DIR, PROJECT_ROOT

# Configure logging.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add a logging handler for `src.log`.
log_handler = logging.FileHandler(str(LOGS_DIR / "src.log"))
log_formatter = logging.Formatter("%(asctime)s %(levelname)s:%(name)s - %(message)s")
log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)

# Add a logging handler for stdout.
stream_formatter = logging.Formatter("%(name)s - %(message)s")
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)

# Don't automatically initialize/update application data when sphinx is running.
if "sphinx" not in sys.modules:
    # Run database migrations.
    db_backend = get_backend(f"sqlite:///{DATABASE_PATH}")
    db_migrations = read_migrations(
        str(PROJECT_ROOT / "backend" / "src" / "migrations")
    )

    with db_backend.lock():
        db_backend.apply_migrations(db_backend.to_apply(db_migrations))

    # Create/update config with default values.
    write_default_config(CONFIG_PATH)
