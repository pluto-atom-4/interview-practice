"""
Fibonacci Algorithm Explained Step-by-Step
-----------------------------------------
The Fibonacci sequence is a classic recursive problem where each number is the sum of the two preceding ones.

Here is how the process works:

1. **Base Cases**:
   - If n <= 0, return 0 (by convention)
   - If n == 1, return 1 (first Fibonacci number)

2. **Recursive Case**:
   - For any n > 1: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
   - This breaks the problem into smaller subproblems

3. **Optimization with Memoization**:
   - Use @lru_cache to store previously computed results
   - Prevents redundant calculations and improves performance dramatically
   - Without memoization: O(2^n) time complexity
   - With memoization: O(n) time complexity

Key Interview Points:
- Demonstrates understanding of recursion and dynamic programming
- Shows optimization techniques (memoization)
- Classic example of how caching can transform exponential to linear time
- Often used to discuss trade-offs between time and space complexity

Time Complexity: O(n) with memoization, O(2^n) without
Space Complexity: O(n) for the cache and call stack

This problem is frequently asked in interviews to test recursive thinking and optimization skills.
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage
if __name__ == "__main__":
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
