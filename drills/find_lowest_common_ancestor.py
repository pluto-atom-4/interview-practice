"""
## Problem Statement

Find the Lowest Common Ancestor (LCA) of two nodes in a tree (represented as a directed graph). 
The goal is to identify the deepest node that is an ancestor of both target nodes. This tests 
understanding of tree traversal, post-order processing, and ancestor relationship logic.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Post-Order DFS with Bottom-Up Merging**:

This approach explores the tree from leaves upward, collecting search results from child branches. When both target nodes 
appear in different child subtrees, the current node is their LCA. This design naturally captures the "deepest common ancestor" 
through recursive depth, avoiding the need to track ancestor paths explicitly.

* Key Concepts:

  - Why post-order traversal with bottom-up merging?
Post-order ensures all descendants are explored before processing a node. When we return from recursive calls, we can 
evaluate whether both targets were found in the subtree rooted at the current node. If both are found, the current node 
is their LCA. This automatically finds the deepest LCA without separate ancestor tracking.

  - Why track found_nodes in a list instead of booleans?
Using a list allows us to pass actual node references up the tree. This enables the three-way decision: (1) LCA found 
(both targets in different branches), (2) one target found (pass it up), (3) nothing found (return None). A boolean 
approach would lose information about which target was found.

  - Why check `len(found_nodes) >= 2` instead of checking parent node matching?
This directly identifies when both targets are found in different child subtrees of the current node. It's the definition 
of LCA: if both targets appear below node X in different branches, X is their LCA. We don't need to check node identity; 
the list length tells us everything.

* Logic:

1. Start DFS from root node
2. Base case: if current node is None or matches target p or q, return it
3. Explore all children and collect results in found_nodes list
4. If found_nodes has 2+ results, both targets found in different branches—current node is LCA
5. If found_nodes has 1 result, one target found—pass it up the tree
6. If found_nodes is empty, neither target in this subtree—return None
7. Continue until reaching root or finding LCA

* **30-Second Pitch**:

I do a DFS from the root, and for each node I recursively explore its children, collecting results in a list. 
If a node finds both targets in its different child subtrees, that node is their LCA. Otherwise, I pass up 
whichever target(s) were found so ancestors can continue the search upward.

* **Rapid-Fire Version**:

- Post-order DFS collecting results from child branches
- Both targets in different children = current node is LCA
- found_nodes list tracks results: 0 = not found, 1 = one found, 2+ = both found
- Return found node or pass up results for ancestor evaluation

* **Ultra-Minimal One-Liner**:

Post-order DFS merging child results identifies the deepest node with both targets in separate subtrees as LCA.

* **Complexity Analysis**:

- **Time Complexity:** O(V) — each node visited once in DFS traversal
- **Space Complexity:** O(h) where h is tree height — recursion stack depth equals height; found_nodes list stores up to 2 items per call

* **Use Cases**:

Finding relationships in file system hierarchies, determining closest common resource in network topologies, 
analyzing organizational reporting structures, computing distances between nodes in tree-based data structures.
"""

from typing import Hashable, TypeVar

from .graph import Graph

T = TypeVar('T', bound=Hashable)


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
