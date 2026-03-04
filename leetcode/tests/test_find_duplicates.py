import pytest

from leetcode.find_duplicates import find_duplicates


def sort_list(lst):
    return sorted(lst)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
        ([1, 1, 2], [1]),
        ([1], []),
        ([2, 2], [2]),
        ([3, 3, 3], [3]),  # appears more than twice but still counted once
    ],
)
def test_find_duplicates(nums, expected):
    result = find_duplicates(nums)
    assert sort_list(result) == sort_list(expected)
