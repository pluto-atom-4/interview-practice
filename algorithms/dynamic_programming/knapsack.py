"""
0/1 Knapsack Problem Algorithm Explained Step-by-Step
---------------------------------------------------------------
The 0/1 Knapsack problem is a classic optimization problem where you have a knapsack with a weight capacity
and a set of items, each with a weight and value. The goal is to select items to maximize total value
without exceeding the capacity. Each item can be taken (1) or left (0), hence "0/1 Knapsack".

Here is how the process works:

1. **Base Case**: If no items remain or capacity is 0, return 0.
   - When i == n (no more items to consider)
   - When remaining capacity == 0 (knapsack is full)
   - The maximum value is 0

2. **Item Too Heavy**: If current item's weight exceeds remaining capacity, skip it.
   - When weights[i] > remaining capacity
   - Move to next item: dp(i + 1, remaining)
   - Cannot include this item in the solution

3. **Decision Point**: Choose the maximum between two options.
   - Option 1: Skip the item → dp(i + 1, remaining)
   - Option 2: Take the item → values[i] + dp(i + 1, remaining - weights[i])
   - Return the maximum of both options to get optimal value

4. **DP Table (Bottom-Up)**: Build a 2D table where dp[i][w] represents maximum value.
   - Rows represent items (0 to n)
   - Columns represent capacity (0 to capacity)
   - Each cell [i][w] shows the max value using first i items with capacity w

5. **Backtracking**: Trace back through the DP table to find selected items.
   - Start from dp[n][capacity]
   - If dp[i][w] != dp[i-1][w], item i-1 was selected
   - Subtract the item's weight and continue backtracking

6. **Memoization (Top-Down)**: Use @lru_cache to store results of subproblems.
   - Prevents recalculating the same (i, remaining) pair multiple times
   - Converts exponential time to polynomial time

Example: weights = [2, 3, 4], values = [3, 4, 5], capacity = 5
- Optimal selection: items 0 and 1 (weights: 2+3=5, values: 3+4=7)
- Process: Consider each item, decide to take or skip based on value/weight ratio

Time Complexity:
- Bottom-Up: O(n * capacity) where n = number of items
- Top-Down Memoized: O(n * capacity)
- Space Complexity: O(n * capacity) for DP table or memoization cache

This algorithm demonstrates dynamic programming for optimization problems and is a fundamental
interview question for understanding resource allocation and decision-making strategies.
"""

from functools import lru_cache
from typing import List, Tuple

import matplotlib.pyplot as plt


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Bottom-up DP solution to the 0/1 Knapsack problem.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_memo(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Top-down memoized recursive solution to the 0/1 Knapsack problem.
    """
    n = len(weights)

    @lru_cache(maxsize=None)
    def dp(i: int, remaining: int) -> int:
        if i == n or remaining == 0:
            return 0
        if weights[i] > remaining:
            return dp(i + 1, remaining)
        return max(dp(i + 1, remaining), values[i] + dp(i + 1, remaining - weights[i]))

    return dp(0, capacity)


def knapsack_with_items(
    weights: List[int], values: List[int], capacity: int
) -> Tuple[int, List[int]]:
    """
    Solves the 0/1 Knapsack problem and returns:
    - the maximum value
    - the list of selected item indices
    Also visualizes the selected items using matplotlib.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]
    selected.reverse()

    # Visualization
    item_labels = [f"Item {i}\n(w={weights[i]}, v={values[i]})" for i in range(n)]
    item_values = values
    colors = ["skyblue" if i in selected else "lightgray" for i in range(n)]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(item_labels, item_values, color=colors)
    for i in selected:
        bars[i].set_edgecolor("blue")
        bars[i].set_linewidth(2)
    plt.title(f"Knapsack Selection (Max Value = {dp[n][capacity]})")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return dp[n][capacity], selected
