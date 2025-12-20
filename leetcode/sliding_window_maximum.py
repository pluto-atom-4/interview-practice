"""
Sliding Window Maximum - Monotonic Queue Problem
-------------------------------------------------
The Sliding Window Maximum problem finds the maximum element in every contiguous subarray of size k
in a given array. A naive approach would be O(n*k) using nested loops or O(n*log(n)) using a heap.
However, the optimal solution uses a monotonic deque data structure to achieve O(n) time complexity.
The key insight is maintaining a deque of indices in decreasing order of their values, where the
front always contains the index of the maximum in the current window.

Here is how the process works:

1. **Monotonic Deque Concept**: Maintain indices in decreasing order of values.
   - Front of deque: index of maximum element in current window
   - Back of deque: most recent element
   - Only store indices of elements that could be future maximums
   - Smaller elements are useless (will never be maximum before being out of window)

2. **Remove Out-of-Window Elements**: Keep the deque valid for current window.
   - Before processing new element, check if front index is outside current window
   - Window at iteration i contains elements from (i - k + 1) to i
   - Remove any indices from front that are older than (i - k + 1)
   - This ensures only current window elements are in the deque

3. **Remove Smaller Elements**: Maintain decreasing order of values.
   - When adding new element with value num, remove all elements from back with value < num
   - These smaller elements cannot be future maximums (current one is larger and added later)
   - Removing them keeps the deque clean and ensures O(n) amortized time
   - Each element enters and exits the deque at most once

4. **Add New Element**: Append current index to the deque.
   - After removing smaller elements, add the current index to the back
   - Front of deque now contains index of maximum in current window
   - This maintains the monotonic decreasing property

5. **Record Maximum**: When window is complete, record the front element.
   - Once we've seen k elements (i >= k-1), the window is complete
   - Front of deque contains the index of maximum for this window
   - Append nums[deque[0]] to result
   - Move to next window iteration

6. **Why This Works**: Greedy maintenance of candidates.
   - Only keep indices of elements that could be maximums
   - For each new element, all previous smaller elements are eliminated
   - Front element is guaranteed to be the maximum in current window
   - Each element processed at most twice (added and removed), so O(n)

Example: nums = [1, 3, 1, 2, 0, 5], k = 3
- i=0: queue=[0], window=[1], i < k-1, skip result
- i=1: value=3, remove 1, queue=[1], window=[1,3], i < k-1, skip result
- i=2: value=1, queue=[1,2], window=[1,3,1], i >= k-1, append queue[0]=3, remove nothing
- i=3: value=2, queue=[1,2], remove 2, queue=[1,3], window=[3,1,2], append 3
- i=4: value=0, queue=[1,3], window=[1,2,0], append 2, remove nothing
- i=5: value=5, remove all, queue=[5], window=[2,0,5], append 5, remove index 2
- Result: [3, 3, 2, 5]

Time Complexity: O(n) where n = len(nums)
- Each element is added to deque exactly once
- Each element is removed from deque at most once
- Two while loops combined do O(n) operations total
- Amortized O(1) per element

Space Complexity: O(k)
- Deque stores at most k elements (window size)
- Can be smaller if array has many increasing elements
- Result array: O(n - k + 1) for output

Comparison of Approaches:
- Naive nested loop: O(n*k) time, O(1) space - too slow for large k
- Max heap: O(n*log(n)) time, O(k) space - heap operations overhead
- Deque monotonic: O(n) time, O(k) space - optimal solution
- Segment tree: O(n*log(n)) time, O(n) space - overkill but works

Interview Discussion Points:
- Why monotonic deque is optimal for this problem
- How to prove each element enters/exits queue at most once
- Trade-offs: deque vs. heap vs. segment tree approaches
- How to modify for minimum instead of maximum (same algorithm)
- Real-world applications: traffic flow, stream processing, time-series analysis
- Follow-up: return indices of maximums, or sliding window median (harder)

Functional vs. Imperative Variants:
- Functional (tuples): Pure, immutable, clear but slightly slower
- Imperative (deque): Mutable collections, faster, more practical
- Both achieve O(n) time complexity with identical logic
"""

from typing import List, Tuple


def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """
    Pure functional-style sliding window maximum.
    Uses an immutable monotonic queue represented as a tuple.
    """

    def push(queue: Tuple[int, ...], value: int) -> Tuple[int, ...]:
        # Remove smaller elements from the right
        return tuple(x for x in queue if x >= value) + (value,)

    def pop(queue: Tuple[int, ...], value: int) -> Tuple[int, ...]:
        # Remove from left only if it matches the outgoing value
        return queue[1:] if queue and queue[0] == value else queue

    queue: Tuple[int, ...] = ()
    result: List[int] = []

    for i, num in enumerate(nums):
        queue = push(queue, num)

        if i >= k - 1:
            result.append(queue[0])
            outgoing = nums[i - k + 1]
            queue = pop(queue, outgoing)

    return result
