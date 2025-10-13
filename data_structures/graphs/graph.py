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
