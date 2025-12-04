"""
Two Sum Problem - Brute Force Solution (Naive Approach)
========================================================
The brute force approach to the Two Sum problem demonstrates the initial, straightforward
thinking before optimization. While not interview-recommended for large inputs due to O(n²)
time complexity, understanding this approach is valuable because:
1. It shows the starting point before optimization
2. It helps explain WHY we need better solutions
3. It's useful for very small arrays or constraints
4. It helps interviewers see your problem-solving progression

This serves as a baseline to compare against the optimized O(n) hash map solution.

Here is how the naive algorithm works:

1. **Problem Understanding**: Given an array of integers and a target sum, find the indices of
   the two numbers that add up to the target. The problem guarantees exactly one valid solution exists.
   - Example: nums = [2, 7, 11, 15], target = 9 → [0, 1] (2 + 7 = 9)
   - Example: nums = [3, 2, 4], target = 6 → [1, 2] (2 + 4 = 6)

2. **Brute Force Approach**: Check Every Possible Pair
   - Use nested loops: outer loop for first number, inner loop for second number
   - Check all pairs where i < j to avoid duplicates and repeated checks
   - If nums[i] + nums[j] == target, return [i, j] immediately
   - If no pair found after checking all combinations, return empty list
   - Time Complexity: O(n²) - for each element, check all remaining elements
   - Space Complexity: O(1) - only use constant extra space for variables
   - Limitation: Unacceptable for large arrays (e.g., n=100,000 → 10 billion operations)

3. **Algorithm Steps**:
   Step 1: Get the length n of the input array
   Step 2: Outer loop: iterate i from 0 to n-1
   Step 3: Inner loop: iterate j from i+1 to n (to avoid checking same pair twice)
   Step 4: For each pair (i, j), check if nums[i] + nums[j] == target
   Step 5: If match found, immediately return [i, j]
   Step 6: After all pairs checked, return empty list (no solution found)

4. **Example Walkthrough** with nums = [2, 7, 11, 15], target = 9:
   - i=0: Check (2,7)→9✓ Found! return [0, 1]
   - Note: Algorithm stops here and doesn't check remaining pairs

   Alternative example: nums = [2, 3, 4], target = 10
   - i=0: Check (2,3)→5✗, (2,4)→6✗
   - i=1: Check (3,4)→7✗
   - No match found, return []

5. **Why This Approach is NOT Optimal**:
   - Redundant Work: Checks all pairs even when early exit is possible
   - Quadratic Growth: Each additional element doubles the work
   - Scalability: For n=1,000 → ~500,000 operations; n=100,000 → ~5 billion operations
   - Practical Limit: Too slow for interviews and real-world applications
   - Better Solution Exists: Hash map reduces complexity to O(n)

6. **Comparison: Naive vs Optimized**:

   Naive (Brute Force):
   - Time: O(n²) - checking all pairs
   - Space: O(1) - no extra data structure
   - Approachable: Easy to understand and implement

   Optimized (Hash Map):
   - Time: O(n) - single pass with O(1) lookups
   - Space: O(n) - store values in hash map
   - Scalable: Much better for large inputs
   - Trade-off: Spend space to save time

7. **When to Use Naive Approach**:
   - Array size is very small (< 100 elements)
   - Memory is extremely limited (embedded systems)
   - Clarity is more important than performance
   - Interview context: Mention as "brute force starting point"
   - Always explain: "This is O(n²), but we can optimize to O(n) with a hash map"

8. **Interview Strategy**:
   - Start with naive approach to show understanding
   - Explain the inefficiency clearly
   - Transition to optimized solution naturally
   - Show you can improve based on constraints
   - Discuss trade-offs: time vs space
   - This demonstrates maturity in problem-solving approach

9. **Key Learning Points**:
   - Recognize when nested loops create quadratic complexity
   - Understand the need for data structures to optimize
   - Learn to balance time and space trade-offs
   - Develop habit of optimizing after initial solution works
   - Practice communicating complexity analysis clearly

This naive approach is intentionally included alongside the optimized solution to show the
evolution of thinking. In interviews, always mention the brute force first, explain why it's
suboptimal, then present the better solution. This demonstrates problem-solving maturity.
"""

from typing import List


def two_sum_naive(nums: List[int], target: int) -> List[int]:
    """
    Brute-force solution: check all pairs.
    Time complexity: O(n^2) - checking all possible pairs.
    Space complexity: O(1) - no extra data structure needed.

    Note: This approach is straightforward but inefficient for large arrays.
    See two_sum.py for the optimized O(n) hash map solution.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
