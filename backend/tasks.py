from huey import Huey

from backend.config import Config
from backend.indexer import run_indexer


def schedule_tasks(huey: Huey) -> None:
    """
    Schedule tasks and start the huey task queue.

    :param huey: The MiniHuey instance to schedule and start.
    """
    config = Config()

    huey.periodic_task(config.index_crontab)(run_indexer)
