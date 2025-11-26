"""
Median of Two Sorted Arrays - Naive Merge Approach
----------------------------------------------------
This is a straightforward but suboptimal solution to finding the median of two sorted arrays.
While this approach is easier to understand and implement, it uses O(m + n) time and space,
making it less efficient than the binary search solution. However, it's useful for:
- Understanding the problem fundamentals
- Serving as a baseline for comparison
- Quick prototyping before optimization
- Interview scenarios where you start with naive and optimize

Here is how the process works:

1. **Two Pointer Merge**: Combine two sorted arrays efficiently.
   - Maintain pointers i and j for nums1 and nums2 respectively
   - Compare elements at current pointers and append smaller one to merged list
   - Move the pointer of the array from which we took the element
   - Continue until one array is exhausted

2. **Remaining Elements**: Append remaining elements from non-exhausted array.
   - If nums1 still has elements (i < len(nums1)), append all remaining from nums1
   - If nums2 still has elements (j < len(nums2)), append all remaining from nums2
   - This preserves sorted order since both arrays are already sorted

3. **Median Calculation**: Find median from merged sorted array.
   - Get total length n = len(merged)
   - For odd n: median is the middle element at index n // 2
   - For even n: median is average of two middle elements at indices n // 2 - 1 and n // 2
   - Convert result to float for consistent return type

Example: nums1 = [1, 3], nums2 = [2]
- Merge process: i=0, j=0 → append 1 from nums1, then append 2, 3 from nums1 and nums2
- Merged array: [1, 2, 3]
- Length = 3 (odd), median = merged[1] = 2
- Result: 2.0

Example: nums1 = [1, 2], nums2 = [3, 4]
- Merge process: append 1, 2, 3, 4 in order
- Merged array: [1, 2, 3, 4]
- Length = 4 (even), median = (merged[1] + merged[2]) / 2 = (2 + 3) / 2 = 2.5
- Result: 2.5

Time Complexity: O(m + n) where m = len(nums1), n = len(nums2)
- Merge phase: O(m + n) to process all elements
- Median calculation: O(1)

Space Complexity: O(m + n) for the merged array storage

This solution demonstrates a foundational approach to the problem. In interviews, starting with
this solution can show your ability to solve the problem, then discussing optimization to the
O(log(min(m, n))) binary search approach demonstrates algorithmic depth and optimization skills.
"""

from typing import List


def find_median_sorted_arrays_naive(nums1: List[int], nums2: List[int]) -> float:
    merged = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    n = len(merged)
    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
