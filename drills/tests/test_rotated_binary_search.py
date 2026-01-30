import pytest

from drills.rotated_binary_search import rotated_binary_search


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 6, 2),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 1, 0),
        ([1], 2, -1),
        ([6, 7, 1, 2, 3, 4, 5], 3, 4),
        ([6, 7, 1, 2, 3, 4, 5], 7, 1),
        ([2, 3, 4, 5, 6, 7, 1], 1, 6),
        ([], 5, -1),
    ],
)
def test_rotated_binary_search(nums, target, expected):
    assert rotated_binary_search(nums, target) == expected


def test_large_rotated_array():
    nums = list(range(1000, 2000)) + list(range(0, 1000))
    assert rotated_binary_search(nums, 1500) == 500
    assert rotated_binary_search(nums, 10) == 1010
    assert rotated_binary_search(nums, 9999) == -1
