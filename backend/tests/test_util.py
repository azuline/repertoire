from dataclasses import dataclass

from src.util import (
    cached_property,
    parse_crontab,
    strip_punctuation,
    update_dataclass,
    without_key,
)


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


def test_update_dataclass():
    @dataclass(frozen=True)
    class Example:
        a: int

    d1 = Example(a=1)
    d2 = update_dataclass(d1, a=2)
    assert d1.a == 1
    assert d2.a == 2
