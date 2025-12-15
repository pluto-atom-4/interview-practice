"""
Move Zeroes Algorithm Explained Step-by-Step
----------------------------------------------
The Move Zeroes problem requires moving all zero elements to the end of an array while maintaining
the relative order of non-zero elements. This is a classic in-place array manipulation problem
frequently asked in technical interviews. It tests understanding of array operations, space
optimization, and different algorithmic approaches (two-pointer, functional, imperative).

Here is how the process works:

1. **Problem Understanding**: In-place modification of the input array.
   - All zeros must be moved to the end
   - Non-zero elements maintain their relative order
   - Must be done in-place (minimal extra space)
   - No return value; modify the input array directly

2. **Functional Approach**: Build the result functionally, apply in-place.
   - Separate non-zero elements using list comprehension
   - Count zeros separately (len(nums) - len(non_zero))
   - Combine: concatenate non-zero list with appropriate number of zeros
   - Apply result back to input array using slice assignment (nums[:] = transformed)
   - Advantages: Clean, readable, demonstrates functional thinking
   - Disadvantages: Uses O(n) extra space for temporary lists

3. **Reduce-Based Approach (Current Implementation)**: Pure functional with reduce abstraction.
   - Uses functools.reduce() for pure functional accumulation
   - Accumulates (non_zero_list, zero_count) tuple as state
   - Step function processes each element:
     * If element is 0: increment zero_count
     * If element is non-zero: append to non_zero_list
   - Initial accumulator: ([], 0) - empty list and zero count
   - Combines accumulated results: non_zero + [0] * zero_count
   - Applies back to input array using slice assignment
   - Demonstrates advanced functional programming paradigm
   - Shows understanding of reduce() for complex aggregations

4. **Alternative: Two-Pointer Approach (Optimal In-Place)**.
   - Maintain a pointer (write_index) for the next position to place non-zero
   - Iterate through array with read pointer
   - When non-zero element found, place it at write_index and increment
   - After iteration, fill remaining positions with zeros
   - Time: O(n), Space: O(1) - true in-place solution
   - Better for interviews when space optimization is emphasized

5. **Key Considerations for Interviews**:
   - **Space Complexity**: Must clarify if in-place means O(1) auxiliary space
   - **Relative Order**: Verify zeros don't shuffle non-zero elements
   - **Edge Cases**: Empty array, all zeros, no zeros, single element
   - **In-Place Modification**: Use slice assignment (nums[:] = ...) in Python
   - **Trade-offs**: Functional clarity vs. imperative efficiency
   - **Reduce Understanding**: Demonstrate knowledge of functional accumulation patterns

6. **Example Walkthrough**: nums = [0, 1, 0, 3, 12]
   - Reduce accumulation:
     * Process 0: ([], 1)
     * Process 1: ([1], 1)
     * Process 0: ([1], 2)
     * Process 3: ([1, 3], 2)
     * Process 12: ([1, 3, 12], 2)
   - Final: [1, 3, 12] + [0, 0] = [1, 3, 12, 0, 0]
   - Result: [1, 3, 12, 0, 0] - non-zeros preserved, zeros at end

Time Complexity: O(n) - single pass with reduce accumulation
Space Complexity: O(n) - intermediate lists and accumulator storage

This algorithm demonstrates:
- Reduce pattern for complex functional aggregation
- Tuple accumulation for multiple state values
- Pure functional approach to imperative problem
- Understanding of higher-order functions and functional programming patterns
Essential for showing functional programming knowledge and problem-solving flexibility in interviews.
"""

from functools import reduce
from typing import List, Tuple


def move_zeroes_reduce(nums: List[int]) -> None:
    """
    Pure functional reduce-based implementation.
    Builds (non_zero_list, zero_count) using reduce,
    then applies the result back into nums in-place.
    """

    def step(acc: Tuple[List[int], int], x: int) -> Tuple[List[int], int]:
        non_zero, zero_count = acc
        if x == 0:
            return (non_zero, zero_count + 1)
        else:
            return (non_zero + [x], zero_count)

    non_zero, zero_count = reduce(step, nums, ([], 0))
    transformed = non_zero + [0] * zero_count

    nums[:] = transformed
