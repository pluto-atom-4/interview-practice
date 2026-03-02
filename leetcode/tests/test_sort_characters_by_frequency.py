import pytest

from leetcode.sort_characters_by_frequency import frequency_sort


def test_basic_examples():
    result = frequency_sort("tree")

    assert result.startswith("ee")
    assert sorted(result[2:]) == sorted("tr")
