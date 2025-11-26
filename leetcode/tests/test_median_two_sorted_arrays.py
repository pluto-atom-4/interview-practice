import pytest

from leetcode.median_two_sorted_arrays import find_median_sorted_arrays


@pytest.mark.parametrize("nums1, nums2, expected", [
    ([1,3], [2], 2.0),
    ([1,2], [3,4], 2.5),
    ([], [1], 1.0),
    ([2], [], 2.0),
    ([0,0], [0,0], 0.0),
    ([1,2], [1,2,3], 2.0),
    ([1,3,5], [2,4,6], 3.5),
])
def test_median_two_sorted_arrays(nums1, nums2, expected):
    assert find_median_sorted_arrays(nums1, nums2) == expected
