"""
K Closest Points to Origin - Sorting Approach Explained Step-by-Step
---------------------------------------------------------------------
The K Closest Points problem can be elegantly solved using sorting based on distance metrics.
This approach is simpler to implement and understand compared to heaps, though it has a slightly
higher time complexity. This demonstrates the trade-off between simplicity and optimization,
which is important in interview settings.

Here is how the sorting approach works:

1. **Distance Metric**: Compute squared Euclidean distance for comparison.
   - Distance from (x, y) to origin (0, 0) is sqrt(x² + y²)
   - We use x² + y² (squared distance) to avoid expensive sqrt() computation
   - Squared distances preserve relative ordering, sufficient for sorting
   - Lambda function captures distance computation for each point

2. **Custom Sort Key**: Use a lambda function to define the sorting criterion.
   - key=lambda p: p[0] * p[0] + p[1] * p[1] computes distance² for each point
   - Sorts all points by their squared distance to origin in ascending order
   - Smallest distances appear first in sorted array
   - Python's sort is stable (preserves relative order of equal elements)

3. **Sorting Algorithm**: Python uses Timsort for list.sort()
   - Hybrid sorting algorithm combining merge sort and insertion sort
   - Optimized for real-world data (partially sorted sequences)
   - Time: O(n log n) worst and average case
   - Time: O(n) best case (already sorted)

4. **Slicing**: Extract first k elements from sorted list.
   - After sorting, closest k points are at indices [0:k]
   - Python slicing creates a shallow copy of k elements
   - Return only the required results
   - No additional data structure overhead

5. **Complete Algorithm Steps**:
   - Step 1: Sort all n points by squared distance (O(n log n))
   - Step 2: Slice first k elements (O(k))
   - Step 3: Return result list (O(k))

6. **Time Complexity Analysis**:
   - Total: O(n log n) for sorting + O(k) for slicing = O(n log n)
   - Dominated by sorting phase regardless of k value
   - Works equally well whether k is small or large

7. **Space Complexity**: O(1) additional space (ignoring output and sort space).
   - Modifies input array in-place (sorts by reference)
   - Python's sort uses O(n) auxiliary space internally
   - No extra data structures needed for comparison

Comparison with Other Approaches:
- Min-heap approach: O(n log n), uses extra O(n) space, good for all k
- Sorting approach: O(n log n), simpler code, modifies input
- Max-heap of size k: O(n log k), best when k << n, more complex
- Quickselect: O(n) average, O(n²) worst, most complex to implement

Practical Considerations:
- Sorting approach: Best for small datasets, interview simplicity, all k values
- Heap approach: Better for large n with small k, preserves input array
- Industry choice depends on: input size, k value, space constraints, readability

Variations:
- Sort by distance to arbitrary point (x, y) instead of origin
- Sort in descending order to find k furthest points
- Return sorted distances along with points for additional context

Example: points = [[1,3],[-2,2],[5,8]], k = 2
- Point [1,3]: distance² = 1 + 9 = 10
- Point [-2,2]: distance² = 4 + 4 = 8
- Point [5,8]: distance² = 25 + 64 = 89
- After sorting: [[-2,2], [1,3], [5,8]]
- Result: [[-2,2], [1,3]] (first k=2 points)

This approach demonstrates the power of choosing appropriate sorting criteria and highlights
how simple implementations can be competitive with more complex data structures. It's essential
for understanding algorithm trade-offs and practical problem-solving in interviews.
"""

from typing import List


def k_closest_sort(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Return the k closest points to the origin using sorting.
    Complexity: O(n log n).
    """
    points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
    return points[:k]
