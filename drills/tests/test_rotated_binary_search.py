"""
FUNCTION rotated_binary_search(nums, target):
    IF nums is empty: RETURN -1

    left = 0
    right = length of nums - 1

    WHILE left <= right:
        mid = (left + right) // 2

        IF nums[mid] EQUALS target:
            RETURN mid

        // Identify which half of the array is sorted
        IF nums[left] <= nums[mid]:
            // Left side [left...mid] is sorted
            IF nums[left] <= target AND target < nums[mid]:
                right = mid - 1  // Target is in the sorted left half
            ELSE:
                left = mid + 1   // Target must be in the right half
        ELSE:
            // Right side [mid...right] is sorted
            IF nums[mid] < target AND target <= nums[right]:
                left = mid + 1   // Target is in the sorted right half
            ELSE:
                right = mid - 1  // Target must be in the left half

    RETURN -1
"""

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
