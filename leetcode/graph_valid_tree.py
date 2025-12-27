"""
Valid Tree (Graph Theory & Union-Find) Algorithm Explained Step-by-Step
------------------------------------------------------------------------
The Valid Tree problem is a classic graph theory problem that determines whether an undirected graph
with n nodes and given edges forms a valid tree. A valid tree must satisfy two conditions:
(1) have exactly n-1 edges, and (2) be fully connected with no cycles. This problem demonstrates
the Union-Find (Disjoint Set Union) data structure, which is essential for cycle detection, connected
components, and network connectivity problems commonly asked in technical interviews.

Here is how the process works:

1. **Edge Count Validation**: Quick sanity check for tree properties.
   - A tree with n nodes must have exactly n-1 edges
   - If edges != n-1, immediately return False
   - This eliminates invalid cases early without expensive computations

2. **Union-Find Initialization**: Set up the Disjoint Set Union (DSU) data structure.
   - parent[i] = i for each node (each node is its own parent initially)
   - rank[i] = 0 for each node (tracks tree height for union optimization)
   - These structures enable efficient cycle detection and connectivity tracking

3. **Find Operation with Path Compression**: Locate the root representative of a node's set.
   - Traverse parent pointers until reaching a node where parent[x] == x
   - Apply path compression: update parent[x] to directly point to root
   - This optimization reduces future find operations to nearly O(1) amortized time

4. **Union Operation with Rank Optimization**: Merge two disjoint sets while detecting cycles.
   - Find roots of both nodes: rootA = find(a), rootB = find(b)
   - If both nodes have same root, they're already connected → cycle detected → return False
   - Otherwise, merge by rank: attach smaller tree to larger tree
   - This maintains balanced trees and ensures O(log n) operations

5. **Cycle Detection Through Union Failures**: Identify cycles by attempting edges.
   - Process each edge by attempting union of its endpoints
   - If union returns False (nodes already connected), a cycle exists → return False
   - If any edge creates a cycle before processing all edges, the graph is invalid

6. **Final Validation**: After processing all edges, verify full connectivity.
   - If all edges were processed without cycle detection, the graph is a valid tree
   - n-1 edges + no cycles automatically means the graph is fully connected
   - Return True to confirm the undirected graph is a valid tree

Example: n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]
- Edge count check: 4 == 5-1 ✓
- Process edges with union-find, no cycles detected ✓
- Result: Valid tree (4 edges, fully connected, no cycles)

Counter-example: n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
- Edge count check: 5 != 5-1 ✗
- Result: Invalid (too many edges, contains cycle)

Time Complexity: O(n * α(n)) where α is the inverse Ackermann function (nearly O(n))
Space Complexity: O(n) for parent and rank arrays

Union-Find is a fundamental algorithm for interview problems involving:
- Cycle detection in undirected graphs
- Detecting connected components
- Checking if a graph is a tree
- Network connectivity verification
- Kruskal's minimum spanning tree algorithm
"""

from typing import List


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    """
    Determine whether the undirected graph is a valid tree.
    A valid tree must:
      - Have exactly n - 1 edges
      - Be fully connected (no cycles)
    """

    # Quick edge-count check
    if len(edges) != n - 1:
        return False

    # Union-Find (Disjoint Set Union)
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path compression
            x = parent[x]
        return x

    def union(a, b):
        rootA, rootB = find(a), find(b)
        if rootA == rootB:
            return False  # cycle detected

        # union by rank
        if rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        elif rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            parent[rootB] = rootA
            rank[rootA] += 1

        return True

    # Process edges
    for a, b in edges:
        if not union(a, b):
            return False

    return True
