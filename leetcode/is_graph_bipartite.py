from collections import deque
from typing import List, Union


def is_bipartite(graph: List[List[int]]) -> bool:
    """
    ## Problem Statement

    Determine whether an undirected graph is bipartite. A bipartite graph can be partitioned 
    into two independent sets such that every edge connects vertices from different sets. This 
    tests understanding of graph coloring, BFS traversal, and connected component detection.

    ## Whiteboard Coding Challenge Notes

    * For this problem, I'm using **BFS 2-Coloring**:

    Graph bipartiteness is fundamentally a coloring problem—we can partition vertices into two 
    sets if and only if the graph is 2-colorable. BFS exploration with alternating color assignment 
    allows us to detect conflicts immediately and handle disconnected components efficiently.

    * Key Concepts:

      - Why BFS with 2-coloring instead of DFS or other approaches?
    BFS processes nodes level-by-level, making color conflicts immediately apparent when we encounter 
    a neighbor that should have the opposite color. This is more intuitive than DFS and equally efficient. 
    The two-color constraint directly maps to bipartite definition: if we can color with 2 colors without 
    conflicts, the graph is bipartite.

      - Why initialize color array as [None] * n and check if color[start] is not None?
    The None sentinel distinguishes unvisited nodes from colored nodes (0 and 1). Checking skip already-colored 
    nodes ensures we handle disconnected components without redundant work. Each component is independently 
    2-colorable, so checking one component at a time covers all vertices.

      - Why use color[neighbor] = 1 - color[node] to alternate colors?
    Subtracting from 1 elegantly toggles between 0 and 1 colors. This ensures adjacent nodes always have 
    opposite colors. A conflict (same color for adjacent nodes) immediately proves the graph is not bipartite, 
    allowing early termination.

    * Logic:

    1. Initialize a color array with None for all vertices (unvisited marker)
    2. For each unvisited vertex, start a BFS if it hasn't been colored
    3. Assign the starting vertex color 0 and enqueue it
    4. While the queue is not empty, process each node:
       - For each neighbor, if uncolored, assign opposite color and enqueue
       - If neighbor is already colored with the same color as current node, conflict detected—return False
    5. If all vertices processed without conflict, the graph is bipartite—return True

    * **30-Second Pitch**:

    I use BFS with 2-coloring to determine bipartiteness. The key idea is that a graph is bipartite if and 
    only if it can be 2-colored without adjacent nodes sharing the same color. I maintain a color array, 
    process each connected component with BFS, alternate colors for neighbors, and immediately return False 
    if a conflict occurs. Otherwise, all components are 2-colorable, so the graph is bipartite.

    * **Rapid-Fire Version**:

    - BFS 2-coloring: bipartite ⟺ 2-colorable
    - Color array tracks visited nodes and their colors (None, 0, 1)
    - For each unvisited node, run BFS assigning alternating colors to neighbors
    - Conflict = same color for adjacent nodes = not bipartite
    - Handle disconnected components by iterating through all starting vertices
    - Early exit on conflict; return True if all components processed

    * **Ultra-Minimal One-Liner**:

    - BFS 2-coloring assigns alternating colors to neighbors; if adjacent nodes share a color, the graph is not bipartite.

    * **Complexity Analysis**:

    - **Time Complexity:** O(V + E) where V is the number of vertices and E is the number of edges. BFS visits 
    each vertex once and explores each edge once (from both endpoints).
    - **Space Complexity:** O(V) for the color array and queue. In the worst case, the queue holds O(V) vertices 
    during BFS traversal.

    * **Use Cases**:

    Bipartite checking is essential in job scheduling (two types of tasks), exam timetabling (conflicts between 
    exam pairs), matching problems, and relationship networks (finding if a social network can be split into two 
    groups with no internal conflicts).
    """

    n = len(graph)
    color: List[Union[None, int]] = [None] * n # None = uncolored, 0 and 1 are the two colors

    for start in range(n):
        if color[start] is not None:
            continue

        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] is None:
                    color[neighbor] = 1 - color[node] # Alternate color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False # Conflict found, not bipartite

    return True


