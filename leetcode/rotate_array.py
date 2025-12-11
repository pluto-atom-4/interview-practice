"""
Array Rotation Algorithms Explained Step-by-Step
------------------------------------------------
The Rotate Array problem is a classic array manipulation question often asked in technical interviews. The goal is to rotate an array to the right by k steps, either by returning a new rotated array or modifying the array in-place. This problem tests understanding of array indexing, modular arithmetic, and in-place algorithms.

Here is how the process works:

1. **Rotation Concept**: Shifting elements right by k steps.
   - For each index i, the new position is (i + k) % n, where n is the array length.
   - Handles cases where k > n by using k % n.
   - Can be implemented by slicing or by rearranging elements in-place.

2. **New Array Approach** (`rotate`):
   - Uses slicing to create a new rotated array.
   - nums[-k:] + nums[:-k] moves the last k elements to the front.
   - Does not modify the original array.
   - Time Complexity: O(n), Space Complexity: O(n).

3. **In-Place Approach** (`rotate_in_place`):
   - Uses reversal algorithm to rotate the array in-place with O(1) extra space.
   - Steps:
     a. Reverse the entire array.
     b. Reverse the first k elements.
     c. Reverse the remaining n-k elements.
   - Efficient for large arrays where extra space is not allowed.
   - Time Complexity: O(n), Space Complexity: O(1).

4. **Edge Cases**:
   - Empty array: return as is.
   - k = 0 or k % n = 0: no rotation needed.
   - k > n: use k % n to avoid redundant rotations.

5. **Applications**:
   - Useful in cyclic scheduling, buffer management, and data transformation.
   - Demonstrates mastery of array manipulation and in-place algorithms.

Example: nums = [1,2,3,4,5,6,7], k = 3
- New array: [5,6,7,1,2,3,4]
- In-place: reverse entire array → [7,6,5,4,3,2,1], reverse first 3 → [5,6,7,4,3,2,1], reverse last 4 → [5,6,7,1,2,3,4]

This problem is fundamental for understanding array operations and is frequently used to assess problem-solving skills in interviews.
"""
from typing import List


def rotate(nums: List[int], k: int) -> List[int]:
    """
    Rotate the array to the right by k steps.
    Returns a new rotated list (does not modify input in-place).
    """
    n = len(nums)
    if n == 0:
        return nums

    k = k % n  # handle k > n
    return nums[-k:] + nums[:-k]


def rotate_in_place(nums: List[int], k: int) -> None:
    """
    Rotate the array to the right by k steps in-place.
    """
    n = len(nums)
    k %= n

    def reverse(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
