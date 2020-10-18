import pytest

from backend.errors import InvalidConfig
from backend.tasks import Config


@pytest.mark.parametrize(
    "crontab",
    [
        "* * * *",
        "* * * * * *",
    ],
)
def test_invalid_index_crontab(crontab):
    config = Config()
    config.parser = {"repertoire": {"index_crontab": crontab}}

    with pytest.raises(InvalidConfig):
        config.index_crontab
