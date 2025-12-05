"""
K-th Smallest Pair Distance (Brute Force Approach) - Interview Preparation
---------------------------------------------------------------------------
The K-th Smallest Pair Distance problem asks: given an array of integers and a value k,
find the k-th smallest distance among all possible pairs in the array. A pair distance
is the absolute difference between two elements at different indices. This problem is
commonly asked in technical interviews to test understanding of sorting, two-pointers,
and binary search optimization techniques.

BRUTE FORCE APPROACH - O(n^2 log n) Solution:
This naive solution demonstrates the straightforward approach before optimization.

Here is how the process works:

1. **Generate All Pairs**: Create all possible pair combinations.
   - For n elements, there are n*(n-1)/2 unique pairs
   - Iterate through all pairs using nested loops with i < j
   - Compute distance for each pair: abs(nums[i] - nums[j])
   - Store all distances in a list

2. **Store Distances**: Maintain a list of all computed distances.
   - Each distance represents |nums[i] - nums[j]| for some i < j
   - This collection contains all possible pair distances
   - No filtering or early termination, compute all n^2 distances

3. **Sort Distances**: Sort the collected distances in ascending order.
   - Use Python's built-in sort (typically Timsort)
   - Sorting takes O(n^2 log n) time for n^2 elements
   - After sorting, distances[0] is smallest, distances[n^2-1] is largest

4. **Retrieve k-th Value**: Access the k-th smallest distance.
   - Return distances[k-1] (0-indexed array)
   - This is the k-th smallest distance among all pairs
   - Direct index access O(1) after sorting

Example: nums = [1, 6, 1], k = 3
- All pairs: (1,6) dist=5, (1,1) dist=0, (6,1) dist=5
- Distances: [5, 0, 5]
- Sorted: [0, 5, 5]
- Result: distances[2] = 5 (3rd smallest)

Time Complexity: O(n^2 + n^2 log n) = O(n^2 log n)
  - O(n^2) to generate all pairs
  - O(n^2 log n) to sort n^2 distances
  - Dominated by sorting term

Space Complexity: O(n^2) for storing all distances
  - Distances array contains all pair distances
  - No optimization of space usage

INTERVIEW INSIGHTS:
- Shows understanding of basic problem-solving approach
- Good baseline for comparing with optimized solutions
- Identifies bottleneck: sorting all distances unnecessarily
- Natural starting point before binary search optimization
- Demonstrates awareness of space-time tradeoff

WHEN TO USE THIS APPROACH:
- Small input sizes (n ≤ 1000)
- When simplicity and correctness are prioritized
- As a baseline for comparison with optimized solutions
- When interview time is limited and working solution needed first
"""

from typing import List


def smallest_distance_pair_naive(nums: List[int], k: int) -> int:
    """
    Brute-force solution: generate all pair distances and sort.
    Time complexity: O(n^2 log n).
    """
    distances = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            distances.append(abs(nums[i] - nums[j]))
    distances.sort()
    return distances[k - 1]
