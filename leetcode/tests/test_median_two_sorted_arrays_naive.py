import pytest

from leetcode.median_two_sorted_arrays_naive import find_median_sorted_arrays_naive


@pytest.mark.parametrize("nums1, nums2, expected", [
    ([1,3], [2], 2.0),
    ([1,2], [3,4], 2.5),
    ([], [1], 1.0),
    ([2], [], 2.0),
    ([0,0], [0,0], 0.0),
])
def test_naive_median(nums1, nums2, expected):
    assert find_median_sorted_arrays_naive(nums1, nums2) == expected
