import pytest

from leetcode.kth_smallest_pair_distance_naive import smallest_distance_pair_naive


@pytest.mark.parametrize("nums, k, expected", [
    ([1,3,1], 1, 0),
    ([1,1,1], 2, 0),
    ([1,6,1], 3, 5),
])
def test_smallest_distance_pair_naive(nums, k, expected):
    assert smallest_distance_pair_naive(nums, k) == expected
