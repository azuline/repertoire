from huey.contrib.mini import MiniHuey

from backend.config import Config
from backend.lib import index_directories

huey = MiniHuey()


def schedule_tasks():
    config = Config()
    huey.task(config.index_crontab)(index_directories)
