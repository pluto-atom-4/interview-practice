"""
Longest Consecutive Sequence - Itertools GroupBy Approach
----------------------------------------------------------
This implementation uses itertools.groupby to solve the Longest Consecutive Sequence problem through
a clever sorting-based technique. Instead of checking membership repeatedly, it sorts the unique numbers
and groups consecutive runs by exploiting a mathematical property: consecutive numbers share the same
difference between their value and their index position.

Here is how the process works:

1. **Handle Empty Input**: Guard clause for empty arrays.
   - Edge case: if nums is empty, return 0
   - Prevents errors in subsequent operations
   - Ensures graceful handling of degenerate input

2. **Create Sorted Unique Set**: Remove duplicates and sort.
   - Convert nums to set (removes duplicates)
   - Sort the set in ascending order
   - Sorted array enables detection of consecutive numbers
   - Foundation for grouping algorithm

3. **Enumerate the Sorted Array**: Pair each value with its index.
   - enumerate(sorted_nums) creates (index, value) tuples
   - Index represents position in the sorted array
   - Value is the actual number from the original array

4. **Group by Mathematical Property - The Key Insight**:
   - Key formula: value - index
   - Consecutive numbers have the SAME (value - index) difference
   - Example: [1,2,3] with indices [0,1,2] → differences are [1,1,1]
   - Example: [5,6,7] with indices [3,4,5] → differences are [2,2,2]
   - groupby automatically groups items where key is identical
   - Each group represents one consecutive sequence run

5. **Count Length of Each Group**: Calculate size of each consecutive run.
   - Generator expression: sum(1 for _ in group)
   - Counts elements in each group without materializing
   - Each group is already a consecutive sequence (no gaps)
   - Produces sequence lengths for all runs

6. **Find Maximum Length**: Return the longest sequence found.
   - max(lengths, default=0) computes maximum from all group sizes
   - Handles empty input gracefully with default=0
   - Single value returned as the solution

Example: nums = [100, 4, 200, 1, 3, 2]
- sorted_nums = [1, 2, 3, 4, 100, 200]
- enumerate: [(0,1), (1,2), (2,3), (3,4), (4,100), (5,200)]
- key function (value - index): [1, 1, 1, 1, 96, 195]
- Groups: [1,1,1,1] → length 4, [96] → length 1, [195] → length 1
- Result: max([4, 1, 1]) = 4

Time Complexity: O(n log n) - dominated by sorting step
Space Complexity: O(n) - for storing sorted unique set
Approach: Sort-based grouping using mathematical property of consecutive sequences

Comparison:
- More elegant mathematical insight (value - index property)
- Slower than set-based approach due to O(n log n) sorting
- Highly readable and demonstrates clever functional thinking
- Shows advanced itertools mastery for interview discussions

This algorithm demonstrates sorting-based solutions, clever mathematical properties, and
itertools mastery - valuable for showing diverse problem-solving approaches in interviews.
"""

from itertools import groupby
from typing import List


def longest_consecutive_groupby(nums: List[int]) -> int:
    """
    Functional version using itertools.groupby.
    Sorts the numbers, groups consecutive runs, and finds the longest.
    """

    if not nums:
        return 0

    sorted_nums = sorted(set(nums))

    # Group by the difference between value and index
    # Consecutive numbers share the same (value - index)
    groups = groupby(
        enumerate(sorted_nums),
        key=lambda pair: pair[1] - pair[0]
    )

    # Length of each group is the size of the consecutive run
    lengths = (sum(1 for _ in group) for _, group in groups)

    return max(lengths, default=0)
