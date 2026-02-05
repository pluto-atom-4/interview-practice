import pytest

from drills.lis import longest_increasing_subsequence


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 1),
        ([], 0),
        ([3], 1),
        ([2, 2, 2, 3, 4], 3),
        ([4, 10, 4, 3, 8, 9], 3),
    ],
)
def test_lis(nums, expected):
    assert longest_increasing_subsequence(nums) == expected


def test_large_case():
    nums = list(range(10000))  # strictly increasing
    assert longest_increasing_subsequence(nums) == 10000
