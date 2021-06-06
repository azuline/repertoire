import logging

from huey import SqliteHuey

from src.constants import IS_DEBUG, IS_PYTEST, IS_SPHINX, constants

logger = logging.getLogger(__name__)


huey = SqliteHuey(
    filename=constants.huey_path,
    # In tests, tasks run immediately. They aren't queued.
    immediate=IS_PYTEST or IS_SPHINX or IS_DEBUG,
)
