from __future__ import annotations

from typing import Dict

"""
## Problem Statement

Given n stairs, find the number of distinct ways to climb them when you can take either 1 or 2 steps 
at a time. This tests understanding of dynamic programming, recurrence relations, and space optimization.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Space-Optimized Dynamic Programming**:

Recognize the Fibonacci-like structure: the number of ways to reach stair n depends only on the previous 
two states. Rather than storing all intermediate results, we track only the last two values and update 
them iteratively, reducing space from O(n) to O(1).

* Key Concepts:

  - Why recognize the DP recurrence relation?
The problem has overlapping subproblems (ways(n) depends on ways(n-1) and ways(n-2)), making it ideal 
for DP. Understanding that this follows a Fibonacci pattern is crucial for optimization.

  - Why use only two variables instead of an array?
We only need the immediately previous two values to compute the current result. By maintaining prev2 
(n-2) and prev1 (n-1), we eliminate the need for O(n) storage while preserving correctness.

* Logic:

1. Handle base cases: n ≤ 0 returns 0, n=1 returns 1, n=2 returns 2
2. Initialize prev2=1 (ways for stair 1) and prev1=2 (ways for stair 2)
3. Iterate from stair 3 to n: compute current ways as prev1 + prev2
4. Slide the window: shift prev1 to prev2, current to prev1
5. Return prev1 as the result for n stairs

* **30-Second Pitch**:

I'm using space-optimized dynamic programming. The key insight is that the number of ways to reach 
stair n equals the sum of ways to reach stairs n-1 and n-2—a Fibonacci recurrence. Instead of storing 
all values, I keep only the last two values and update them iteratively, achieving O(n) time and O(1) space.

* **Rapid-Fire Version**:

- Classic DP recurrence: ways[n] = ways[n-1] + ways[n-2]
- Space optimization: only track last two values
- Rolling window approach: prev2, prev1 → update iteratively
- Result slides down as we progress through stairs

* **Ultra-Minimal One-Liner**:

- Space-optimized DP using rolling window to compute Fibonacci-like stair combinations in O(n) time, O(1) space.

* **Complexity Analysis**:

- **Time Complexity:** O(n) — single pass from stair 3 to n
- **Space Complexity:** O(1) — only two variables regardless of n
"""

def climb_stairs(n: int) -> int:
    """
    Return the number of distinct ways to climb n stairs
    when you can take either 1 or 2 steps at a time.

    This is the classic DP recurrence:
        ways[n] = ways[n-1] + ways[n-2]

    Time:  O(n)
    Space: O(1)

    Example:
        climb_stairs(5) -> 8

    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev2, prev1 = 1, 2  # ways for n-2 and n-1

    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1
