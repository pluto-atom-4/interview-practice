"""
## Problem Statement

Find all unique duplicate numbers in an array of any integers. Multiple elements may be duplicated, and 
duplicates can appear any number of times. The output should contain each duplicate value exactly once, 
without repetition. This tests understanding of comparison logic and efficient duplicate detection.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **sorted array with two-pointer comparison**:

After sorting, duplicate numbers become adjacent. We traverse with two pointers, comparing each pair. When 
a match is found, we add it to results only if it's not already there (check against the last added value). 
This approach works with any integer values and handles multiple duplicates cleanly without hash tables.

* Key Concepts:

  - Why sort first?
Sorting groups identical elements together, making duplicates adjacent and easy to detect with a simple 
comparison. The trade-off is O(n log n) time vs. O(n) with hashing, but this teaches algorithmic thinking 
and works when hash tables are restricted. Sorting also enables other optimizations like binary search.

  - Why use two-pointer after sorting?
After sorting, we only need to compare adjacent elements. Two pointers moving in sync (left, right = i, i+1) 
simplify the logic: one pointer stays, the other advances. This is intuitive and requires O(1) extra space 
(not counting the sorted array), making it interview-friendly when space efficiency is discussed.

  - Why check duplicates[-1] before appending?
We want each duplicate value exactly once in results, but an element might appear 3, 4, or more times. 
By comparing the current duplicate against the last added value, we skip re-adding the same duplicate. 
This one-liner prevents redundancy without a separate set or flag.

* Logic:

1. Handle edge case: if array has fewer than 2 elements, no duplicates possible
2. Sort the array to group identical elements adjacently
3. Initialize left=0, right=1 to compare adjacent pairs
4. Iterate through the sorted array: if elements match and we haven't added this duplicate yet, add it
5. Advance both pointers together to check the next pair
6. Return the list of duplicates

* **30-Second Pitch**:

We sort the array first, which groups duplicates together. Then we use two pointers to walk through the 
sorted array, comparing adjacent elements. Whenever we find a match that hasn't been added to results yet, 
we add it once. This gives O(n log n) time and O(1) space (excluding the sort), and it's universally 
applicable to any integer array.

* **Rapid-Fire Version**:

- Sort the array to group duplicates adjacently
- Use two pointers (left, right) to compare adjacent elements
- When a match is found, add it to results if it's not already there
- Prevent duplicate entries in the result by checking the last added value
- Time: O(n log n), Space: O(1) excluding sort
- Works with any integers, multiple duplicates, unsorted input

* **Ultra-Minimal One-Liner**:

- Sort the array and traverse with two pointers comparing adjacent elements, adding each unique duplicate once.

* **Complexity Analysis**:

- **Time Complexity:** O(n log n) – dominated by sorting; the two-pointer pass is O(n)
- **Space Complexity:** O(1) – only two pointer variables (not counting the sorted array if done in-place)

* **Use Cases**:

General duplicate detection when space efficiency is prioritized, interview questions emphasizing 
algorithmic thinking over data structure usage, and scenarios where hash tables are unavailable or restricted.
"""

from __future__ import annotations

from typing import List


def two_pointer_find_duplicates(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return []

    nums_sorted = sorted(nums)
    duplicates = []

    left = 0
    right = 1

    while right < len(nums_sorted):
        if nums_sorted[left] == nums_sorted[right]:
            # Add only once
            if not duplicates or duplicates[-1] != nums_sorted[left]:
                duplicates.append(nums_sorted[left])
        left += 1
        right += 1

    return duplicates
