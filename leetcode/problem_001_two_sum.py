"""
LeetCode Problem 1: Two Sum
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

Assume that each input has exactly one solution, and you may not use the same element twice.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] == 9
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Returns indices of the two numbers that add up to the target.

    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        List[int]: Indices of the two numbers.
    """
    num_map = {}  # Maps number to its index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    raise ValueError("No two sum solution found")


# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices: {result}")  # Output: [0, 1]
