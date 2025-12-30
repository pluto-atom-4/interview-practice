"""
Quick Sort Algorithm Explained Step-by-Step
---------------------------------------------
Quick Sort is a highly efficient divide-and-conquer sorting algorithm that selects a 'pivot' element
and partitions the array around it, then recursively sorts the resulting subarrays. It's one of the most
widely used sorting algorithms in practice due to its excellent average-case performance and cache efficiency.
The algorithm is fundamental for understanding sorting, algorithmic complexity, and optimization techniques.

Here is how the process works:

1. **Pivot Selection**: Choose an element as the pivot for partitioning.
   - Strategy: Can use first, last, middle, or random element
   - The middle element is used in this implementation for balance
   - Different strategies affect worst-case performance but not average case
   - Random pivot is often preferred to avoid worst-case on sorted arrays

2. **Partitioning**: Divide the array into three parts based on the pivot.
   - Elements less than pivot (left partition)
   - Elements equal to pivot (middle partition)
   - Elements greater than pivot (right partition)
   - This separation is done using list comprehensions in this functional approach
   - In-place partitioning versions modify the array without extra space

3. **Recursive Sorting**: Recursively sort the left and right partitions.
   - Base case: Arrays with 0 or 1 element are already sorted
   - Recursive calls: Sort left partition, then right partition
   - The middle partition (equal elements) needs no sorting
   - Recursion continues until all subarrays are base cases

4. **Combine Results**: Concatenate the sorted partitions with the pivot.
   - Order: sorted_left + pivot_equal + sorted_right
   - This maintains the sorted order from partitioning
   - The functional style concatenation is clean but creates new lists
   - In-place versions modify the original array in-place

5. **Divide-and-Conquer Strategy**: Breaking problem into smaller subproblems.
   - Each partition becomes an independent subproblem
   - Solving subproblems recursively and combining results
   - Similar strategy used in merge sort and quick select
   - Demonstrates how to apply recursion for sorting

6. **Why Quick Sort is Efficient**:
   - Excellent cache locality with in-place partitioning
   - Divides problem in-half on average, leading to O(n log n)
   - Simpler than merge sort with no extra merge phase
   - Practical choice for most real-world sorting needs
   - Works well with system memory hierarchies

Example: arr = [5, 2, 8, 1, 9, 3]
- Pivot: 8 (middle element at index 2)
- Partition: left=[5, 2, 1, 3], mid=[8], right=[9]
- Recursively sort left and right
- Combine: sort([5, 2, 1, 3]) + [8] + sort([9])
- Result: [1, 2, 3, 5, 8, 9]

Time Complexity:
- Best Case: O(n log n) - pivot divides array evenly each time
- Average Case: O(n log n) - typical balanced partitioning
- Worst Case: O(n²) - pivot always smallest/largest (rare with good pivot selection)
- Note: Worst case occurs with sorted arrays and first/last pivot selection

Space Complexity:
- This functional version: O(n log n) for creating new lists during partitioning
- In-place in-situ version: O(log n) for recursion call stack only
- Trade-off: Clarity and simplicity vs. space efficiency

Optimization Techniques:
1. Random pivot selection to avoid worst-case on sorted data
2. Three-way partitioning for arrays with many duplicates (like this implementation)
3. Hybrid approach: switch to insertion sort for small subarrays
4. In-place Hoare or Lomuto partitioning to save space
5. Tail recursion optimization for the larger partition

Interview Tips:
- Explain why average case is O(n log n) and when worst case O(n²) occurs
- Compare with merge sort (stable, guaranteed O(n log n)) and heap sort
- Discuss in-place vs. this functional approach trade-offs
- Mention how pivot selection affects performance on different inputs
- Be ready to code in-place partition and explain the challenges
- Quick select algorithm uses similar partition technique to find kth smallest
- Quick sort is often preferred in practice due to better constants than merge sort

This algorithm is essential for understanding sorting, recursion, and algorithmic analysis.
It demonstrates divide-and-conquer strategy and how to analyze average vs. worst-case complexity.
"""

from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    """
    Pure functional quick-sort implementation.
    Returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)
