import logging

from huey import SqliteHuey

from src import config
from src.constants import IS_DEBUG, IS_PYTEST, IS_SPHINX, constants

logger = logging.getLogger(__name__)


huey = SqliteHuey(
    filename=constants.huey_path,
    # In tests, tasks run immediately. They aren't queued.
    immediate=IS_PYTEST or IS_SPHINX or IS_DEBUG,
)


def schedule_tasks():
    """
    This function schedules the application's periodic tasks and imports the tasks
    declared across the application.
    """
    from src.indexer import run_indexer

    @huey.periodic_task(config.index_crontab())
    def indexer():  # noqa
        run_indexer()

    # IDK if this actually works but it should!
    import src.indexer.scanner  # noqa
