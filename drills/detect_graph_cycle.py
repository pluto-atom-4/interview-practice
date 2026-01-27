"""
## Problem Statement

Detect if a directed graph contains a cycle. The goal is to identify cyclic dependencies, which is critical 
for task scheduling validation and deadlock detection. This tests understanding of graph traversal with 
state tracking and DFS backtracking mechanics.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **DFS with Three-Color Marking (White/Gray/Black)**:

The three-color approach uniquely identifies back edges (edges to nodes in the current recursion path), which indicate 
cycles. Unlike simple visited tracking, this distinguishes between nodes being actively explored vs. fully processed, 
catching cycles that other methods might miss.

* Key Concepts:

  - Why three colors instead of a simple visited set?
A single visited set can't distinguish between nodes in the active recursion path and nodes fully explored. A back edge 
(edge to a Gray node) proves a cycle; an edge to a Black node is just a cross-edge. This distinction is essential for 
detecting cycles vs. just traversing already-explored branches.

  - Why remove from rec_stack on backtrack?
Removing marks the node as Black (fully processed). This prevents false positives where we revisit a node in a different 
branch and incorrectly flag it as part of the current cycle. The removal happens AFTER exploring all descendants, ensuring 
accurate state tracking.

  - Why iterate over all vertices?
Directed graphs may have disconnected components. Iterating over unvisited vertices ensures we explore all components. 
A cycle in any component makes the entire graph cyclic, so we process until a cycle is found or all components are checked.

* Logic:

1. Initialize visited set (Black nodes) and rec_stack set (Gray/active nodes)
2. For each unvisited vertex, start DFS from that vertex
3. Mark vertex as visited and add to recursion stack (turning Gray)
4. For each neighbor: if unvisited, recursively explore; if in rec_stack, cycle detected
5. On backtracking, remove vertex from rec_stack (mark as Black)
6. Return True if any DFS finds a cycle; False if all components are acyclic

* **30-Second Pitch**:

I'm using DFS with a recursion stack to track the active path through the graph. If I encounter a neighbor already 
in the current recursion path, that's a back edge proving a cycle. I mark nodes as visited and track them in a stack 
as I explore, removing them when backtracking to distinguish cyclic vs. already-explored paths.

* **Rapid-Fire Version**:

- DFS with recursion stack (Gray nodes = active path)
- Visited set for previously processed (Black nodes)
- Back edge detection: neighbor in rec_stack = cycle found
- Backtracking removes nodes from rec_stack (mark as Black)
- Check all components for disconnected graphs

* **Ultra-Minimal One-Liner**:

DFS with three-color marking detects back edges (edges to active recursion nodes) proving cycles in directed graphs.

* **Complexity Analysis**:

- **Time Complexity:** O(V + E) — each vertex visited once, each edge checked once during adjacency traversal
- **Space Complexity:** O(V) — visited and rec_stack sets each store up to V nodes; recursion depth up to V

* **Use Cases**:

Task scheduling validation (detecting impossible dependencies), deadlock detection in resource allocation, 
compiler dependency analysis, circuit timing analysis in hardware design.
"""

from typing import TypeVar

from .graph import Graph

T = TypeVar('T')


def graph_cycle_detection(graph: Graph[T]) -> bool:
    visited = set()    # Black nodes (fully processed)
    rec_stack = set()  # Gray nodes (in current recursion path = active path)

    def dfs(v: T) -> bool:
        visited.add(v)      # Mark node as being processed (transitioning to Gray)
        rec_stack.add(v)    # Add to recursion stack (node is Gray: in current path)

        for neighbor, _ in graph.adj_list[v]:
            if neighbor not in visited:     # White node (unvisited)
                if dfs(neighbor):           # Recursively explore White node
                    return True
            elif neighbor in rec_stack:     # Gray node found = back edge detected = cycle exists
                return True

        rec_stack.remove(v)     # BACKTRACKING: Remove from Gray set (mark as Black: fully processed)
        return False

    for vertex in graph.adj_list:
        if vertex not in visited:           # Start DFS from unvisited White nodes
            if dfs(vertex):                 # Cycle found in this connected component
                return True

    return False    # No cycles detected in entire graph
