"""
Linked List Data Structure Explained Step-by-Step
-----------------------------------------------
A linked list is a linear data structure where each element (node) contains a value and a reference to the next node.

Here is how the process works:

1. **Append**: Traverse to the end and add a new node.
   - If the list is empty, make the new node the head
   - Otherwise, traverse to the last node and link it to the new node

2. **Prepend**: Insert a new node at the beginning, updating the head.
   - Create a new node and point it to the current head
   - Update the head to point to the new node

3. **Delete**: Find the node with the target value and remove it by updating references.
   - Handle special case if the head needs to be deleted
   - Otherwise, find the node before the target and update its next pointer

4. **Find**: Traverse the list to check if a value exists.
   - Start from the head and check each node's value
   - Return True if found, False if we reach the end

5. **To List**: Collect all node values into a Python list for easy viewing.
   - Traverse from head to tail, collecting values

6. **Reverse**: Reverse the linked list in-place by updating node references.
   - Start with prev as None and curr as the head
   - For each node, store the next node, set curr.next to prev, then move prev and curr forward
   - After traversal, set head to prev (the new front)

Linked lists are useful for dynamic data where insertions and deletions are frequent and efficient.

Time Complexity:
- Append/Prepend: O(n)/O(1) respectively
- Delete/Find: O(n)
- Reverse: O(n)
- Space Complexity: O(1) for operations, O(n) for storage

This data structure demonstrates pointer manipulation and is commonly discussed in interviews
for its simplicity and fundamental importance in computer science.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Adds a node to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, value):
        """Adds a node to the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """Deletes the first node with the given value."""
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.value != value:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def find(self, value):
        """Returns True if value is in the list, else False."""
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def to_list(self):
        """Returns a Python list of all values in the linked list."""
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

    def reverse(self):
        """Reverses the linked list in-place with debug output."""
        prev = None
        curr = self.head
        step = 1

        print("🔁 Starting reversal of linked list...")
        print(f"Initial list: {self}")

        while curr:
            next_node = curr.next
            print(f"\nStep {step}:")
            print(f"  Current node: {curr.value}")
            print(f"  Next node: {next_node.value if next_node else 'None'}")
            print(f"  Reversing: {curr.value}.next → {prev.value if prev else 'None'}")

            curr.next = prev
            prev = curr
            curr = next_node
            step += 1

        self.head = prev
        print(f"\n✅ Reversal complete. New list: {self}")

    def insert_at_index(self, index, value):
        """Inserts a new node with the given value at the specified index."""
        if index < 0:
            raise IndexError("Index cannot be negative")

        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        curr_index = 0

        while curr and curr_index < index - 1:
            curr = curr.next
            curr_index += 1

        if curr is None:
            raise IndexError("Index out of bounds")

        new_node.next = curr.next
        curr.next = new_node

    def __str__(self):
        return " -> ".join(str(v) for v in self.to_list()) + " -> None"
