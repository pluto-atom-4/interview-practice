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
            self.adj_list[vertex] = []

    def add_edge(self, src: T, dest: T, weight: int) -> None:
        self.add_vertex(src)
        self.add_vertex(dest)
        edge = (dest, weight)
        if edge not in self.adj_list[src]:  # Check before adding
            self.adj_list[src].append(edge)
        if not self.directed:
            reverse_edge = (src, weight)
            if reverse_edge not in self.adj_list[dest]:
                self.adj_list[dest].append(reverse_edge)

    def remove_edge(self, src: T, dest: T, weight: int) -> None:
        edge = (dest, weight)
        if edge in self.adj_list[src]:
            self.adj_list[src].remove(edge)
        if not self.directed:
            reverse_edge = (src, weight)
            if reverse_edge in self.adj_list[dest]:
                self.adj_list[dest].remove(reverse_edge)

    def remove_vertex(self, vertex: T) -> None:
        # Remove the vertex and its outgoing edges
        if vertex in self.adj_list:
            del self.adj_list[vertex]

        # Remove all incoming edges (edges pointing to this vertex)
        for src in self.adj_list:
            self.adj_list[src] = [edge for edge in self.adj_list[src] if edge[0] != vertex]