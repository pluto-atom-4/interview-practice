"""
Merge Intervals (Optimal Greedy Solution) - Algorithm Explained Step-by-Step
=============================================================================
The Merge Intervals problem is a classic interval manipulation problem that combines intervals that overlap.
Given a list of intervals, merge all overlapping intervals and return a list of non-overlapping intervals.
This problem is fundamental for understanding greedy algorithms, interval scheduling, and is frequently
asked in technical interviews to assess problem-solving skills and algorithm optimization ability.

Here is how the process works:

1. **Problem Understanding**: Given a list of intervals [start, end], merge overlapping ones.
   - Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
   - Example: [[1,4],[4,5]] → [[1,5]] (touching intervals also merge)
   - Key insight: Two intervals [a,b] and [c,d] overlap if c ≤ b (when sorted by start)

2. **Key Insight - Sorting**: The crucial observation that enables the greedy approach.
   - If we sort intervals by start time, we can process them left to right
   - After sorting, overlapping intervals will be adjacent or nearby
   - This ordering allows single-pass greedy merging without complex comparisons
   - Sorting enables linear-time merging instead of checking all pairs

3. **Greedy Approach**: Merge as we iterate through sorted intervals.
   - Sort intervals by start position: O(n log n)
   - Initialize merged list with first interval
   - For each subsequent interval:
     - If it overlaps with the last interval in merged: extend the end
     - If it doesn't overlap: add it as a new interval
   - Time Complexity: O(n log n) dominated by sorting
   - Space Complexity: O(1) if not counting output, O(n) for output

4. **Overlap Detection**: Determine when two intervals overlap.
   - Current interval [c, d] overlaps with previous [a, b] if: c ≤ b
   - This works because array is sorted by start time (c ≥ a guaranteed)
   - Non-overlapping case: c > b (current starts after previous ends)
   - Touching case: c = b (intervals touch at one point, considered overlapping)

5. **Merging Process**: Combine overlapping intervals efficiently.
   - When overlap found: extend end of previous interval
   - New end = max(prev_end, current_end) (handles nested intervals)
   - Example: merge [1,3] and [2,6] → [1, max(3,6)] = [1,6]
   - Example: merge [1,6] and [4,5] → [1, max(6,5)] = [1,6] (nested case)

6. **Algorithm Steps**:
   Step 1: Handle edge case - if intervals is empty, return empty list
   Step 2: Sort intervals by start time using key=lambda x: x[0]
   Step 3: Initialize merged list with the first interval: merged = [intervals[0]]
   Step 4: Iterate through remaining intervals starting from index 1
   Step 5: Get previous interval (last item in merged): prev = merged[-1]
   Step 6: Check overlap condition: if current[0] <= prev[1]
   Step 7: If overlapping: extend previous interval end = max(prev[1], current[1])
   Step 8: If not overlapping: append current interval to merged list
   Step 9: Return the merged list of non-overlapping intervals

7. **Example Walkthrough** with [[1,3],[2,6],[8,10],[15,18]]:
   - Sorted: [[1,3],[2,6],[8,10],[15,18]] (already sorted by start)
   - merged = [[1,3]]
   - [2,6]: 2 ≤ 3? Yes! Merge: [1, max(3,6)] = [1,6] → merged = [[1,6]]
   - [8,10]: 8 ≤ 6? No! Add: merged = [[1,6], [8,10]]
   - [15,18]: 15 ≤ 10? No! Add: merged = [[1,6], [8,10], [15,18]]
   - Result: [[1,6], [8,10], [15,18]] ✓

8. **Key Insights for Interviews**:
   - **Sorting Strategy**: Key to unlocking efficient solution
   - **Greedy Works**: Once sorted, greedy choice is always optimal
   - **Single Pass**: After sorting, one pass through intervals is sufficient
   - **Overlap Definition**: Understanding c ≤ b condition is critical
   - **Max Function**: Handle nested intervals correctly with max()
   - **Why Efficient**: O(n log n) is much better than O(n²) checking all pairs

9. **Why This Approach is Optimal**:
   - Cannot avoid sorting: any correct solution requires knowing interval relationships
   - Greedy is optimal: after sorting, merging adjacent overlaps always works
   - Single pass: process each interval only once after sorting
   - Space efficient: modify in-place possible, only output array needed

10. **Common Follow-ups and Variations**:
    - Insert interval into list of merged intervals
    - Remove overlapping intervals (keep maximum)
    - Find conflicting appointments
    - Interval scheduling maximization
    - Minimum number of rooms needed (calendar)
    - Find gaps between intervals
    - Interval list intersection
    - Work scheduling with constraints

This algorithm demonstrates the power of sorting combined with greedy strategies, making it
essential for understanding interval-based problems and optimization techniques crucial in
technical interviews. The key lesson: always consider sorting as a problem-solving tool!

Time Complexity: O(n log n) - dominated by sorting, merging is O(n)
Space Complexity: O(1) excluding output, O(n) for output array
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.
    Sort intervals by start time, then merge greedily.
    Time: O(n log n), Space: O(1) excluding output
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        prev = merged[-1]
        if current[0] <= prev[1]:
            # Overlap: merge
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)

    return merged
