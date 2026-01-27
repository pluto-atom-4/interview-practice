"""
## Problem Statement

Implement a generic Graph data structure supporting both directed and undirected graphs with weighted edges.
The goal is to provide core graph operations (add/remove vertices and edges) as the foundation for graph algorithms.
This tests understanding of adjacency lists, graph representation, and data structure design.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using an **Adjacency List representation**:

The adjacency list is chosen over an adjacency matrix because it scales efficiently for sparse graphs (common in interviews) 
and provides O(V + E) iteration. Each vertex maps to a list of (neighbor, weight) tuples, making edge operations intuitive.

* Key Concepts:

  - Why adjacency list with (neighbor, weight) tuples?
The tuple pairing isolates weight data from neighbor identity, enabling edge removal by exact match and simplifying 
weight-based queries. This design supports Dijkstra's algorithm and other weighted graph algorithms naturally.

  - Why use defaultdict(list) for initialization?
defaultdict automatically initializes missing vertices with empty lists, eliminating explicit None checks during 
edge iteration. This reduces defensive coding and prevents KeyError exceptions during traversal.

  - Why check for edge existence before adding?
This prevents duplicate edges that could skew algorithm results (particularly in cycle detection). The check ensures 
each unique edge exists exactly once, maintaining graph invariants.

* Logic:

1. Initialize adjacency list as defaultdict(list) to support automatic vertex creation
2. Store edges as (neighbor, weight) tuples for clean separation of node and weight data
3. When adding an edge: ensure both vertices exist, create tuple, check for duplicates, add to source's list
4. For undirected graphs: automatically add reverse edge from destination back to source
5. When removing: find and delete exact matching edge tuple; remove reverse edge if undirected
6. When removing vertex: delete its entry and purge all references from other vertices

* **30-Second Pitch**:

I'm using an adjacency list with weighted edge tuples. Each vertex maps to a list of (neighbor, weight) pairs. 
When adding edges, I ensure both endpoints exist, prevent duplicates, and automatically mirror edges for undirected graphs. 
This gives clean O(1) vertex lookup and O(degree) edge iteration, scaling well for sparse graphs.

* **Rapid-Fire Version**:

- Adjacency list with (neighbor, weight) tuples
- Automatic vertex creation via defaultdict
- Duplicate edge prevention via existence check
- Undirected graphs auto-mirror edges
- Vertex removal cascades through all incident edges

* **Ultra-Minimal One-Liner**:

Generic adjacency list graph supporting weighted directed/undirected edges with O(1) vertex and O(degree) edge operations.

* **Complexity Analysis**:

- **Time Complexity:** 
  - add_vertex: O(1) 
  - add_edge: O(degree) for duplicate check, O(1) amortized for append
  - remove_edge: O(degree) for search and removal
  - remove_vertex: O(V + E) to purge all references
- **Space Complexity:** O(V + E) for storing vertices and all edges in adjacency list

* **Use Cases**:

Foundation for graph algorithms (BFS, DFS, Dijkstra, cycle detection, topological sort). Common in interview questions 
requiring graph manipulation or traversal, particularly when weighted edge support is needed.
"""

from collections import defaultdict, deque
from typing import Generic, Hashable, Iterator, TypeVar

T = TypeVar('T', bound=Hashable)

class Graph(Generic[T]):
    def __init__(self, directed: bool = False) -> None:
        self.adj_list: dict[T, list[T]] = defaultdict(list)
        self.directed = directed

    def size(self):
        return len(self.adj_list)
    
    def add_vertex(self, vertex: T) -> None:
        if vertex not in self.adj_list:
            # Initialize the vertex with an empty list of edges
            self.adj_list[vertex] = []

    def add_edge(self, src: T, dest: T, weight: int) -> None:
        # Add the 1st and 2nd vertices if they don't exist
        self.add_vertex(src)
        self.add_vertex(dest)
        edge = (dest, weight)
        # Add the edge from src to dest
        if edge not in self.adj_list[src]:  # Check before adding
            self.adj_list[src].append(edge)
        # If undirected, add the reverse edge as well
        if not self.directed:
            reverse_edge = (src, weight)
            # Add the edge from dest to src
            if reverse_edge not in self.adj_list[dest]:
                self.adj_list[dest].append(reverse_edge)

    def remove_edge(self, src: T, dest: T, weight: int) -> None:
        edge = (dest, weight)
        # Remove the edge from src to dest
        if edge in self.adj_list[src]:
            self.adj_list[src].remove(edge)
        # If undirected, remove the reverse edge as well
        if not self.directed:
            reverse_edge = (src, weight)
            # Remove the edge from dest to src
            if reverse_edge in self.adj_list[dest]:
                self.adj_list[dest].remove(reverse_edge)

    def remove_vertex(self, vertex: T) -> None:
        # Remove the vertex and its outgoing edges
        if vertex in self.adj_list:
            del self.adj_list[vertex]

        # Remove all incoming edges (edges pointing to this vertex)
        for src in self.adj_list:
            self.adj_list[src] = [edge for edge in self.adj_list[src] if edge[0] != vertex]

