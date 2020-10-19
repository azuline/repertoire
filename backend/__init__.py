from gevent import monkey

monkey.patch_all()

import logging
import sys

from yoyo import get_backend, read_migrations

from backend.config import write_default_config
from backend.constants import CONFIG_PATH, DATABASE_PATH, LOGS_DIR, PROJECT_ROOT

# Configure logging.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(levelname)s:%(name)s - %(message)s")

log_handler = logging.FileHandler(str(LOGS_DIR / "backend.log"))
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Run database migrations.
db_backend = get_backend(f"sqlite:///{DATABASE_PATH}")
db_migrations = read_migrations(str(PROJECT_ROOT / "backend" / "migrations"))

with db_backend.lock():
    db_backend.apply_migrations(db_backend.to_apply(db_migrations))

# Create/update config with default values.
write_default_config(CONFIG_PATH)
