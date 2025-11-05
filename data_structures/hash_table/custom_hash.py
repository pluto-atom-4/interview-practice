"""
hash functions that combine several operations: addition, multiplication, XOR, and bit rotation.

- Addition: Adds each character’s byte value to the hash.
- Multiplication: Amplifies changes using a prime multiplier.
- XOR: Introduces non-linearity.
- Rotation: Mixes bits to reduce clustering.
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
