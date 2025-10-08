import pytest

from algorithms.sorting.merge_sort import merge_sort


@pytest.mark.parametrize(
    "input_arr,expected",
    [
        ([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6]),
        ([1], [1]),
        ([], []),
        ([9, 7, 5, 3], [3, 5, 7, 9]),
    ],
)
def test_merge_sort(input_arr, expected):
    assert merge_sort(input_arr) == expected
