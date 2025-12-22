"""
Tree Data Structure Explained Step-by-Step
-----------------------------------------
A tree is a hierarchical data structure consisting of nodes, where each node has zero or more children and exactly one parent (except the root).

Key Operations:
1. **Add Child**: Attach a child node to a parent node.
2. **Traversals**:
   - Preorder: Visit root, then children recursively
   - Postorder: Visit children recursively, then root
   - Level-order: Visit nodes level by level (BFS)

Time Complexity:
- Add Child: O(1)
- Traversals: O(N) where N is the number of nodes

This structure is essential for representing hierarchies, file systems, and more.
"""

from collections import deque
from typing import Generic, Iterator, List, Optional, TypeVar

T = TypeVar("T")

class TreeNode(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.children: List[TreeNode[T]] = []

    def add_child(self, child: "TreeNode[T]") -> None:
        self.children.append(child)

    def __repr__(self) -> str:
        return f"TreeNode({self.value!r})"

class Tree(Generic[T]):
    def __init__(self, root: Optional[TreeNode[T]] = None) -> None:
        self.root = root

    def preorder(self) -> Iterator[T]:
        def _preorder(node: Optional[TreeNode[T]]):
            if node:
                yield node.value
                for child in node.children:
                    yield from _preorder(child)
        return _preorder(self.root)

    def postorder(self) -> Iterator[T]:
        def _postorder(node: Optional[TreeNode[T]]):
            if node:
                for child in node.children:
                    yield from _postorder(child)
                yield node.value
        return _postorder(self.root)

    def level_order(self) -> Iterator[T]:
        if not self.root:
            return iter([])
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            yield node.value
            queue.extend(node.children)

    def __str__(self) -> str:
        lines = []
        def _display(node: TreeNode[T], depth: int):
            lines.append("  " * depth + f"- {node.value}")
            for child in node.children:
                _display(child, depth + 1)
        if self.root:
            _display(self.root, 0)
        return "\n".join(lines)

if __name__ == "__main__":
    # Example usage
    root = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")
    root.add_child(b)
    root.add_child(c)
    b.add_child(d)
    b.add_child(e)
    c.add_child(f)
    tree = Tree(root)
    print("Tree Structure:\n", tree)
    print("Preorder:", list(tree.preorder()))
    print("Postorder:", list(tree.postorder()))
    print("Level-order:", list(tree.level_order()))

