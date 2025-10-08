"""
Merge Sort Algorithm Explained Step-by-Step
------------------------------------------
Merge sort is a divide-and-conquer algorithm that efficiently sorts an array by breaking it down into smaller subarrays.

Here is how the process works:

1. **Divide**: Split the array into two halves repeatedly until each subarray contains only one element.
   - Arrays with one element are considered sorted by definition.

2. **Conquer**: Merge the sorted subarrays back together in the correct order:
   - Compare the first elements of each subarray
   - Take the smaller element and add it to the result
   - Move the pointer in that subarray forward
   - Repeat until all elements are merged

3. **Combine**: Continue merging larger and larger subarrays until the entire array is sorted.

Key advantages:
- Stable sort (maintains relative order of equal elements)
- Guaranteed O(n log n) performance regardless of input
- Predictable behavior makes it excellent for large datasets

Time Complexity: O(n log n) - always
Space Complexity: O(n) - requires additional space for merging

This algorithm demonstrates important concepts like recursion, divide-and-conquer strategy, 
and is frequently discussed in technical interviews for its reliability and efficiency.
"""


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
