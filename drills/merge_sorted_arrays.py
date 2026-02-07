"""
## Problem Statement:

Merge two sorted arrays in place without using extra space.
The goal is to achieve this efficiently by minimizing the number of comparisons and swaps.
This is a common problem in technical interviews, testing your understanding of in-place algorithms and optimization techniques.

## Whiteboard Coding Challenge Notes:

* For this problem, I'm using the GAP method inspired by Shell Sort:

The GAP method starts by comparing elements far apart and gradually reduces the gap until it becomes 1.
This ensures that large inversions are resolved early, leading to fewer swaps in the later stages.

* Key Concepts:

  - Why update the gap as `(gap + 1) // 2` and initialize it with `n + m`?
  The GAP method is inspired by the Shell Sort algorithm.
  The gap is initialized to the combined length of the two arrays (`n + m`) to ensure that elements far apart are compared and swapped first.
  This reduces large inversions early in the process.
  The gap is then reduced using `(gap + 1) // 2` to ensure it eventually reaches 1, allowing for a final pass that guarantees the arrays are fully sorted.
  The formula `(gap + 1) // 2` ensures that the gap decreases gradually and avoids getting stuck at zero.

  - Why implement the `get` and `set_val` functions?
  The `get` and `set_val` functions abstract the logic of accessing and modifying elements across two arrays (`a` and `b`).
  This abstraction is necessary because the two arrays are treated as a single logical sequence during the merge process.
  By using these helper functions, the code avoids repetitive and error-prone index calculations, improving readability and maintainability.

* Logic:

1. Initialize the gap as the combined length of the two arrays (`n + m`).
2. Compare elements separated by the gap and swap if they are out of order.
3. Reduce the gap using the formula `(gap + 1) // 2` until it becomes 1.
4. Use helper functions `get` and `set_val` to abstract access to elements across the two arrays.

* **30-Second Pitch**:

The GAP method merges two sorted arrays in place by iteratively reducing the gap between compared elements.
This minimizes space complexity while maintaining efficient time complexity.

* **Rapid-Fire Version**:

- GAP method: compare far-apart elements, reduce gap, and repeat until arrays are merged.

* **Ultra-Minimal One-Liner**:

- GAP method merges two sorted arrays in place with O((n + m) * log(n + m)) time and O(1) space.
"""

from __future__ import annotations

from typing import List


def merge_sorted_arrays_in_place(list_a: List[int], list_b: List[int]) -> None:
    """
    Merge two sorted arrays in place using the GAP method.

    After merging, reading `a + b` as a single sequence yields a sorted array.

    Time:  O((n + m) * log(n + m))
    Space: O(1)
    """
    n, m = len(list_a), len(list_b)

    def get(idx: int) -> int:
        return list_a[idx] if idx < n else list_b[idx - n]

    def set_val(idx: int, value: int) -> None:
        if idx < n:
            list_a[idx] = value
        else:
            list_b[idx - n] = value

    gap = n + m

    while gap > 1:
        gap = (gap + 1) // 2

        for i in range(0, n + m - gap):
            j = i + gap
            if get(i) > get(j):
                v_i, v_j = get(i), get(j)
                set_val(i, v_j)
                set_val(j, v_i)
