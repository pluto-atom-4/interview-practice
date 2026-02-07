"""
## Problem Statement

Given an array of integers where every number appears exactly twice except for one number
that appears exactly once, find and return the single number. The challenge is to solve this
in O(1) space without using extra data structures—a classic bit manipulation interview problem.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **XOR (Bitwise Exclusive OR) Properties**:

  The XOR operation has special mathematical properties that make it perfect for this problem.
  By XORing all numbers together, the duplicates cancel each other out, leaving only the single number.

* Key Concepts:

  - **x ^ x = 0 (Self-cancellation)**: When you XOR a number with itself, the result is always 0.
    This is the core insight—any number appearing exactly twice will XOR to 0, effectively "removing" it.

  - **x ^ 0 = x (Identity property)**: XORing any number with 0 returns the number itself.
    After all pairs cancel to 0, only the single number remains when XORed with the running result.

  - **XOR is commutative and associative**: Order doesn't matter—(a ^ b ^ c) = (c ^ b ^ a).
    This means we can process the array in any order and still get the correct result.

* Logic:

  1. Initialize result to 0 (identity element for XOR)
  2. Iterate through each number in the array
  3. XOR the current number with the result
  4. Each duplicate pair cancels to 0; the single number survives
  5. Return the final result (the single non-duplicate number)

* **30-Second Pitch**:

  I XOR all numbers together. Since XOR of identical numbers is zero, all duplicates cancel out,
  leaving only the single number. It's O(n) time and O(1) space—no extra data structures needed.

* **Rapid-Fire Version**:

  - XOR property: x ^ x = 0, x ^ 0 = x
  - All pairs (duplicates) XOR to 0
  - Single number XORed with 0 remains
  - Single pass through array = O(n) time, O(1) space
  - No hash maps, sorting, or extra memory required

* **Ultra-Minimal One-Liner**:

  XOR all numbers together—duplicates cancel out, leaving the single number.

* **Complexity Analysis**:

  - **Time Complexity:** O(n) — Single pass through the array; each XOR operation is constant time.
  - **Space Complexity:** O(1) — Only using a single integer variable; no additional data structures.

* **Use Cases**:

  - Interview favorite for testing bit manipulation knowledge; used in systems checking for corrupted data
  where a single bit flip indicates an error. Also appears in LeetCode #136 and similar constraints-focused problems.
  - (e.g., flag unique status codes in embedded sensor data).

"""

from __future__ import annotations

from typing import List


def xor_single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result
