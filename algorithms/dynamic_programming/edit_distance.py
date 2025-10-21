"""
Edit Distance (Levenshtein Distance) Algorithm Explained Step-by-Step
---------------------------------------------------------------------
The Edit Distance problem, also known as Levenshtein Distance, is a classic string algorithm that computes
the minimum number of operations required to transform one string into another. The allowed operations are:
insert a character, delete a character, or replace a character. This problem demonstrates dynamic programming
for string manipulation and is fundamental for spell checkers, DNA sequence alignment, and version control.

Here is how the process works:

1. **Base Cases**: Initialize the DP table boundaries.
   - dp[i][0] = i (delete all i characters from word1 to get empty string)
   - dp[0][j] = j (insert all j characters to get word2 from empty string)
   - These represent the cost of transforming from/to empty strings

2. **Character Match**: If characters at current positions are the same, no operation needed.
   - When word1[i-1] == word2[j-1]
   - dp[i][j] = dp[i-1][j-1] (inherit cost from diagonal without adding operation)
   - No additional cost since characters already match

3. **Character Mismatch**: Choose the minimum cost among three operations.
   - Delete: dp[i-1][j] + 1 (remove character from word1)
   - Insert: dp[i][j-1] + 1 (add character to word1)
   - Replace: dp[i-1][j-1] + 1 (substitute character in word1)
   - Take minimum of all three options and add 1 for the operation cost

4. **DP Table Construction**: Build a 2D table where dp[i][j] represents minimum operations.
   - Rows represent prefixes of word1 (0 to m)
   - Columns represent prefixes of word2 (0 to n)
   - Each cell [i][j] shows min operations to transform word1[0:i] to word2[0:j]

5. **Bottom-Up Approach**: Fill the table row by row, left to right.
   - Start from dp[1][1] after initializing base cases
   - Each cell depends on three previously computed cells (left, top, diagonal)
   - Build solution incrementally using optimal substructure

6. **Final Result**: The answer is stored in dp[m][n].
   - Represents minimum operations to transform entire word1 to word2
   - This cell contains the optimal solution for the complete problem
   - Return this value as the edit distance between the two strings

Example: word1 = "cat", word2 = "dog"
- Operations: replace 'c'→'d', replace 'a'→'o', replace 't'→'g'
- Process: Build 4x4 DP table, fill based on character comparisons and operation costs
- Result: 3 operations needed

Time Complexity: O(m * n) where m = len(word1), n = len(word2)
Space Complexity: O(m * n) for the DP table
Optimized Space: O(min(m, n)) using only two rows instead of full table

This algorithm demonstrates dynamic programming for string problems and is essential for
understanding sequence alignment, approximate string matching, and text similarity metrics.
"""

from functools import lru_cache


def edit_distance(word1: str, word2: str) -> int:
    """
    Computes the minimum number of operations required to convert word1 to word2.
    Allowed operations: insert, delete, replace.
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # insert all characters

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # delete
                    dp[i][j - 1],  # insert
                    dp[i - 1][j - 1],  # replace
                )

    return dp[m][n]


def edit_distance_memo(word1: str, word2: str) -> int:
    """
    Top-down memoized recursive solution to compute the minimum edit distance.
    """

    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> int:
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        if word1[i] == word2[j]:
            return dp(i + 1, j + 1)
        return 1 + min(
            dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1)  # delete  # insert  # replace
        )

    return dp(0, 0)
