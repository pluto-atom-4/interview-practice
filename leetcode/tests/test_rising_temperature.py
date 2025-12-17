import pytest

from leetcode.rising_temperature import rising_temperature


def test_rising_temperature_example():
    weather = [
        {"id": 1, "recordDate": "2015-01-01", "temperature": 10},
        {"id": 2, "recordDate": "2015-01-02", "temperature": 25},
        {"id": 3, "recordDate": "2015-01-03", "temperature": 20},
        {"id": 4, "recordDate": "2015-01-04", "temperature": 30},
    ]

    result = rising_temperature(weather)
    assert sorted(result) == [2, 4]


def test_rising_temperature_no_rise():
    weather = [
        {"id": 1, "recordDate": "2020-01-01", "temperature": 50},
        {"id": 2, "recordDate": "2020-01-02", "temperature": 40},
        {"id": 3, "recordDate": "2020-01-03", "temperature": 30},
    ]

    assert rising_temperature(weather) == []


def test_rising_temperature_single_entry():
    weather = [
        {"id": 1, "recordDate": "2020-01-01", "temperature": 10},
    ]

    assert rising_temperature(weather) == []


def test_rising_temperature_unordered_input():
    weather = [
        {"id": 3, "recordDate": "2020-01-03", "temperature": 20},
        {"id": 1, "recordDate": "2020-01-01", "temperature": 10},
        {"id": 2, "recordDate": "2020-01-02", "temperature": 15},
    ]

    assert rising_temperature(weather) == [2, 3]
