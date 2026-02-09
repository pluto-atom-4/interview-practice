"""
## Problem Statement

Given an array of work order IDs where values are in the range 1..n (n = array length),
return a list of all duplicate values. The solution must run in O(n) time and use O(1) extra space
by marking the input array in-place. This tests understanding of array indexing tricks and space-efficient algorithms.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using the **Index Marking (Array Indexing) technique**:

This approach leverages the constraint that values are in range 1..n. Each value can be used as an index
to mark locations in the same array, eliminating the need for extra space. When we encounter a value for
the second time, the location it maps to is already marked, revealing a duplicate.

Before diving into the implementation, here's what I need to know to avoid pitfalls:

* **Values in Range 1..n:** My work order IDs must fall within [1, n], where n is the array length.
  This is crucial because it lets every value map to a valid array index using the formula `abs(value) - 1`.
  Without this constraint, I'll get index errors.
* **Duplicates Exist:** At least one duplicate must be present in my data.
  Thanks to the Pigeonhole Principle, if I have n elements with values in range 1..n, a duplicate is guaranteed—no exceptions.
* **Input Array Mutability:** Fair warning: this solution modifies my input array in-place by negating values.
  If I can't accept that the original array gets altered, this technique won't work for me.
* **No Additional Data Structures:** I can only use the input array itself for marking.
  No hash sets, dictionaries, or auxiliary arrays allowed—they'd break the O(1) space constraint I'm aiming for.
* **Handling Edge Cases:** Out-of-range values (anything less than 1 or greater than n) should be skipped
  to prevent index errors and keep my results clean. Invalid input shouldn't corrupt my algorithm.

* Key Concepts:

  - Why use `abs(value) - 1` to convert values to indices?
The problem constraints guarantee values are in range 1..n, so each value maps uniquely to a valid index.
Subtracting 1 converts the 1-indexed value range to 0-indexed array indices. Using `abs()` handles already-negated
values from previous marks, ensuring we can always derive the correct index even after modification.

  - Why negate values instead of using a separate set/dictionary?
Negation uses the value itself to record "seen" status with zero extra space. When we encounter a negative value
at an index, it means that index's original value (and all duplicates of it) have appeared before. This satisfies
the O(1) space constraint by using the input array as a boolean lookup table.

  - Why handle out-of-range values with `continue`?
Input validation protects against malformed data. If values fall outside 1..n, they can't be properly mapped to
valid indices and shouldn't be processed as valid work order IDs. Skipping them prevents index errors and false
duplicate detections.

* Logic:

1. Iterate through each work order ID in the array
2. Convert the ID to its corresponding index using `abs(value) - 1`
3. Check if the value at that index is negative (indicating we've seen this ID before)
4. If negative, the current ID is a duplicate—add it to the results
5. If positive, mark it as seen by negating the value at that index
6. Return sorted unique duplicates

* **30-Second Pitch**:

I use the array itself as a marking tool. Since values are guaranteed to be 1..n, each value points to a unique
index. I iterate through and negate the value at the index each value points to. When I find an index that's
already negative, I've found a duplicate. This gives O(n) time with O(1) extra space—no hash map needed.

* **Rapid-Fire Version**:

- Values 1..n map directly to indices 0..n-1 (subtract 1)
- Mark seen values by negating the array at their index
- Negative value = duplicate found
- O(1) space: use input array as boolean lookup
- O(n) time: single pass, each element processed once
- Handle out-of-range values to prevent index errors

* **Ultra-Minimal One-Liner**:

Use array values as indices to mark seen elements by negation—when you find a negative marker, you've hit a duplicate.

* **Complexity Analysis**:

- **Time Complexity:** O(n) - Single pass through the array, each element examined once, constant-time operations per element
- **Space Complexity:** O(1) excluding output - Only use the input array for marking; duplicates set is unavoidable for output

* **Use Cases**:

- Finding duplicates in constrained ranges (LeetCode 287, 442), detecting cycles in linked lists (similar indexing principle),
interview problems testing space-optimization awareness, and scenarios where modifying input is acceptable.
- To prevent the redundant factory tasks
"""


def find_duplicates(work_orders: list[int]) -> list[int]:
    """
    Finds all duplicate work order IDs in the given list.

    This function modifies the input list in-place to mark seen IDs by negating
    the values at corresponding indices. It runs in O(n) time and uses O(1) extra space.

    Args:
        work_orders (list[int]): List of work order IDs where each ID is in the range 1..n.

    Returns:
        list[int]: List of duplicate work order IDs in sorted order (unique duplicates only).
    """
    duplicates = set()  # Use set to store unique duplicates only

    for value in work_orders:
        index = abs(value) - 1  # Get index corresponding to the absolute value

        # Handle edge case: out-of-range values (e.g., value > n or value < 1)
        if index < 0 or index >= len(work_orders):
            continue

        if work_orders[index] < 0:
            # If the value at this index is already negative, we've seen this value before
            duplicates.add(abs(value))
        else:
            # Mark the value at this index as seen by negating it
            work_orders[index] = -work_orders[index]

    return sorted(duplicates)
