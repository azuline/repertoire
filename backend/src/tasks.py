import logging

from huey import SqliteHuey

from src.config import config
from src.constants import constants
from src.indexer import run_indexer

logger = logging.getLogger(__name__)


huey = SqliteHuey(filename=constants.huey_path)

logger.debug("Scheduling periodic tasks.")


@huey.periodic_task(config.index_crontab)
def indexer():
    run_indexer()
