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
