import logging

from huey import Huey

from src.config import Config
from src.indexer import run_indexer

logger = logging.getLogger(__name__)


def schedule_tasks(huey: Huey) -> None:
    """
    Schedule tasks and start the huey task queue.

    :param huey: The MiniHuey instance to schedule and start.
    """
    logger.debug("Scheduling periodic tasks.")

    config = Config()
    huey.periodic_task(config.index_crontab)(run_indexer)
