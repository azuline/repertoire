import logging
import sys

from src.constants import IS_PYTEST

# Configure logging.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add a logging handler for stdout unless we are testing. Pytest
# captures logging output on its own.
if not IS_PYTEST:  # pragma: no cover
    stream_formatter = logging.Formatter(
        "%(asctime)s.%(msecs)03d - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(stream_formatter)
    logger.addHandler(stream_handler)
