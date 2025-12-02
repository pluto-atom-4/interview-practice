"""
K Closest Points to Origin Algorithm Explained Step-by-Step
------------------------------------------------------------
The K Closest Points problem is a classic heap-based algorithm that finds the k points
closest to the origin in 2D space. This problem demonstrates the practical application of
heap data structures, distance computation, and is commonly used in machine learning, spatial
queries, geographic information systems, and recommendation systems.

Here is how the min-heap approach works:

1. **Distance Metric**: Compute squared Euclidean distance to avoid floating-point errors.
   - Distance from (x, y) to origin (0, 0) is sqrt(x² + y²)
   - We use x² + y² to avoid expensive sqrt() computation
   - Squared distance preserves the ordering, so it's sufficient for comparison

2. **Min-Heap Construction**: Build a min-heap with (distance, point) tuples.
   - Each element is a tuple of (squared_distance, coordinates)
   - Python's heapq is a min-heap by default
   - The heap property ensures the smallest distance is at the root
   - Time: O(n) for heapify or O(n log n) for n insertions

3. **Heap Operations**: Use heappush to insert and heappop to extract.
   - heappush(heap, (dist, point)) adds element maintaining heap property
   - heappop(heap) removes and returns minimum element
   - Both operations take O(log n) time

4. **Extraction Phase**: Pop the k smallest elements from the heap.
   - Perform k heappop operations to get k closest points
   - Each pop operation is O(log n)
   - Total time for extraction: O(k log n)
   - Store points in result list

5. **Time Complexity Analysis**:
   - Heap construction: O(n log n) for n heappush operations
   - Extraction: O(k log n) for k heappop operations
   - Total: O(n log n) where we process all n points

6. **Space Complexity**: O(n) for storing all points in the heap.

Alternative Approaches and Trade-offs:
- Sorting approach: O(n log n) time, simpler implementation but must sort all points
- Quickselect approach: O(n) average time, but more complex to implement correctly
- Max-heap of size k: O(n log k) time, better when k << n, requires inverting distances
- Bucket approach: O(n + k) average time when coordinates are bounded

Variations:
- Find k points closest to a specific point (x, y) instead of origin
- Find k furthest points (use max-heap by negating distances)
- Stream version where points arrive continuously (maintain fixed-size max-heap)

Example: points = [[1,3],[-2,2]], k = 1
- Point [1,3]: distance² = 1 + 9 = 10
- Point [-2,2]: distance² = 4 + 4 = 8
- Result: [[-2,2]] (closest point)

This algorithm demonstrates practical heap usage and is essential for understanding
spatial data structures, priority queues, and optimization techniques commonly used
in real-world systems like location-based services and data analysis.
"""

import heapq
from typing import List


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Return the k closest points to the origin (0,0).
    Uses a min-heap based on squared Euclidean distance.
    """
    # Build a heap with (distance, point)
    heap = []
    for (x, y) in points:
        dist = x * x + y * y  # squared distance
        heapq.heappush(heap, (dist, [x, y]))

    result = []
    for _ in range(k):
        _, point = heapq.heappop(heap)
        result.append(point)

    return result
