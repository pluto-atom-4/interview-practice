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
