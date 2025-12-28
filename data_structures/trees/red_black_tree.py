"""
Red-Black Tree (Self-Balancing Binary Search Tree) Algorithm Explained Step-by-Step
-----------------------------------------------------------------------------------
The Red-Black Tree is a self-balancing binary search tree that maintains balance through node coloring
and rotation operations. Each node is colored either RED or BLACK, and the tree enforces specific
coloring properties to ensure O(log n) height guarantee. Unlike AVL trees that use strict height balance,
Red-Black trees use a more relaxed balancing criterion allowing greater insertion/deletion efficiency.
This problem demonstrates advanced tree balancing techniques used in real-world systems (Linux kernel,
Java Collections Framework) and is essential for understanding performance trade-offs and practical
balancing strategies discussed in technical interviews and system design.

Here is how the process works:

1. **Red-Black Tree Properties**: Understanding the fundamental coloring invariants.
   - Property 1: Every node is either RED or BLACK
   - Property 2: Root node must be BLACK
   - Property 3: All leaf nodes (NIL) are BLACK
   - Property 4: If a node is RED, both children must be BLACK (no consecutive reds)
   - Property 5: All paths from node to descendant leaves have same number of BLACK nodes
   - These properties ensure O(log n) height: max_height ≤ 2 * log2(n+1)
   - Red-Black trees are less strictly balanced than AVL but allow faster insertions/deletions

2. **Node Structure & NIL Sentinel**: Simplifying edge cases and rotations.
   - Each node stores: key, color (RED/BLACK), left child, right child, parent
   - NIL sentinel node: a single BLACK node representing all null pointers
   - Using NIL sentinel eliminates null pointer checks in rotation/fixup logic
   - All leaf pointers point to NIL instead of being null
   - Simplifies algorithm implementation and makes code more uniform

3. **BST Property Maintenance**: Preserving binary search tree invariant.
   - Standard BST ordering: left_subtree.keys < node.key < right_subtree.keys
   - Coloring and rotations don't violate BST property
   - Search operation is standard binary search: O(log n)
   - Insert and delete maintain BST structure while enforcing color properties

4. **Tree Rotations**: Local restructuring for rebalancing operations.
   - **Left Rotation**: Right child moves up, left subtree shifts left
     - Used when right subtree is too deep (right-heavy)
     - Preserves BST property and parent-child relationships
   - **Right Rotation**: Left child moves up, right subtree shifts right
     - Used when left subtree is too deep (left-heavy)
     - Symmetric to left rotation
   - Rotations are local O(1) operations on 3 nodes and 4 pointers
   - Parent pointers must be updated for correct tree structure

5. **Insertion Process & Fixup**: Adding nodes while maintaining color properties.
   - Insert new node as in standard BST at leaf position
   - Color new node RED (less likely to violate properties)
   - Insertion fixup restores color properties:
     - Case 1: Uncle is RED → recolor parent, uncle, grandparent; continue upward
     - Case 2: Uncle is BLACK, node on "right" side → rotate left to Case 3 configuration
     - Case 3: Uncle is BLACK, node on "left" side → rotate right and recolor
   - Fixup processes from inserted node up to root
   - At most 2 rotations needed to restore balance (O(1) rotations)

6. **Deletion Process & Fixup**: Removing nodes while maintaining color properties.
   - Delete node using standard BST deletion algorithm
   - Track deleted node color (if it was BLACK, properties may be violated)
   - Find replacement node (successor for 2-child case)
   - Deletion fixup handles BLACK violations:
     - Case 1: Sibling is RED → rotate and recolor to transform to other cases
     - Case 2: Sibling is BLACK with two BLACK children → recolor sibling
     - Case 3: Sibling is BLACK, near child RED, far child BLACK → rotate and recolor
     - Case 4: Sibling is BLACK, far child RED → rotate, recolor, and done
   - May require O(log n) iterations in worst case (walking up tree)

7. **Color Properties Guarantee**: Why Red-Black trees ensure O(log n) operations.
   - All paths to NIL have same number of BLACK nodes (Property 5)
   - Maximum red nodes between two BLACK nodes is 1 (Property 4)
   - No path can be more than 2x the minimum path length
   - Path lengths differ by at most factor of 2 → balanced height
   - Height is O(log n), guaranteeing O(log n) search, insert, delete

Example: Inserting [7, 3, 18, 10, 22, 8, 11, 26] into Red-Black tree
- Insert nodes as RED at leaf positions
- Each insertion may trigger color violations (consecutive reds)
- Fixup operations rebalance through rotations and recoloring
- Result: Balanced tree where longest path ≤ 2x shortest path
- All operations maintain O(log n) height guarantee

Time Complexity: O(log n) for insert, delete, search
Space Complexity: O(n) for storing n nodes, O(log n) for recursion stack
Rotations Per Operation: At most 2 for insertion, O(1) amortized for deletion

Advantages over AVL Trees:
- Faster insertion/deletion (fewer rotations required)
- Better cache locality due to less strict balancing
- Used in production systems (Linux kernel, Java TreeMap, C++ std::map)

Disadvantages compared to AVL Trees:
- Slower search (relaxed balancing allows taller trees)
- More complex implementation due to color handling
- Requires understanding of 4+ fixup cases

This algorithm demonstrates advanced self-balancing techniques, practical trade-offs between balancing
strictness and operation efficiency, and implementation patterns used in production systems. Understanding
Red-Black trees is crucial for system design interviews, appreciating why standard library collections
use them, and comparing different balancing strategies for different workload patterns.
"""

