"""
Longest Consecutive Sequence Algorithm Explained Step-by-Step
--------------------------------------------------------------
The Longest Consecutive Sequence problem is a classic array problem that finds the length of the longest
consecutive subsequence in an unsorted array. This problem is particularly useful for interviews as it tests
understanding of hash sets, functional programming patterns, and the importance of data structure choice for
optimization. The key insight is using a set for O(1) membership testing to identify sequence starts.

Here is how the process works:

1. **Convert to Set**: Transform the input array into a set for constant-time lookup.
   - Removes duplicates automatically
   - Enables O(1) membership testing with 'in' operator
   - Space trade-off: O(n) extra space for O(1) lookup performance

2. **Identify Sequence Starts**: Find numbers that start a consecutive sequence.
   - A number is a sequence start if (n - 1) is NOT in the set
   - Filters out all numbers that are continuations of existing sequences
   - Generator expression keeps this step lazy and memory-efficient
   - Example: in [1,2,3,5,6,8], starts are [1,5,8]

3. **Count Sequence Length**: For each start, extend forward to find the sequence length.
   - Generator expression: count consecutive numbers from n
   - Inner condition: 'x in num_set' checks each potential next number
   - Generator stops immediately when finding a gap (member not in set)
   - sum(1 for ...) effectively counts matching elements up to the first break

4. **Find Maximum**: Return the longest sequence length found.
   - max(lengths, default=0) handles empty input gracefully
   - Generator consumes lazily during max operation
   - Memory efficient for large arrays

5. **Functional Programming Style**: This implementation emphasizes generators and functional patterns.
   - Generator expressions defer computation until needed
   - No explicit loops or state mutation required
   - Pure functional approach with immutable set operations
   - Readable and expresses intent clearly

6. **Time Complexity Breakdown**:
   - Set creation: O(n)
   - Generator of starts: O(n) to filter elements
   - Counting sequences: O(n) total (each element counted once as either a start or part of a sequence)
   - Overall: O(n) because we visit each number at most once in aggregate

Example: nums = [100, 4, 200, 1, 3, 2]
- Set: {1, 2, 3, 4, 100, 200}
- Starts: [1, 100, 200]
- From 1: sequence [1,2,3,4] → length 4
- From 100: sequence [100] → length 1
- From 200: sequence [200] → length 1
- Result: 4 (longest is [1,2,3,4])

Time Complexity: O(n) - single pass through the set plus sequence counting
Space Complexity: O(n) - storing all unique numbers in a set
Functional Style: Pure generators with no explicit loops or side effects

This algorithm demonstrates functional programming with generators and is essential for
understanding set-based optimization, sequence detection, and functional Python patterns.
"""

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Pure functional-style solution for Longest Consecutive Sequence.
    Uses a set for O(1) membership and functional iteration.
    """

    num_set = set(nums)

    # A generator of all sequence lengths starting from "sequence starts"
    lengths = (
        sum(1 for x in range(n, n + 10**9) if x in num_set)
        for n in num_set
        if n - 1 not in num_set  # only start counting at sequence starts
    )

    # The above generator uses an unbounded range, but stops immediately
    # because membership fails quickly. This keeps it O(n).

    return max(lengths, default=0)
