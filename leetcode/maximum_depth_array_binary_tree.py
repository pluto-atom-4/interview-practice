"""
Maximum Depth of Binary Tree (Array Representation) - Interview Guide
----------------------------------------------------------------------
The Maximum Depth of a Binary Tree problem asks to find the height (longest path from root to leaf)
of a binary tree. When the tree is represented as an array (level-order representation), we must
understand array indexing rules to navigate the tree structure. This demonstrates tree traversal,
recursion, and understanding of tree properties—all critical for system design and algorithm interviews.

Here is how the process works:

1. **Array Representation**: Binary trees can be stored in arrays using level-order indexing.
   - For node at index i:
     - Left child is at index 2*i + 1
     - Right child is at index 2*i + 2
   - None values represent missing nodes (sparse trees)
   - Root node is always at index 0
   - This is memory efficient for complete binary trees

2. **Base Cases**: Stop recursion when reaching boundaries or missing nodes.
   - If index i >= array length, node doesn't exist → return 0
   - If values[i] is None, node is missing → return 0
   - These conditions handle array bounds and sparse representation
   - Both cases contribute 0 to the depth calculation

3. **Recursive Exploration**: Calculate depth by exploring both subtrees.
   - For each valid node, recursively find depth of left subtree
   - For each valid node, recursively find depth of right subtree
   - Combine results: depth = 1 + max(left_depth, right_depth)
   - The 1 represents the current node in the path

4. **Depth Calculation**: At each node, take the maximum of two branches.
   - Depth of tree = 1 + max(left subtree depth, right subtree depth)
   - This ensures we find the longest path to any leaf
   - Compare both children's depths and take the larger one
   - Single node tree has depth 1 (base case returns 0, + 1 = 1)

5. **Why Recursive Approach**: Recursion naturally mirrors tree structure.
   - Each subtree is a complete tree problem (optimal substructure)
   - Tree problems are inherently recursive by nature
   - Easy to understand and implement correctly
   - Matches the tree traversal pattern used in interviews

6. **Interview Insights**: This problem tests several concepts.
   - Understanding tree representations and indexing schemes
   - Recursive thinking and base case handling
   - Tree traversal and depth-first search (DFS)
   - Handle edge cases: empty trees, single nodes, None values
   - Can compare with node-based tree representation approaches

Example: values = [3, 9, 20, None, None, 15, 7]
- Tree structure:
      3
     / \\
    9  20
      / \\
     15  7
- Calculate: depth(0) → 1 + max(depth(1), depth(2))
- depth(1) = 1 (leaf node 9)
- depth(2) = 1 + max(depth(5), depth(6)) = 1 + max(1, 1) = 2
- Result: 1 + max(1, 2) = 3

Time Complexity: O(n) where n is the number of nodes
- Must visit all nodes in worst case to find maximum depth
- Each node processed once due to recursive calls

Space Complexity: O(h) where h is the height of the tree
- Recursion call stack depth equals tree height
- For balanced trees: O(log n)
- For skewed trees: O(n) in worst case
- No additional data structures needed

This problem teaches tree traversal patterns essential for system design,
understanding recursion depth, and handling different tree representations commonly used in interviews.
"""

from typing import List, Optional


def max_depth_array_tree(values: List[Optional[int]]) -> int:
    """
    Compute the maximum depth of a binary tree represented as an array.
    Missing nodes are represented as None.

    Index rules:
        left(i)  = 2*i + 1
        right(i) = 2*i + 2
    """

    n = len(values)

    def depth(i: int) -> int:
        if i >= n or values[i] is None:
            return 0
        return 1 + max(depth(2 * i + 1), depth(2 * i + 2))

    return depth(0)
