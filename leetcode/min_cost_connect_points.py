"""
Minimum Cost to Connect All Points - Prim's Algorithm Explained Step-by-Step
------------------------------------------------------------------------------
The Minimum Cost to Connect All Points problem asks to connect all given points with minimum total
distance, where the distance between two points is their Manhattan distance. This is a Minimum
Spanning Tree (MST) problem. Prim's algorithm builds the MST by starting from one node and greedily
adding the minimum-cost edge that connects a visited node to an unvisited node. This problem is
essential for network design, infrastructure planning, and graph optimization applications.

Here is how Prim's algorithm works:

1. **Initialization**: Start with one arbitrary node (typically node 0).
   - visited[i] tracks which nodes have been included in the MST
   - min_heap stores (cost, node_index) pairs representing available edges
   - Start with (0, 0) since initial node has no cost
   - total_cost accumulates the total MST cost

2. **Greedy Selection**: Always pick the minimum-cost edge connecting visited to unvisited nodes.
   - Pop the minimum element from the priority queue
   - If node is already visited, skip it (handles duplicate edges in heap)
   - Mark the new node as visited and add its cost to total_cost
   - Increment edges_used counter (stop when n nodes are included)

3. **Edge Relaxation**: Add all edges from newly visited node to unvisited nodes.
   - For each unvisited node v, calculate Manhattan distance: |x1-x2| + |y1-y2|
   - Push (distance, v) to the min_heap
   - These edges become candidates for future MST inclusion
   - Lazy deletion: duplicate entries in heap are handled by visited check

4. **Manhattan Distance**: The distance metric used for edge weights.
   - For points (x1, y1) and (x2, y2): distance = |x1-x2| + |y1-y2|
   - Unlike Euclidean distance, Manhattan distance doesn't require sqrt calculations
   - Works on grid-like problems and is efficient for this application

5. **Termination**: Algorithm stops after adding n nodes to MST.
   - When edges_used == n, all nodes are connected
   - The MST is complete and minimum cost is achieved
   - Early termination saves processing time compared to processing all edges

6. **Final Result**: total_cost contains the minimum spanning tree cost.
   - Sum of all edge weights in the optimal MST
   - Guaranteed to be optimal due to Prim's greedy property
   - Return this value as the answer

Example: points = [[0,0], [2,2], [3,10], [5,2], [7,0]]
- Start at node 0, greedily connect nearest unvisited nodes
- Build MST by always choosing minimum-cost edge to unvisited nodes
- Process: Add edges connecting nodes with minimum Manhattan distances
- Result: Sum of edge costs in the MST

Time Complexity: O(n^2 * log n) where n = number of points
  - Generate O(n^2) edges in worst case (all pairs)
  - Each heap operation is O(log n)
  - Each node processed once, examining all unvisited nodes

Space Complexity: O(n^2) for the min_heap in worst case
  - Heap can contain O(n^2) entries for all possible edges
  - visited array uses O(n) space

Prim's Algorithm vs Kruskal's Algorithm:
  - Prim's: Better for dense graphs, naturally handles multiple implementations
  - Kruskal's: Better for sparse graphs, requires Union-Find structure
  - Both guarantee optimal MST with same total cost

This algorithm demonstrates graph optimization using greedy strategy and is essential for
understanding MST problems, priority queue applications, and graph connectivity challenges.
"""

import heapq
from typing import List


def min_cost_connect_points(points: List[List[int]]) -> int:
    """
    Use Prim's algorithm to find the Minimum Spanning Tree (MST).
    Each edge weight is the Manhattan distance between two points.
    """
    n = len(points)
    if n <= 1:
        return 0

    visited = [False] * n
    min_heap = [(0, 0)]  # (cost, point_index)
    total_cost = 0
    edges_used = 0

    while edges_used < n:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        edges_used += 1

        # Add all edges from u to unvisited nodes
        for v in range(n):
            if not visited[v]:
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(min_heap, (dist, v))

    return total_cost
