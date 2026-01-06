"""
Deque (Double-Ended Queue) - Array Implementation Explained Step-by-Step
--------------------------------------------------------------------------
A Deque is a linear data structure that allows insertion and deletion of elements at both ends.
The name "Deque" is a portmanteau of "double-ended queue". Unlike regular queues (FIFO) or stacks (LIFO),
deques support operations at both the front and rear, making them versatile for problems requiring
flexible access patterns. This implementation uses a circular array for efficient space management.

Here is how the process works:

1. **Circular Array Design**: Use a dynamic circular array to efficiently manage space.
   - Maintain _front pointer to track the start of the deque
   - Maintain _size to track number of elements
   - Use modulo arithmetic to wrap around when reaching array boundaries
   - Enables O(1) append/pop operations without continuous shifting

2. **Append Operations**: Add elements to either end efficiently.
   - append(value): Add to the right end using circular position calculation
   - Position: (front + size) % array_length gives next available slot
   - append_left(value): Add to the left end by decrementing front pointer
   - Front pointer: (front - 1) % array_length wraps around correctly

3. **Pop Operations**: Remove elements from either end.
   - pop(): Remove from right end, decrement size, keep front unchanged
   - Calculate back index using: (front + size - 1) % array_length
   - pop_left(): Remove from left end by advancing front pointer
   - Front pointer: (front + 1) % array_length moves forward
   - Both operations maintain constant O(1) time complexity

4. **Dynamic Resizing**: Automatically expand array when capacity is reached.
   - Trigger: When size equals array capacity
   - Action: Create new array with doubled capacity
   - Rebuild: Copy elements in order (important to linearize the circular structure)
   - Reset: Set front to 0 for simplified indexing after resize

5. **Modulo Arithmetic**: Key technique for circular array wrapping.
   - Maps logical indices (0 to size-1) to physical positions in array
   - Prevents index out of bounds errors naturally
   - Example: With capacity=8, indices 0,1,2...7 wrap back to 0,1,2...
   - Enables efficient space usage without gaps

6. **Space Management**: Circular array eliminates need for shifting elements.
   - Without circular design: pop_left() requires O(n) shifting of all elements
   - With circular design: Only update front pointer, O(1) operation
   - Memory-efficient for frequent operations at both ends
   - Automatic cleanup: Set elements to None when popped for garbage collection

Example: Operations sequence on ArrayDeque
- append(10): _front=0, _data=[10, None, None...], _size=1
- append(20): _front=0, _data=[10, 20, None...], _size=2
- append_left(5): _front=7 (after % 8), _data=[10, 20, None...5], _size=3
- pop(): Returns 20, _size=2
- pop_left(): Returns 5, _front=0, _size=1

Time Complexity:
- append()/pop()/append_left()/pop_left(): O(1) amortized (except resize)
- resize(): O(n) when doubling capacity
- Space Complexity: O(n) where n is the maximum number of elements stored

This data structure is essential for:
- Sliding window problems requiring both-end access
- Breadth-first search (BFS) implementations
- Processing tasks where you need to handle both front and back
- Cache implementations (LRU cache patterns)
- Palindrome checking and validation problems
"""


class ArrayDeque:
    """Deque implemented using a circular array."""

    def __init__(self, capacity=8):
        self._data = [None] * capacity
        self._front = 0
        self._size = 0

    def append(self, value):
        """Add to the right end."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = value
        self._size += 1

    def append_left(self, value):
        """Add to the left end."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = value
        self._size += 1

    def pop(self):
        """Remove from right end."""
        if self.is_empty():
            raise IndexError("pop from empty deque")

        back_index = (self._front + self._size - 1) % len(self._data)
        value = self._data[back_index]
        self._data[back_index] = None
        self._size -= 1
        return value

    def pop_left(self):
        """Remove from left end."""
        if self.is_empty():
            raise IndexError("pop_left from empty deque")

        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return value

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def _resize(self, new_capacity):
        old = self._data
        self._data = [None] * new_capacity
        walk = self._front

        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)

        self._front = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"ArrayDeque(size={self._size}, data={self._data})"
