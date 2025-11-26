"""
Median of Two Sorted Arrays - Optimal Binary Search Solution
--------------------------------------------------------------
The Median of Two Sorted Arrays is a classic problem that asks to find the median of two sorted arrays
without merging them, achieving O(log(min(m, n))) time complexity. This is a key interview question
that tests understanding of binary search, array partitioning, and problem-solving optimization skills.

Here is how the process works:

1. **Problem Setup**: Find the median of two sorted arrays efficiently.
   - For even total length: median is average of two middle elements
   - For odd total length: median is the single middle element
   - Goal: Avoid O(m + n) merge operation, achieve O(log(min(m, n))) with binary search

2. **Array Optimization**: Ensure the first array is smaller.
   - If len(nums1) > len(nums2), swap them
   - This minimizes the binary search space in the smaller array
   - Reduces iterations needed in the binary search loop

3. **Binary Search on Partition**: Use binary search to find the correct partition point.
   - imin and imax define the search range for partition index in nums1
   - i represents the partition index in nums1
   - j = (m + n + 1) // 2 - i represents the corresponding partition in nums2
   - The partition divides both arrays such that left side has (m + n + 1) // 2 elements

4. **Validity Checking**: Determine if current partition is valid.
   - Valid partition when: nums2[j-1] <= nums1[i] and nums1[i-1] <= nums2[j]
   - If nums2[j-1] > nums1[i]: partition is too far left, increase i (imin = i + 1)
   - If nums1[i-1] > nums2[j]: partition is too far right, decrease i (imax = i - 1)
   - Otherwise, partition is valid and we can calculate the median

5. **Median Calculation**: Compute median from valid partition.
   - Left side max = max(nums1[i-1], nums2[j-1])
   - Right side min = min(nums1[i], nums2[j])
   - Handle edge cases when i == 0, j == 0, i == m, or j == n
   - For odd total length: median is left side max
   - For even total length: median is average of left max and right min

6. **Time Complexity Explanation**: O(log(min(m, n))) achieved through binary search.
   - Binary search runs on the smaller array
   - Each iteration eliminates half of the remaining search space
   - Typically requires O(log(min(m, n))) iterations

Example: nums1 = [1, 3], nums2 = [2]
- Total length = 3 (odd), need 2 elements on left side
- With i=1, j=1: left=[1,2], right=[3], median = max(1,2) = 2
- Result: 2.0

Example: nums1 = [1, 2], nums2 = [3, 4]
- Total length = 4 (even), need 2 elements on left side
- With i=1, j=1: left=[1,3], right=[2,4], median = (3+2)/2 = 2.5
- Result: 2.5

Time Complexity: O(log(min(m, n))) where m = len(nums1), n = len(nums2)
Space Complexity: O(1) - only using a constant amount of extra space

This algorithm is a classic interview problem that demonstrates binary search expertise and
deep understanding of array partitioning. It's often asked at top tech companies to assess
problem-solving ability and algorithmic thinking under constraints.
"""

from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and nums2[j-1] > nums1[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0: max_of_left = nums2[j-1]
            elif j == 0: max_of_left = nums1[i-1]
            else: max_of_left = max(nums1[i-1], nums2[j-1])

            if (m + n) % 2 == 1:
                return float(max_of_left)

            if i == m: min_of_right = nums2[j]
            elif j == n: min_of_right = nums1[i]
            else: min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0
