"""
Min Heap Data Structure Explained Step-by-Step
----------------------------------------------
A Min Heap is a complete binary tree data structure where each parent node is smaller than or
equal to its children, ensuring the smallest element is always at the root. This property makes
it ideal for efficiently accessing the minimum element and maintaining sorted order in dynamic
datasets. Min heaps are fundamental for implementing priority queues, heap sort algorithms,
and graph algorithms like Dijkstra's shortest path. The heap maintains its structure through
careful insertion and deletion operations that preserve the heap property.

Here is how the process works:

1. **Heap Property**: Maintain the min-heap invariant where parent ≤ children.
   - Root node contains the smallest element in the entire heap
   - Each parent node is smaller than or equal to both its children
   - This property must be maintained after every operation
   - Ensures O(1) access to the minimum element at any time

2. **Complete Binary Tree Structure**: Store elements in a level-order array representation.
   - Fill levels from left to right without gaps
   - For element at index i: left child at 2i+1, right child at 2i+2
   - Parent of element at index i is at (i-1)//2
   - This representation allows efficient storage without pointers

3. **Insert Operation**: Add new element and restore heap property via bubble-up.
   - Append new element to the end of the array (bottom-right of tree)
   - Compare with parent and swap if child is smaller
   - Continue bubbling up until heap property is satisfied
   - Time complexity: O(log n) due to tree height

4. **Extract Min Operation**: Remove root and restore heap property via bubble-down.
   - Save the root element (minimum value) to return
   - Replace root with the last element in the heap
   - Remove the last element to maintain complete tree structure
   - Bubble down the new root by comparing with children and swapping with smaller child
   - Continue until heap property is restored throughout the tree

5. **Bubble-Up Process**: Restore heap property after insertion by moving element upward.
   - Compare inserted element with its parent
   - If child is smaller than parent, swap them
   - Repeat comparison and swapping up the tree until parent ≤ child
   - Stops when heap property is satisfied or element reaches root

6. **Bubble-Down Process**: Restore heap property after extraction by moving element downward.
   - Compare element with both children (if they exist)
   - Find the smallest among parent and its children
   - If a child is smaller, swap parent with that child
   - Continue down the tree until element is smaller than both children
   - Ensures minimum element bubbles up to maintain heap property

Extract Min Use Cases and Data State:
- **Priority Queue**: Remove highest priority (lowest value) task from scheduler
  - Before: [1, 3, 2, 7, 8, 4, 5] → After: [2, 3, 4, 7, 8, 5] (returns 1)
- **Dijkstra's Algorithm**: Extract vertex with minimum distance for pathfinding
  - Before: [0, 5, 3, 10, 8] → After: [3, 5, 8, 10] (returns 0, process node 0)
- **Heap Sort**: Repeatedly extract minimum to build sorted sequence
  - Before: [2, 4, 3, 8, 7] → After: [3, 4, 7, 8] (returns 2, add to sorted result)
- **Event Simulation**: Process events in chronological order by timestamp
  - Before: [9:00, 9:15, 9:05, 9:30] → After: [9:05, 9:15, 9:30] (returns 9:00 event)

Benefits:
- O(1) access to minimum element
- O(log n) insertion and deletion operations
- Space-efficient array representation
- Suitable for dynamic datasets with frequent min queries

Common Use Cases:
- Priority queues in operating systems and task scheduling
- Graph algorithms (Dijkstra's, Prim's minimum spanning tree)
- Heap sort algorithm for in-place sorting
- K-way merge operations and finding K smallest elements
- Event-driven simulations and real-time systems

Drawbacks:
- No efficient search for arbitrary elements (O(n) linear search)
- Not suitable for frequent maximum queries (use Max Heap instead)
- Requires rebalancing after each insertion/deletion
- Memory overhead for maintaining heap structure

This data structure demonstrates efficient priority-based access patterns and
is essential for algorithms requiring dynamic minimum element retrieval.
"""


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_val

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        length = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            index = smallest
