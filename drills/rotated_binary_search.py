from __future__ import annotations

from typing import List, Optional

"""
## Problem Statement

Search for a target value in a rotated sorted array using modified binary search. A rotated sorted array 
is a sorted array that has been rotated at some unknown pivot point. This problem tests understanding of 
binary search adaptability, state tracking, and handling edge cases—essential for optimization interviews.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Modified Binary Search with Rotation Detection**:

Standard binary search assumes a fully sorted array. Here, we detect which half of the array is sorted at 
each iteration, then determine if the target lies in that sorted half. This allows us to eliminate half the 
search space each iteration despite the rotation.

* Key Concepts:

  - Why check if nums[left] <= nums[mid] to determine sorted half?
If the left side's first element is ≤ the midpoint, the left half is sorted (no rotation in that range). 
Otherwise, the right half is sorted. This check determines which half preserves the sorted property despite 
the overall array rotation.

  - Why compare target against the sorted half's boundaries?
Once we know a half is sorted, we can use standard sorted array logic. If the target falls within the 
sorted half's range [left, mid], search there. Otherwise, search the other half. This is faster than 
checking if left <= target <= mid on unsorted data.

  - Why use strict comparisons like `nums[left] <= target < nums[mid]`?
The boundaries must match the half's properties. If left half is sorted and target is between its bounds, 
target must be there. Using == could miss edge cases; using < ensures we stay within the sorted range 
and handle equal elements correctly with the rotation.

* Logic:

1. Initialize left = 0, right = len(nums) - 1
2. While left <= right:
   a. Compute mid = (left + right) // 2
   b. If nums[mid] equals target, return mid
   c. Determine which half is sorted (compare nums[left] vs nums[mid])
   d. Check if target lies in sorted half's range
   e. If yes, search that half; if no, search the other half
3. Return -1 if target not found after loop completes

* **30-Second Pitch**:

I use modified binary search. At each iteration, I determine which half is sorted by comparing endpoints 
and midpoint. Then I check if the target falls within the sorted half's value range. If yes, I search that 
half; if no, I search the other half. This achieves O(log n) time despite the rotation.

* **Rapid-Fire Version**:

- Detect sorted half: compare nums[left] with nums[mid]
- Check if target in sorted half's range [nums[left], nums[mid]]
- Adjust boundaries based on target location relative to sorted half
- Handles edge cases with proper boundary comparisons
- Binary search on rotated array in logarithmic time

* **Ultra-Minimal One-Liner**:

- Modified binary search detecting sorted half at each step to locate target in rotated array in O(log n).

* **Complexity Analysis**:

- **Time Complexity:** O(log n) — standard binary search halving; doesn't degrade due to rotation
- **Space Complexity:** O(1) — only two pointers, no auxiliary data structures

* **Use Cases**:

- Rotated database indices
- Finding pivot points in sorted sequences
- Optimization problems requiring fast search on transformed sorted data
- (e.g., search for timestamps in cyclically shifted production logs).

"""

def rotated_binary_search(nums: List[int], target: int) -> int:
    """
    Search for a target in a rotated sorted array using modified binary search.

    Returns:
        Index of target if found, otherwise -1.

    Example:
        nums = [4,5,6,7,0,1,2], target = 0  → returns 4
    """
    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which side is sorted
        if nums[left] <= nums[mid]:
            # Left side sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right side sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
