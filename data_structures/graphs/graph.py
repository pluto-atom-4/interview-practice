"""
Graph Data Structure Explained Step-by-Step
------------------------------------------
A graph is a collection of nodes (vertices) connected by edges. It can be directed or undirected.

Here is how the process works:

1. **Add Edge**: Connect two nodes by adding an edge between them.
   - For undirected graphs, add the connection in both directions
   - For directed graphs, add the connection from source to destination only

2. **Print Graph**: Display the adjacency list showing each node and its neighbors.
   - Traverse all nodes and print their connections

3. **Depth-First Search (DFS)**: Explore as far as possible along each branch before backtracking.
   - Start from a node, mark it as visited
   - Recursively visit all unvisited neighbors

4. **Breadth-First Search (BFS)**: Explore all neighbors at the current depth before moving deeper.
   - Use a queue to track nodes to visit
   - Mark nodes as visited and enqueue their unvisited neighbors

Graphs are fundamental for modeling relationships and networks, and are widely used in computer science interviews.

Time Complexity:
- Add Edge: O(1)
- DFS/BFS: O(V + E) where V is vertices and E is edges
- Space Complexity: O(V + E) for adjacency list

This data structure demonstrates traversal algorithms and is essential for solving connectivity and pathfinding problems.
"""

from collections import defaultdict, deque
from typing import Generic, Hashable, Iterator, TypeVar

T = TypeVar("T", bound=Hashable)


class Graph(Generic[T]):
    """A flexible graph data structure supporting directed and undirected graphs.

    Attributes:
        directed: If True, edges are directed; otherwise, undirected.
    """

    def __init__(self, directed: bool = False) -> None:
        """Initialize a graph.

        Args:
            directed: Whether the graph is directed (default: False).
        """
        self.adj_list: dict[T, list[T]] = defaultdict(list)
        self.directed = directed

    def add_edge(self, src: T, dest: T) -> None:
        """Add an edge between two nodes.

        For undirected graphs, creates a bidirectional edge.
        For directed graphs, creates a one-way edge from src to dest.

        Args:
            src: Source node.
            dest: Destination node.
        """
        self.adj_list[src].append(dest)
        if not self.directed:
            self.adj_list[dest].append(src)

    def __repr__(self) -> str:
        """Return string representation of the graph."""
        graph_type = "Directed" if self.directed else "Undirected"
        return f"{self.__class__.__name__}({graph_type}, nodes={len(self.adj_list)})"

    def __iter__(self) -> Iterator[T]:
        """Iterate over all nodes in the graph."""
        return iter(self.adj_list)

    def neighbors(self, node: T) -> list[T]:
        """Get all neighbors of a node.

        Args:
            node: The node to query.

        Returns:
            List of neighboring nodes.
        """
        return self.adj_list.get(node, [])

    def dfs(self, start: T) -> Iterator[T]:
        """Depth-first search traversal.

        Yields nodes in DFS order starting from the given node.

        Args:
            start: Starting node for traversal.

        Yields:
            Nodes visited in depth-first order.
        """
        visited: set[T] = set()

        def _dfs_recursive(node: T) -> Iterator[T]:
            visited.add(node)
            yield node
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    yield from _dfs_recursive(neighbor)

        yield from _dfs_recursive(start)

    def bfs(self, start: T) -> Iterator[T]:
        """Breadth-first search traversal.

        Yields nodes in BFS order starting from the given node.

        Args:
            start: Starting node for traversal.

        Yields:
            Nodes visited in breadth-first order.
        """
        visited: set[T] = {start}
        queue: deque[T] = deque([start])

        while queue:
            node = queue.popleft()
            yield node
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def __str__(self) -> str:
        """String representation of adjacency list."""
        lines = [f"{node} -> {neighbors}" for node, neighbors in self.adj_list.items()]
        return "\n".join(lines)


if __name__ == "__main__":
    # Create an undirected graph
    g: Graph[str] = Graph[str](directed=False)

    # Add edges
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    for src, dest in edges:
        g.add_edge(src, dest)

    # Display graph info
    print(f"Graph Info: {g!r}\n")

    # Display adjacency list
    print("Adjacency List:")
    print(g)

    # DFS traversal
    print("\nDFS from A:", " -> ".join(g.dfs("A")))

    # BFS traversal
    print("BFS from A:", " -> ".join(g.bfs("A")))

    # Get neighbors
    print(f"\nNeighbors of D: {g.neighbors('D')}")

    # Iterate over all nodes
    print(f"All nodes: {list(g)}")
