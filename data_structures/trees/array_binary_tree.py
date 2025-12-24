"""
Array-Based Binary Tree Representation Explained Step-by-Step
--------------------------------------------------------------
The Array-Based Binary Tree, also known as Heap Array Representation, is an elegant way to represent
a complete binary tree using a contiguous array. Instead of using pointers (as in node-based trees),
indices are used to determine parent-child relationships. This is the foundation for heaps, priority
queues, and is essential for understanding space-efficient tree storage and level-order traversal.

Here is how the representation works:

1. **Index-Based Navigation**: Use mathematical relationships to navigate the tree.
   - left_child(i) = 2*i + 1 (multiply by 2 and add 1)
   - right_child(i) = 2*i + 2 (multiply by 2 and add 2)
   - parent(i) = (i - 1) // 2 (integer division of (index - 1) divided by 2)
   - These formulas work because of level-order (breadth-first) storage

2. **Array Storage Structure**: Elements are stored level by level, left to right.
   - Index 0 is the root of the tree
   - For a complete binary tree, children are always stored immediately after parents
   - No gaps in the array (except for incomplete last level)
   - This layout enables O(1) parent-child lookups without pointers

3. **Memory Efficiency**: No pointer overhead compared to node-based trees.
   - Each node only stores a value, no left/right references
   - Space complexity is O(n) for n nodes, with minimal overhead
   - Cache-friendly since data is contiguous in memory
   - Ideal for static trees or frequently traversed structures

4. **Complete Binary Trees**: Best suited for complete binary trees.
   - All levels filled except possibly the last (filled left to right)
   - Sparse trees waste space due to None placeholders
   - For sparse trees, node-based representations are better
   - Heaps (min-heap, max-heap) are perfect candidates for this structure

5. **Key Operations**: Fundamental operations and their complexities.
   - Access parent/child: O(1) using index formulas
   - Insert at index: O(1) amortized (with capacity expansion)
   - Get value: O(1) direct array access
   - Traverse level-order: O(n) single pass through array
   - Tree traversals (in-order, pre-order) require explicit recursion

6. **Advantages and Use Cases**:
   - Heaps: Priority queues, heap sort, Dijkstra's algorithm
   - Level-order traversal: Naturally efficient with array storage
   - Space savings: No pointer overhead, better cache locality
   - Dynamic arrays can grow as needed with proper capacity management

Example: Tree structure with indices
```
        0 (root)
       / \
      1   2
     / \ / \
    3  4 5  6
```
Array representation: [root, node1, node2, node3, node4, node5, node6]

Time Complexity: O(1) for navigation, O(n) for tree construction
Space Complexity: O(n) for storing n nodes, O(1) extra space for navigation

This data structure demonstrates how mathematical relationships can replace pointers,
enabling efficient tree representations and is crucial for understanding heaps,
priority queues, and memory-efficient algorithms.
"""

from typing import List, Optional


class ArrayBinaryTree:
    """
    A simple array-based binary tree representation.
    Index relationships:
        left(i)  = 2*i + 1
        right(i) = 2*i + 2
        parent(i) = (i - 1) // 2
    """

    def __init__(self, values: Optional[List[Optional[int]]] = None):
        # Allow None placeholders for missing nodes
        self._arr = list(values) if values is not None else []

    def __len__(self):
        return len(self._arr)

    def __getitem__(self, index: int):
        return self._arr[index]

    def __setitem__(self, index: int, value):
        self._ensure_capacity(index)
        self._arr[index] = value

    def _ensure_capacity(self, index: int):
        """Expand internal list to fit index."""
        if index >= len(self._arr):
            self._arr.extend([None] * (index + 1 - len(self._arr)))

    # --- Navigation helpers ---

    @staticmethod
    def left(i: int) -> int:
        return 2 * i + 1

    @staticmethod
    def right(i: int) -> int:
        return 2 * i + 2

    @staticmethod
    def parent(i: int) -> Optional[int]:
        return (i - 1) // 2 if i > 0 else None

    # --- Tree operations ---

    def insert(self, index: int, value):
        """Insert or overwrite a node at a given index."""
        self._ensure_capacity(index)
        self._arr[index] = value

    def get_left(self, index: int):
        child = self.left(index)
        return self._arr[child] if child < len(self._arr) else None

    def get_right(self, index: int):
        child = self.right(index)
        return self._arr[child] if child < len(self._arr) else None

    def get_parent(self, index: int):
        p = self.parent(index)
        return self._arr[p] if p is not None and p < len(self._arr) else None

    def to_list(self) -> List[Optional[int]]:
        """Return the underlying array."""
        return list(self._arr)
