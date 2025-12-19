"""
Course Schedule - Cycle Detection in Directed Graphs
------------------------------------------------------
The Course Schedule problem determines if all courses can be completed given a set of prerequisites.
This is a classic graph cycle detection problem where courses are nodes and prerequisites define edges.
If there's a cycle in the dependency graph, courses cannot be completed. The problem requires detecting
whether a directed acyclic graph (DAG) exists or if circular dependencies prevent completion.

Here is how the process works:

1. **Problem Understanding**: Model the problem as a directed graph.
   - Each course is a node
   - Each prerequisite pair [a, b] means course a requires course b as a prerequisite
   - Edge direction: a → b (must do b before a)
   - Completion is possible if and only if no cycles exist

2. **Graph Representation**: Build an adjacency list for efficient traversal.
   - Initialize: graph[i] = [] for all courses i
   - For each prerequisite [a, b]: add b to graph[a]
   - This represents what must be done before each course

3. **Cycle Detection Strategy**: Use DFS with three node states.
   - visiting (White): Currently in the DFS recursion stack
   - visited (Black): Completely processed, no cycle found
   - Not visited (Gray): Not yet explored
   - If we encounter a node in "visiting" set during DFS, a cycle exists

4. **DFS Algorithm**: Perform depth-first search from each unvisited node.
   - If current node is in "visiting" set: cycle detected, return False
   - If current node is in "visited" set: already processed safely, return True
   - Mark current node as "visiting" before exploring neighbors
   - Recursively explore all neighbors
   - If any neighbor returns False: cycle found in subtree, return False
   - After processing all neighbors: cycle not found from this path, return True

5. **Global Check**: Verify all courses can be completed.
   - Run DFS from each course as starting point
   - All courses must return True (no cycles)
   - Use all() to ensure every course is reachable without cycles

6. **Why This Works**: Topological sorting prerequisite.
   - If no cycles exist, a valid course completion order exists
   - DFS approach finds cycles in O(V + E) time
   - Immutable sets avoid side effects in functional programming style

Example: numCourses = 4, prerequisites = [[1, 0], [2, 1], [3, 2]]
- Graph: 0←1←2←3
- DFS from 0: visits nothing, returns True
- DFS from 1: visits 0, returns True
- DFS from 2: visits 1→0, returns True
- DFS from 3: visits 2→1→0, returns True
- Result: True (valid order: 3, 2, 1, 0)

Example: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
- Graph: 0←→1 (cycle)
- DFS from 0: visiting {0}, explore 1, then explore 0 (in visiting), cycle detected
- Result: False

Time Complexity: O(V + E) where V = numCourses, E = len(prerequisites)
- Each node visited once, each edge traversed once
- V DFS calls at most (each returns quickly if visited)

Space Complexity: O(V + E)
- Graph storage: O(V + E) for adjacency list
- Recursion stack: O(V) in worst case (linear chain)
- Sets for visiting/visited: O(V)

This algorithm demonstrates topological sorting, cycle detection, and graph algorithms essential
for understanding dependency management, package installation, build systems, and data pipeline validation.
"""

from typing import Dict, List, Set


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Pure functional-style solution for Course Schedule.
    Detects cycles using DFS with immutable visited sets.
    """

    # Build adjacency list (functional: returns new dict)
    graph: Dict[int, List[int]] = {
        i: [] for i in range(numCourses)
    }
    for a, b in prerequisites:
        graph[a] = graph[a] + [b]  # functional append

    # DFS returns True if no cycle from this node
    def dfs(course: int, visiting: Set[int], visited: Set[int]) -> bool:
        if course in visiting:
            return False  # cycle detected
        if course in visited:
            return True   # already processed safely

        new_visiting = visiting | {course}

        # Explore neighbors
        for prereq in graph[course]:
            if not dfs(prereq, new_visiting, visited):
                return False

        # Mark as fully processed
        new_visited = visited | {course}
        return True

    # Check all courses
    return all(dfs(c, set(), set()) for c in range(numCourses))
