import pytest
from voluptuous import Invalid

from backend.webserver.validators import StringBool


def test_string_bool_true():
    assert StringBool("true") is True


def test_string_bool_false():
    assert StringBool("false") is False


@pytest.mark.parametrize("val", ["1", "0", "tru", "haha!"])
def test_string_bool_error(val):
    with pytest.raises(Invalid):
        StringBool(val)
