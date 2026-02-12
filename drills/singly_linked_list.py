from typing import Optional


class SinglyLinkedListNode:
    def __init__(self, node_data: int):
        self.data = node_data
        self.next: Optional['SinglyLinkedListNode'] = None

class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[SinglyLinkedListNode] = None
        self.tail: Optional[SinglyLinkedListNode] = None

    def insert_node(self, node_data: int) -> None:
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node: Optional[SinglyLinkedListNode], sep: str, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)