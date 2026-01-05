"""
Queue Data Structure (Linked List Implementation) Explained Step-by-Step
-------------------------------------------------------------------------
A Queue is a fundamental data structure that implements the First-In-First-Out (FIFO) principle, where
the first element added is the first to be removed. It's commonly used in breadth-first search (BFS),
task scheduling, message queues, and printer job management. This implementation uses a singly linked
list to provide efficient O(1) enqueue and dequeue operations.

Here is how the process works:

1. **Structure Overview**: The Queue maintains two pointers and a size counter.
   - front: Points to the first node in the queue (where elements are dequeued)
   - rear: Points to the last node in the queue (where elements are enqueued)
   - _size: Tracks the number of elements for O(1) size lookup
   - Linked list allows dynamic memory allocation without resizing

2. **Enqueue Operation (Insert at Rear)**: Add elements to the end of the queue.
   - Create a new node with the given value
   - If queue is empty (rear is None): Set both front and rear to the new node
   - If queue is not empty: Attach new node to rear.next and update rear pointer
   - Increment size counter
   - Time Complexity: O(1) - Direct pointer update, no traversal needed

3. **Dequeue Operation (Remove from Front)**: Remove and return the first element.
   - Check if queue is empty, raise IndexError if true
   - Extract value from front node
   - Move front pointer to the next node
   - If front becomes None, update rear to None (queue now empty)
   - Decrement size counter
   - Return the extracted value
   - Time Complexity: O(1) - Direct pointer manipulation

4. **Peek Operation (View Front)**: Access the first element without removal.
   - Check if queue is empty, raise IndexError if true
   - Return the value of the front node without modifying structure
   - Time Complexity: O(1) - Simple pointer dereference

5. **Memory Model**: Unlike arrays, linked list queues use dynamic memory.
   - Each node occupies separate memory location with pointer to next
   - No need for resizing or capacity management
   - Memory overhead: Extra storage for 'next' pointer in each node
   - Trade-off: Slightly higher space per element vs. simpler implementation

6. **Key Advantages vs. Array-based Queue**:
   - No resizing overhead during enqueue operations
   - Simpler implementation logic
   - Natural representation of unbounded queues
   - No wasted capacity from preallocated arrays

7. **Key Disadvantages vs. Array-based Queue**:
   - Extra memory for pointers (typically 8 bytes per node on 64-bit systems)
   - No random access to elements
   - Cache-unfriendly due to scattered memory locations
   - Interviewers may prefer circular array implementation for efficiency

Real-world Applications: Task scheduling, printer queues, message passing systems, BFS graph traversal,
customer service call handling, and any system requiring FIFO ordering.

Time Complexity Summary:
  - Enqueue: O(1) - constant time insertion at rear
  - Dequeue: O(1) - constant time removal from front
  - Peek: O(1) - constant time access to front
  - is_empty: O(1) - simple null check

Space Complexity: O(n) where n is the number of elements (including pointer overhead per node)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """Queue implemented using a singly linked list (FIFO)."""

    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            # empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.front.value

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size

    def __len__(self):
        return self._size

    def __repr__(self):
        items = []
        curr = self.front
        while curr:
            items.append(curr.value)
            curr = curr.next
        return f"Queue({items})"
