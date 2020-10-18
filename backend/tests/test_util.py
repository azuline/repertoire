from backend.util import cached_property, parse_crontab, strip_punctuation


def test_cached_property():
    var = 1

    class Test:
        @cached_property
        def attr(self):
            return var

    test = Test()
    assert test.attr == 1
    var = 2
    assert test.attr == 1


def test_parse_crontab():
    dict_ = parse_crontab("0 1 2 3 4")

    assert dict_["minute"] == "0"
    assert dict_["hour"] == "1"
    assert dict_["day"] == "2"
    assert dict_["month"] == "3"
    assert dict_["day_of_week"] == "4"


def test_strip_punctuation():
    assert "abc" == strip_punctuation("[a.b!?c))")
