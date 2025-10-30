"""
Max Heap Data Structure Explained Step-by-Step
----------------------------------------------
A Max Heap is a complete binary tree data structure where each parent node is greater than or
equal to its children, ensuring the largest element is always at the root. This property makes
it ideal for efficiently accessing the maximum element and maintaining reverse sorted order in
dynamic datasets. Max heaps are fundamental for implementing priority queues (where higher values
have higher priority), heap sort algorithms in descending order, and algorithms requiring frequent
maximum element access. The heap maintains its structure through careful insertion and deletion
operations that preserve the max heap property.

Here is how the process works:

1. **Heap Property**: Maintain the max-heap invariant where parent ≥ children.
   - Root node contains the largest element in the entire heap
   - Each parent node is greater than or equal to both its children
   - This property must be maintained after every operation
   - Ensures O(1) access to the maximum element at any time
   - **Key Difference from Min Heap**: Comparison operators are reversed (> instead of <)

2. **Complete Binary Tree Structure**: Store elements in a level-order array representation.
   - Fill levels from left to right without gaps
   - For element at index i: left child at 2i+1, right child at 2i+2
   - Parent of element at index i is at (i-1)//2
   - This representation allows efficient storage without pointers
   - **Same as Min Heap**: Tree structure and indexing remain identical

3. **Insert Operation**: Add new element and restore heap property via bubble-up.
   - Append new element to the end of the array (bottom-right of tree)
   - Compare with parent and swap if child is larger (opposite of min heap)
   - Continue bubbling up until heap property is satisfied
   - Time complexity: O(log n) due to tree height
   - **Key Difference from Min Heap**: Bubble up when child > parent (not child < parent)

4. **Extract Max Operation**: Remove root and restore heap property via bubble-down.
   - Save the root element (maximum value) to return
   - Replace root with the last element in the heap
   - Remove the last element to maintain complete tree structure
   - Bubble down the new root by comparing with children and swapping with larger child
   - Continue until heap property is restored throughout the tree
   - **Key Difference from Min Heap**: Extract maximum (not minimum) and swap with larger child

5. **Bubble-Up Process**: Restore heap property after insertion by moving element upward.
   - Compare inserted element with its parent
   - If child is larger than parent, swap them (opposite logic from min heap)
   - Repeat comparison and swapping up the tree until parent ≥ child
   - Stops when heap property is satisfied or element reaches root
   - **Key Difference from Min Heap**: Bubble up when child > parent

6. **Bubble-Down Process**: Restore heap property after extraction by moving element downward.
   - Compare element with both children (if they exist)
   - Find the largest among parent and its children (not smallest)
   - If a child is larger, swap parent with that child
   - Continue down the tree until element is larger than both children
   - Ensures maximum element bubbles up to maintain heap property
   - **Key Difference from Min Heap**: Find largest child and bubble larger elements up

Extract Max Use Cases and Data State:
- **Priority Queue**: Remove highest priority (largest value) task from scheduler
  - Before: [10, 8, 9, 4, 7, 5, 6] → After: [9, 8, 6, 4, 7, 5] (returns 10)
- **Game Leaderboards**: Extract highest score for winner determination
  - Before: [9500, 8200, 8800, 7100, 6900] → After: [8800, 8200, 6900, 7100] (returns 9500)
- **Heap Sort Descending**: Repeatedly extract maximum to build reverse sorted sequence
  - Before: [8, 6, 7, 2, 4] → After: [7, 6, 4, 2] (returns 8, add to sorted result)
- **Resource Allocation**: Assign resources to highest priority requests first
  - Before: [100, 75, 85, 60, 70] → After: [85, 75, 70, 60] (returns 100, allocate to top priority)

Benefits:
- O(1) access to maximum element
- O(log n) insertion and deletion operations
- Space-efficient array representation
- Suitable for dynamic datasets with frequent max queries
- Ideal for priority systems where higher values indicate higher priority

Common Use Cases:
- Priority queues where larger values have higher priority
- Job scheduling systems (higher priority numbers processed first)
- Game systems (highest scores, strongest characters)
- Heap sort algorithm for descending order sorting
- Finding K largest elements in a dataset
- CPU scheduling with priority-based algorithms

Drawbacks:
- No efficient search for arbitrary elements (O(n) linear search)
- Not suitable for frequent minimum queries (use Min Heap instead)
- Requires rebalancing after each insertion/deletion
- Memory overhead for maintaining heap structure

Max Heap vs Min Heap Logic Differences:
- **Comparison Direction**: Max heap uses > comparisons, min heap uses <
- **Bubble-Up Condition**: Max heap bubbles when child > parent, min heap when child < parent
- **Bubble-Down Target**: Max heap finds largest child, min heap finds smallest child
- **Root Element**: Max heap root is maximum, min heap root is minimum
- **Priority Semantics**: Max heap treats larger values as higher priority
- **Sort Order**: Max heap naturally produces descending order, min heap ascending

This data structure demonstrates efficient priority-based access patterns for maximum elements
and is essential for algorithms requiring dynamic maximum element retrieval and high-priority processing.
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return max_val

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                break

    def _bubble_down(self, index):
        length = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < length and self.heap[left] > self.heap[largest]:
                largest = left
            if right < length and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest
