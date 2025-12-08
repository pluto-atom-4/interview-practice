"""
Merge Intervals (Brute Force Approach) - Algorithm Explained Step-by-Step
==========================================================================
The brute force approach to the Merge Intervals problem demonstrates the initial, straightforward
thinking before optimization. While not optimal due to O(n²) time complexity, understanding this
approach is valuable because:
1. It shows the starting point before discovering sorting optimization
2. It helps explain WHY we need better solutions
3. It demonstrates naive interval comparison logic
4. It helps interviewers see your problem-solving progression

This serves as a baseline to compare against the optimized O(n log n) sorted greedy solution.

Here is how the naive algorithm works:

1. **Problem Understanding**: Given a list of intervals [start, end], merge overlapping ones.
   - Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
   - Example: [[1,4],[4,5]] → [[1,5]] (touching intervals also merge)
   - Two intervals [a,b] and [c,d] overlap if NOT (b < c or a > d)

2. **Brute Force Approach**: Repeatedly check and merge all overlapping intervals.
   - Use a while loop with changed flag to track if any merges occurred
   - Each iteration: check all pairs and merge any overlapping ones
   - Continue until no more merges possible (entire array scanned with no changes)
   - Time Complexity: O(n²) per iteration, multiple iterations → O(n³) or worse
   - Space Complexity: O(n) for storing intervals
   - Limitation: Inefficient for large input sets, needs repeated passes

3. **Overlap Detection Logic**: Check if two intervals overlap.
   - Two intervals [a,b] and [c,d] overlap if: NOT (b < c OR a > d)
   - Equivalent to: b >= c AND a <= d
   - Example: [1,3] and [2,6] overlap because 3 >= 2 AND 1 <= 6 ✓
   - Example: [1,3] and [5,7] don't overlap because 3 < 5 ✓

4. **Merging Process**: Combine overlapping intervals.
   - When overlap found: merge into one interval
   - New interval: [min(a,c), max(b,d)]
   - Remove the second interval from list
   - Update the position in the list

5. **Algorithm Steps**:
   Step 1: Make a copy of input intervals to work with
   Step 2: Set changed flag to True to enter the while loop
   Step 3: While changed is True (merges are still happening):
   Step 4: Set changed to False at start of iteration
   Step 5: Iterate through intervals popping from the list
   Step 6: For each current interval, check all remaining intervals
   Step 7: If overlap found with another interval, merge them
   Step 8: Set changed to True and continue to next current interval
   Step 9: If no overlap found, add current to new_intervals list
   Step 10: Replace merged with new_intervals for next iteration
   Step 11: Return merged list when no more changes occur

6. **Example Walkthrough** with [[1,3],[2,6],[8,10]]:
   Iteration 1:
   - merged = [[1,3],[2,6],[8,10]], changed = False
   - Pop [8,10]: check against [1,3] → no overlap → new_intervals = [[8,10]]
   - Pop [2,6]: check against [1,3] → overlap! merge [1,max(3,6)]=[1,6]
   - Set changed = True, merged = [[1,6]]
   - Pop [1,6]: no more to check → new_intervals = [[8,10], [1,6]]
   - merged = [[8,10], [1,6]], changed = True

   Iteration 2:
   - Pop [1,6]: check against [8,10] → no overlap → new_intervals = [[1,6]]
   - Pop [8,10]: no more to check → new_intervals = [[1,6], [8,10]]
   - merged = [[1,6], [8,10]], changed = False → exit loop
   - Result: [[1,6], [8,10]] ✓

7. **Why This Approach is NOT Optimal**:
   - Multiple Passes: Needs to repeat until convergence
   - Quadratic Comparisons: Each iteration checks O(n²) pairs
   - No Ordering: Lacks structure, can't leverage sorting insight
   - Inefficient for Large Inputs: Becomes prohibitively slow for n > 100
   - Redundant Work: May check same pairs multiple times

8. **Comparison: Naive vs Optimized**:

   Naive (Brute Force):
   - Time: O(n³) worst case or O(n² × iterations)
   - Space: O(n) for storing intervals
   - Simple: Easy to understand and implement

   Optimized (Sort + Greedy):
   - Time: O(n log n) - sort dominates
   - Space: O(1) excluding output
   - Scalable: Works efficiently for large inputs

9. **When to Use Naive Approach**:
   - Array size is very small (< 20 elements)
   - Interview context: Always mention as "brute force starting point"
   - Correctness is more important than efficiency
   - Learning: Understand problem deeply before optimization
   - Never in production: Too slow for real-world use

10. **Interview Strategy**:
    - Start with naive approach to show understanding
    - Explain the inefficiency: repeated passes, O(n²) comparisons
    - Transition to optimized solution: sorting enables single pass
    - Show you can improve based on analysis
    - Discuss trade-offs and optimization insights
    - This demonstrates mature problem-solving approach

This naive approach is intentionally included alongside the optimized solution to show the
evolution of thinking. In interviews, always mention the brute force first, explain why it's
suboptimal, then present the better solution. This demonstrates problem-solving maturity and
understanding of algorithm optimization.

Time Complexity: O(n²) per iteration × O(n) iterations = O(n³) worst case
Space Complexity: O(n) for storing intervals
"""

from typing import List


def merge_naive(intervals: List[List[int]]) -> List[List[int]]:
    """
    Naive solution: repeatedly merge overlapping intervals until no more merges occur.
    Time complexity: O(n²) to O(n³) depending on overlap pattern.
    Space complexity: O(n) for storing intervals.
    """
    if not intervals:
        return []

    merged = intervals[:]
    changed = True
    while changed:
        changed = False
        new_intervals = []
        while merged:
            current = merged.pop()
            overlap_found = False
            for i, other in enumerate(merged):
                if not (current[1] < other[0] or current[0] > other[1]):
                    # Merge
                    merged[i] = [min(current[0], other[0]), max(current[1], other[1])]
                    overlap_found = True
                    changed = True
                    break
            if not overlap_found:
                new_intervals.append(current)
        merged = new_intervals
    return merged
