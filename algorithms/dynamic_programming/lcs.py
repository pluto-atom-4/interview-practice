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
