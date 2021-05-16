import logging

from huey import Huey

from src.config import config
from src.indexer import run_indexer

logger = logging.getLogger(__name__)


def schedule_tasks(huey: Huey) -> None:
    """
    Schedule the recurring tasks.

    :param huey: The Huey instance to schedule the tasks on.
    """
    logger.debug("Scheduling periodic tasks.")

    huey.periodic_task(config.index_crontab)(run_indexer)
