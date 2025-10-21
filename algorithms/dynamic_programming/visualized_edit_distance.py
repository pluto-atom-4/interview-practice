from typing import List, Tuple

import matplotlib.pyplot as plt
from tabulate import tabulate


def visualize_edit_operations(word1: str, word2: str) -> List[Tuple[str, str]]:
    """
    Returns a list of operations to convert word1 to word2.
    Each operation is a tuple: (operation_type, description)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # delete
                    dp[i][j - 1],    # insert
                    dp[i - 1][j - 1] # replace
                )

    # Backtrack to find operations
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i - 1] == word2[j - 1]:
            operations.append(("match", f"Keep '{word1[i - 1]}'"))
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(("replace", f"Replace '{word1[i - 1]}' with '{word2[j - 1]}'"))
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            operations.append(("insert", f"Insert '{word2[j - 1]}'"))
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(("delete", f"Delete '{word1[i - 1]}'"))
            i -= 1

    operations.reverse()

    # Print table
    print(tabulate([[op[0], op[1]] for op in operations], headers=["Operation", "Description"], tablefmt="grid"))

    # Optional: visualize with matplotlib
    labels = [f"{op[0].capitalize()}: {op[1]}" for op in operations]
    colors = {
        "match": "lightgreen",
        "replace": "orange",
        "insert": "skyblue",
        "delete": "salmon"
    }
    bar_colors = [colors[op[0]] for op in operations]

    plt.figure(figsize=(12, 2))
    plt.barh(range(len(labels)), [1]*len(labels), color=bar_colors)
    plt.yticks(range(len(labels)), labels)
    plt.title(f"Edit Operations to Convert '{word1}' → '{word2}'")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

    return operations
