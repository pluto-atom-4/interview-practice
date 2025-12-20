"""
Sliding Window Maximum - Monotonic Deque (Imperative Version)
--------------------------------------------------------------
The Sliding Window Maximum problem finds the maximum element in every contiguous subarray of size k
in an array. This imperative version uses Python's collections.deque for optimal O(n) performance.
The algorithm maintains a decreasing monotonic deque of indices, ensuring the front always contains
the index of the current window's maximum element. This is the most practical and performant approach
for solving this problem in real-world scenarios and technical interviews.

Here is how the process works:

1. **Initialize Deque and Result**: Set up data structures.
   - dq = deque(): Stores indices (not values) of elements in decreasing order of their values
   - result = []: Will store the maximum of each window
   - Deque operations (popleft, pop, append) are O(1)

2. **Remove Out-of-Window Indices**: Maintain window boundaries.
   - Check if front index (dq[0]) is outside current window bounds
   - Window bounds: from (i - k) to i (inclusive)
   - If dq[0] <= i - k: front element is too old, remove it with dq.popleft()
   - This ensures deque only contains indices of current window elements

3. **Remove Smaller Elements**: Maintain decreasing monotonic property.
   - While back of deque has element with value smaller than current value
   - While dq and nums[dq[-1]] < num: dq.pop()
   - Remove these smaller elements because current element is larger and came later
   - These eliminated elements can never be window maximum (current element will outlive them in future windows)
   - This cleanup is crucial for maintaining O(n) amortized complexity

4. **Add Current Index**: Append to back of deque.
   - dq.append(i): Add current index to deque
   - Front of deque now has the index of maximum in current window
   - Deque maintains decreasing order: nums[dq[0]] >= nums[dq[1]] >= ... >= nums[dq[-1]]

5. **Record Window Maximum**: When window is fully formed.
   - Once i >= k - 1: We have a complete window of size k
   - result.append(nums[dq[0]]): Front of deque is window maximum
   - This is recorded for each complete window
   - Continue to next iteration and slide the window

6. **Why Indices Not Values**: Indices enable efficient window boundary checking.
   - Storing indices allows checking if element is outside window
   - Storing values would make window boundary removal difficult
   - Indices also enable reconstruction of max-providing element if needed

Example: nums = [1, 3, 1, 2, 0, 5], k = 3
Step-by-step trace:
- i=0, num=1: dq=[0]
- i=1, num=3: remove 1 (nums[0]=1 < 3), dq=[1]
- i=2, num=1: dq=[1,2], i >= k-1, append 3 (nums[dq[0]]=3), result=[3]
- i=3, num=2: remove 2 (nums[2]=1 < 2), dq=[1,3], i >= k-1, append 3, result=[3,3]
- i=4, num=0: dq=[1,3,4], remove index 1 (1 <= 4-3=1), dq=[3,4], append 2, result=[3,3,2]
- i=5, num=5: remove 3 and 4 (both < 5), dq=[5], append 5, result=[3,3,2,5]
Final result: [3, 3, 2, 5]

Time Complexity: O(n) where n = len(nums)
- Outer loop: O(n) iterations
- Each element added to deque once: O(n) total
- Each element removed from deque at most once: O(n) total
- While loops combined across entire algorithm: O(n) total operations
- Amortized O(1) per element despite nested while loops

Space Complexity: O(k)
- Deque stores at most k indices (window size)
- In practice, deque size depends on data pattern (few duplicates vs. many)
- Result array: O(n - k + 1) for output

Algorithm Characteristics:
- In-place window sliding: moves one element at a time
- Greedy elimination: smaller elements removed immediately
- Two-pointer pattern variant: front and back of deque move independently
- Cache-friendly: sequential array access pattern

Comparison of Approaches:
- Brute force with nested loops: O(n*k) - too slow for large k
- Priority queue (max heap): O(n*log(k)) - heap overhead, deletion not supported
- Segment tree with range max: O(n*log(n)) - overkill for this problem
- **Monotonic deque: O(n)** - optimal solution, most efficient

Interview Insights & Follow-ups:
- Explain why monotonic deque beats heap (no deletion overhead)
- Modify for minimum: same algorithm, keep increasing monotonic queue
- Variation: return index of maximum (store in deque already)
- Variation: sliding window median (harder, requires two heaps or balanced BST)
- Real applications: stock trading (max profit over window), traffic flow, sensor data
- Explain amortized analysis: why nested while loops still O(n)
- Discuss functional vs. imperative trade-offs (this is most practical)

Edge Cases to Consider:
- k = 1: Each element is its own maximum, result = nums
- k = n: Only one window, result = [max(nums)]
- All equal elements: All indices stay in deque, front is oldest
- Strictly decreasing: Deque always has all k elements
- Strictly increasing: Deque always has exactly 1 element
"""

from collections import deque
from typing import List


def sliding_window_maximum_imperative(nums: List[int], k: int) -> List[int]:
    """
    Classic imperative O(n) deque-based solution.
    Maintains decreasing monotonic deque of indices for optimal performance.
    """
    dq = deque()
    result = []

    for i, num in enumerate(nums):
        # Remove elements outside the window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements from the right
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
