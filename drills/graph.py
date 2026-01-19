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

def graph_lowest_common_ancestor(graph: Graph[T], root: T, p: T, q: T) -> T | None:
    def dfs(node: T) -> T | None:
        if node is None or node == p or node == q:  # Base case: found target or dead end
            return node

        found_nodes = []  # Track results from child branches
        for neighbor, _ in graph.adj_list[node]:    # Explore all children
            result = dfs(neighbor)                  # Recursively search in subtree
            if result is not None:                  # Child branch found a match
                found_nodes.append(result)

        if len(found_nodes) >= 2:                   # Both p and q found in different branches = node is LCA
            return node

        return found_nodes[0] if found_nodes else None  # Pass up result from single branch or None

    return dfs(root)  # Start DFS from root node