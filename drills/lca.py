
"""
## Problem Statement

Find the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree.
Given a BST root and two values, identify the deepest node that is an ancestor 
to both values. This tests understanding of BST properties and tree traversal optimization.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **BST Property Exploitation (Iterative Approach)**:

The key insight is that Binary Search Trees have an ordering property—values in the 
left subtree are all smaller than the parent, and values in the right subtree are all 
larger. This allows us to navigate directly to the LCA without exploring unnecessary 
branches, making the solution highly efficient.

* Key Concepts:

  - **Why exploit BST properties instead of generic tree traversal?**
Generic tree LCA requires exploring both subtrees and comparing; BST properties let us 
navigate directly by comparing values. Since both v1 and v2 follow predictable paths, 
we can detect the "split point" where they diverge—that's the LCA. This reduces time 
complexity from O(n) to O(h), where h is height (potentially log n in balanced trees).

  - **Why use an iterative approach instead of recursion?**
Iterative is more interview-friendly: cleaner code, O(1) space complexity (no recursion 
stack), and easier to explain. Recursion would accumulate calls on the stack proportional 
to tree height. The iterative approach directly reassigns root, making space usage minimal.

  - **Why check both values against root.info in each iteration?**
Each iteration eliminates an entire subtree. If both v1 and v2 are smaller, they're both 
in the left subtree. If both are larger, they're both in the right subtree. When they 
diverge (one smaller, one larger), or when we hit exact match, we've found the LCA—the 
point where the paths to v1 and v2 would diverge.

* Logic:

1. Start at the root of the BST
2. Compare both values against the current node's value
3. If both values are smaller than the current node, move to the left subtree
4. If both values are larger than the current node, move to the right subtree
5. If one value is smaller and one is larger (or matches the node), the current node is the LCA
6. Continue until finding the LCA or exhausting the tree (return None)

* **30-Second Pitch**:

For a BST's Lowest Common Ancestor, I navigate down the tree by comparing both values 
against each node. Since BST values are ordered, if both values lie on the same side, 
I move that direction. When they diverge (one left, one right) or match a node, that's 
the LCA. This exploits ordering to achieve O(h) time with O(1) space iteratively.

* **Rapid-Fire Version**:

- Use BST property: left subtree < node < right subtree
- Navigate by comparing both values to current node
- Both smaller → go left; both larger → go right
- Divergence point or exact match = LCA found
- Time O(h), Space O(1) iteratively
- No need to explore irrelevant branches

* **Ultra-Minimal One-Liner**:

- Navigate a BST by comparing both target values, moving left/right based on ordering, 
until they diverge—that's the LCA.

* **Complexity Analysis**:

- **Time Complexity:** O(h), where h is the height of the tree. In a balanced BST, 
this is O(log n). In the worst case (skewed tree), it's O(n). Each iteration eliminates 
one subtree level, so we traverse at most h nodes.

- **Space Complexity:** O(1) for this iterative approach. No recursion stack or data 
structures scale with input size. Only storing a few pointers/values.

* **Use Cases**:

- **Genealogy systems:** Finding the closest common ancestor of two people
- **File system hierarchies:** Identifying the deepest common parent directory
- **DOM trees in browsers:** Finding the lowest common ancestor of two HTML elements
- **Version control systems:** Finding merge base of two branches
- **Organizational hierarchies:** Identifying common manager/department
"""

from typing import Optional

from drills.binary_search_tree import Node


def lca(root: Optional[Node], v1: int, v2: int) -> Optional[Node]:
    """
    Finds the Lowest Common Ancestor in a BST.
    Time Complexity: O(h), where h is the height of the tree.
    Space Complexity: O(1) for this iterative approach.
    """
    while root:
        # If both values are smaller than root, LCA is in the left subtree
        if v1 < root.info and v2 < root.info:
            root = root.left
        # If both values are larger than root, LCA is in the right subtree
        elif v1 > root.info and v2 > root.info:
            root = root.right
        else:
            # We found the split point or one of the nodes matches the current root
            return root
    return None
