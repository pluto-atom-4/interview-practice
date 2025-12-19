"""
Course Schedule - Cycle Detection in Directed Graph (Topological Sort)
-----------------------------------------------------------------------
The Course Schedule problem is a classic graph algorithm that determines if a set of courses can be completed
given prerequisite constraints. Each course may have prerequisites (other courses that must be completed first),
forming a directed graph. The goal is to detect if a cycle exists in this graph - if cycles exist, it's impossible
to complete all courses. This problem is fundamental for understanding topological sorting, graph traversal, and
cycle detection algorithms commonly asked in technical interviews.

Here is how the process works:

1. **Graph Construction**: Build an adjacency list representation of courses and their prerequisites.
   - Create a dictionary where key is a course and value is list of its prerequisites
   - For each [course, prerequisite] pair, add prerequisite as a neighbor of course
   - This represents: "course depends on prerequisite" (directed edge: prerequisite → course)
   - Time: O(P) where P is number of prerequisites

2. **State Tracking with Three Sets**: Use two sets to track visited and currently visiting states.
   - visited set: Contains courses that have been completely processed (no cycle found in their path)
   - visiting set: Contains courses currently in the recursion stack (DFS path)
   - A course in visiting set means we're exploring its dependencies
   - If we encounter a course already in visiting, we found a back edge (cycle detected)

3. **Depth-First Search (DFS)**: Explore each course's prerequisite dependencies recursively.
   - For each course, check if it's in visiting (cycle detected) or visited (already processed)
   - Mark course as visiting before exploring its prerequisites
   - Recursively explore all prerequisites (neighbors in graph)
   - If any recursive call returns False, propagate the cycle detection up
   - After exploring all prerequisites, remove from visiting and add to visited (backtrack)

4. **Cycle Detection Logic**: Three cases determine if a cycle exists at each step.
   - If course in visiting: We've encountered a node currently in recursion stack = back edge = CYCLE
   - If course in visited: Already fully processed, no cycle in that subtree = skip
   - Otherwise: First visit, mark visiting and explore prerequisites recursively

5. **Complete Traversal**: Check all courses to ensure entire graph is traversed.
   - Use all() with DFS on each unvisited course
   - all(dfs(c) for c in range(numCourses)) ensures all components are checked
   - Returns True only if all courses can be completed (no cycles found anywhere)
   - Short-circuits on first False (first cycle detected)

6. **Complexity Analysis**:
   - Time: O(N + P) where N = numCourses, P = prerequisites (visiting each node/edge once in DFS)
   - Space: O(N + P) for graph storage + O(N) for visiting/visited sets + O(N) recursion stack

Example: numCourses = 4, prerequisites = [[1,0],[2,1],[3,2]]
- Graph: 0 → 1 → 2 → 3 (linear dependency, no cycle)
- DFS from 0: explores 1, then 2, then 3 (no prerequisites for 3)
- Result: True (can complete all courses in order 0 → 1 → 2 → 3)

Example: numCourses = 2, prerequisites = [[1,0],[0,1]]
- Graph: 0 → 1 → 0 (circular dependency, cycle exists)
- DFS from 0: explores 1, which depends on 0 (0 already in visiting)
- Result: False (impossible, courses depend on each other)

Key Interview Insights:
- This is classic "detect cycle in directed graph" problem
- Imperative version with mutable sets is fastest (minimal overhead)
- Alternatives: recursive with tuples, functional with immutable data structures
- Related problems: topological sort, all course schedules, alien dictionary
- Can optimize with memoization or result tuple representation
"""

from typing import Dict, List


def canFinish_imperative(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Imperative DFS version (fastest).
    Uses mutable visited and visiting sets to detect cycles in directed graph.
    """

    graph: Dict[int, List[int]] = {i: [] for i in range(numCourses)}
    for a, b in prerequisites:
        graph[a].append(b)

    visiting = set()
    visited = set()

    def dfs(course: int) -> bool:
        if course in visiting:
            return False
        if course in visited:
            return True

        visiting.add(course)

        for nei in graph[course]:
            if not dfs(nei):
                return False

        visiting.remove(course)
        visited.add(course)
        return True

    return all(dfs(c) for c in range(numCourses))
