"""
Range Sum Query - Mutable (Fenwick Tree / Binary Indexed Tree) Algorithm Explained
------------------------------------------------------------------------------------
Range Sum Query on Mutable Array is a classic data structure problem that asks to efficiently handle:
1. Update operations: modify a single element in the array
2. Range sum queries: compute the sum of elements in a given range

A naive approach (updating array and summing on query) leads to O(n) per operation. This solution uses
a Fenwick Tree (Binary Indexed Tree), an elegant data structure that balances updates and queries at O(log n).

Here is how the Fenwick Tree process works:

1. **Fenwick Tree Concept**: A compact array-based representation of prefix sums.
   - Uses 1-indexed array to simplify bit manipulation logic
   - Tree structure implicitly represented by array indices
   - Index i's parent is i + (i & -i), where & -i isolates the lowest set bit
   - Stores cumulative sums for specific ranges, not individual elements
   - Much more space-efficient than full 2D prefix sum array

2. **Low-Bit Isolation Technique**: The magic behind Fenwick Trees.
   - i & -i extracts the lowest set bit of index i
   - Example: i=6 (binary 110), -i=-6 (binary ...11111010 in two's complement)
   - i & -i = 2, indicating the range this node covers
   - Used to navigate the tree implicitly and compute parent/child relationships
   - Enables O(log n) traversal without explicit tree structure

3. **Tree Building (Initialization)**: Construct the Fenwick tree from input array.
   - Process each element and add its contribution to affected nodes
   - For each position i, update tree nodes at i, i + (i & -i), i + 2*(i & -i), etc.
   - Each node accumulates sums for a power-of-2 range of elements
   - Result: O(n log n) preprocessing to build efficient query structure

4. **Update Operation**: Efficiently modify an element and propagate changes.
   - Calculate delta = new_value - old_value
   - Update the original array copy to track actual values
   - Starting from index+1 (1-indexed), propagate delta up the tree
   - At each step, add delta to tree[j] and move to j + (j & -j)
   - Time: O(log n) as tree height is logarithmic

5. **Prefix Sum Query**: Calculate sum of elements from index 0 to i using tree.
   - Start with result = 0 and current index = i+1 (1-indexed)
   - Accumulate tree[current] into result
   - Move to next level up: current = current - (current & -current)
   - Continue until index becomes 0
   - Time: O(log n) due to logarithmic tree traversal

6. **Range Sum Calculation**: Combine two prefix sums for any range.
   - sumRange(left, right) = prefixSum(right+1) - prefixSum(left)
   - This uses difference principle: sum(left to right) = sum(0 to right) - sum(0 to left-1)
   - Two prefix sum queries, each O(log n)
   - Total time: O(log n) per range query

Example: nums = [1, 3, 5, 7, 9, 11]
- Build Fenwick tree capturing prefix sum information
- update(2, 8): Change nums[2] from 5 to 8, delta = 3, propagate to affected nodes
- sumRange(1, 4): Query prefix sums and compute 3+8+7+9 = 27
- Tree enables this without recalculating all sums

Time Complexity:
- Initialization: O(n log n) to build tree
- Update: O(log n) per operation
- Range Query: O(log n) per operation
- Much better than naive O(n) update or O(n) query approaches

Space Complexity: O(n) for the Fenwick tree array (plus copy of original array)

Why Fenwick Trees are Important for Interviews:
- Demonstrates advanced data structure understanding beyond basic arrays
- Shows knowledge of bit manipulation and clever index calculations
- Solves practical problems efficiently (stock prices, running aggregates)
- Interview question covering algorithm design, optimization, and implementation detail
- Tests ability to work with 1-indexed vs 0-indexed arrays correctly
- Common in competitive programming and system design scenarios
"""

from typing import List


class NumArray:
    """
    Modern Python implementation using a Fenwick Tree (Binary Indexed Tree).
    Supports update and prefix-sum queries in O(log n).
    """

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self.arr = nums[:]  # keep a copy of original values

        for i, v in enumerate(nums):
            self._add(i + 1, v)

    def _add(self, index: int, delta: int) -> None:
        """Internal Fenwick tree update."""
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def update(self, index: int, val: int) -> None:
        """Update nums[index] to val."""
        delta = val - self.arr[index]
        self.arr[index] = val
        self._add(index + 1, delta)

    def _prefix_sum(self, index: int) -> int:
        """Sum of nums[0:index]."""
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= index & -index
        return s

    def sumRange(self, left: int, right: int) -> int:
        """Return sum(nums[left:right+1])."""
        return self._prefix_sum(right + 1) - self._prefix_sum(left)
