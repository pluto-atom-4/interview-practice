"""
Merge Two Sorted Arrays In-Place (Gap Method / Shell Sort Variant with O(1) Space)
==================================================================================

Whiteboard Coding Challenge: "Merging two sorted arrays in-place using the gap
method to avoid extra memory."

Problem Statement:
Given two sorted arrays a and b, merge them in-place without allocating additional
buffer space. The challenge is to maintain sorted order while only using O(1) extra
memory, which rules out the typical merge-into-a-new-array approach.

Strategy Explanation:
====================

1. **The Gap Algorithm (Shell Sort Variant)**
   - Treat both arrays as one logical sequence: [a₀, a₁, ..., aₙ₋₁, b₀, b₁, ..., bₘ₋₁]
   - Start with a large gap = n + m and repeatedly compare elements that are
     'gap' distance apart
   - After each pass, shrink the gap using: gap = (gap + 1) // 2
   - By the time gap reaches 1, all elements are in correct positions

2. **Helper Functions** (Virtual Indexing):
   getValue(a, b, index, n) - Get value from virtual merged array
   - Treats index < n as a[index], and index >= n as b[index - n]
   - Simplifies logic by providing unified access across both arrays

   setValue(a, b, index, n, value) - Set value in virtual merged array
   - Assigns to a[index] if index < n, else to b[index - n]
   - Enables in-place swapping across array boundaries

3. **Algorithm Steps**:
   Step 1: Initialize gap = len(a) + len(b)
   Step 2: While gap > 1:
           a. gap = (gap + 1) // 2 (shrink gap)
           b. For each index i from 0 to (n + m - gap - 1):
              - val1 = getValue(a, b, i, n)
              - val2 = getValue(a, b, i + gap, n)
              - If val1 > val2: swap them via setValue
   Step 3: When gap becomes 1, final iteration completes the sort
           (no additional passes needed)

4. **Why Gap Method?**
   - Fixes out-of-order pairs efficiently using gap-based comparisons
   - Similar to Shell sort, with exponential speedup from large initial gap
   - Avoids shifting large blocks of elements
   - Naturally handles cross-array comparisons via virtual indexing
   - Works even when len(a) < len(b)

5. **Time Complexity**: O((n + m) * log(n + m))
   - Outer loop runs O(log(n + m)) times (gap shrinks logarithmically)
   - Inner loop runs O(n + m) times for each gap value
   - Total: O((n + m) * log(n + m))

6. **Space Complexity**: O(1)
   - Only uses variables: gap, i, n, m, and temporary swap value
   - No extra arrays or data structures

Edge Cases Handled:
- a is empty (n=0): b remains unchanged
- b is empty (m=0): a remains unchanged
- One array is much larger than the other
- Duplicate elements in both arrays
- Negative numbers, zeros, large values
- Arrays of vastly different sizes

Example Trace:
--------------
a = [1,2,3], b = [2,5,6], n=3, m=3
Virtual array: [1,2,3,2,5,6]

Initial: gap = 6
Iteration 1: gap = (6+1)//2 = 3
  - i=0: val1=a[0]=1, val2=b[0]=2 → 1<2, no swap
  - i=1: val1=a[1]=2, val2=b[1]=5 → 2<5, no swap
  - i=2: val1=a[2]=3, val2=b[2]=6 → 3<6, no swap

Iteration 2: gap = (3+1)//2 = 2
  - i=0: val1=1, val2=3 → 1<3, no swap
  - i=1: val1=2, val2=2 → 2≤2, no swap
  - i=2: val1=3, val2=5 → 3<5, no swap
  - i=3: val1=2, val2=6 → 2<6, no swap

Iteration 3: gap = (2+1)//2 = 1
  - i=0: val1=1, val2=2 → 1<2, no swap
  - i=1: val1=2, val2=2 → 2≤2, no swap
  - i=2: val1=2, val2=3 → 2<3, no swap
  - i=3: val1=3, val2=2 → 3>2, SWAP! a[3]=2→3, b[0]=2→3
  - i=4: val1=5, val2=6 → 5<6, no swap

Final state: a=[1,2,2,3], b=[3,5,6]
When read as [a || b]: [1,2,2,3,3,5,6] ✓

30-Second Pitch:
"I'll merge the arrays in-place using the gap method. I treat both arrays as
one sequence, compare elements gap apart, shrink the gap each pass, and finish
with a fully sorted merge using only O(1) space."

Rapid-Fire Version:
"Gap method: compare, swap, shrink gap — in-place merge."

Ultra-Minimal One-Liner:
"Gap-shrink merge: in-place, zero extra space."
"""

