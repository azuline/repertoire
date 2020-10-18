from backend.util import parse_crontab, strip_punctuation, to_posix_time


def test_to_posix_time():
    assert 1602988618 == to_posix_time("2020-10-18 02:36:58")


def test_parse_crontab():
    dict_ = parse_crontab("0 1 2 3 4")

    assert dict_["minute"] == "0"
    assert dict_["hour"] == "1"
    assert dict_["day"] == "2"
    assert dict_["month"] == "3"
    assert dict_["day_of_week"] == "4"


def test_strip_punctuation():
    assert "abc" == strip_punctuation("[a.b!?c))")
