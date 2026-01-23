"""
Problem Statement: Given an int[] of work order IDs where values are in the range 1..n (n = array length),
return a list of all duplicate values.

The preferred solution should run in O(n) time and use O(1) extra space by marking the input array in-place.

Example: input [4,3,2,7,8,2,3,1] -> output [2,3].
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

    for i in range(len(work_orders)):
        value = work_orders[i]
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
