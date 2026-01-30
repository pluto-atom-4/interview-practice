from __future__ import annotations

from typing import List

"""
## Problem Statement

Find the single number that appears once in an array where every other number appears exactly twice. 
This problem tests understanding of bitwise operations, particularly XOR properties, and demonstrates 
how mathematical properties can replace brute-force approaches—a key interview skill.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **XOR Bitwise Operation**:

XOR has three critical properties: x ^ x = 0 (same values cancel), x ^ 0 = x (identity), and commutativity/ 
associativity. Applying XOR to all numbers causes pairs to cancel out (become 0), leaving only the single 
unpaired number. This elegant mathematical trick achieves O(n) time with O(1) space.

* Key Concepts:

  - Why does XOR make duplicates cancel?
XOR compares bits: 1^1 = 0 and 0^0 = 0 (matching bits → 0), 1^0 = 1 and 0^1 = 1 (differing bits → 1). 
When applied to identical numbers (same bit pattern), every bit position XORs to 0. The result is 0 for 
the pair, leaving the single number unaffected.

  - Why is XOR commutative and associative for this solution?
Commutativity (a ^ b = b ^ a) means order doesn't matter. Associativity ((a ^ b) ^ c = a ^ (b ^ c)) means 
grouping doesn't matter. We can XOR all numbers in any order—pairs cancel regardless. This property makes 
a simple loop-based solution correct.

  - Why initialize result to 0?
0 is the XOR identity element: x ^ 0 = x. Initializing to 0 ensures that XORing the first number produces 
itself, and subsequent operations correctly accumulate or cancel. Any other starting value would corrupt 
the final result.

* Logic:

1. Initialize result = 0
2. Iterate through each number in the array
3. XOR the number with result: result ^= num
4. After all iterations, result contains only the unpaired number (pairs have canceled to 0)
5. Return result

* **30-Second Pitch**:

I use the XOR bitwise operation. The key insight is that x ^ x = 0 and x ^ 0 = x, plus XOR is commutative. 
So XORing all numbers causes every duplicate pair to become 0, and the single number survives unchanged. 
It's elegant: one loop, O(1) space, O(n) time.

* **Rapid-Fire Version**:

- XOR identity: x ^ 0 = x
- XOR cancellation: x ^ x = 0
- Commutativity: order of XOR operations doesn't matter
- Pairs cancel automatically during iteration
- Single number emerges after all XOR operations

* **Ultra-Minimal One-Liner**:

- XOR all array elements to cancel duplicates and reveal the single number in O(n) time, O(1) space.

* **Complexity Analysis**:

- **Time Complexity:** O(n) — single pass through all n numbers
- **Space Complexity:** O(1) — only one variable (result)

* **Use Cases**:

- Error detection in data transmission
- Finding missing or unpaired elements
- Bit manipulation optimization in systems with memory constraints
"""

def single_non_duplicate_bitwise(nums: List[int]) -> int:
    """
    Find the single number in the array where every other number appears twice.

    Uses XOR properties:
    - x ^ x = 0
    - x ^ 0 = x
    - XOR is commutative and associative

    Time:  O(n)
    Space: O(1)
    """
    result = 0
    for num in nums:
        result ^= num
    return result
