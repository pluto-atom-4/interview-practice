"""
Longest Consecutive Sequence - Pure Functional Generator Pipeline Version
--------------------------------------------------------------------------
This implementation demonstrates a pure functional approach using generator pipelines to solve the
Longest Consecutive Sequence problem. It emphasizes elegant, composable code patterns that minimize
state and maximize readability. The generator-based approach defers computation and maintains memory
efficiency by processing data lazily through a pipeline of transformations.

Here is how the process works:

1. **Convert to Set**: Transform the input array into a set for O(1) lookup.
   - Removes duplicates in a single operation
   - Enables efficient membership testing
   - Foundation for identifying sequence starts and boundaries

2. **Identify Starting Points - Generator Pipeline Stage 1**: Create a generator of sequence start positions.
   - Filter: numbers where (n - 1) is NOT in the set
   - Only numbers that begin a consecutive sequence are yielded
   - Lazy evaluation: starts are generated on-demand, not stored
   - Memory efficient: doesn't materialize entire list of starts

3. **Define Sequence Counter Function**: Helper function to count length of consecutive sequence.
   - Takes a starting number n
   - Iterates forward while consecutive numbers exist in the set
   - Counts elements until hitting a gap (number not in set)
   - Returns the total length of the sequence from n

4. **Apply Counter to Each Start - Generator Pipeline Stage 2**: Map the counter function over all starts.
   - Generator: lazily applies chain_length to each starting number
   - Produces lengths as they're needed, not all at once
   - Composable pipeline: starts → lengths transformation
   - Memory efficient for arrays with many sequences

5. **Find Maximum Length - Pipeline Termination**: Consume the generator pipeline to find the maximum.
   - max(lengths, default=0) terminal operation on lazy generator
   - Computes only what's needed to find the maximum
   - Handles empty input gracefully with default=0
   - Single-pass evaluation of all sequences

6. **Functional Programming Principles**:
   - Generator expressions for lazy evaluation
   - Pure functions with no side effects
   - Composable pipeline of transformations
   - Data flows through: nums → set → starts → lengths → max

Example: nums = [100, 4, 200, 1, 3, 2]
- Set: {1, 2, 3, 4, 100, 200}
- Generator starts: yields 1, then 100, then 200
- chain_length(1): yields 4 (sequence 1→2→3→4)
- chain_length(100): yields 1 (sequence 100)
- chain_length(200): yields 1 (sequence 200)
- Result: max([4, 1, 1]) = 4

Time Complexity: O(n) - set conversion O(n), filtering starts O(n), counting all sequences O(n) total
Space Complexity: O(n) - for the set; generators use O(1) additional space beyond set
Functional Style: Pure generator pipeline with composition and lazy evaluation

This algorithm demonstrates advanced functional Python patterns and is essential for understanding
generator pipelines, lazy evaluation, functional composition, and interview-level code elegance.
"""

from typing import List


def longest_consecutive_generators(nums: List[int]) -> int:
    """
    Pure functional generator-pipeline version.
    """

    num_set = set(nums)

    # Generator of starting points (numbers whose predecessor is missing)
    starts = (n for n in num_set if n - 1 not in num_set)

    # For each start, count how long the chain continues
    def chain_length(n):
        count = 0
        current = n
        while current in num_set:
            count += 1
            current += 1
        return count

    lengths = (chain_length(n) for n in starts)

    return max(lengths, default=0)
