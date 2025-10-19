"""
Longest Common Subsequence (LCS) Algorithm Explained Step-by-Step
---------------------------------------------------------------
The Longest Common Subsequence finds the longest sequence of characters that appear in the same order
in both strings, but not necessarily consecutively.

Here is how the process works:

1. **Base Case**: If either string is exhausted (reached the end), return 0.
   - When i == len(text1) or j == len(text2), there are no more characters to compare
   - The LCS length is 0

2. **Characters Match**: If text1[i] == text2[j], include this character in the LCS.
   - Add 1 to the result
   - Move both pointers forward: dp(i + 1, j + 1)
   - This character is part of the common subsequence

3. **Characters Don't Match**: Try both possibilities and take the maximum.
   - Option 1: Skip current character in text1 → dp(i + 1, j)
   - Option 2: Skip current character in text2 → dp(i, j + 1)
   - Return the maximum of both options

4. **Memoization**: Use @lru_cache to store results of subproblems.
   - Prevents recalculating the same (i, j) pair multiple times
   - Converts exponential time to polynomial time

5. **Visualization**: Build a 2D table to show how the algorithm fills in values.
   - Rows represent characters in text1
   - Columns represent characters in text2
   - Each cell [i][j] shows the LCS length up to those positions

Example: text1 = "ABCD", text2 = "ACBD"
- LCS = "ABD" (length 3)
- Process: A matches → B matches → C skipped → D matches

Time Complexity:
- Memoized: O(m * n) where m = len(text1), n = len(text2)
- Space Complexity: O(m * n) for memoization cache

This algorithm demonstrates dynamic programming principles and is a classic interview question
for understanding optimization through memoization and table-based approaches.
"""

from functools import lru_cache

import matplotlib.pyplot as plt
import seaborn as sns


def longest_common_subsequence_memo(text1: str, text2: str) -> int:
    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + dp(i + 1, j + 1)
        else:
            return max(dp(i + 1, j), dp(i, j + 1))

    return dp(0, 0)


def visualize_lcs_table(text1: str, text2: str):
    m, n = len(text1), len(text2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if text1[i] == text2[j]:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        table,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=[""] + list(text2),
        yticklabels=[""] + list(text1),
    )
    plt.title("LCS DP Table")
    plt.xlabel("Text2")
    plt.ylabel("Text1")
    plt.tight_layout()
    plt.show()
