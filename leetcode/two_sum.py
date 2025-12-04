"""
Two Sum Problem - Hash Map Solution
====================================
The Two Sum problem is a classic LeetCode challenge that asks to find two numbers in an array
that add up to a given target value and return their indices. This is an excellent problem for
demonstrating hash map usage for optimal time complexity optimization and is frequently asked
in technical interviews. It showcases the complement pattern, space-time trade-offs, and efficient
data structure usage for solving array problems.

Here is how the optimized algorithm works:

1. **Problem Understanding**: Given an array of integers and a target sum, find the indices of
   the two numbers that add up to the target. The problem guarantees exactly one valid solution exists.
   - Example: nums = [2, 7, 11, 15], target = 9 → [0, 1] (2 + 7 = 9)
   - Example: nums = [3, 2, 4], target = 6 → [1, 2] (2 + 4 = 6)
   - Key constraint: Return indices, not values; each element used only once

2. **Naive Approach**: Brute Force with Nested Loops
   - Check every pair of numbers using nested loops: for i in range(n): for j in range(i+1, n)
   - If nums[i] + nums[j] == target, return [i, j]
   - Time Complexity: O(n²) - checking all pairs is inefficient for large arrays
   - Space Complexity: O(1) - no extra space needed beyond variables
   - Limitation: Acceptable for small arrays, becomes prohibitively slow for large datasets

3. **Key Insight - Complement Pattern**: The crucial observation that enables optimization.
   - If we need nums[i] + nums[j] = target, then nums[j] = target - nums[i]
   - For each number, we can calculate what value it needs to pair with (complement)
   - Instead of checking all pairs, we look up if the complement exists in a hash map
   - This transforms O(n²) problem into O(n) by trading space for time

4. **Optimized Approach**: Hash Map (Single Pass)
   - Use a hash map to store seen values and their indices: {value: index}
   - Iterate through array once, for each number calculate complement = target - current_number
   - Check if complement already exists in the hash map
   - If found: return [index_of_complement, current_index]
   - If not found: add current number and its index to the hash map, continue
   - Time Complexity: O(n) - single pass through the array with O(1) lookups
   - Space Complexity: O(n) - hash map stores up to n elements in worst case
   - Benefit: Linear time is dramatically better than quadratic for large inputs

5. **Algorithm Steps**:
   Step 1: Initialize an empty hash map to track {value: index} pairs
   Step 2: Iterate through the array with index tracking using enumerate()
   Step 3: For each number, calculate complement = target - current_number
   Step 4: If complement exists in hash map, immediately return [hash_map[complement], current_index]
   Step 5: Otherwise, store current_number and current_index in hash map
   Step 6: Continue until solution found (guaranteed by problem statement)
   Step 7: Return empty list if no solution (problem guarantees this won't happen)

6. **Example Walkthrough** with nums = [2, 7, 11, 15], target = 9:
   - i=0, num=2: complement=9-2=7, not in seen={}, add 2 → seen={2:0}
   - i=1, num=7: complement=9-7=2, found in seen! return [seen[2], 1] = [0, 1]
   - Result: indices [0, 1] where nums[0]=2, nums[1]=7, and 2+7=9 ✓
   - Note: Why order matters - [0, 1] not [1, 0] because we check seen BEFORE adding

7. **Key Insights for Interviews**:
   - **Trade-off**: Exchange space (hash map storage) for time (from O(n²) to O(n))
   - **Hash Map Efficiency**: Dictionary lookups are O(1) average case in Python
   - **Single Pass**: Combine checking and storing in one loop for efficiency
   - **Complement Pattern**: Essential technique applicable to 3Sum, 4Sum, and other problems
   - **Why Not Two Pointers**: Two-pointer approach requires sorted array, loses original indices
   - **Index Preservation**: Hash map preserves original array indices crucial for this problem

8. **Common Follow-ups and Variations**:
   - Two Sum II (Sorted Array): Use two pointers instead, return 1-indexed
   - Two Sum III (Data Structure): Design class with add() and find() methods
   - Two Sum IV (BST): Given BST root and target, find two values summing to target
   - 3Sum / 4Sum: Extend to find N numbers summing to target
   - Closest Sum: Find pair with sum closest to target (not necessarily equal)
   - Count Pairs: Count how many pairs sum to target instead of returning indices

This algorithm is fundamental for understanding hash maps, space-time trade-offs, and the
complement-based searching pattern, making it essential interview preparation material. Practice
explaining the trade-offs and why hash map is better than brute force.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Return indices of the two numbers such that they add up to target.
    Uses a hash map for O(n) time complexity and O(n) space complexity.
    """
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    # Problem guarantees exactly one solution
    return []