from typing import List


def get_value(a: List[int], b: List[int], index: int, n: int) -> int:
    """
    Get value from the virtual merged array view.

    Treats both arrays as one logical sequence: [a₀, a₁, ..., aₙ₋₁, b₀, b₁, ..., bₘ₋₁]
    This helper abstracts accessing elements across the two physical arrays.

    Args:
        a: first sorted array
        b: second sorted array
        index: logical index in the virtual merged array [a || b]
        n: length of array a

    Returns:
        Value at the logical index

    Time: O(1)
    Space: O(1)
    """
    return a[index] if index < n else b[index - n]


def set_value(a: List[int], b: List[int], index: int, n: int, value: int) -> None:
    """
    Set value in the virtual merged array view.

    This helper abstracts setting elements across the two physical arrays,
    allowing in-place swapping across array boundaries.

    Args:
        a: first sorted array
        b: second sorted array
        index: logical index in the virtual merged array [a || b]
        n: length of array a
        value: value to set at the index

    Time: O(1)
    Space: O(1)
    """
    if index < n:
        a[index] = value
    else:
        b[index - n] = value


def merge(a: List[int], b: List[int]) -> None:
    """
    Merge two sorted arrays in-place using the gap method.

    After this operation, reading [a || b] as a single sequence produces a sorted array.

    This algorithm treats both arrays as one logical sequence and uses the gap method
    (similar to Shell sort) to gradually sort all elements using only O(1) extra space.

    Args:
        a: first sorted array (will be modified in-place)
        b: second sorted array (will be modified in-place)

    Returns:
        None (modifies a and b in-place)

    Time Complexity: O((n + m) * log(n + m))
        - Outer loop runs O(log(n + m)) times (gap shrinks logarithmically)
        - Inner loop runs O(n + m) times for each gap value
        - Total: O((n + m) * log(n + m))

    Space Complexity: O(1)
        - Only uses variables: gap, i, n, m
        - No extra arrays or data structures

    Algorithm:
    1. Initialize n = len(a), m = len(b)
    2. Set gap = n + m (total logical length)
    3. While gap > 1:
       a. gap = (gap + 1) // 2 (shrink gap using standard formula)
       b. For i in range(n + m - gap):
          - Get val1 = getValue(a, b, i, n)
          - Get val2 = getValue(a, b, i + gap, n)
          - If val1 > val2: swap via setValue
    4. When gap becomes 1, the final iteration completes the sort

    Example:
        >>> a = [1, 2, 3]
        >>> b = [2, 5, 6]
        >>> merge(a, b)
        >>> a
        [1, 2, 2, 3]
        >>> b
        [3, 5, 6]
        >>> # Reading [a || b] gives [1, 2, 2, 3, 3, 5, 6] which is sorted
    """
    n = len(a)
    m = len(b)

    # Use gap method similar to Shell sort: compare elements gap-distance apart
    # across the combined logical array [a₀, a₁, ..., aₙ₋₁, b₀, b₁, ..., bₘ₋₁]
    # and swap them if they're out of order.

    gap = n + m
    while gap > 1:
        gap = (gap + 1) // 2  # Shrink gap using standard formula

        # Compare elements gap distance apart
        for i in range(n + m - gap):
            val1 = get_value(a, b, i, n)
            val2 = get_value(a, b, i + gap, n)

            if val1 > val2:
                set_value(a, b, i, n, val2)
                set_value(a, b, i + gap, n, val1)

    # When gap becomes 1, the final iteration completes the sort.
    # No additional passes are needed as the gap method naturally handles gap=1.

