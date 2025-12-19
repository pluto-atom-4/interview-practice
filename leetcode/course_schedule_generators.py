"""
Course Schedule - Cycle Detection using Generator Pipelines
------------------------------------------------------------
This is a variant of the Course Schedule problem using Python generators and comprehensions for
a functional pipeline approach. The problem determines if courses can be completed by detecting cycles.
This implementation builds the adjacency list using generator pipelines and demonstrates lazy evaluation,
which is particularly useful for demonstrating Python-specific optimizations in interviews.

Here is how the process works:

1. **Problem Understanding**: Cycle detection in a course dependency graph.
   - Each course is a node; prerequisite [a, b] means b must come before a
   - Build edge: a → b (what each course depends on)
   - Success ⟺ no cycles in the dependency graph
   - Use DFS with state tracking to detect cycles

2. **Graph Building with Generators**: Efficient comprehension-based adjacency list.
   - Use dictionary comprehension: {c: [b for a, b in prerequisites if a == c] for c in range(numCourses)}
   - For each course c, filter prerequisites where a == c and collect b values
   - Inner comprehension acts as a generator expression (lazy evaluation)
   - More Pythonic than reduce(), easier to read, avoids intermediate dicts
   - Time: O(V * E) due to O(E) scan per course, but cache-friendly in practice

3. **Generator Comprehensions**: Lazy evaluation benefits.
   - [b for a, b in prerequisites if a == c] doesn't evaluate until needed
   - Single pass through prerequisites per course
   - Memory efficient: no intermediate list creation if not consumed
   - Perfect for expressing filter-map-collect patterns cleanly

4. **Cycle Detection with Generators**: DFS with lazy neighbor exploration.
   - dfs() explores neighbors lazily using generator expression
   - checks = (dfs(nei, new_visiting, visited) for nei in graph[course])
   - Generator pauses between dfs() calls, enabling short-circuit on first False
   - all(checks) consumes generator only until first False is found
   - More efficient than collecting all results first: all([...])

5. **Why Use Generators for Interview**: Demonstrates Python optimization skills.
   - Shows understanding of lazy evaluation and memory efficiency
   - Proves ability to write idiomatic Python code
   - Useful for demonstrating generator expressions and comprehensions
   - Can discuss: readability, performance, and when generators help
   - Compares well against list comprehensions in explanations

6. **Algorithm Flow**: DFS cycle detection on generated graph.
   - If node in visiting set: cycle found, return False (back edge)
   - If node in visited set: already processed, return True (safe)
   - Mark node as visiting before exploring neighbors
   - Recursively check all neighbors (lazy generation)
   - If any neighbor returns False: cycle in subtree, return False
   - After all neighbors processed safely: return True

Example: numCourses = 3, prerequisites = [[0, 1], [1, 2]]
- Generator creates: {0: [1], 1: [2], 2: []}
- DFS from 0: visits 1 via [1], then 2 via [2], no cycle
- Result: True (can complete all courses in order: 2, 1, 0)

Example: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
- Generator creates: {0: [1], 1: [0]} (cycle 0↔1)
- DFS from 0: visiting={0}, explore 1; then explore 0 (already visiting), cycle!
- Result: False (circular dependency prevents completion)

Time Complexity: O(V * E) for graph building + O(V + E) for DFS
- Graph building: for each course, scan all edges for matches → V * E
- DFS: O(V + E) standard graph traversal
- Total: O(V * E) dominated by graph building (worse than other variants!)
- However, in practice with sparse graphs, often acceptable

Space Complexity: O(V + E)
- Adjacency list: O(V + E)
- DFS recursion stack: O(V) in worst case
- Generator state: O(1) additional per level

Interview Discussion Points:
- Generator expressions vs. list comprehensions
- Lazy evaluation and when it matters
- Trade-offs: readability vs. efficiency (this approach slower than reduce)
- When generators provide memory benefits
- How all() with generators enables short-circuiting
- Pythonic idioms: comprehensions over reduce()

Performance Comparison of Three Approaches:
- Standard (imperative): Fast graph building O(E), simple logic
- Reduce (functional): O(V + E) graph building, demonstrates pure functions
- Generators (Pythonic): O(V * E) graph building, clearest intent, lazy evaluation

This variant is excellent for demonstrating Pythonic code style and understanding of
generators, comprehensions, and lazy evaluation in Python interviews.
"""

from typing import Dict, List, Set


def canFinish_generators(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Pure functional generator-pipeline version of Course Schedule.
    """

    # Build adjacency list using generator pipeline
    graph: Dict[int, List[int]] = {
        c: [b for a, b in prerequisites if a == c]
        for c in range(numCourses)
    }

    # Functional DFS cycle detection
    def dfs(course: int, visiting: Set[int], visited: Set[int]) -> bool:
        if course in visiting:
            return False
        if course in visited:
            return True

        new_visiting = visiting | {course}

        # generator pipeline for recursive DFS
        checks = (
            dfs(nei, new_visiting, visited)
            for nei in graph[course]
        )

        if all(checks):
            return True

        return False

    return all(dfs(c, set(), set()) for c in range(numCourses))
