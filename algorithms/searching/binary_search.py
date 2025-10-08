"""
Binary Search Algorithm Explained Step-by-Step
---------------------------------------------
Binary search is a highly efficient method for finding a target value within a sorted list.

Here is how the process works:

1. Start with two pointers, one at the beginning (left) and one at the end (right) of the list.
2. Find the middle element of the current interval.
3. Compare the middle element to the target value:
   - If it matches, the search is complete.
   - If the target is less than the middle element, repeat the search on the left half.
   - If the target is greater, repeat the search on the right half.
4. Continue narrowing the interval by updating the pointers until the target is found or the interval is empty.

This approach reduces the search space by half with each step, making it much faster than linear search for large, sorted datasets.

Time Complexity: O(log n)
Space Complexity: O(1)

Binary search is a fundamental algorithm often discussed in interviews for its clarity, efficiency, and practical use in real-world applications.
"""


def binary_search(arr, target):
    """
    Performs binary search on a sorted array.

    Args:
        arr (List[int]): Sorted list of integers.
        target (int): Value to search for.

    Returns:
        int: Index of target if found, else -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage
if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    target = 7
    result = binary_search(nums, target)
    print(f"Target {target} found at index: {result}")
