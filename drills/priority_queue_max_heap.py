"""
## Problem Statement

Implement a priority queue for scheduling factory tasks by urgency level. Design a data structure that 
efficiently retrieves the highest-urgency task first while supporting fast insertion and deletion. This 
tests understanding of heap data structures, in-place operations, and real-world scheduling systems.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using an **array-based binary max-heap**:

Why this approach? A max-heap provides O(1) peek for the most urgent task and O(log n) insertion/removal, 
making it ideal for priority scheduling. Array storage eliminates pointer overhead and maintains cache 
locality. The binary structure ensures logarithmic depth, minimizing bubble-up/bubble-down iterations.

* Key Concepts:

  - **Why store (priority, task) tuples in a single array?**
  
    Tuples pair urgency with the actual task object, enabling direct comparison by priority while preserving 
    task identity. A single array eliminates parallel data structure synchronization issues and ensures O(1) 
    access to both priority and task during operations. The heap compares only the first element (priority) 
    during heapify operations.

  - **Why maintain parent urgency ≥ children urgency (max-heap property)?**
  
    The max-heap property ensures the root (index 0) always contains the highest-priority task. This enables 
    O(1) peek without traversal. When inserting or removing, only the affected path (length O(log n)) needs 
    rebalancing, not the entire heap. The property is maintained by comparing with children during bubble-down 
    and with parent during bubble-up.

  - **Why initialize with parent index `(i-1)//2` and children at `2*i+1`, `2*i+2`?**
  
    These indices define the implicit binary tree structure within the array. Parent index formula ensures 
    integer division for backward navigation. Child indices scale to 2*i+1 and 2*i+2 to maintain complete 
    binary tree layout. This compact representation uses no extra pointers and enables cache-efficient tree 
    traversal.

* Logic:

1. **Initialization:** Create empty heap array and task registry (dict for O(1) task lookup/deletion validation)
2. **Insertion:** Append new (priority, task) tuple to heap end, then bubble-up by swapping with parent until heap property restored
3. **Extraction:** Swap root with last element, remove last, then bubble-down from root until max-heap property restored
4. **Peek:** Return root element (highest priority) without modification
5. **Heapify-up:** From child position, compare with parent; swap and move up if child > parent, else stop
6. **Heapify-down:** From parent position, compare with both children; swap with larger child and move down, else stop
   - To avoid an infinite loop inHeapify-down, ensure that the loop only continues when a swap is needed (i.e., the current node is not the largest among itself and its children). The loop breaks when no swap occurs, meaning the max-heap property is restored. This is handled by the if largest != index: condition—if no child has a higher priority, largest == index and the loop exits.
   - Also, always check child indices are within bounds (left < size, right < size) before accessing them. This prevents out-of-range errors that could cause unexpected behavior.

* **30-Second Pitch**:

I'm implementing a max-heap priority queue using an array to store (priority, task) tuples. The root 
always contains the highest-urgency task. When adding a task, I append it and bubble up to restore the 
max-heap property. When extracting, I swap the root with the last element, remove it, and bubble down. 
This gives O(1) peek and O(log n) insert/remove operations.

* **Rapid-Fire Version**:

- Array-based binary max-heap storing (priority, task) tuples
- Root always holds max-priority task (O(1) peek)
- Bubble-up on insert, bubble-down on extract
- Parent index: (i-1)//2; children: 2i+1, 2i+2
- Heapify operations run in O(log n) due to tree depth
- Task registry (dict) tracks added tasks for validation

* **Ultra-Minimal One-Liner**:

- Max-heap priority queue: array-based binary tree with parent ≥ children, O(1) peek, O(log n) insert/remove via bubble operations.

* **Complexity Analysis**:

- **Time Complexity:**
  - Peek: O(1) – direct root access
  - Insert: O(log n) – bubble-up traverses at most heap height (log n)
  - Extract: O(log n) – swap + bubble-down traverses at most heap height
  - Size/is_empty: O(1) – array length check

- **Space Complexity:**
  - O(n) for heap array storing n tasks
  - O(n) for task registry dictionary
  - O(log n) implicit recursion stack (if implemented recursively, but iterative avoids this)

* **Use Cases**:

- CPU process scheduling (OS task queues with priority levels)
- Hospital triage systems (patients prioritized by severity)
- Network packet routing (high-priority packets sent first)
- Event-driven simulation systems (process events by timestamp)
- Dijkstra's algorithm (extract minimum-distance vertex)
"""

from __future__ import annotations

from typing import Generic, List, Optional, Tuple, TypeVar

T = TypeVar("T")


class MaxHeapPriorityQueue(Generic[T]):
    """
    Priority Queue implemented as a max-heap using an array-based binary tree.

    Stores items as (priority, task) tuples.
    """

    def __init__(self) -> None:
        self._heap: List[Tuple[int, T]] = []

    # -----------------------------
    # Heap helper methods
    # -----------------------------
    def _parent(self, index: int) -> int:
        return (index - 1) // 2

    def _left(self, index: int) -> int:
        return 2 * index + 1

    def _right(self, index: int) -> int:
        return 2 * index + 2

    def _swap(self, i: int, j: int) -> None:
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    # -----------------------------
    # Core operations
    # -----------------------------
    def insert(self, task: T, priority: int) -> None:
        """Insert a task with a given priority."""
        self._heap.append((priority, task))
        self._heapify_up(len(self._heap) - 1)

    def _heapify_up(self, index: int) -> None:
        while index > 0:
            parent = self._parent(index)
            if self._heap[index][0] > self._heap[parent][0]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def extract_max(self) -> Optional[Tuple[int, T]]:
        """Remove and return the highest-priority task."""
        if not self._heap:
            return None

        self._swap(0, len(self._heap) - 1)
        max_item = self._heap.pop()
        self._heapify_down(0)
        return max_item

    def _heapify_down(self, index: int) -> None:
        size = len(self._heap)

        while True:
            left = self._left(index)
            right = self._right(index)
            largest = index

            if left < size and self._heap[left][0] > self._heap[largest][0]:
                largest = left
            if right < size and self._heap[right][0] > self._heap[largest][0]:
                largest = right

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def peek(self) -> Optional[Tuple[int, T]]:
        """Return the highest-priority task without removing it."""
        return self._heap[0] if self._heap else None

    def size(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return len(self._heap) == 0
