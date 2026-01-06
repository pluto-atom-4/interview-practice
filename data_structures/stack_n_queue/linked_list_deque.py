"""
Deque (Double-Ended Queue) - Linked List Implementation Explained Step-by-Step
--------------------------------------------------------------------------------
A Deque is a linear data structure that allows insertion and deletion of elements at both ends.
This implementation uses a doubly linked list, where each node maintains pointers to both the next
and previous nodes. This design provides O(1) insertion and deletion at both ends without the overhead
of circular array resizing, making it ideal for scenarios requiring frequent operations at both extremes.

Here is how the process works:

1. **Node Structure**: Doubly linked nodes with bidirectional pointers.
   - Each node contains a value and two pointers: prev and next
   - prev pointer links to the previous node (or None if at front)
   - next pointer links to the next node (or None if at rear)
   - Enables traversal in both directions and efficient insertions/deletions

2. **Deque Structure**: Maintain front and rear pointers for both ends.
   - front pointer: References the first node in the deque
   - rear pointer: References the last node in the deque
   - _size counter: Tracks total number of elements
   - Both pointers are None when deque is empty

3. **Append Operations**: Add elements to either end.
   - append(value): Add to the right (rear) end
   - Create new node and link it after current rear
   - Update rear pointer to new node, set new node's prev link
   - If deque was empty, set both front and rear to new node
   - append_left(value): Add to the left (front) end
   - Create new node and link it before current front
   - Update front pointer to new node, set new node's next link

4. **Pop Operations**: Remove elements from either end.
   - pop(): Remove from right (rear) end
   - Extract value from rear node
   - Move rear pointer to rear.prev (previous node)
   - Update new rear's next link to None (or set front to None if empty)
   - Decrement size and return value
   - pop_left(): Remove from left (front) end
   - Extract value from front node
   - Move front pointer to front.next (next node)
   - Update new front's prev link to None (or set rear to None if empty)

5. **Bidirectional Links**: Critical feature of doubly linked deques.
   - When appending to rear: new_node.prev = rear, rear.next = new_node
   - When popping from rear: rear = rear.prev, rear.next = None
   - When appending to front: new_node.next = front, front.prev = new_node
   - When popping from front: front = front.next, front.prev = None
   - Enables efficient operations without traversing the entire list

6. **Edge Cases**: Handle empty deque transitions carefully.
   - When deque becomes empty after pop: Set both front and rear to None
   - When adding to empty deque: Set both front and rear to new node
   - This ensures consistency and prevents null pointer errors

Example: Operations sequence on LinkedListDeque
- append(10): front→[10]←rear, size=1
- append(20): front→[10]↔[20]←rear, size=2
- append_left(5): front→[5]↔[10]↔[20]←rear, size=3
- pop(): Returns 20, front→[5]↔[10]←rear, size=2
- pop_left(): Returns 5, front→[10]←rear, size=1

Time Complexity:
- append()/pop()/append_left()/pop_left(): O(1) guaranteed (no resizing)
- is_empty()/size(): O(1)
- Space Complexity: O(n) where n is the number of elements

Advantages over Array Implementation:
- No resizing overhead: No O(n) operations needed
- Unbounded size: Can grow indefinitely without resizing
- No wasted capacity: Uses only as much memory as needed
- Predictable performance: All operations are strictly O(1)

This data structure is essential for:
- Implementing stable FIFO/LIFO hybrid data structures
- Memory-constrained systems requiring guaranteed O(1) operations
- Scenarios with unpredictable deque growth patterns
- Applications requiring bidirectional traversal capabilities
- Task scheduling with priority handling at both ends
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedListDeque:
    """Deque implemented using a doubly linked list."""

    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def append(self, value):
        new = Node(value)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            new.prev = self.rear
            self.rear = new
        self._size += 1

    def append_left(self, value):
        new = Node(value)
        if self.front is None:
            self.front = self.rear = new
        else:
            new.next = self.front
            self.front.prev = new
            self.front = new
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty deque")

        value = self.rear.value
        self.rear = self.rear.prev

        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None

        self._size -= 1
        return value

    def pop_left(self):
        if self.is_empty():
            raise IndexError("pop_left from empty deque")

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None

        self._size -= 1
        return value

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"LinkedListDeque(size={self._size})"
