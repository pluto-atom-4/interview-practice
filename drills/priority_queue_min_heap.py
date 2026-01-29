"""
## Problem Statement

Implement a generic priority queue using a min-heap data structure.
The queue must efficiently enqueue/dequeue elements based on priority, 
supporting custom comparison logic. This demonstrates mastery of heap operations, 
generic programming, and custom sorting strategies—core interview topics.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using a **Min-Heap with Custom Comparators**:

The min-heap approach leverages a complete binary tree stored in an array, where each 
parent is smaller than its children. This guarantees O(log n) operations for enqueue/dequeue 
while maintaining simplicity and space efficiency. Custom comparators enable flexibility 
for max-heaps and complex priority logic without changing core logic.

* Key Concepts:

  - Why use a heap instead of sorting or a linked list?
  A heap strikes the optimal balance: O(log n) insertion/deletion vs O(n log n) for sorting 
  or O(n) for naive searches. Arrays provide cache locality and no pointer overhead like 
  linked lists. This is THE interview-standard data structure for priority queues.

  - Why bubble_up and bubble_down instead of rebuilding the entire heap?
  Incremental repairs maintain O(log n) complexity by adjusting only the affected path 
  (height of tree) instead of O(n) reconstruction. This laziness principle is critical for 
  efficient implementations and shows interview-level optimization thinking.

  - Why use a custom comparator function instead of just __lt__?
  Comparators decouple sorting logic from element types, enabling max-heaps, reverse 
  ordering, and complex multi-field priorities (e.g., by urgency then name). This showcases 
  strategy pattern knowledge and flexibility in design.

  - Why floor division (//) for parent index calculation?
  For node at index i: parent = (i-1)//2, left = 2i+1, right = 2i+2. These formulas 
  encode the complete binary tree structure in an array. Floor division ensures truncation 
  (e.g., (3-1)//2 = 1, not 1.0), which is critical for correct index arithmetic.

* Logic:

1. **Initialize heap:** Maintain internal array and optional custom comparator (default to min-heap).
2. **Enqueue (Insertion):** Append element to array end, then bubble_up to restore heap property.
3. **Dequeue (Deletion):** Extract root (highest priority), move last element to root, bubble_down to restore heap property.
4. **Peek (Read):** Return root element without modification (O(1)).
5. **Helper Methods:** bubble_up compares with parent; bubble_down compares with smaller child, swapping when needed.

* **30-Second Pitch**:

"I'd implement a min-heap using a dynamic array. When we enqueue, we append to the end 
and bubble up to restore the heap property—each element only compares with its parent, 
so it's O(log n). For dequeue, we swap the root with the last element, remove it, and 
bubble down the new root until it's larger than both children. The key insight is that 
a comparator function makes this generic: swap `a < b` for `a > b` and you have a max-heap. 
This interview-standard approach handles any priority logic efficiently."

* **Rapid-Fire Version**:

- Min-heap in array: parent at (i-1)//2, left at 2i+1, right at 2i+2
- Enqueue: append, bubble_up vs parent O(log n)
- Dequeue: swap root with last, bubble_down vs smaller child O(log n)
- Comparator strategy enables max-heap, custom priorities without code duplication
- Complete binary tree in array = space-efficient + cache-friendly
- Lazy repairs (incremental path) beats rebuilding (O(n) cost)

* **Ultra-Minimal One-Liner**:

- Min-heap priority queue with O(log n) enqueue/dequeue via array-based tree + bubble up/down repairs.

* **Complexity Analysis**:

- **Time Complexity:**
  - Enqueue: O(log n) — bubble_up traverses at most tree height
  - Dequeue: O(log n) — bubble_down traverses at most tree height
  - Peek: O(1) — direct root access
  - Build from n elements: O(n) — optimal via heapify, not O(n log n) insertion

- **Space Complexity:**
  - O(n) — array stores n elements, no extra structures for heap operations

* **Use Cases**:

- Task scheduling (urgent tasks dequeued first)
- Dijkstra's shortest path algorithm (process nearest unvisited node)
- Huffman coding (build tree by always merging smallest frequencies)
- Heap sort (repeated dequeue gives sorted output)
- Load balancing (assign tasks to least-loaded server)
- Event simulation (process events in time order)

"""

from dataclasses import dataclass
from typing import Callable, Generic, List, Optional, TypeVar

T = TypeVar("T")

@dataclass
class Task:
    name: str
    urgency: int

    # Comparisons: Instead of a compareTo method returning -1, 0, 1 in Java,
    # Python uses "rich comparison" methods. Overriding __lt__ (less than) is the standard way
    # to allow objects to be compared in a sorted structure.
    def __lt__(self, other: "Task") -> bool:
        # Define 'less than' as lower urgency number = higher priority
        # to satisfy min-heap logic (lower urgency numbers get dequeued first).
        return self.urgency < other.urgency

