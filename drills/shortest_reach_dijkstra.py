"""
## Problem Statement

Find the shortest path from a source node to all other nodes in a weighted, 
undirected graph. Return distances to all reachable nodes, with -1 for unreachable 
nodes. This is the HackerRank "Shortest Reach 2" challenge—a classic interview 
problem testing Dijkstra's algorithm implementation and graph traversal understanding.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Dijkstra's Algorithm with Min-Heap Priority Queue**:

Dijkstra's algorithm is optimal for single-source shortest paths in graphs with 
non-negative weights. A min-heap ensures we always process the nearest unvisited 
node first, achieving optimal time complexity and guaranteeing correctness.

* Key Concepts:

  - **Why use a min-heap priority queue instead of naive selection?**
  
    Without a heap, finding the minimum unvisited distance requires O(n) per iteration, 
    yielding O(n²) overall. A min-heap reduces this to O(log n) per operation, achieving 
    O((n + m) log n) where m is edges. This is essential for large graphs in interviews.

  - **Why skip outdated distance entries in the priority queue?**
  
    Since we push multiple (distance, node) tuples for the same node, older entries with 
    worse distances become stale. The check `if current_dist > distances[u]: continue` 
    skips processing stale entries, avoiding redundant relaxation and improving efficiency 
    without requiring a "visited" set.

  - **Why handle parallel edges and self-loops during graph construction?**
  
    Parallel edges (duplicates u-v) may have different weights; we keep only the minimum. 
    Self-loops (u==v) are irrelevant to shortest paths and are skipped. This preprocessing 
    prevents incorrect distance calculations and ensures clean input handling.

  - **Why initialize distances to infinity and use float('-inf') for unreachable nodes?**
  
    Infinity is a sentinel representing "not yet computed". After Dijkstra completes, 
    nodes still at infinity are unreachable (no path from source). We return -1 to signal 
    unreachability per the problem specification.

* Logic:

1. **Build the adjacency list** from edges, storing node pairs and weights, handling 
   parallel edges by keeping the minimum weight and skipping self-loops.
2. **Initialize distances** to infinity for all nodes except the source (set to 0), 
   and insert the source into the priority queue.
3. **Process nodes in order of increasing distance** by repeatedly popping the nearest 
   unvisited node from the heap and relaxing its neighbors (updating their distances 
   if a shorter path is found).
4. **Skip stale entries** to avoid reprocessing nodes; once a node is optimally settled, 
   ignore later heap entries with worse distances.
5. **Format and return results** by converting final distances to integers, mapping 
   infinity to -1, and excluding the source node.

* **30-Second Pitch**:

I use Dijkstra's algorithm with a min-heap priority queue. I build an adjacency list 
handling parallel edges and self-loops, initialize distances to infinity except the 
source at zero, then repeatedly extract the nearest node and relax its neighbors. 
Stale heap entries are skipped using a distance check. Finally, I return shortest 
distances as integers, with -1 for unreachable nodes.

* **Rapid-Fire Version**:

- Dijkstra's algorithm with min-heap for O((n + m) log n) efficiency
- Adjacency list with deduplication (minimum weight for parallel edges)
- Lazy deletion: skip stale priority queue entries via distance check
- Relax neighbors when shorter paths are found
- Return distances as integers; -1 for unreachable nodes

* **Ultra-Minimal One-Liner**:

- Dijkstra's single-source shortest path using a min-heap priority queue to efficiently relax edges and handle unreachable nodes.

* **Complexity Analysis**:

- **Time Complexity:** O((n + m) log n) where n is nodes and m is edges. Each node is 
  popped once from the heap (O(n log n)), and each edge is relaxed once 
  (O(m log n) for m heap pushes).
- **Space Complexity:** O(n + m) for the adjacency list and distances array, plus 
  O(n) for the priority queue in the worst case.

* **Use Cases**:

GPS navigation (shortest route finding), network routing protocols (OSPF), game 
pathfinding (NPC AI), robot motion planning, and any shortest-path problem on 
weighted graphs with non-negative weights.
"""

import heapq
from typing import Dict, List, Union


def shortestReach(n: int, edges: List[List[int]], s: int) -> List[int]:
    """
    Implements Dijkstra's algorithm for the HackerRank 'Shortest Reach 2' challenge.

    Args:
        n: The number of nodes in the graph.
        edges: A 2D list where each element is [u, v, weight].
        s: The starting node (1-indexed).

    Returns:
        A list of shortest distances to all nodes except the start node,
        using -1 for unreachable nodes.
    """

    # 1. Build Adjacency List with Type Hinting
    # adj[u] maps neighbor v to the minimum weight w
    adj: List[Dict[int, int]] = [{} for _ in range(n + 1)]

    for u, v, w in edges:
        if u == v:
            continue # Skip self-loops

        # Keep only the minimum weight for parallel edges
        if v not in adj[u] or w < adj[u][v]:
            adj[u][v] = w
            adj[v][u] = w

    # 2. Dijkstra's Algorithm initialization
    # Distances initialized to infinity; using Union for type clarity if needed
    distances: List[float] = [float('inf')] * (n + 1)
    distances[s] = 0.0

    # Priority Queue stores tuples of (distance, node)
    pq: List[tuple[Union[int, float], int]] = [(0.0, s)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        # Optimization: skip processing if we found a better path already
        if current_dist > distances[u]:
            continue

        for v, weight in adj[u].items():
            new_dist = current_dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    # 3. Format result (exclude start node, handle unreachable nodes)
    result: List[int] = []
    for i in range(1, n + 1):
        if i == s:
            continue
        dist = distances[i]
        result.append(int(dist) if dist != float('inf') else -1)

    return result