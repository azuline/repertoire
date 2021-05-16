import logging

from huey import SqliteHuey

from src.constants import constants

logger = logging.getLogger(__name__)


huey = SqliteHuey(filename=constants.huey_path)


def schedule_tasks():
    """
    This function imports the periodic tasks declared across the application.
    """
    # IDK if this actually works but it should!
    import src.indexer  # noqa
