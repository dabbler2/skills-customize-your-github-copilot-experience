import pytest

from calculator import average, calculate_discount, parse_age


def test_calculate_discount_applies_a_percentage():
    assert calculate_discount(100, 20) == 80


def test_average_returns_the_mean():
    assert average([10, 20, 30]) == 20


def test_average_rejects_an_empty_list():
    with pytest.raises(ValueError):
        average([])


def test_parse_age_returns_an_integer():
    assert parse_age("16") == 16


def test_parse_age_rejects_non_numeric_text():
    with pytest.raises(ValueError):
        parse_age("sixteen")
