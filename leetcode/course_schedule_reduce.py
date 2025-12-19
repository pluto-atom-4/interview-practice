"""
Course Schedule - Cycle Detection using Functional Reduce Pattern
-------------------------------------------------------------------
This is a variant of the Course Schedule problem using the functional programming paradigm with reduce().
The problem determines if all courses can be completed given prerequisites by detecting cycles in a
directed graph. This implementation uses reduce() to build the adjacency list functionally, avoiding
mutable state, which is useful for demonstrating functional programming patterns in Python interviews.

Here is how the process works:

1. **Problem Understanding**: Model prerequisites as a directed graph for cycle detection.
   - Each course is a node
   - Each prerequisite [a, b] means: must complete b before a
   - Edge: a → b (dependency direction)
   - Can complete all courses ⟺ no cycles in graph

2. **Functional Graph Building with reduce()**: Immutably construct adjacency list.
   - Instead of mutating a dictionary in a loop, use reduce()
   - reduce() takes a function and sequences of prerequisites
   - Each step creates a new dictionary (immutable update: {**graph, a: graph[a] + [b]})
   - Benefits: purely functional, easier to reason about, parallelizable
   - Disadvantage: less efficient than imperative (creates new dict for each edge)

3. **Reduce Function Mechanics**: How add_edge accumulates the graph.
   - Signature: add_edge(graph, pair) → new_graph
   - Takes current graph state and next prerequisite [a, b]
   - Returns new dict with edge b added to graph[a]
   - {**graph, a: graph[a] + [b]} creates new dict, avoiding mutation
   - reduce() chains these operations to build complete graph

4. **Why Use Reduce for Interview**: Demonstrates functional programming knowledge.
   - Shows understanding of higher-order functions and composition
   - Proves ability to transform imperative code to functional style
   - Useful for demonstrating immutability and pure functions
   - Can discuss trade-offs: readability vs. functional purity vs. performance

5. **Cycle Detection**: Same DFS strategy as standard version.
   - Use three node states: visiting (in stack), visited (complete), unvisited
   - If encounter node in "visiting" set: cycle detected, return False
   - If encounter visited node: safe path, return True
   - Mark node as visiting before recursion
   - Process all neighbors recursively

6. **Global Validation**: Check all courses can complete.
   - Run DFS from each course
   - All must return True (no cycles reachable from any starting point)
   - all() checks every course individually

Example: numCourses = 3, prerequisites = [[0, 1], [1, 2]]
- reduce() builds: {0: [1], 1: [2], 2: []}
- DFS detects no cycles
- Result: True

Example: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
- reduce() builds: {0: [1], 1: [0]} (cycle)
- DFS detects cycle: 0→1→0
- Result: False

Time Complexity: O(V + E)
- reduce() iterates E edges: O(E)
- DFS visits each node and edge: O(V + E)
- Total: O(V + E) for both graph building and traversal

Space Complexity: O(V + E)
- Graph adjacency list: O(V + E)
- Reduce creates intermediate dicts: O(V) per step, O(V + E) total
- DFS recursion stack: O(V)

Interview Discussion Points:
- Functional vs. imperative approaches
- Trade-offs: clarity vs. performance vs. paradigm demonstration
- How reduce() is useful for aggregation and accumulation patterns
- When to use functional patterns in Python
- Comparison with iterative, generator, and memoization approaches

This variant is excellent for demonstrating functional programming patterns and is often used
in interviews to assess understanding of higher-order functions and immutable data structures.
"""

from functools import reduce
from typing import Dict, List, Set


def canFinish_reduce(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Pure functional reduce-based version of Course Schedule.
    """

    # Build adjacency list using reduce
    def add_edge(graph, pair):
        a, b = pair
        return {**graph, a: graph[a] + [b]}

    graph: Dict[int, List[int]] = reduce(
        add_edge,
        prerequisites,
        {i: [] for i in range(numCourses)}
    )

    # DFS cycle detection
    def dfs(course: int, visiting: Set[int], visited: Set[int]) -> bool:
        if course in visiting:
            return False
        if course in visited:
            return True

        new_visiting = visiting | {course}

        for nei in graph[course]:
            if not dfs(nei, new_visiting, visited):
                return False

        return True

    return all(dfs(c, set(), set()) for c in range(numCourses))