from __future__ import annotations

from typing import Optional

RED = True
BLACK = False


class RBNode:
    def __init__(self, key: int, color=RED):
        self.key = key
        self.color = color
        self.left: Optional["RBNode"] = None
        self.right: Optional["RBNode"] = None
        self.parent: Optional["RBNode"] = None

    def __repr__(self):
        c = "R" if self.color else "B"
        return f"{self.key}{c}"


class RedBlackTree:
    def __init__(self):
        self.nil = RBNode(key=None, color=BLACK)
        self.root: RBNode = self.nil

    # ------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------

    def insert(self, root: Optional[RBNode], key: int) -> RBNode:
        """Insert key and return new root."""
        new_node = RBNode(key)
        new_node.left = self.nil
        new_node.right = self.nil

        parent = None
        current = self.root

        while current != self.nil:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return self.root  # ignore duplicates

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = RED
        self._insert_fixup(new_node)
        return self.root

    def search(self, root: Optional[RBNode], key: int) -> bool:
        node = self.root
        while node != self.nil:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, root: Optional[RBNode], key: int) -> Optional[RBNode]:
        node = self._find_node(key)
        if node is None:
            return self.root

        self._delete_node(node)
        return self.root

    # ------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------

    def _find_node(self, key: int) -> Optional[RBNode]:
        node = self.root
        while node != self.nil:
            if key == node.key:
                return node
            node = node.left if key < node.key else node.right
        return None

    # ------------------------------------------------------------
    # Rotations
    # ------------------------------------------------------------

    def _rotate_left(self, x: RBNode):
        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _rotate_right(self, x: RBNode):
        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # ------------------------------------------------------------
    # Insert Fixup
    # ------------------------------------------------------------

    def _insert_fixup(self, z: RBNode):
        while z.parent and z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # uncle
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._rotate_left(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left  # uncle
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._rotate_right(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rotate_left(z.parent.parent)

        self.root.color = BLACK

    # ------------------------------------------------------------
    # Delete helpers
    # ------------------------------------------------------------

    def _transplant(self, u: RBNode, v: RBNode):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node: RBNode) -> RBNode:
        while node.left != self.nil:
            node = node.left
        return node

    def _delete_node(self, z: RBNode):
        y = z
        y_original_color = y.color

        if z.left == self.nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right

            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == BLACK:
            self._delete_fixup(x)

    def _delete_fixup(self, x: RBNode):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._rotate_left(x.parent)
                    w = x.parent.right

                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self._rotate_right(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._rotate_right(x.parent)
                    w = x.parent.left

                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._rotate_left(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._rotate_right(x.parent)
                    x = self.root

        x.color = BLACK
