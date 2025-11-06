"""
Custom Hash Function Algorithm Explained Step-by-Step
----------------------------------------------------
A custom hash function is a computational algorithm that transforms input data (keys) into fixed-size
hash values for efficient data storage and retrieval. This implementation combines multiple mathematical
operations to create a robust hash function that minimizes collisions and provides good distribution.
Hash functions are fundamental for hash tables, dictionaries, caching systems, and data integrity verification.

Here is how the process works:

1. **Initialization**: Start with a seed value (default 0).
   - hash_val = seed (provides initial state for hash computation)
   - Seed allows for different hash values for same input across different contexts
   - Useful for implementing multiple hash functions or adding randomization

2. **Character Processing**: Iterate through each character in the input string.
   - for char in key: (process each character sequentially)
   - Convert character to its ASCII/Unicode byte value using ord(char)
   - Sequential processing ensures all characters contribute to final hash

3. **Addition Operation**: Add character's byte value to current hash.
   - hash_val += byte (accumulates character values)
   - Simple addition ensures every character affects the hash value
   - Provides basic mixing of input data into hash state

4. **Multiplication**: Amplify changes using prime number multiplication.
   - hash_val *= 31 (prime multiplier spreads values across hash space)
   - Prime numbers reduce patterns and improve distribution
   - Creates exponential growth that separates similar inputs

5. **XOR with Rotation**: Introduce non-linearity and bit mixing.
   - hash_val ^= rotate_left(byte, 5) (XOR with rotated byte value)
   - Rotation spreads individual bits across different positions
   - XOR operation adds non-linear transformation for better distribution

6. **Overflow Control**: Simulate 32-bit integer overflow behavior.
   - hash_val &= 0xFFFFFFFF (mask to keep only lower 32 bits)
   - Ensures consistent behavior across different platforms
   - Prevents unlimited growth of hash values

Example: key = "hello"
- Process: Initialize with 0, add 'h'(104), multiply by 31, XOR with rotated bits
- Continue: Add 'e'(101), multiply, XOR, repeat for all characters
- Result: Final 32-bit hash value with good distribution properties

Time Complexity: O(n) where n = length of input string
Space Complexity: O(1) constant space usage
Collision Rate: Low due to multiple mathematical operations and prime multiplication

The rotate_left function performs circular bit shifting, moving bits to the left and wrapping
overflow bits to the right side. This operation maximizes bit mixing and reduces clustering
in the hash output, creating better distribution across the hash table buckets.

This algorithm demonstrates hash function design principles and is essential for
understanding hash tables, data structures, and collision resolution strategies.
"""

def rotate_left(value, shift, width=32):
    shift %= width
    return ((value << shift) & (2**width - 1)) | (value >> (width - shift))

def custom_hash(key: str, seed: int = 0) -> int:
    hash_val = seed
    for char in key:
        byte = ord(char)
        hash_val += byte
        hash_val *= 31
        hash_val ^= rotate_left(byte, 5)
        hash_val &= 0xFFFFFFFF  # simulate 32-bit overflow
    return hash_val
