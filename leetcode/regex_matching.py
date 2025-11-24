"""
Regular Expression Matching (Dynamic Programming) — Explanation and Interview Notes
-------------------------------------------------------------------------------
Problem: Implement regular expression matching where '.' matches any single character
and '*' matches zero or more of the preceding element. This is a classic DP problem
that tests understanding of pattern semantics, state definition, and table transitions.

Here is how the process works:

1. Pattern semantics
   - '.' matches any single character.
   - '*' applies to the immediately preceding element and means "zero or more" of that element.
   - Important: '*' is not a standalone character and must be interpreted together with its preceding token.

2. State definition (DP table)
   - Define dp[i][j] as whether s[:i] (first i chars of s) matches p[:j] (first j chars of p).
   - Use lengths m = len(s), n = len(p) and construct a (m+1) x (n+1) boolean table.

3. Base cases
   - dp[0][0] = True (empty pattern matches empty string).
   - dp[i][0] = False for i > 0 (non-empty string cannot match empty pattern).
   - dp[0][j] can be True when pattern can represent an empty string, e.g., "a*", "a*b*".
     Handle these by checking occurrences of '*' and whether they can be skipped: dp[0][j] = dp[0][j-2] when p[j-1] == '*'.

4. Transition rules
   - If p[j-1] == s[i-1] or p[j-1] == '.': dp[i][j] = dp[i-1][j-1] (match consumes one char).
   - If p[j-1] == '*': two possibilities
       a) Treat '*' as zero occurrences of the preceding element: dp[i][j] = dp[i][j-2]
       b) Treat '*' as one or more occurrences: if p[j-2] matches s[i-1] (or p[j-2] == '.') then dp[i][j] |= dp[i-1][j]
   - Always be careful to check indices; '*' logic requires j >= 2.

5. Fill order
   - Initialize base row and column, then fill the table for i from 1..m and j from 1..n.
   - Each cell depends on left, top, and diagonal cells already computed.

6. Edge cases and notes
   - Patterns like "*a" are invalid by usual problem constraints; implementations assume valid patterns
     where '*' is not the first character or is properly paired.
   - Watch empty string matching with patterns containing repeated "x*" groups.

7. Complexity
   - Time: O(m * n) where m = len(s) and n = len(p).
   - Space: O(m * n) for the full DP table. Can be optimized to O(n) using rolling rows.

8. Example (brief)
   - s = "aab", p = "c*a*b"
     Explanation: c* -> zero 'c's, a* -> two 'a's, then 'b' matches 'b' => full match.

Return: dp[m][n] is True when the full string matches the full pattern.
"""

def is_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c* that can match empty string
    for j in range(2, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == "*":
                # zero occurrence of preceding char
                dp[i][j] = dp[i][j - 2]
                # one or more occurrence
                if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[m][n]
