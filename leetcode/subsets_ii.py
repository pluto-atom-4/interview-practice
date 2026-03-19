"""
## Problem Statement

Generate all unique subsets from a list that may contain duplicate elements.
The goal is to return all possible combinations where duplicates are treated as identical,
avoiding repeated subsets. This problem tests understanding of backtracking with deduplication
and set generation under constraints.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using a **backtracking algorithm with duplicate skipping**:

* **Ultra-Minimal One-Liner**:

- Sort the array, then use backtracking to explore all subsets, skipping duplicate elements
  at each recursion level to avoid duplicate subsets.

* **Complexity Analysis**:

  - **Time Complexity:** O(2^n) where n is the number of unique elements. In the worst case
    (all unique), we generate all 2^n subsets. Sorting takes O(n log n), which is dominated
    by the exponential subset generation.

  - **Space Complexity:** O(n) for the recursion call stack depth (at most n levels). The
    output list containing all subsets requires exponential space, but this is necessary
    for the problem's output.

## Algorithm Explanation

This approach uses backtracking with a deduplication strategy. By sorting the input first,
duplicate elements become adjacent in the array. At each recursion level, we skip duplicate
elements that we've already explored in the same position, preventing duplicate subsets
from being generated.

* Key Concepts:

  - **Sorting for Duplicate Adjacency**: Why?
  Sorting groups identical elements together, making it easy to detect and skip duplicates
  using a simple index-based comparison (nums[i] == nums[i-1]). How? We check if the
  current element equals the previous one and skip if we're not at the start of recursion
  (i > start), ensuring each unique element is tried exactly once per depth level.

  - **Index-Based Deduplication (i > start check)**: Why?
  This distinguishes between skipping a duplicate vs. starting a fresh exploration at a
  new recursion level. If i == start, we're at the beginning of this level and should not
  skip, even if the element matches the previous one. How? We compare position: only skip
  if i > start AND the element matches the previous, meaning we've already tried this
  element at this depth.

  - **Backtrack with Restore Pattern**: Why?
  Enables exploration of multiple branches from the same state without explicitly creating
  copies of the state. How? We append to the subset, recurse, then pop immediately after,
  allowing the next iteration to start from a clean state. This maintains O(n) space for
  the recursion stack instead of O(n^2) if we copied the state each time.

## Algorithm Logic

1. **Sort the input array** to make duplicate elements adjacent, enabling efficient detection
   and skipping of duplicates during recursion.

2. **Initialize empty result list and subset list**: result stores all unique subsets found,
   subset is the current working subset being built.

3. **Define backtrack(start) helper function**: Recursively builds subsets by trying each
   unused element as the next addition.

4. **In each backtrack call**: First, add a copy of the current subset to results (this is
   the subset at this state).

5. **Iterate from start index to end**: For each position, check if it's a duplicate at the
   current depth. Skip if it matches the previous element and we're not at the start
   (i > start).

6. **For each non-duplicate element**: Append it to subset, recurse with updated start
   (i + 1) to avoid reusing elements, then pop to restore state.

7. **Termination**: When start reaches the end of nums, the for loop has no iterations,
   backtracking returns, and parent calls continue exploring other branches.

## Summary Variations

* **30-Second Pitch**:

We generate all unique subsets by using backtracking with intelligent deduplication.
First, we sort the array so identical elements sit together. Then during our recursive
exploration, whenever we encounter a duplicate element at the same recursion depth, we
skip it because we've already explored all subsets that include that element at this
position. We build subsets incrementally using a mutable list, adding each valid subset
to our result, and restoring the state after each recursive call.

* **Rapid-Fire Version**:

- Sort the array to group duplicates adjacently
- Use backtracking to explore all subset combinations
- At each depth, skip duplicate elements (check i > start && nums[i] == nums[i-1])
- Append current subset to result, then recursively extend with remaining elements
- Pop after recursion to restore state (standard backtracking pattern)
- Time: O(2^n), Space: O(n) for recursion depth

## Use Cases:

- **Interview context**: Tests understanding of both backtracking and deduplication; common
  LeetCode medium problem for practicing constraint-based recursion.
- **Real-world**: Generating all valid configurations from a set with repeated options
  (e.g., subset of database queries with duplicate filters, combination generation in
  combinatorial optimization).
- **Related problems**: Permutations II, Combinations, Letter Combinations of Phone Number,
  N-Queens (all backtracking with constraints).
"""

from typing import List


def subsets_with_dup(nums: List[int]) -> List[List[int]]:

    nums.sort()
    result: List[List[int]] = []
    subset: List[int] = []

    def backtrack(start: int) -> None:
        result.append(subset.copy())

        for i in range(start, len(nums)):
            # skip duplicates at the same recursion depth
            if i > start and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

    backtrack(0)
    return result