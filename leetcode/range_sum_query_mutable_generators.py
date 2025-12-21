"""
Range Sum Query - Mutable (Fenwick Tree / Binary Indexed Tree) - Generator Pipeline Version
----------------------------------------------------------------------------------------------
This is an alternative implementation of Range Sum Query using generator expressions and pipelines
to traverse the Fenwick Tree. It demonstrates the same O(log n) time complexity while showcasing
Pythonic functional programming paradigms with generators.

Fenwick Tree (Binary Indexed Tree) fundamentals remain the same, but this version emphasizes:
1. **Lazy Evaluation**: Generator expressions delay computation until values are consumed
2. **Functional Pipelines**: Using generators to chain tree traversal operations
3. **Python Idioms**: Leveraging sum() with generators for elegant accumulation

Here is how the generator-based Fenwick Tree process works:

1. **Generator Function for Index Progression**: Replace while loops with generator expressions.
   - fenwick_indices(i) yields i, then i + (i & -i), then the next parent, etc.
   - Lazy generation: values produced on-demand, not pre-computed
   - Reduces intermediate variable assignments and improves code clarity
   - Same tree traversal logic, but expressed functionally

2. **Index Navigation in Both Directions**:
   - **Upward traversal** (for updates): fenwick_indices(i) where i += i & -i
     Yields i, then parent nodes up the tree
   - **Downward traversal** (for prefix sums): fenwick_indices(i) where i -= i & -i
     Yields i, then ancestor nodes back to root

3. **Tree Building with Generators**: Initialize using generator-driven updates.
   - For each input value, generate affected tree indices using fenwick_indices
   - More declarative than nested while loops
   - Same O(n log n) initialization, different implementation style

4. **Update Operation with Generator Pipeline**:
   - Calculate delta = new_value - old_value
   - Use fenwick_indices generator to traverse affected nodes
   - For each yielded index j, accumulate delta into tree[j]
   - Generator pattern: def fenwick_indices(i) yields all affected indices
   - Consumes generator in for loop: for j in fenwick_indices(index + 1): tree[j] += delta

5. **Prefix Sum Query with Generator Accumulation**:
   - Define fenwick_indices(i) to yield indices going downward: i -= i & -i
   - Use sum() with generator expression: sum(self.tree[j] for j in fenwick_indices(index))
   - Combines multiple Python features: generators, sum() with generator arg, lazy evaluation
   - Time complexity: still O(log n) despite functional approach

6. **Generator vs Traditional Comparison**:
   Traditional loop:
   ```
   s = 0
   while index > 0:
       s += self.tree[index]
       index -= index & -index
   return s
   ```
   Generator pipeline:
   ```
   return sum(self.tree[j] for j in fenwick_indices(index))
   ```
   - Same complexity, but more Pythonic and expressive
   - Separates concerns: index generation vs. value aggregation

Example: nums = [1, 3, 5, 7, 9, 11]
- update(2, 8): fenwick_indices(3) generates 3, 4, 8, ... then delta accumulated to each
- sumRange(1, 4): Uses two generator-based prefix sum calls to compute range
- Generator pattern makes index traversal explicit and reusable

Time Complexity:
- Initialization: O(n log n) - same as traditional Fenwick
- Update: O(log n) per operation
- Range Query: O(log n) per operation
- Generator overhead is negligible; complexity class unchanged

Space Complexity: O(n) for tree array

Why Generator Approach Matters:
- **Pythonic Code**: Demonstrates familiarity with Python idioms and functional programming
- **Maintainability**: Separates index generation from value processing logic
- **Reusability**: fenwick_indices can be called for different traversal patterns
- **Interview Value**: Shows understanding of both algorithm AND language features
- **Code Clarity**: Intent is clearer when generation is separated from aggregation
- **Performance**: In CPython, generator expressions are optimized and often faster than manual loops
"""

from typing import List


class NumArrayGenerators:
    """
    Generator‑pipeline flavored Fenwick Tree.
    Uses generator expressions to compute prefix sums
    and to walk Fenwick indices.
    """

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self.arr = nums[:]

        # Build tree using generator-driven index updates
        for i, v in enumerate(nums, start=1):
            j = i
            while j <= self.n:
                self.tree[j] += v
                j += j & -j

    def update(self, index: int, val: int) -> None:
        delta = val - self.arr[index]
        self.arr[index] = val

        # Generator pipeline for Fenwick index progression
        def fenwick_indices(i):
            while i <= self.n:
                yield i
                i += i & -i

        for j in fenwick_indices(index + 1):
            self.tree[j] += delta

    def _prefix_sum(self, index: int) -> int:
        # Generator pipeline for prefix sum accumulation
        def fenwick_indices(i):
            while i > 0:
                yield i
                i -= i & -i

        return sum(self.tree[j] for j in fenwick_indices(index))

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right + 1) - self._prefix_sum(left)
