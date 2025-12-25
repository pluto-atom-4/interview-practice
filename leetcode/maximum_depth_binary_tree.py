"""
Maximum Depth of Binary Tree Algorithm Explained Step-by-Step
--------------------------------------------------------------
The Maximum Depth problem asks to find the maximum height (or depth) of a binary tree.
The depth is defined as the number of nodes along the longest path from the root node to the farthest leaf node.
This is a fundamental tree problem that demonstrates depth-first search (DFS), tree traversal, and recursion.
It's commonly used in interview questions and has applications in tree balancing, tree analysis, and validation.

Here is how the process works:

1. **Base Case**: Handle empty trees.
   - If root is None, return 0 (empty tree has no depth)
   - This is the termination condition for recursion

2. **Recursive Case**: Compute depth of left and right subtrees.
   - For a non-null node, recursively call maxDepth on both left and right children
   - This explores all nodes in the tree via DFS (depth-first search)
   - Each recursive call goes deeper until reaching leaf nodes

3. **Combine Results**: Take the maximum of two subtree depths.
   - The depth of current node is 1 (the node itself) plus the maximum depth of its subtrees
   - Formula: depth(node) = 1 + max(depth(left), depth(right))
   - This ensures we find the longest path from root to any leaf

4. **Recursion Tree**: Understand the call stack flow.
   - Each node triggers two recursive calls for its children
   - Leaf nodes return 1 (base case: themselves)
   - Parent nodes combine results from children with 1 + max(...)
   - The tree is traversed post-order (process children before parent)

5. **DFS Traversal**: The algorithm performs depth-first exploration.
   - Explore completely down one path before backtracking
   - Visit all nodes in the tree (guaranteed for correct max depth)
   - Stack space used is proportional to tree height in recursion

6. **Final Result**: The maximum depth is returned from the root call.
   - Root call combines all subtree depths recursively
   - Final result is 1 + max(left_depth, right_depth) for the root
   - This value represents the longest path from root to leaf

Example: Binary tree with structure
         1
        / \\
       2   3
      / \\
     4   5
- Node 4 (leaf): maxDepth(4) = 1
- Node 5 (leaf): maxDepth(5) = 1
- Node 2: maxDepth(2) = 1 + max(1, 1) = 2
- Node 3 (leaf): maxDepth(3) = 1
- Root 1: maxDepth(1) = 1 + max(2, 1) = 3
- Result: 3 (path 1→2→4 or 1→2→5 has 3 nodes)

Alternative Approaches:
- **Iterative BFS**: Use queue to traverse level-by-level, count levels
  - Time: O(n), Space: O(w) where w is max width
  - Better space complexity for very unbalanced trees in some cases
- **Iterative DFS**: Use explicit stack instead of recursion
  - Time: O(n), Space: O(h) where h is tree height
  - Avoids recursion depth limitations

Time Complexity: O(n) where n is the number of nodes
  - Must visit every node to ensure we find the maximum depth
  - Cannot prune without exploring all branches
  - Each node processed exactly once

Space Complexity: O(h) where h is the height of the tree
  - Recursion call stack depth equals tree height
  - Best case: O(log n) for balanced tree (h = log n)
  - Worst case: O(n) for skewed tree (h = n)
  - Height-balanced trees minimize space usage

This problem demonstrates fundamental tree concepts: recursion, DFS, base cases,
and combining results from subproblems. It's a stepping stone for tree problems like
LCA (Lowest Common Ancestor), diameter, and tree DP problems.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    """
    Compute the maximum depth of a binary tree using DFS.
    Depth of an empty tree is 0.
    """
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
