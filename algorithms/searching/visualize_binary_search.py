def visualize_binary_search(arr, target):
    """
    Performs binary search and prints each step of the search.

    Args:
        arr (List[int]): Sorted list of integers.
        target (int): Value to search for.

    Returns:
        int: Index of target if found, else -1.
    """
    left, right = 0, len(arr) - 1
    step = 1

    print(f"🔍 Starting binary search for {target} in {arr}")

    while left <= right:
        mid = (left + right) // 2
        print(f"\nStep {step}:")
        print(f"  Left index: {left} → {arr[left]}")
        print(f"  Right index: {right} → {arr[right]}")
        print(f"  Mid index: {mid} → {arr[mid]}")

        if arr[mid] == target:
            print(f"✅ Found target {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"🔼 Target is greater than {arr[mid]} → Searching right half")
            left = mid + 1
        else:
            print(f"🔽 Target is less than {arr[mid]} → Searching left half")
            right = mid - 1

        step += 1

    print(f"❌ Target {target} not found in array.")
    return -1


# Example usage
if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    target = 7
    visualize_binary_search(nums, target)
