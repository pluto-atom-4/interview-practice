"""
Permutations II using Itertools - Alternative Approach Explained
-----------------------------------------------------------------
This is an alternative, more Pythonic approach to generating unique permutations using Python's built-in
itertools.permutations function combined with set deduplication. While less efficient than the backtracking
approach with pruning, it demonstrates how to leverage standard library functions and is useful for
understanding different problem-solving paradigms. This approach trades efficiency for simplicity and
readability, making it suitable for quick prototyping or smaller inputs.

Here is how the process works:

1. **Generate All Permutations**: Use itertools.permutations to generate all permutations.
   - itertools.permutations(nums) generates every possible ordering of elements
   - Time complexity of generation: O(n! * n) - generates all n! permutations
   - Does not consider duplicates in the input, so duplicates create duplicate permutations
   - Example: permutations([1, 1, 2]) generates 6 permutations (treating 1's as distinct)

2. **Deduplicate with Set**: Convert permutations to a set to remove duplicates.
   - Each permutation is a tuple, which is hashable and can be added to set
   - Set automatically removes duplicate tuples (duplicate permutations)
   - O(n!) set operations to add all generated permutations
   - For array with many duplicates, this removes significant redundancy
   - Example: {(1,1,2), (1,2,1), (2,1,1)} - duplicates eliminated

3. **Convert Back to Lists**: Transform result from set of tuples to list of lists.
   - Convert each tuple permutation back to a list for standard output format
   - List comprehension: [list(p) for p in perms]
   - O(n!) conversion operations, each taking O(n) to create list
   - Returns results in the expected format for compatibility

Comparison with Backtracking Approach:
- **Itertools Approach**:
  * Simpler code (2 lines vs 15+ lines)
  * Easier to understand and less error-prone
  * Generates all n! permutations then deduplicates
  * Worse performance with many duplicates

- **Backtracking Approach**:
  * More complex code with careful duplicate pruning
  * Avoids generating duplicate permutations upfront
  * Only generates unique permutations from the start
  * Better performance overall, especially with duplicates

Example: nums = [1, 1, 2]
- Generate all permutations: (1,1,2), (1,2,1), (1,1,2), (1,2,1), (2,1,1), (2,1,1)
- Set deduplicates: {(1,1,2), (1,2,1), (2,1,1)}
- Convert to lists: [[1,1,2], [1,2,1], [2,1,1]]
- Total: 3 unique permutations

Time Complexity: O(n! * n)
  - Generate all n! permutations: O(n! * n) - each permutation takes O(n) to create
  - Add to set and deduplicate: O(n! * n) in worst case
  - Convert back to lists: O(n! * n)
  - Overall: O(n! * n) regardless of duplicates

Space Complexity: O(n! * n) for storing results plus O(n! * n) for temporary set
  - Set of all generated permutations: O(n! * n)
  - Result list: O(k * n) where k is number of unique permutations (k ≤ n!)
  - With many duplicates, this can be wasteful (generates n! tuples then discards duplicates)

Performance Impact of Duplicates:
  - Backtracking approach: O(unique_perms * n) - much better with duplicates
  - Itertools approach: O(n! * n) - no improvement even with many duplicates
  - For input [1,1,1,1] with n=4: backtracking generates 1 permutation, itertools generates 24

Real-World Usage:
- Quick prototyping and testing when code clarity matters more than performance
- Educational purposes to understand permutation generation
- Small input sizes (n < 8) where performance difference is negligible
- Situations where standard library usage is preferred over custom algorithms

This approach demonstrates pragmatic problem-solving: sometimes using built-in tools is better than
writing complex custom code, depending on context, constraints, and priorities. Important for interviews:
be ready to discuss trade-offs and explain why you chose a particular approach.
"""

import itertools
from typing import List


def permute_unique_itertools(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations using itertools.permutations
    and deduplicate with a set.
    """
    perms = set(itertools.permutations(nums))
    return [list(p) for p in perms]
