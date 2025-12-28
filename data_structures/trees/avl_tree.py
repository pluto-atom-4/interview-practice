"""
AVL Tree (Self-Balancing Binary Search Tree) Algorithm Explained Step-by-Step
-------------------------------------------------------------------------------
The AVL Tree is a self-balancing binary search tree that maintains height balance through rotations.
Named after Adelson-Velsky and Landis, AVL trees guarantee O(log n) operations (insert, search, delete)
by enforcing a balance property: the height difference (balance factor) between left and right subtrees
of any node must be at most 1. This problem demonstrates self-balancing tree concepts essential for
maintaining performance guarantees, understanding tree rotations, and optimizing search-heavy applications
commonly discussed in technical interviews and system design.

Here is how the process works:

1. **AVL Tree Properties & Balance Factor**: Understanding the self-balancing constraint.
   - Balance Factor: height(left_subtree) - height(right_subtree)
   - Valid AVL property: -1 ≤ balance_factor ≤ 1 for all nodes
   - Violating this property requires rebalancing through rotations
   - Height of AVL tree with n nodes is approximately 1.44 * log2(n)
   - Guarantees O(log n) height regardless of insertion order

2. **Node Height Calculation & Updates**: Tracking vertical extent of subtrees.
   - Height of leaf node = 1
   - Height of null/empty node = 0
   - Height of parent = 1 + max(left_height, right_height)
   - Update heights after each insertion/deletion operation
   - Heights enable efficient balance factor computation

3. **Tree Rotations - Single Rotations**: Rebalancing technique for simple imbalances.
   - **Left Rotation (Right-Heavy Case)**: Right child becomes parent
     - Right child of z moves to z's right child position
     - z becomes left child of its old right child
     - Fixes Right-Right imbalance (BF < -1 with right child BF ≤ 0)
   - **Right Rotation (Left-Heavy Case)**: Left child becomes parent
     - Left child of z moves to z's left child position
     - z becomes right child of its old left child
     - Fixes Left-Left imbalance (BF > 1 with left child BF ≥ 0)
   - Single rotation restores balance in 2 of 4 imbalance cases

4. **Tree Rotations - Double Rotations**: Handling complex imbalances.
   - **Left-Right Case (BF > 1 with left child BF < 0)**:
     - First rotate left child left (convert to Left-Left)
     - Then rotate parent right (standard right rotation)
   - **Right-Left Case (BF < -1 with right child BF > 0)**:
     - First rotate right child right (convert to Right-Right)
     - Then rotate parent left (standard left rotation)
   - Double rotations handle the remaining 2 of 4 imbalance cases

5. **Insertion with Rebalancing**: Adding nodes while maintaining balance.
   - Insert new node as in standard BST (leaf position)
   - Update heights of ancestors moving up the tree
   - Calculate balance factor for each ancestor
   - Apply appropriate rotation(s) when balance factor violates [-1, 1] range
   - Single insertion triggers at most 2 rotations (worst case)
   - Return rebalanced subtree root for recursive updates

6. **Deletion with Rebalancing**: Removing nodes while maintaining balance.
   - Delete node as in standard BST (handle 0, 1, or 2 children cases)
   - Find inorder successor for nodes with 2 children
   - Update heights of ancestors moving up the tree
   - Apply appropriate rotations for any imbalanced nodes encountered
   - May require up to O(log n) rotations in worst case
   - Ensure parent pointers/tree structure remain valid

7. **Search Operation**: Leveraging BST property for efficient lookup.
   - Standard binary search tree search algorithm
   - Compare target with current node key
   - Recursively search left (if target < key) or right (if target > key)
   - Benefits from O(log n) guaranteed height of AVL tree
   - No rebalancing needed for search operations

Example: Inserting [10, 20, 30] in order
- Insert 10: tree = [10]
- Insert 20: tree = [10, 20] (right child)
- Insert 30: Balance factor of 10 = -2 (right-heavy, Right-Right case)
  - Single left rotation on 10: 20 becomes root, 10 becomes left child
  - Result: [20 with left=10, right=30], all balance factors in [-1, 1]

Time Complexity: O(log n) for insert, delete, search
Space Complexity: O(n) for storing n nodes, O(log n) for recursion stack
Rotations Per Operation: At most 1 for insertion, O(log n) for deletion

This algorithm demonstrates self-balancing tree concepts, rotation techniques, and height-balanced
data structure design. Understanding AVL trees is crucial for system design (database indexing),
competitive programming, and appreciating trade-offs between implementation complexity and performance
guarantees compared to simpler trees or other balanced structures like Red-Black trees.
"""

from __future__ import annotations

from typing import Optional


class AVLNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height = 1  # new node is initially a leaf


class AVLTree:
    def insert(self, root: Optional[AVLNode], key: int) -> AVLNode:
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # duplicates not inserted

        root.height = 1 + max(self._height(root.left), self._height(root.right))
        balance = self._balance(root)

        # Left Left
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)

        # Right Right
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def delete(self, root: Optional[AVLNode], key: int) -> Optional[AVLNode]:
        if root is None:
            return None

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with one or zero children
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: get inorder successor
            successor = self._min_value_node(root.right)
            root.key = successor.key
            root.right = self.delete(root.right, successor.key)

        if root is None:
            return None

        root.height = 1 + max(self._height(root.left), self._height(root.right))
        balance = self._balance(root)

        # Left Left
        if balance > 1 and self._balance(root.left) >= 0:
            return self._rotate_right(root)

        # Left Right
        if balance > 1 and self._balance(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right Right
        if balance < -1 and self._balance(root.right) <= 0:
            return self._rotate_left(root)

        # Right Left
        if balance < -1 and self._balance(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def search(self, root: Optional[AVLNode], key: int) -> bool:
        if root is None:
            return False
        if key == root.key:
            return True
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # -----------------------------
    # Helpers
    # -----------------------------

    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _balance(self, node: Optional[AVLNode]) -> int:
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_left(self, z: AVLNode) -> AVLNode:
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _rotate_right(self, z: AVLNode) -> AVLNode:
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _min_value_node(self, node: AVLNode) -> AVLNode:
        current = node
        while current.left:
            current = current.left
        return current
