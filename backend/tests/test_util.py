from dataclasses import dataclass

from src.util import (
    make_fts_match_query,
    parse_crontab,
    uniq_list,
    update_dataclass,
    without_key,
)


def test_without_key():
    assert {1: 2} == without_key({1: 2, 3: 4}, 3)


def test_parse_crontab():
    dict_ = parse_crontab("0 1 2 3 4")

    assert dict_["minute"] == "0"
    assert dict_["hour"] == "1"
    assert dict_["day"] == "2"
    assert dict_["month"] == "3"
    assert dict_["day_of_week"] == "4"


def test_update_dataclass():
    @dataclass(frozen=True)
    class Example:
        a: int

    d1 = Example(a=1)
    d2 = update_dataclass(d1, a=2)
    assert d1.a == 1
    assert d2.a == 2


def test_uniq_list():
    assert [1, 2, 3] == uniq_list([1, 1, 2, 3, 2, 1, 3])


def test_make_fts_match_query():
    searchstr = "test terms one two three"
    expect = '"test" AND "terms" AND "one" AND "two" AND "three"'
    assert make_fts_match_query(searchstr) == expect
