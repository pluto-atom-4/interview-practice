
from typing import Optional


class Node:
    def __init__(self, info: int):
        self.info: int = info
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.level: Optional[int] = None

    def __str__(self) -> str:
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def create(self, val: int) -> None:
        if self.root is None:
            self.root = Node(val)
            return

        current = self.root
        while True:
            if val < current.info:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
            elif val > current.info:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    break
            else:
                break