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
