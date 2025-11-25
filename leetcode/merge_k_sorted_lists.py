"""
Merge K Sorted Lists (Min-Heap Approach) - LeetCode Problem
-------------------------------------------------------------
The Merge K Sorted Lists problem requires combining multiple sorted linked lists into a single
sorted linked list. The min-heap approach leverages a priority queue to efficiently track and merge
the smallest elements from all lists. This is a classic problem demonstrating the use of heaps for
merging multiple sequences and is essential for understanding greedy algorithms and data structures.

Here is how the process works:

1. **Initialize the Heap**: Create a min-heap with the head nodes of all lists.
   - For each non-empty list, push its head node into the heap
   - Use tuple format: (node_value, index, node) to ensure proper ordering
   - The index prevents comparison errors between nodes with equal values
   - This heap will always give us the smallest node among current list heads

2. **Build Result List Structure**: Create a dummy node to simplify result construction.
   - Dummy node serves as a starting point for the result linked list
   - Current pointer tracks where to attach the next smallest node
   - This avoids special cases for handling the first node separately

3. **Extract Minimum Elements**: Repeatedly extract the smallest node from the heap.
   - Pop the minimum element (smallest value) from the heap
   - Attach this node to the result list via current.next
   - Advance the current pointer to the newly added node
   - This ensures the result list maintains sorted order

4. **Add Next Nodes to Heap**: Push the successor of the extracted node if it exists.
   - After extracting a node, check if it has a next node in its original list
   - If yes, push this next node into the heap for future extraction
   - This maintains a heap size of at most k (number of lists)
   - Continue until all nodes from all lists are processed

5. **Heap Operations Complexity**: Each heap operation has logarithmic cost.
   - Insert/Extract operations: O(log k) where k is the number of lists
   - With N total nodes, total heap operations: O(N log k)
   - Min-heap ensures we always get the globally smallest node next
   - No explicit merging or comparison between lists needed

6. **Final Result**: Return the sorted merged list starting from dummy.next.
   - The result list is already sorted as we extracted nodes in order
   - Return dummy.next to exclude the dummy node from the result
   - The merged list combines all k sorted lists into one sorted sequence

Example: lists = [[1,4,5], [1,3,4], [2,6]]
- Converted to linked lists: 1->4->5, 1->3->4, 2->6
- Heap operations extract: 1, 1, 2, 3, 4, 4, 5, 6
- Result: 1->1->2->3->4->4->5->6

Time Complexity: O(N log k) where N = total nodes, k = number of lists
  - Each of N nodes is pushed and popped once: O(N)
  - Each heap operation costs O(log k)
  - Total: O(N log k)

Space Complexity: O(k) for the heap storing at most k list heads
This heap-based approach is intuitive and efficient for merging multiple sorted sequences.
It demonstrates the power of priority queues for solving merging and scheduling problems.
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}->{self.next}" if self.next else f"{self.val}"

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists using a min-heap.
    """
    heap = []
    # Initialize heap with head nodes
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

# Utility functions for testing
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
