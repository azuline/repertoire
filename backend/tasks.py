from huey.contrib.mini import MiniHuey

from backend.config import Config
from backend.indexer import run_indexer


def schedule_and_start(huey: MiniHuey) -> None:
    """
    Schedule tasks and start the huey task queue.

    :param huey: The MiniHuey instance to schedule and start.
    """
    config = Config()

    huey.task(config.index_crontab)(run_indexer)

    huey.start()
