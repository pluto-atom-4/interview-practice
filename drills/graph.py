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