"""
Dependency Graph & Cycle Detection Algorithm Explained Step-by-Step
-------------------------------------------------------------------
A Dependency Graph is a directed graph data structure used to model relationships between entities
where edges represent dependencies. This is fundamental for task scheduling, build systems, package
managers, and deadlock detection. The key operation is cycle detection—identifying circular dependencies
that would create impossible situations (e.g., Task A depends on B, B depends on C, C depends on A).

Here is how the process works:

1. **Graph Representation**: Use an adjacency list to store the graph efficiently.
   - Each node maps to a set of nodes it depends on
   - Supports O(1) edge lookups and dynamic node addition
   - Scales well for sparse graphs typical in real-world dependency systems

2. **Cycle Detection via DFS**: Use depth-first search with a recursion stack.
   - Maintain three states: unvisited, visiting (in current path), visited (complete)
   - When exploring a node, mark it as "visiting" and add to recursion stack
   - If we encounter a node already in recursion stack, a cycle exists
   - This approach works because cycles must appear on the same DFS path

3. **Three Sets for State Tracking**:
   - **visited**: Nodes completely processed (all descendants explored)
   - **recursion_stack**: Nodes on current DFS path (detects back edges)
   - A node visited but not in recursion_stack means we explored it via another path
   - If neighbor is unvisited, recursively explore it
   - If neighbor is in recursion_stack, cycle detected

4. **Backtracking**: Remove nodes from recursion stack after exploring.
   - After processing all neighbors, pop node from recursion_stack
   - Allows detection of cycles in different graph branches
   - Critical for correctly identifying cycles that don't share the same starting point

5. **Cycle Extraction**: Optional step to identify actual nodes forming the cycle.
   - When a back edge is detected (node in recursion_stack), we found a cycle
   - Extract cycle nodes from recursion_stack using the index of the cycle start
   - Useful for debugging: "These tasks have a circular dependency"

6. **Graph Algorithms Foundation**:
   - This pattern applies to: task scheduling, deadlock detection, build order validation
   - Topological sorting requires acyclic graphs—cycle detection is the prerequisite check
   - Time complexity ensures feasibility even for large real-world dependency systems

Example: Tasks with circular dependency
- Task A depends on B
- Task B depends on C
- Task C depends on A
- Process: Start DFS from A → visit B → visit C → detect A in recursion_stack → cycle found!
- Result: True (cycle exists), nodes involved: [A, B, C]

Time Complexity: O(V + E) where V = number of nodes, E = number of edges (edges = dependencies)
Space Complexity: O(V) for visited set, recursion_stack, and graph storage
Graph Type: Directed acyclic graph (DAG) check—returns False if valid, True if cycle exists

This algorithm is essential for understanding graph traversal, detecting circular dependencies in
real systems (package managers, build tools), and preparing for system design interviews.
"""
class DependencyGraph:
    """
    Directed graph used to model dependencies and detect cycles.
    Each node can depend on multiple other nodes.
    """

    def __init__(self):
        self.graph = {}  # adjacency list

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = set()

    def add_dependency(self, node, depends_on):
        """
        Add an edge: node -> depends_on
        Meaning: node depends on depends_on
        """
        self.add_node(node)
        self.add_node(depends_on)
        self.graph[node].add(depends_on)

    def has_cycle(self):
        """
        Detect cycles using DFS with recursion stack.
        Returns True if a cycle exists.
        """

        visited = set()
        recursion_stack = set()

        def dfs(node):
            if node in recursion_stack:
                return True  # cycle found

            if node in visited:
                return False

            visited.add(node)
            recursion_stack.add(node)

            for neighbor in self.graph[node]:
                if dfs(neighbor):
                    return True

            recursion_stack.remove(node)
            return False

        for node in self.graph:
            if dfs(node):
                return True

        return False

    def get_cycle_nodes(self):
        """
        Optional helper: return nodes involved in a cycle.
        Useful for debugging or deadlock reporting.
        """

        visited = set()
        recursion_stack = []

        def dfs(node):
            visited.add(node)
            recursion_stack.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    result = dfs(neighbor)
                    if result:
                        return result
                elif neighbor in recursion_stack:
                    # cycle found → return the cycle slice
                    idx = recursion_stack.index(neighbor)
                    return recursion_stack[idx:]

            recursion_stack.pop()
            return None

        for node in self.graph:
            result = dfs(node)
            if result:
                return result

        return None
