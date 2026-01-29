"""
## Problem Statement

Given an integer array and an integer k, return the k most frequent elements. 
The goal is to efficiently identify and return the top-k elements with highest frequency.
This problem tests understanding of data structures (heap, hash map) and optimization techniques.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using a **Min-Heap of Size K** with Counter:

A min-heap of fixed size k maintains only the top-k most frequent elements. 
By tracking the minimum frequency in the heap, we can efficiently reject smaller frequencies 
without storing all elements in memory.

* Key Concepts:

  - Why build frequency map manually?
Building a frequency map is essential preprocessing. By iterating through the list and
incrementally counting occurrences, we achieve O(n) time complexity without external dependencies.
This gives us the "frequency ranking" needed to identify top-k candidates.

  - Why min-heap of size k instead of sorting all frequencies?
Sorting all n distinct elements would cost O(n log n). A fixed-size min-heap maintains O(k) space 
and O(n log k) time complexity because we only push/pop when heap exceeds k elements. 
The heap's root always holds the minimum frequency among top-k elements, making removal of 
lower frequencies O(log k).

  - Why extract with sorted(heap, reverse=True) at the end?
The heap is a partial ordering, not a complete sort. Sorting the k elements ensures we return 
them in descending frequency order, providing consistent output. At k elements, sorting costs O(k log k), 
which doesn't dominate the O(n log k) heap operations.

* Logic:

1. Build frequency map using Counter in O(n) time
2. Iterate through (value, frequency) pairs and maintain a min-heap of size k
3. For each element: push (frequency, value) into heap
4. If heap exceeds k, pop the minimum frequency element (least frequent of top-k candidates)
5. Sort remaining k elements by frequency (descending) and extract values

* **30-Second Pitch**:

I use a min-heap approach paired with a frequency counter. I iterate through all elements, 
maintaining a heap of exactly k elements. When the heap exceeds k, I remove the element with 
the lowest frequency. This guarantees the heap holds the k most frequent elements with O(n log k) 
time complexity—much better than sorting all n elements.

* **Rapid-Fire Version**:

- Use Counter for O(n) frequency counting
- Maintain min-heap of size k to track top-k candidates
- Push (frequency, value); pop when heap > k (removes min frequency)
- At end, sort k elements and extract values for descending frequency order
- Avoids O(n log n) sorting of all elements

* **Ultra-Minimal One-Liner**:

- Counter + fixed-size min-heap identifies top-k frequent elements in O(n log k) time, 
avoiding full sort.

* **Complexity Analysis**:

- **Time Complexity:** O(n log k)
  - Counter builds frequency map: O(n)
  - Heap operations (push/pop) for n elements, max heap size k: O(n log k)
  - Final sort of k elements: O(k log k), dominated by O(n log k)

- **Space Complexity:** O(n)
  - Counter stores all unique elements and their frequencies: O(unique elements) ≤ O(n)
  - Min-heap stores at most k elements: O(k)

* **Use Cases**:

- Identifying trending topics or keywords in text
- Finding most frequently accessed files or endpoints
- Analytics: top products by purchase frequency, top users by activity
- Any scenario where you need top-k items by frequency without processing all items
"""

from __future__ import annotations

import heapq
from collections import Counter
from typing import Any, List


def top_k_frequent(nums: List[Any], k: int) -> List[Any]:
    if k <= 0:
        return []

    # Build frequency map manually without Counter
    freq: dict[Any, int] = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Min-heap of (frequency, value)
    heap: List[tuple[int, Any]] = []

    for value, count in freq.items():
        heapq.heappush(heap, (count, value))
        if len(heap) > k:
            heapq.heappop(heap)

    # Extract values sorted by highest frequency first
    return [value for (_, value) in sorted(heap, reverse=True)]