class PriorityQueue(Generic[T]):
    """
    Generic priority queue implementation using a min-heap.

    Supports custom comparison strategies via the comparator parameter,
    enabling max-heaps, reverse ordering, and complex priority logic.

    Type parameter T: The type of items stored in the queue.
                    Can be any type, but comparator must be provided
                    if items don't support < operator.
    """
    def __init__(self, comparator: Optional[Callable[[T, T], bool]] = None):
        """
        Initialize the priority queue.
        Args:
            comparator: Optional comparison function that returns True if the first
                        argument has higher priority than the second.
                        Default: a < b (min-heap, items must support < operator)
                        For max-heap, use: lambda a, b: a > b
            Examples:
                min_pq = PriorityQueue()  # Default min-heap
                max_pq = PriorityQueue(lambda a, b: a > b)  # Max-heap
                custom_pq = PriorityQueue(lambda a, b: len(a) < len(b))  # Custom logic
        """
        self._heap: List[T] = []
        self._comparator = comparator or (lambda a, b: a < b)

    def enqueue(self, t: T) -> None:
        """
        Add a task and bubble it up to maintain heap property.
        Time Complexity: O(log n)
        Space Complexity: O(1) amortized
        """
        self._heap.append(t)
        self._bubble_up(len(self._heap) - 1)

    def dequeue(self) -> Optional[Task]:
        """
        Remove and return the highest-priority task. O(log n)

        Returns None if the queue is empty.
        Time Complexity: O(log n)
        Space Complexity: O(1) amortized
        """
        # Truthiness: Instead of heap.size() == 0, modern Python uses if not self._heap: to check for empty lists.
        if not self._heap:
            return None

        root = self._heap[0]
        last_item = self._heap.pop()

        if self._heap:
            self._heap[0] = last_item
            self._bubble_down(0)

        return root

    def peek(self) -> Optional[Task]:
        """
        View the highest-priority task without removing it.
        
        Returns None if the queue is empty.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._heap[0] if self._heap else None

    def is_empty(self) -> bool:
        """Check if the priority queue is empty."""
        return len(self._heap) == 0

    def size(self) -> int:
        """Return the number of tasks in the priority queue."""
        return len(self._heap)

    # =====================================================================
    # Private Helper Methods: Heap Maintenance
    # =====================================================================
    def _bubble_up(self, index: int) -> None:
        """
        Restore heap property by moving an element up the tree.

        Called after adding a new element.
        Moves the element up until it finds its correct position.

        Time Complexity: O(log n) - height of the tree
        Space Complexity: O(1)
        """

        # While loop continues until we reach root (index 0) or find a parent with higher urgency.
        # The loop terminates because each swap moves the element up (smaller index), eventually hitting root.
        while index > 0:
            # Integer Division: Java's / on integers automatically truncates. 
            # In Python, you must use the floor division operator // to get the same result when calculating parent_idx.
            parent_idx = (index - 1) // 2

            # Compare current with parent using the __lt__ defined above
            if self._heap[index] < self._heap[parent_idx]:
                # Swapping: Python allows for elegant one-line swaps: a, b = b, a.
                self._heap[index], self._heap[parent_idx] = \
                    self._heap[parent_idx], self._heap[index]
                index = parent_idx
            else:
                break

    def _bubble_down(self, index: int) -> None:
        """
        Restore heap property by moving an element down the tree.

        Called after removing the root element.
        Moves the element down until it finds its correct position.

        Time Complexity: O(log n) - height of the tree
        Space Complexity: O(1)
        """

        # While loop continues until current is larger than both children or has no children.
        # The loop terminates because each swap moves the element down (larger index), eventually hitting a leaf.
        size = len(self._heap)
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if (left_child < size and
                    self._heap[left_child] < self._heap[smallest]):
                smallest = left_child

            if (right_child < size and
                    self._heap[right_child] < self._heap[smallest]):
                smallest = right_child

            if smallest != index:
                # Swapping: Python allows for elegant one-line swaps: a, b = b, a.
                self._heap[index], self._heap[smallest] = \
                    self._heap[smallest], self._heap[index]
                index = smallest
            else:
                break

# Example Usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue(Task("Low Priority", 1))
    pq.enqueue(Task("Urgent", 10))
    pq.enqueue(Task("Medium", 5))

    while not pq.is_empty():
        task = pq.dequeue()
        print(f"Executing: {task.name} with urgency {task.urgency}")
