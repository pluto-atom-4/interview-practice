"""
## Problem Statement

Generate all possible permutations of a list of distinct integers. Return a list containing 
all permutations in any order. This is a classic backtracking problem that tests understanding 
of recursive exploration and state management during algorithm execution.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Backtracking with State Tracking**:

* **Ultra-Minimal One-Liner**:
  - Use backtracking to recursively explore all possible orderings, maintaining a used array to track 
    which elements are already in the current permutation.

* **Complexity Analysis**:
  - **Time Complexity:** O(n! × n) — There are n! permutations, and for each we build a permutation 
    (O(n) copy operation), plus n operations per recursive call to check availability.
  - **Space Complexity:** O(n) for the recursion depth and auxiliary structures (used array, path), 
    excluding the output list which stores all n! permutations.

## Algorithm Explanation

Backtracking is ideal here because we need to explore all possible orderings without knowing them 
upfront. The key insight is to build permutations incrementally: at each step, try placing each 
unused element in the current position, then recursively complete the permutation. When we've placed 
all n elements, we save the permutation and backtrack to explore other possibilities.

* Key Concepts:

  - **Backtracking via State Management**: Why/How?
    The used array tracks which elements are already in the current permutation path. This prevents 
    reusing the same element and enables efficient pruning—when an element is marked used, we skip 
    it in subsequent iterations. When we backtrack (remove from path), we mark it unused again, 
    allowing it to be tried in other positions.

  - **Path Copy at Terminal State**: Why/How?
    We append path.copy() (not path itself) because path is mutated throughout recursion. Without 
    copy(), all permutations in result would reference the same path object, ending up identical 
    after recursion completes. Copying captures the exact state at that moment, preserving each 
    unique permutation.

  - **Recursive Exploration Order**: Why/How?
    We iterate through all indices and try each unused element. This systematic exploration ensures 
    we visit all branches of the decision tree. The order of trying elements (left to right) is 
    arbitrary but consistent, making it easy to verify correctness and debug.

## Algorithm Logic

1. **Initialize state**: Create empty result list, used array to track availability, and empty path for 
   current permutation being built.
2. **Define backtracking function**: Recursively build permutations by trying each unused element at the 
   current position.
3. **Base case (terminal state)**: When path length equals n (all elements placed), copy the path into 
   result and return.
4. **Recursive case**: For each index i from 0 to n-1, if element i is unused, mark it used, append to path, 
   recurse to fill remaining positions, then backtrack by popping from path and unmarking as used.
5. **Return result**: After exploring all permutations, return the complete result list.

## Summary Variations

* **30-Second Pitch**:
  Use backtracking to generate all permutations. At each step, try placing each unused element into the 
  current position, then recursively complete the permutation. Maintain a used array to efficiently skip 
  already-placed elements. When you've placed all n elements, save a copy of the permutation. This explores 
  the full decision tree systematically while tracking state to avoid duplicates.

* **Rapid-Fire Version**:
  - Build permutations recursively using backtracking
  - Maintain a used array to track which elements are in the current permutation
  - For each position, try all unused elements, recurse, then backtrack
  - At terminal state (length == n), append a copy of the path to results
  - Time: O(n! × n), Space: O(n) excluding output

## Use Cases

Permutations appear in many interview and real-world scenarios:
- **Scheduling problems** — Determine all possible task orderings
- **Password generation** — Generate all valid character arrangements
- **Game AI** — Explore all possible move sequences in game trees
- **Combinatorial optimization** — Find best arrangement among all possibilities
- **Resource allocation** — Determine all possible assignment patterns
"""

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    used = [False] * len(nums)
    path: List[int] = []

    def backtrack() -> None:
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append((nums[i]))
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return  result