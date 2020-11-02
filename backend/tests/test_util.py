from src.util import cached_property, parse_crontab, strip_punctuation, without_key


def test_cached_property():
    var = 1

    class Test:
        @cached_property
        def a(self):
            return var

        @cached_property
        def b(self):
            return var

    test = Test()
    assert test.a == 1
    var = 2
    assert test.a == 1

    assert test.b == 2
    var = 3
    assert test.b == 2


def test_without_key():
    assert {1: 2} == without_key({1: 2, 3: 4}, 3)


def test_parse_crontab():
    dict_ = parse_crontab("0 1 2 3 4")

    assert dict_["minute"] == "0"
    assert dict_["hour"] == "1"
    assert dict_["day"] == "2"
    assert dict_["month"] == "3"
    assert dict_["day_of_week"] == "4"


def test_strip_punctuation():
    assert "abcàà" == strip_punctuation("[a.b!?c))àà")
