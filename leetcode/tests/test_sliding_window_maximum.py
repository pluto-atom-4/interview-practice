import pytest

from leetcode.sliding_window_maximum import sliding_window_maximum


@pytest.mark.parametrize("nums, k, expected", [
    ([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]),
    ([1], 1, [1]),
    ([9, 11], 2, [11]),
    ([4, -2], 1, [4, -2]),
    ([7,2,4], 2, [7,4]),
])
def test_sliding_window_maximum(nums, k, expected):
    assert sliding_window_maximum(nums, k) == expected
