"""
Permutation Sequence (Brute Force) Algorithm Explained Step-by-Step
------------------------------------------------------------------
This is the naive brute-force approach to solve the Permutation Sequence problem.
Instead of using the factorial number system to directly calculate the kth permutation,
this solution generates all n! permutations and then returns the kth one.
While simple and easy to understand, this approach is inefficient for large n values
and is not suitable for interview settings where optimization is expected.
However, understanding this approach provides a baseline for comparison and helps
clarify what the problem is asking for.

Here is how the process works:

1. **Generate All Permutations**:
   - Use itertools.permutations() to generate all possible permutations of [1..n]
   - itertools generates permutations in lexicographic order
   - Total number of permutations generated: n! (factorial of n)
   - Example: for n=3, generates 6 permutations: (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)

2. **Iterate Through Permutations**:
   - Use enumerate() with start=1 to track which permutation we're on (1-indexed)
   - Iterate through all generated permutations sequentially
   - Compare current iteration number with target k
   - Stop iteration as soon as the kth permutation is found

3. **Extract and Format Result**:
   - When i == k, convert the tuple of digits to a string
   - Use map(str, perm) to convert each integer to string
   - Join all string digits together with "".join()
   - Return the resulting kth permutation string

4. **Edge Cases**:
   - If k is out of range (k > n!), function returns empty string
   - Although in typical interview problems, k is guaranteed to be valid
   - The range of valid k is 1 to n! (inclusive)

Example Walkthrough: n=3, k=3 (3rd permutation)
- Generate all permutations: (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)
- Iterate: i=1 (1,2,3), i=2 (1,3,2), i=3 (2,1,3) ← match found
- Convert: map(str, (2,1,3)) → ["2", "1", "3"]
- Join: "".join(...) → "213"
- Result: "213" (the 3rd permutation in lexicographic order)

Time Complexity: O(n! * n)
- Generate all n! permutations: O(n!) time
- Each permutation conversion to string: O(n) time
- Total: O(n! * n) for worst case (when k = n!)

Space Complexity: O(n! * n)
- Store all n! permutations in memory
- Each permutation is a tuple of size n
- Not practical for n > 10 or so

Comparison with Optimized Approach:
- Naive: O(n! * n) time, O(n! * n) space
- Optimized: O(n²) time, O(n) space
- For n=13: Naive generates 6.2 billion permutations; Optimized finds answer directly

Key Insights:
- This approach is a brute-force baseline and should NOT be used in interviews
- Demonstrates why optimization is important: factorial growth is extremely steep
- Shows the value of mathematical approaches over brute force
- Useful for testing/validating correctness of optimized solutions
- Good for understanding the problem clearly before implementing optimal solution

When to Use:
- Testing and validation of optimized algorithms
- Small input values (n < 8) where performance doesn't matter
- Educational purposes to understand the problem first
- Generating test cases for correctness verification

When NOT to Use:
- Interview settings (will fail on large inputs)
- Production code with reasonable n values
- When you need to optimize time/space complexity
- When constraints allow n up to 13 (as in typical LeetCode constraints)

This comparison highlights why the factorial number system approach (optimized version)
is essential knowledge for senior-level interview preparation.
"""

import itertools


def get_permutation_naive(n: int, k: int) -> str:
    """
    Brute-force approach: generate all permutations using itertools,
    then return the kth one.
    """
    perms = itertools.permutations(range(1, n + 1))
    for i, perm in enumerate(perms, start=1):
        if i == k:
            return "".join(map(str, perm))
    return ""
