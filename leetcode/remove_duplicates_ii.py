from __future__ import annotations
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates from a sorted array in-place such that
    each unique element appears at most twice.

    Returns:
        k (int): number of elements kept in the modified array.

    Time:  O(n)
    Space: O(1)
    """
    if len(nums) <= 2:
        return len(nums)

    write = 2  # next position to write a valid element

    for read in range(2, len(nums)):
        # Only write nums[read] if it's not equal to nums[write-2]
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    return write
