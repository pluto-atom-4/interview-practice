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


class Graph:
    def __init__(self, directed=False):
        self.adj_list = defaultdict(list)
        self.directed = directed

    def add_edge(self, src, dest):
        """Adds an edge from src to dest."""
        self.adj_list[src].append(dest)
        if not self.directed:
            self.adj_list[dest].append(src)

    def print_graph(self):
        """Prints the adjacency list of the graph."""
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")

    def dfs(self, start, visited=None):
        """Performs depth-first search from the start node."""
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.adj_list[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        """Performs breadth-first search from the start node."""
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


if __name__ == "__main__":
    g = Graph(directed=False)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")

    print("Graph:")
    g.print_graph()

    print("\nDFS from A:")
    g.dfs("A")

    print("\n\nBFS from A:")
    g.bfs("A")
