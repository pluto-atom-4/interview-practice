"""
FUNCTION longest_increasing_subsequence(nums):
    IF nums is empty: RETURN 0

    INITIALIZE tails as an empty list

    FUNCTION bisect_left(arr, target):
        left = 0, right = length of arr
        WHILE left < right:
            mid = (left + right) // 2
            IF arr[mid] < target:
                left = mid + 1
            ELSE:
                right = mid
        RETURN left

    FOR each num in nums:
        // Use binary search to find where num fits in tails
        idx = bisect_left(tails, num)

        // If num is larger than all elements, extend the subsequence
        IF idx == length of tails:
            APPEND num TO tails
        // Otherwise, replace the existing tail to maintain potential for longer sequences
        ELSE:
            tails[idx] = num

    RETURN length of tails

"""

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
