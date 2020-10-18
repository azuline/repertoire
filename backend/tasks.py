from huey.contrib.mini import MiniHuey

from backend.config import Config
from backend.indexer import run_indexer

huey = MiniHuey()


def schedule_tasks():
    config = Config()

    huey.task(config.index_crontab)(run_indexer)
