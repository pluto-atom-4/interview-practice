"""
## Problem Statement

Find the length of the longest increasing subsequence (LIS) in an array.
(e.g., sequence of work order timestamps for dependency analysis).
Given a sequence of elements, find the longest subsequence where elements are 
in strictly increasing order (not necessarily contiguous). This problem tests 
understanding of dynamic programming optimization and patience-sorting techniques.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Patience Sorting with Binary Search**:

The key insight is that we don't need to track the actual LIS—just its length.
By maintaining a `tails` array where `tails[i]` is the smallest ending value of 
all increasing subsequences of length `i+1`, we can use binary search to find 
where each new number fits.

* Key Concepts:

  - **Why use the tails array instead of DP?**
  
    A naive DP approach tries all previous elements: O(n²). The tails array 
    exploits monotonicity—as we process elements, tails remains sorted. This 
    property allows binary search to find the insertion position in O(log n), 
    reducing overall complexity to O(n log n). The array is small (at most n 
    elements) and always maintains sorted order.

  - **Why replace instead of append when idx < len(tails)?**
  
    When we find a position idx where num should go, replacing tails[idx] 
    preserves optimality. A smaller ending value at position idx opens more 
    opportunities for future elements to extend that subsequence. Replacing 
    maintains the invariant that tails[i] is the minimum tail for subsequences 
    of length i+1, without affecting the length count.

  - **Why use bisect_left over a manual binary search?**
  
    bisect_left finds the leftmost insertion point for num in the sorted tails 
    array. This is exactly what we need—if num equals an existing tail, we want 
    to find the position where it first appears (or would appear). Using the 
    library function eliminates bugs and improves readability.

* Logic:

1. Initialize an empty `tails` array to track the smallest ending value of each LIS length
2. For each number in the input array:
   a. Use binary search (bisect_left) to find the position where this number would fit
   b. If the position equals the length of tails, we've found a longer subsequence—append
   c. Otherwise, replace the value at that position with the new number (optimization for future elements)
3. Return the length of tails, which equals the length of the LIS

* **30-Second Pitch**:

I'm using patience sorting with binary search. The idea is to maintain a `tails` 
array where each position represents the smallest ending value for that LIS length. 
As I scan through the numbers, I use binary search to find where each number fits, 
either extending the LIS or improving an existing position. This runs in O(n log n) 
time—much better than the naive O(n²) DP approach.

* **Rapid-Fire Version**:

- Maintain `tails` array: smallest tail for each LIS length
- Binary search (bisect_left) finds insertion position: O(log n)
- Append if new length, replace if optimization opportunity
- Invariant: tails always sorted, length = LIS length
- Result: O(n log n) time, O(n) space

* **Ultra-Minimal One-Liner**:

- Patience sorting with binary search: track smallest tail per LIS length, binary search each number, O(n log n) time.

* **Complexity Analysis**:

- **Time Complexity:** O(n log n) — We iterate through n elements (O(n)), and for each, 
  we perform a binary search on tails (O(log n) since tails has at most n elements).

- **Space Complexity:** O(n) — The tails array stores at most n values (one per potential 
  LIS length). No additional data structures beyond this.

* **Use Cases**:

This approach is ideal for interview settings because it demonstrates both algorithmic 
knowledge (dynamic programming) and optimization intuition (binary search). Real-world 
applications include stock trading (finding longest profit sequence), DNA sequence 
analysis (longest matching subsequences), and task scheduling (dependency chain detection).
"""

from __future__ import annotations

from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    Compute the length of the Longest Increasing Subsequence (LIS)
    using the O(n log n) patience-sorting method.

    Example:
        [10, 9, 2, 5, 3, 7, 101, 18] → 4  (LIS = [2, 3, 7, 18])

    Enhancement:
        Uses a custom nested binary search function instead of bisect_left.
    """
    if not nums:
        return 0

    tails: List[int] = []

    def bisect_left(arr: List[int], target: int) -> int:
        """
        Find the leftmost index to insert target in arr to maintain sorted order.
        Equivalent to bisect_left(arr, target).
        """
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    for num in nums:
        # Find insertion point in tails using custom binary search
        idx = bisect_left(tails, num)

        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num

    return len(tails)
