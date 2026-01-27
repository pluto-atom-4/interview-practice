"""
## Problem Statement

Implement breadth-first search (BFS) and depth-first search (DFS) graph traversals that yield nodes in visit order.
The goal is to explore all reachable nodes from a starting vertex, enabling connectivity analysis and shortest-path 
discovery. This tests understanding of queue/stack-based traversal and the yield keyword for generator-based iteration.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Generator-Based BFS and DFS with Yield**:

Both functions use the yield keyword to return an iterator instead of building a full result list. BFS uses a deque for 
level-order exploration; DFS uses a stack for depth-first exploration. Generators defer computation, enabling lazy evaluation 
and memory efficiency—crucial for large graphs where only partial exploration might be needed.

* Key Concepts:

  - Why yield instead of building a list?
Generators allow lazy evaluation: results are produced on-demand rather than computing the entire traversal upfront. 
For massive graphs, clients might only need the first few nodes, making generators far more efficient than materializing 
the full traversal. This supports infinite graphs and reduces memory footprint significantly.

  - Why deque for BFS vs. list for DFS?
Deques support O(1) popleft() for queue behavior; lists don't (O(n)). For DFS, stack behavior (pop from end) is O(1) 
on lists. Using the right data structure ensures both algorithms run in O(V + E) without hidden quadratic costs.

  - Why reverse neighbors before appending in DFS?
Reversing ensures DFS explores neighbors in their original adjacency order. Without reversal, the stack's LIFO 
behavior would visit neighbors in reverse order, changing the traversal sequence unexpectedly.

* Logic:

**BFS:**
1. Initialize visited set and deque with start node
2. Mark start as visited
3. While deque not empty: popleft a node, yield it, add unvisited neighbors to deque and mark visited

**DFS:**
1. Initialize visited set and stack with start node
2. While stack not empty: pop a node; if unvisited, mark visited and yield it
3. Add unvisited neighbors to stack (reversed to maintain order)

* **30-Second Pitch**:

BFS explores level-by-level using a deque queue—all immediate neighbors first, then their neighbors, creating a breadth-wise 
expansion. DFS explores deeply using a stack—following one path to its end before backtracking, creating depth-wise traversal. 
Both yield nodes one at a time, enabling lazy evaluation without building the full traversal upfront.

* **Rapid-Fire Version**:

- BFS: deque queue, level-order exploration, FIFO visits nodes breadth-first
- DFS: list stack, depth-first exploration, LIFO follows paths to depth before backtracking
- Both use yield for lazy, memory-efficient iteration
- Visited set prevents revisiting nodes
- DFS reverses neighbors for correct traversal order

* **Ultra-Minimal One-Liner**:

BFS and DFS generators enable lazy graph exploration level-by-level (BFS) or depth-first (DFS) with O(V + E) efficiency.

* **Complexity Analysis**:

- **Time Complexity:** O(V + E) for both — each vertex visited once, each edge traversed once during neighbor checks
- **Space Complexity:** O(V) — visited set stores up to V nodes; queue/stack stores up to V nodes in worst case

* **Use Cases**:

Finding shortest paths in unweighted graphs (BFS), detecting connected components, maze solving, network broadcasting, 
social network analysis (degrees of separation), exploring game trees, checking graph connectivity, topological sorting preparation.
"""

from collections import deque
from typing import Iterator, TypeVar

from .graph import Graph

T = TypeVar('T')


def graph_bfs(graph: Graph[T], start: T) -> Iterator[T]:
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        yield vertex

        for neighbor, _ in graph.adj_list[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def graph_dfs(graph: Graph[T], start: T) -> Iterator[T]:
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            yield vertex

            for neighbor, _ in reversed(graph.adj_list[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
