"""
Minimum Cost to Connect All Points - Kruskal's Algorithm with Union-Find Explained Step-by-Step
------------------------------------------------------------------------------------------------
The Minimum Cost to Connect All Points problem asks to connect all given points with minimum total
distance, where the distance between two points is their Manhattan distance. This is a Minimum
Spanning Tree (MST) problem. Kruskal's algorithm builds the MST by sorting all edges by weight and
greedily adding edges that don't create cycles using Union-Find (Disjoint Set Union). This approach
is efficient for sparse graphs and demonstrates both graph theory and union-find data structure usage.

Here is how Kruskal's algorithm works:

1. **Union-Find Data Structure**: Foundation for cycle detection.
   - parent[i] stores the parent of node i in the disjoint set
   - rank[i] stores the rank (approximate depth) of node i's tree
   - find(x): Finds the root of x's set with path compression
   - Path compression: Directly link nodes to root to flatten trees
   - union(x, y): Merges two sets using union by rank for efficiency

2. **Path Compression**: Optimization technique in find() operation.
   - When finding root, update parent[x] to point directly to root
   - Flattens the tree structure for faster future lookups
   - Amortized time complexity approaches O(α(n)) per operation
   - Critical for performance in large graphs

3. **Union by Rank**: Optimization technique in union() operation.
   - Always attach smaller tree under larger tree to minimize depth
   - Prevents degeneration into linear chains
   - Combined with path compression, ensures near-constant operations
   - rank[i] approximates tree height

4. **Edge Generation & Sorting**: Prepare all edges and sort by weight.
   - Generate all n(n-1)/2 possible edges between point pairs
   - Calculate Manhattan distance for each edge: |x1-x2| + |y1-y2|
   - Store edges as (cost, point_i, point_j) tuples
   - Sort edges by cost in ascending order
   - Process minimum-cost edges first

5. **Greedy MST Construction**: Add edges that don't create cycles.
   - Iterate through sorted edges in increasing cost order
   - For each edge (u, v), check if u and v are in different sets
   - union(u, v) only returns True if sets were different (no cycle)
   - Add edge to MST and accumulate cost
   - Continue until n-1 edges are added (complete spanning tree)

6. **Cycle Detection via Union-Find**: Prevent redundant edges.
   - find(u) == find(v) means u and v are already connected
   - Adding edge between them would create a cycle
   - Union-Find efficiently detects this without explicit graph storage
   - Ensures result is a tree (acyclic connected graph)

7. **Final Result**: total_cost contains the minimum spanning tree cost.
   - Sum of all edge weights in the optimal MST
   - Early termination after n-1 edges added
   - Guaranteed to be optimal due to Kruskal's greedy property
   - Return this value as the answer

Example: points = [[0,0], [2,2], [3,10], [5,2], [7,0]]
- Generate all edges: 10 edges total for 5 points
- Sort by Manhattan distance
- Process: Add edges connecting different components until all connected
- Result: n-1=4 edges forming minimum spanning tree

Time Complexity: O(n^2 * log n) overall
  - Generate all edges: O(n^2)
  - Sort edges: O(n^2 * log n)
  - Union-Find operations: O(n * α(n)) ≈ O(n)
  - Dominated by sorting

Space Complexity: O(n^2) for storing all edges
  - Edge list: O(n^2) entries
  - Union-Find structures: O(n)
  - Total dominated by edge storage

Prim's Algorithm vs Kruskal's Algorithm:
  - Prim's: Better for dense graphs, naturally works with adjacency matrices
  - Kruskal's: Better for sparse graphs, naturally works with edge lists
  - Both guarantee optimal MST with same total cost
  - Kruskal's showcases Union-Find data structure

Union-Find Applications:
  - Cycle detection in graphs
  - Connected components detection
  - Detecting redundant connections
  - Kruskal's MST algorithm
  - LCA (Lowest Common Ancestor) problems

This algorithm demonstrates graph optimization using greedy strategy combined with efficient
disjoint set operations, and is essential for understanding MST problems, Union-Find applications,
and competitive programming techniques.
"""

from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

def min_cost_connect_points_kruskal(points: List[List[int]]) -> int:
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((dist, i, j))

    edges.sort(key=lambda x: x[0])
    uf = UnionFind(n)
    total_cost = 0
    edges_used = 0

    for cost, u, v in edges:
        if uf.union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break

    return total_cost
