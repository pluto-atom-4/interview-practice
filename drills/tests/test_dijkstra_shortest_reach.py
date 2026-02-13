"""
FUNCTION shortestReach(n, edges, s):
    // 1. Build Adjacency List
    // Create a list of dictionaries to handle parallel edges by keeping min weight
    adj = NEW LIST OF EMPTY DICTIONARIES OF SIZE n + 1

    FOR EACH [u, v, w] IN edges:
        IF u EQUALS v: CONTINUE // Skip self-loops

        // Keep only the minimum weight if multiple edges exist between same nodes
        IF v NOT IN adj[u] OR w < adj[u][v]:
            adj[u][v] = w
            adj[v][u] = w

    // 2. Dijkstra's Algorithm Initialization
    // Initialize distances to infinity and start node distance to 0
    distances = ARRAY OF SIZE n + 1 FILLED WITH infinity
    distances[s] = 0

    // Priority Queue stores pairs of (distance, node)
    pq = NEW MIN-PRIORITY-QUEUE
    pq.PUSH((0, s))

    WHILE pq IS NOT EMPTY:
        // Get the node with the smallest distance
        current_dist, u = pq.POP_MIN()

        // Optimization: skip processing if a shorter path was already found
        IF current_dist > distances[u]:
            CONTINUE

        FOR EACH neighbor v WITH weight IN adj[u]:
            new_dist = current_dist + weight

            // If a shorter path to v is found, update and push to queue
            IF new_dist < distances[v]:
                distances[v] = new_dist
                pq.PUSH((new_dist, v))

    // 3. Format result
    result = EMPTY LIST
    FOR i FROM 1 TO n:
        IF i EQUALS s: CONTINUE

        dist = distances[i]
        // Use -1 for unreachable nodes, otherwise use the calculated distance
        IF dist EQUALS infinity:
            result.APPEND(-1)
        ELSE:
            result.APPEND(dist)

    RETURN result
"""

import pytest

from drills.dijkstra_shortest_reach import shortestReach


@pytest.mark.parametrize(
    "n, edges, s, expected",
    [
        # Basic case: simple graph
        (4, [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]], 1, [24, 3, 15]),
        # Graph with unreachable nodes
        (5, [[1, 2, 10], [1, 3, 5]], 1, [10, 5, -1, -1]),
        # Graph with multiple edges between same nodes
        (3, [[1, 2, 10], [1, 2, 5], [2, 3, 1]], 1, [5, 6]),
        # Graph with self-loops
        (3, [[1, 1, 10], [1, 2, 5], [2, 3, 1]], 1, [5, 6]),
        # Graph with all nodes reachable
        (4, [[1, 2, 1], [2, 3, 1], [3, 4, 1]], 1, [1, 2, 3]),
        # Graph with parallel edges and different weights
        (4, [[1, 2, 10], [1, 2, 5], [2, 3, 1], [2, 3, 2], [3, 4, 1]], 1, [5, 6, 7]),
        # Graph with single node
        (1, [], 1, []),
        # Graph with two nodes and one edge
        (2, [[1, 2, 10]], 1, [10]),
    ]
)
def test_shortestReach(n, edges, s, expected):
    assert shortestReach(n, edges, s) == expected