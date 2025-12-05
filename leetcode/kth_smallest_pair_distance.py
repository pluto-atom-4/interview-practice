"""
K-th Smallest Pair Distance (Binary Search + Two Pointers Optimization) - Interview Preparation
-------------------------------------------------------------------------------------------------
The K-th Smallest Pair Distance problem asks: given an array of integers and a value k,
find the k-th smallest distance among all possible pairs. This optimized solution uses binary
search combined with the two-pointer technique to avoid generating and sorting all distances.
This demonstrates advanced problem-solving skills crucial for senior technical interviews.

OPTIMIZED APPROACH - O(n log n + n log(max_dist)) Solution:
Binary search on the answer space combined with two-pointer counting strategy.

Here is how the process works:

1. **Sort the Array**: Arrange numbers in ascending order.
   - Sorting enables the two-pointer technique to work efficiently
   - O(n log n) time complexity for sorting
   - Enables distance computation: nums[right] - nums[left] (no abs needed)
   - Foundation for all subsequent operations

2. **Binary Search on Distance Range**: Search for the k-th smallest distance.
   - Search space: [0, nums[-1] - nums[0]] (min and max possible distances)
   - low = 0 (minimum possible distance between distinct elements)
   - high = nums[-1] - nums[0] (maximum possible distance after sorting)
   - We're searching for the smallest distance where count_pairs(distance) >= k

3. **Count Pairs with Two Pointers**: Efficient counting without generating all distances.
   - For each right pointer, find valid left pointer position
   - Pairs (left, right) all have distance <= max_dist when left < right
   - Use while loop to move left pointer right (left increasing never decreases)
   - Count all valid pairs: (right - left) pairs share the same left, right positions

4. **Binary Search Logic**: Narrow down the search space.
   - If count_pairs(mid) >= k: we might have answer here or smaller (high = mid)
   - If count_pairs(mid) < k: answer must be larger (low = mid + 1)
   - Continue until low == high (convergence to answer)
   - This finds the smallest distance where at least k pairs exist

5. **Return the Result**: The converged low/high value is the k-th smallest distance.
   - Binary search ensures low == high at termination
   - This is the minimum distance needed to include k pairs
   - Perfect balance: not too small (< k pairs), not too large (unnecessary)

Example: nums = [1, 6, 1, 1], k = 3
- Sorted: [1, 1, 1, 6]
- Distance range: 0 to 5
- Binary search: find smallest distance where count >= 3
- Pairs with distance 0: (1,1), (1,1), (1,1) = 3 pairs
- Result: 0

Example: nums = [1, 3, 1], k = 1
- Sorted: [1, 1, 3]
- Distance range: 0 to 2
- count_pairs(0): (1,1) = 1 pair >= 1
- Result: 0

Time Complexity: O(n log n + n log(max_dist))
  - O(n log n) for sorting
  - Binary search: O(log(max_dist)) iterations
  - Each count_pairs: O(n) with two pointers
  - Total: O(n log n + n log(max_dist))
  - For reasonable distance ranges, effectively O(n log n)

Space Complexity: O(1) (excluding input/output)
  - Only uses pointers and variables
  - No additional arrays for storing distances
  - Significant improvement over brute force O(n^2)

INTERVIEW INSIGHTS & ADVANTAGES:
- Demonstrates knowledge of binary search on answer space (not index)
- Shows two-pointer technique for efficient counting
- Avoids generating and storing all distances (space optimization)
- Much faster than sorting all O(n^2) distances
- Handles large inputs efficiently (n up to 100,000+)

KEY OPTIMIZATION IDEAS FOR DISCUSSION:
- Why binary search works: monotonic property (more pairs exist at larger distances)
- Why two pointers work: array is sorted, left only needs to increase
- Why we avoid explicit pair generation: unnecessary memory overhead
- Trading space for time: O(1) space vs O(n^2) in naive approach
- Connection to other problems: find k-th element, binary search on answer

WHEN TO USE THIS APPROACH:
- Large input sizes (n > 1000)
- When space optimization is important
- Production code or time-sensitive applications
- Technical interviews emphasizing optimization skills
- Follow-up to brute force: "Can you optimize this?"

RELATED TECHNIQUES:
- Binary search on answer: works when monotonic property exists
- Two-pointer technique: efficient for sorted arrays
- Count-based searching: avoid explicit generation when possible
- Space-time tradeoff: understand when optimization is worthwhile
"""

from typing import List


def smallest_distance_pair(nums: List[int], k: int) -> int:
    """
    Find the k-th smallest pair distance using binary search and two pointers.
    """
    nums.sort()

    def count_pairs(max_dist: int) -> int:
        # Count number of pairs with distance <= max_dist
        count = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > max_dist:
                left += 1
            count += right - left
        return count

    low, high = 0, nums[-1] - nums[0]
    while low < high:
        mid = (low + high) // 2
        if count_pairs(mid) >= k:
            high = mid
        else:
            low = mid + 1
    return low
