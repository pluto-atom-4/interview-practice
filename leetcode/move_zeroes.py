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

2. **Functional Approach (Current Implementation)**: Build the result functionally, apply in-place.
   - Separate non-zero elements using list comprehension
   - Count zeros separately (len(nums) - len(non_zero))
   - Combine: concatenate non-zero list with appropriate number of zeros
   - Apply result back to input array using slice assignment (nums[:] = transformed)
   - Advantages: Clean, readable, demonstrates functional thinking
   - Disadvantages: Uses O(n) extra space for temporary lists

3. **Alternative: Two-Pointer Approach (Optimal In-Place)**.
   - Maintain a pointer (write_index) for the next position to place non-zero
   - Iterate through array with read pointer
   - When non-zero element found, place it at write_index and increment
   - After iteration, fill remaining positions with zeros
   - Time: O(n), Space: O(1) - true in-place solution
   - Better for interviews when space optimization is emphasized

4. **Reduce-Based Approach**: Pure functional with reduce abstraction.
   - Accumulates (non_zero_list, zero_count) tuple
   - Each element either increments zero_count or extends non_zero_list
   - Combines results and applies back in-place
   - Demonstrates functional programming paradigm
   - More complex but shows deeper functional knowledge

5. **Key Considerations for Interviews**:
   - **Space Complexity**: Must clarify if in-place means O(1) auxiliary space
   - **Relative Order**: Verify zeros don't shuffle non-zero elements
   - **Edge Cases**: Empty array, all zeros, no zeros, single element
   - **In-Place Modification**: Use slice assignment (nums[:] = ...) in Python
   - **Trade-offs**: Functional clarity vs. imperative efficiency

6. **Example Walkthrough**: nums = [0, 1, 0, 3, 12]
   - Functional: Extract [1, 3, 12], count zeros = 2, combine [1, 3, 12, 0, 0]
   - Two-Pointer: write_index moves through, place non-zeros, fill rest with zeros
   - Result: [1, 3, 12, 0, 0] - non-zeros preserved, zeros at end
   - Multiple approaches show algorithmic flexibility

Time Complexity: O(n) - single or multiple passes through array
Space Complexity:
  - Functional approach: O(n) - temporary lists
  - Two-pointer approach: O(1) - in-place modification only
  - Reduce approach: O(n) - intermediate list accumulation

This algorithm demonstrates array manipulation, in-place modification techniques, and the ability
to approach the same problem through multiple paradigms (functional, imperative, pointer-based).
Essential for understanding space optimization and algorithmic flexibility in interviews.
"""

from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Pure functional logic + in-place update.
    The transformation is functional; the mutation is only at the end.
    """

    # Functional transformation: build the new list
    non_zero = [x for x in nums if x != 0]
    zeros = [0] * (len(nums) - len(non_zero))
    transformed = non_zero + zeros

    # Apply back in-place
    nums[:] = transformed
