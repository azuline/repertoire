# Don't import this file at the module level.

from huey import crontab
from huey.contrib.mini import MiniHuey

from backend.config import Config
from backend.lib import index_directories
from backend.util import hours_to_crontab

huey = MiniHuey()
config = Config()

# Schedule index_directories on the config index interval.
params = hours_to_crontab(config.index_interval)
huey.task(crontab(**params))(index_directories)
