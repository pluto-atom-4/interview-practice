
"""
## Problem Statement

Given a list of integers and a positive integer k, return the k most frequent elements 
in the list. The order of elements in the output does not matter. This tests understanding 
of heap data structures, frequency counting, and optimization when partial sorting is needed.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Heap-based Frequency Selection**:

Rather than fully sorting the array (O(n log n)), I use a max-heap to efficiently extract 
the k largest elements by frequency. This is particularly valuable when k is significantly 
smaller than the number of unique elements, allowing O(n + k log n) performance instead of 
O(n log n). Python provides only a min-heap, so I simulate a max-heap by negating frequencies.

* Key Concepts:

  - **Why use Counter instead of manually building a frequency dictionary?**
  
    Counter is optimized for frequency counting and handles edge cases elegantly. It's cleaner, 
    faster (implemented in C), and more readable than a manual loop building a dictionary. Since 
    frequency counting is a prerequisite to our heap approach, using the standard library's 
    efficient implementation lets us focus on the core algorithm logic.

  - **Why negate frequencies in the heap instead of using a max-heap directly?**
  
    Python's heapq module only provides min-heap behavior. To simulate a max-heap, we negate 
    the frequencies so that the smallest (most negative) values—representing the largest 
    frequencies—are at the top. When we pop, we get the element with the highest frequency. 
    This avoids importing external libraries or implementing a custom heap comparator.

  - **Why use a heap instead of sorting the frequency dictionary?**
  
    When k is much smaller than the number of unique elements (which is often the case in 
    interview problems), a heap is more efficient. Sorting requires O(n log n) time even if 
    we only need k elements. A heap extracts k elements in O(k log n), making it the better 
    choice when k << unique_elements. However, if k is close to the number of unique elements, 
    sorting might be simpler.

  - **Why store tuples of (frequency, number) in the heap?**
  
    The heap needs both the frequency (for ordering) and the number itself (for the result). 
    Python's heapq naturally compares tuples element-by-element, so placing frequency first 
    ensures correct ordering. The number is secondary and only used for retrieval.

* **30-Second Pitch**:

I count the frequency of each element using Counter, then use a max-heap to extract the k 
elements with the highest frequencies. Since Python only has a min-heap, I negate the 
frequencies to flip the ordering. This is more efficient than sorting when k is much smaller 
than the number of unique elements, giving me O(n + k log n) instead of O(n log n).

* **Rapid-Fire Version**:

- Use Counter to count element frequencies in O(n)
- Push all (frequency, element) pairs into a min-heap, negating frequencies for max-heap behavior
- Pop k times to extract the k most frequent elements in O(k log n)
- Total: O(n + k log n) time, O(n) space for the counter and heap
- More efficient than sorting when k << number of unique elements

* **Ultra-Minimal One-Liner**:

- Count frequencies with Counter, then extract k largest via negated-value min-heap in O(n + k log n).

* **Complexity Analysis**:

- **Time Complexity:** O(n + k log n)
  - Counting frequencies: O(n) where n is the length of nums
  - Building heap and pushing all unique elements: O(n) amortized (heappush is O(log m) where m 
    is heap size, and m grows to at most the number of unique elements)
  - Extracting k elements: O(k log m) where m is the number of unique elements
  - Overall: O(n) for counting + O(n) for heap building + O(k log n) ≈ O(n + k log n)
  
- **Space Complexity:** O(n) in the worst case
  - Counter stores all unique elements and their frequencies: O(unique_elements)
  - Heap stores all unique elements and frequencies: O(unique_elements)
  - In the worst case where all elements are unique, this is O(n)

* **Use Cases**:

- Finding trending topics by mention frequency in social media data
- Identifying most common errors in log analysis systems
- Recommendation systems: returning the k most-watched/liked items
- Data mining: extracting the most significant patterns or values from large datasets
- Query optimization: caching the most frequently accessed data items
- Traffic analysis: identifying the top k IP addresses by request count

---

"""

from collections import Counter
import heapq
from typing import List

def tok_k_frequent(nums: List[int], k: int) -> List[int]:
 """ 
 Return the k most frequent elements in nums.

 Uses a max-heap simulated via negative frequencies.
 """
 freq = Counter(nums)
 heap: List[tuple[int, int]] = []

 for num, count in freq.items():
     heapq.heappush(heap, (-count, num))

 result = []
 for _ in range(k):
     _, num = heapq.heappop(heap)
     result.append(num)

 return result