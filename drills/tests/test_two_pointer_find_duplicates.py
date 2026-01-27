import pytest

from drills.two_pointer_find_duplicates import two_pointer_find_duplicates


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 2], [2]),
        ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
        ([1, 1, 1, 1], [1]),
        ([1, 2, 3, 4], []),
        ([5, 4, 3, 2, 1, 5], [5]),
        ([10, 9, 8, 7, 7, 7], [7]),
        ([], []),
        ([42], []),
        ([2, 1, 2, 1], [1, 2]),
        ([100, 50, 100, 50, 100], [50, 100]),
    ],
)
def test_two_pointer_find_duplicates(nums, expected):
    assert two_pointer_find_duplicates(nums) == expected
