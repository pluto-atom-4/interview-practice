"""
Regular Expression Matching (Recursive + Memoization) — Explanation and Interview Notes
--------------------------------------------------------------------------------------
Problem: Implement regex matching where '.' matches any single character and '*' matches
zero or more of the preceding element. The recursive solution uses backtracking with memoization
to avoid redundant computations.

Here is how the process works:

1. Recursion state
   - Define dfs(i, j) to mean: does s[i:] match p[j:]? (i and j are current indices into s and p)
   - The goal is dfs(0, 0).

2. Base case
   - If j == len(p): pattern exhausted -> return i == len(s) (only True if string also exhausted).

3. First-match check
   - first_match = (i < len(s)) and (p[j] == s[i] or p[j] == '.')
   - This determines whether the current characters align and whether recursion can advance.

4. Handling '*'
   - If the next pattern character (j+1) exists and is '*', there are two possibilities:
       a) Skip the 'x*' construct entirely: dfs(i, j+2) (zero occurrences)
       b) If first_match: consume one character from s and stay on the same pattern (dfs(i+1, j))
          because '*' can match multiple occurrences.
   - Combine with logical OR to accept either path.

5. No '*'
   - If there's no '*' following, the result is first_match and dfs(i+1, j+1).

6. Memoization
   - Use caching (lru_cache or explicit dict) to store results for (i, j) to prevent exponential blow-up.
   - With memoization the recurrence has at most O(m * n) unique states.

7. Complexity
   - Time: O(m * n) due to memoization (m = len(s), n = len(p)).
   - Space: O(m * n) for recursion stack + memo table in the worst case.

8. Practical notes for interviews
   - The recursive solution is natural to explain (state, choices, memo). Discuss base cases and
     the two behaviors of '*' (zero vs many).
   - Show how memoization converts exponential naive recursion into polynomial time by eliminating
     repeated subproblems.

Return: dfs(0, 0) indicates whether the full string matches the full pattern.
"""

from functools import lru_cache


def is_match_recursive(s: str, p: str) -> bool:
    @lru_cache(None)
    def dfs(i, j):
        if j == len(p):
            return i == len(s)

        first_match = i < len(s) and (p[j] in {s[i], "."})

        if j + 1 < len(p) and p[j + 1] == "*":
            # Case 1: skip "x*" (zero occurrence)
            # Case 2: use "x*" if first_match
            return dfs(i, j + 2) or (first_match and dfs(i + 1, j))
        else:
            return first_match and dfs(i + 1, j + 1)

    return dfs(0, 0)
