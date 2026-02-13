"""
## Problem Statement

Given an undirected graph with n nodes and m edges where each edge has weight 6,
find the shortest distance from a starting node s to all other nodes. Return a list
of distances (excluding the start node), using -1 for unreachable nodes.
This tests BFS fundamentals and graph traversal optimization.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using Breadth-First Search (BFS) with an adjacency list:

BFS explores nodes level-by-level, making it ideal for unweighted/equally-weighted graphs.
By processing nodes in queue order, we guarantee that the first time we visit a node,
we've found the shortest path to it. This avoids the overhead of Dijkstra's algorithm.

* Key Concepts:

  - Why use an adjacency list with sets?
Sets automatically deduplicate edges, so parallel edges don't cause revisits.
The adjacency list representation is O(V + E) efficient for sparse graphs,
much better than a full matrix for typical interview problems.

  - Why initialize distances to -1 and mark visited nodes during traversal?
The -1 sentinel value distinguishes unvisited/unreachable nodes from distance 0.
By updating distance before enqueuing, we prevent duplicate queue entries—critical
for O(V + E) time complexity. A single visited flag would also work but distances
here serve dual purpose (distance + visited marker).

  - Why return distances excluding the start node?
Standard problem requirement. The start node's distance to itself is always 0,
adding no value to the result. Filtering it keeps the output clean and consistent
with typical graph distance problem conventions.

* Logic:

1. Build an adjacency list from edges, using sets for each node's neighbors to automatically handle duplicate edges
2. Initialize distances array with -1 (unvisited), set distances[s] = 0
3. Enqueue start node and process queue level-by-level with a while loop
4. For each dequeued node, mark unvisited neighbors with distance and enqueue them
5. Collect distances for all nodes except the start node in the result list

* **30-Second Pitch**:

I'm using BFS because all edges have equal weight (6), making this an unweighted graph
shortest path problem. I build an adjacency list using sets to handle duplicate edges
automatically, then traverse level-by-level from the start node. Since BFS visits
nodes in order of distance, the first time I reach a node is guaranteed to be the
shortest path. I return distances for all nodes except the start, using -1 for unreachable ones.

* **Rapid-Fire Version**:

- BFS for unweighted graph shortest path (all edges weight 6)
- Adjacency list with sets deduplicates edges automatically
- Mark visited by setting distance (dual purpose: distance + visited flag)
- Queue-based level-by-level traversal guarantees shortest path on first visit
- Time: O(V + E), Space: O(V + E) for adjacency list + queue
- Return distances excluding start node, -1 for unreachable

* **Ultra-Minimal One-Liner**:

- BFS on undirected graph using queue-based level traversal to find shortest distances from a source, returning -1 for unreachable nodes.

* **Complexity Analysis**:

- **Time Complexity:** O(V + E) where V is the number of nodes and E is the number of edges.
  Each node is enqueued and dequeued once, and each edge is traversed once (twice for undirected).
  Duplicate edges are eliminated by sets, so worst case is still linear in nodes + edges.

- **Space Complexity:** O(V + E) for the adjacency list (V nodes, E edges stored).
  The queue holds at most O(V) nodes in the worst case. Distances array is O(V).

* **Use Cases**:

Social networks (degrees of separation), game AI (shortest path to goal), network routing
(hop count), collaboration graphs (finding connections). Any scenario where equal-weight
edges require shortest path finding and Dijkstra overhead is unnecessary.
"""

from collections import deque
from typing import List


def bfs(n: int, m: int, edges: List[List[int]], s: int) -> List[int]:
    """
    Solves 'Breadth First Search: Shortest Reach' using a queue.

    Args:
        n: Number of nodes.
        m: Number of edges.
        edges: List of [u, v] pairs representing undirected edges.
        s: Starting node.

    Returns:
        List of distances to all nodes except the start node,
        using -1 for unreachable nodes.
    """
    # 1. Build Adjacency List
    # We use a set for neighbors to handle duplicate edges efficiently
    adj = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # 2. BFS Initialization
    # distances[i] stores the shortest distance from s to i
    distances = [-1] * (n + 1)
    distances[s] = 0

    # Queue stores (current_node)
    queue = deque([s])

    # 3. Traverse the Graph
    edge_weight = 6
    while queue:
        u = queue.popleft()

        for v in adj[u]:
            # If the neighbor hasn't been visited (distance is -1)
            if distances[v] == -1:
                distances[v] = distances[u] + edge_weight
                queue.append(v)

    # 4. Prepare result: skip node s and the 0-index
    result = []
    for i in range(1, n + 1):
        if i == s:
            continue
        result.append(distances[i])

    return result