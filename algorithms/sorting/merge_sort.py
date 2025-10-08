def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        arr (List[int]): List of integers to sort.

    Returns:
        List[int]: Sorted list.
    """
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer (merge)
    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    Args:
        left (List[int]): Left half.
        right (List[int]): Right half.

    Returns:
        List[int]: Merged and sorted list.
    """
    result = []
    i = j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example usage
if __name__ == "__main__":
    nums = [38, 27, 43, 3, 9, 82, 10]
    sorted_nums = merge_sort(nums)
    print(f"Sorted: {sorted_nums}")
