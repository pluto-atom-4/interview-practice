"""
## Problem Statement

Find the single duplicate number in an array where numbers range from 1 to n, the array has n+1 elements, 
and exactly one number is duplicated (possibly multiple times). Must achieve this efficiently without 
using extra space. This problem tests understanding of XOR properties and bit manipulation optimization.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **XOR (exclusive OR) bit manipulation**:

XOR has a unique mathematical property: any number XORed with itself equals 0 (a ⊕ a = 0), and any 
number XORed with 0 equals itself (a ⊕ 0 = a). By XORing all array elements with all expected numbers 
(1 to n), the non-duplicate numbers cancel out, leaving only the duplicate.

* Key Concepts:

  - Why XOR eliminates non-duplicates?
When we XOR all array numbers with all numbers 1..n, each non-duplicate appears exactly twice and cancels 
to 0. The duplicate appears more than twice, so one instance survives. This works because XOR is commutative 
and associative: (a ⊕ a ⊕ b) = (a ⊕ b ⊕ a) = b. No extra space needed—just two variables.

  - Why initialize two separate XOR accumulators?
Computing xor_all_nums from the array and xor_1_to_n separately makes the logic clearer and easier to trace. 
We could combine them into one loop, but separating makes the XOR cancellation principle more obvious during 
interviews. It's a trade-off between pure efficiency and clarity.

* Logic:

1. Initialize n = len(nums) - 1 to know which numbers should appear (1 to n)
2. XOR all elements in the input array into xor_all_nums
3. XOR all numbers from 1 to n into xor_1_to_n
4. Return xor_all_nums ⊕ xor_1_to_n—the duplicate emerges from the cancellation

* **30-Second Pitch**:

We use XOR because it's a self-cancelling operation: any number XORed with itself equals zero. So we XOR 
all array elements together, then XOR with all expected numbers 1 to n. All non-duplicates cancel out to zero, 
leaving just the duplicate. This gives us O(n) time, O(1) space with no sorting or hashing.

* **Rapid-Fire Version**:

- XOR is self-cancelling: a ⊕ a = 0
- XOR all array elements into one accumulator
- XOR all expected numbers 1..n into another accumulator
- Result of the two accumulated XORs reveals the duplicate
- Time: O(n), Space: O(1)

* **Ultra-Minimal One-Liner**:

- XOR all array elements and all expected numbers 1..n separately; XOR the two results to isolate the duplicate.

* **Complexity Analysis**:

- **Time Complexity:** O(n) – two linear passes (one through array, one through 1..n)
- **Space Complexity:** O(1) – only two integer variables, no data structures

* **Use Cases**:

- Interview questions on bit manipulation, finding duplicates under memory constraints, and demonstrating understanding of XOR properties.
Also applicable in duplicate detection for constrained embedded systems.
- (e.g., flag unique status codes in embedded sensor data).
"""

from __future__ import annotations

from typing import List


def xor_find_duplicate(nums: List[int]) -> int:
    n = len(nums) - 1

    xor_all_nums = 0
    xor_1_to_n = 0

    # XOR all elements in the array
    for num in nums:
        xor_all_nums ^= num

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor_1_to_n ^= i

    # Duplicate = XOR of the two results
    return xor_all_nums ^ xor_1_to_n
