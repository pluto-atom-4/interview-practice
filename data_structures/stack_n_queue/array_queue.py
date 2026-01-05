"""
Queue Data Structure (Circular Array Implementation) Explained Step-by-Step
---------------------------------------------------------------------------
A Queue is a fundamental data structure that implements the First-In-First-Out (FIFO) principle. This
implementation uses a circular array (ring buffer), which is the preferred approach for interviews and
production systems. It provides O(1) operations for all queue methods while maintaining cache efficiency
and predictable memory allocation. The circular design elegantly handles wraparound without shifting elements.

Here is how the process works:

1. **Circular Array Structure**: Uses a fixed-size array that wraps around logically.
   - _data: Fixed-size array allocated upfront
   - _front: Index of the first element (where dequeue happens)
   - _size: Current number of elements in queue
   - Capacity grows dynamically via resizing when needed
   - Indices wrap around using modulo arithmetic: (index + 1) % capacity

2. **Initialization**: Create queue with default or specified capacity.
   - Allocate array of size 'capacity' (default 8, a power of 2)
   - Initialize _front to 0 (start of array)
   - Initialize _size to 0 (empty queue)
   - Using power-of-2 capacity optimizes modulo operation for resizing

3. **Enqueue Operation (Insert at Rear)**: Add elements efficiently using wraparound.
   - Check if queue is full: _size == len(_data)
   - If full, trigger resize() to double capacity
   - Calculate available position: avail = (_front + _size) % len(_data)
   - Place value at calculated position
   - Increment _size
   - Time Complexity: O(1) amortized - resizing happens rarely
   - No element shifting needed; uses circular wraparound instead

4. **Dequeue Operation (Remove from Front)**: Remove and return first element.
   - Check if queue is empty, raise IndexError if true
   - Extract value from _data[_front]
   - Clear the cell: _data[_front] = None (helps garbage collection)
   - Advance front pointer: _front = (_front + 1) % len(_data)
   - Decrement _size
   - Return extracted value
   - Time Complexity: O(1) - No array shifting, just pointer update

5. **Circular Wraparound Logic**: The key insight for efficiency.
   - When rear index reaches end of array, it wraps to beginning
   - Formula: next_index = (current_index + offset) % array_length
   - Example: array of size 5, _front=3, _size=2 → rear is at index (3+2)%5 = 0
   - Eliminates need to shift elements when queue wraps around
   - Requires careful index management but provides optimal performance

6. **Resize Operation**: Double capacity when queue reaches maximum.
   - Create new array with double capacity
   - Copy elements from old array respecting circular order
   - Start from _front and walk through _size elements
   - Place copied elements sequentially in new array starting at index 0
   - Reset _front to 0 after copying
   - Old array is discarded (garbage collected)
   - Time Complexity: O(n) amortized - happens infrequently

7. **Key Advantages over Linked List Queue**:
   - Cache-friendly: Contiguous memory locations improve CPU cache hit rate
   - No pointer overhead: Saves 8 bytes per element on 64-bit systems
   - Predictable performance: No pointer chasing, direct array indexing
   - Better for interviews: Demonstrates understanding of array optimization
   - Fixed iteration speed: Predictable amortized O(1) performance

8. **Why Interviewers Prefer Circular Array**:
   - Demonstrates knowledge of advanced data structure techniques
   - Shows understanding of modulo arithmetic and wraparound logic
   - Better space efficiency (no pointer overhead)
   - Cache locality awareness (important for systems programming)
   - Practical choice for high-performance systems

Real-world Applications: Kernel task scheduling, network packet buffering, thread pools, game loops,
streaming processors, embedded systems with limited memory, and any high-throughput FIFO system.

Time Complexity Summary:
  - Enqueue: O(1) amortized - O(n) during rare resize operations
  - Dequeue: O(1) - constant time removal
  - Peek: O(1) - direct array access
  - is_empty: O(1) - simple size check

Space Complexity: O(n) where n is the number of elements
Amortized Analysis: After doubling, array has extra space for ~n more operations before next resize

Design Pattern: Ring Buffer - used in buffers, caches, and streaming systems
"""


class ArrayQueue:
    """Queue implemented using a circular array (interviewer‑preferred)."""

    def __init__(self, capacity=8):
        self._data = [None] * capacity
        self._front = 0
        self._size = 0

    def enqueue(self, value):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = value
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[self._front]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def _resize(self, new_capacity):
        old_data = self._data
        self._data = [None] * new_capacity
        walk = self._front

        for i in range(self._size):
            self._data[i] = old_data[walk]
            walk = (walk + 1) % len(old_data)

        self._front = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"ArrayQueue(size={self._size}, data={self._data})"
