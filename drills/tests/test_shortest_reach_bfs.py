"""
USING BSF with PQ

INIT adj set()... size: n + 1
LOOP each of edges -> src, dst
  SET: adj src -> dst and dst -> src

INIT distances -1... size: n + 1
SET distances[s] = 0

INIT pq [s]
SET default_weight = 6

# main process
LOOP: pq
  POP pq -> u
  LOOP: each of adj[u] -> v
    CHK|BSF: distances[v] == -1 # not visited
       SET: distances[v] = distances[u] + default_weight
       ENQ: v -> pq

# post process
SET result from distances skipping the first item and index is s

RET: result
"""

"""
FUNCTION bfs(n, m, edges, s):
    // 1. Build Adjacency List
    // Use sets to automatically handle duplicate edges
    adj = NEW LIST OF EMPTY SETS OF SIZE n + 1

    FOR EACH [u, v] IN edges:
        adj[u].ADD(v)
        adj[v].ADD(u)

    // 2. BFS Initialization
    // Initialize distances with -1 to represent unvisited/unreachable nodes
    distances = ARRAY OF SIZE n + 1 FILLED WITH -1
    distances[s] = 0

    // Initialize queue with the starting node
    queue = NEW QUEUE
    queue.ENQUEUE(s)

    // 3. Traverse the Graph
    edge_weight = 6
    WHILE queue IS NOT EMPTY:
        u = queue.DEQUEUE()

        FOR EACH neighbor v IN adj[u]:
            // If the neighbor hasn't been visited yet
            IF distances[v] EQUALS -1:
                // Update distance and add to queue to explore its neighbors
                distances[v] = distances[u] + edge_weight
                queue.ENQUEUE(v)

    // 4. Prepare result
    result = EMPTY LIST
    FOR i FROM 1 TO n:
        // Skip the start node as per requirements
        IF i EQUALS s: CONTINUE

        result.APPEND(distances[i])

    RETURN result
"""

import pytest

from drills.shortest_reach_bfs import bfs


@pytest.mark.parametrize(
    "n, m, edges, s, expected",
    [
        # Basic case: simple graph
        (4,  3, [[1, 2], [1, 3], [3, 4]], 1, [6, 6, 12]),
        # Graph with unreachable nodes
        (5, 2, [[1, 2], [1, 3]], 1, [6, 6, -1, -1]),
        # Graph with multiple edges between same nodes
        (3, 3, [[1, 2], [1, 2], [2, 3]], 1, [6, 12]),
        # Graph with self-loops (should not affect distances)
        (3, 3, [[1, 1], [1, 2], [2, 3]], 1, [6, 12]),
        # Graph with all nodes reachable
        (4, 3, [[1, 2], [2, 3], [3, 4]], 1, [6, 12, 18]),
        # Graph with parallel edges (should not affect distances)
        (4, 5, [[1, 2], [1, 2], [2, 3], [2, 3], [3, 4]], 1, [6, 12, 18]),
        # Graph with single node
        (1, 0, [], 1, []),
        # Graph with two nodes and one edge
        (2, 1, [[1, 2]], 1, [6]),
    ]
)
def test_bfs(n, m, edges, s, expected):
    assert bfs(n, m, edges, s) == expected