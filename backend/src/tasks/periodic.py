import time
from typing import Optional

from huey.api import TaskWrapper

from src import config
from src.tasks.hueyy import huey

# Global variable for the current indexer.
indexer: Optional[TaskWrapper] = None  # type: ignore


def schedule_tasks():
    """
    This function (re)schedules the application's periodic tasks and imports
    the tasks declared across the application.

    Huey periodic tasks should really be defined in global scope, but we fetch
    our crontab values from a config that requires in-app initialization. To work
    around this, we define our periodic tasks initially with a dummy crontab. We
    then re-schedule them in this function and overwrite the function definition.
    """
    # Import declared tasks.
    # IDK if this actually works but it should!
    import src.indexer.scanner  # noqa

    # Reschedule our tasks.
    reschedule_indexer()


def reschedule_indexer():
    """
    Reschedule the library indexer with our configuration-defined crontab.
    """
    from src.indexer import run_indexer

    global indexer
    # Revoke the old library indexer task.
    if indexer:
        indexer.revoke()

    # Schedule the new library indexer task.
    # indexer = huey.periodic_task(config.index_crontab())(run_indexer)  # type: ignore
    indexer = huey.periodic_task(
        config.index_crontab(),
        name=f"indexer+{time.time()}",
    )(run_indexer)
