from __future__ import annotations

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates from a sorted array in-place.
    Returns the number of unique elements (k).

    After the function runs:
      - The first k elements of nums contain the unique values.
      - Elements beyond index k-1 may be ignored.

    Time:  O(n)
    Space: O(1)
    """
    if not nums:
        return 0

    write = 1  # index where the next unique element should be written

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write
