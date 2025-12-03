"""
Permutations II (Unique Permutations) Algorithm Explained Step-by-Step
-----------------------------------------------------------------------
The Permutations II problem asks to generate all unique permutations of a list containing duplicate elements.
Unlike the standard permutations problem where all elements are distinct, this problem requires handling duplicates
to avoid generating the same permutation multiple times. This is a classic backtracking problem that demonstrates
constraint satisfaction, pruning strategies, and handling duplicate values in combinatorial problems.

Here is how the process works:

1. **Sorting for Duplicate Handling**: Sort the input array first.
   - When array is sorted, duplicate elements become adjacent
   - Allows us to identify and skip duplicate choices efficiently
   - Example: [1, 1, 2] instead of [1, 2, 1] makes duplicates obvious

2. **Backtracking Framework**: Use recursive backtracking to explore permutations.
   - Maintain a 'path' list to build current permutation
   - Maintain a 'used' boolean array to track which elements are in current path
   - Base case: when path length equals nums length, add permutation to results
   - Recursive case: try adding each unused element to path

3. **Duplicate Skipping Strategy**: The key to handling duplicates.
   - Check condition: if i > 0 and nums[i] == nums[i-1] and not used[i-1]
   - This ensures we only use duplicate at position i if the previous duplicate at i-1 is already used
   - Prevents multiple identical permutations from being generated
   - Example: for [1, 1, 2], use second 1 only after first 1 is in the path

4. **Used Array Tracking**: Track which elements are currently in the permutation.
   - Before recursing: mark element as used and add to path
   - After recursing: unmark element (backtrack) and remove from path
   - Allows reusing elements in different branches of recursion tree

5. **Recursion Tree Exploration**: Systematically explore all valid branches.
   - For each position in permutation, try all available unused elements
   - Skip elements that would create duplicate permutations (via duplicate check)
   - When permutation is complete, save a copy to results
   - Continue exploring other branches through backtracking

6. **Result Collection**: Collect all unique permutations.
   - Use results list to store all valid permutations
   - Append a copy of path (path[:]) to avoid reference issues
   - Each unique permutation appears exactly once in results

Example: nums = [1, 1, 2]
- Sort: [1, 1, 2]
- Permutations generated:
  * [1, 1, 2]: use first 1, then second 1, then 2
  * [1, 2, 1]: use first 1, then 2, then second 1
  * [2, 1, 1]: use 2, then first 1, then second 1
- Total: 3 unique permutations (not 6, which would include duplicates)

Time Complexity: O(n! * n) where n = len(nums)
  - Generate n! permutations in worst case (all elements distinct)
  - Each permutation takes O(n) to copy/append
  - Duplicate skipping reduces actual permutations when duplicates exist

Space Complexity: O(n! * n) for storing all permutations plus O(n) for recursion stack
  - Output space: O(n! * n) to store results
  - Recursion stack depth: O(n) for backtracking
  - Used array: O(n) for tracking

Optimized Space: Cannot reduce output space as we must return all permutations

This algorithm demonstrates key backtracking techniques: recursive exploration, constraint satisfaction,
pruning strategies (duplicate skipping), and state management (used array). Essential for understanding
combinatorial problems, constraint programming, and optimization in coding interviews.
"""

from typing import List


def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of nums using backtracking.
    Handles duplicates by sorting and skipping repeated choices.
    """
    nums.sort()
    results = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            results.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            # Skip duplicates: if same number as previous and previous not used
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return results
