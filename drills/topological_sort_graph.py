"""
## Problem Statement

Generate a topological sort of a directed acyclic graph (DAG). The goal is to produce a linear ordering where 
for every edge from node u to node v, u appears before v in the ordering. This tests understanding of DFS post-order 
traversal and dependency resolution in task scheduling and build systems.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **DFS Post-Order Traversal with Reversal**:

Post-order traversal appends nodes only after all descendants are fully explored. Reversing the post-order list naturally 
produces topological order because descendants (which complete first) end up later in post-order, placing them at the 
front when reversed. This elegant approach avoids stacks/priority queues and leverages DFS traversal naturally.

* Key Concepts:

  - Why post-order traversal instead of pre-order?
Topological order requires dependencies (descendants) to complete before dependents (ancestors). Post-order appends 
nodes AFTER exploring descendants, so descendants end up earlier in the list. Reversing this produces the correct order. 
Pre-order would append before exploring descendants, destroying the dependency ordering.

  - Why reverse the post-order list?
Post-order puts deepest (most dependent) nodes first. We want ancestors (least dependent) first. Reversal flips this 
to achieve topological order: if u → v, then u (ancestor) appears before v (descendant) in the reversed output.

  - Why iterate over all vertices for disconnected components?
DAGs can have multiple disconnected components. Iterating ensures all components are processed. Skipping unvisited 
vertices would miss nodes in disconnected components, producing incomplete output.

* Logic:

1. Initialize visited set (Black nodes) and post_order list for appending nodes
2. For each unvisited vertex, start DFS
3. During DFS, recursively explore all neighbors (dependencies)
4. After all neighbors are explored, append current node to post_order (PIN-POINT: post-order)
5. After all vertices processed, reverse post_order to produce topological sort
6. Return reversed list as final topological order

* **30-Second Pitch**:

I do a DFS from all unvisited vertices, and here's the key: I only append a node to my post_order list AFTER 
I've explored all its neighbors (dependencies). Then I reverse the list. This puts dependencies first and 
dependents last, which is exactly topological order: each node appears after all its dependencies.

* **Rapid-Fire Version**:

- DFS visit all unvisited vertices (handle disconnected components)
- Append to post_order AFTER exploring all neighbors (post-order, not pre-order)
- Deeper nodes (more dependencies) naturally end up earlier in post-order
- Reverse post_order to get topological sort
- O(V + E) time, O(V) space

* **Ultra-Minimal One-Liner**:

Post-order DFS appends nodes after descendants, then reverse to produce topological order respecting all dependencies.

* **Complexity Analysis**:

- **Time Complexity:** O(V + E) — each vertex visited once, each edge traversed once; reversal is O(V)
- **Space Complexity:** O(V) — visited set stores up to V nodes; post_order list stores V nodes; recursion depth up to V

* **Use Cases**:

Compiler dependency analysis (compile source files in correct order), package manager resolution (install dependencies before packages), 
task scheduling with prerequisites, build system ordering, course prerequisite fulfillment planning.
"""

from typing import TypeVar

from .graph import Graph

T = TypeVar('T')


def graph_topological_sort(graph: Graph[T]) -> list[T]:
    visited = set()         # Black nodes (fully processed)
    post_order = []         # Nodes added after all descendants explored

    def dfs_post_order(v: T) -> None:
        visited.add(v)      # Mark node as visited (being processed)

        for neighbor, _ in graph.adj_list[v]:  # Explore all neighbors (dependencies)
            if neighbor not in visited:        # White node (unvisited)
                dfs_post_order(neighbor)       # Recursively explore neighbor

        post_order.append(v)  # PIN-POINT: Add to list ONLY after all neighbors explored (Post-Order)

    for vertex in graph.adj_list:               # Process all vertices for disconnected components
        if vertex not in visited:               # Start DFS from unvisited White nodes
            dfs_post_order(vertex)              # DFS traversal in Post-Order

    return post_order[::-1]  # Reverse Post-Order to get Topological Order
