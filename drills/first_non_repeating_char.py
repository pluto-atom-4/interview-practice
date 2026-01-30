"""
## Problem Statement

Find the first non-repeating character in a string. This classic string manipulation problem 
tests understanding of hash tables and the importance of iteration order. The goal is to efficiently 
identify the first character that appears exactly once while handling edge cases like empty strings 
and strings with all repeating characters.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using a **two-pass hash table approach**:

  Two passes ensure we maintain the original string order while tracking frequencies. The first pass 
  counts all character frequencies; the second pass finds the first character with count 1.

* Key Concepts:

  - **Why two passes instead of one?**
    
    A single pass could track characters, but we wouldn't know if a character is final without seeing 
    the entire string. Two passes decouple counting from searching, making the logic clear and correct. 
    This is a trade-off: O(n) time for clarity over a more complex single-pass approach.

  - **Why preserve string order in iteration?**
    
    We iterate through the original string (not the hash table) to find the first non-repeating character. 
    Dictionaries in Python 3.7+ maintain insertion order, but iterating over the original string ensures 
    we check characters in their actual appearance order—this is critical for correctness.

  - **Why return None instead of raising an exception?**
    
    Returning None is Pythonic for "not found" scenarios. It allows the caller to handle the absence 
    gracefully without exception handling overhead, making the function more usable in conditional logic.

* Logic:

  1. Handle edge case: Return None immediately if the string is empty
  2. Initialize an empty dictionary to track character frequencies
  3. First pass: iterate through the string, incrementing the frequency count for each character
  4. Second pass: iterate through the string again, checking each character's frequency
  5. Return the first character whose frequency is exactly 1
  6. If no such character is found after the second pass, return None

* **30-Second Pitch**:

  "I use a two-pass hash table approach. First, I iterate through the string counting character 
  frequencies in a dictionary. Then, I iterate through the string again and return the first character 
  with a frequency of 1. This ensures I find the first non-repeating character while preserving 
  the original order. If no such character exists, I return None."

* **Rapid-Fire Version**:

  - Count frequencies in first pass using a hash table (dictionary)
  - Search for first character with count=1 in second pass
  - Two passes allow easy order preservation and correct logic
  - Return None if no unique character found
  - Handles empty strings gracefully

* **Ultra-Minimal One-Liner**:

  - Hash table + two-pass scan to find the first character with frequency 1 in O(n) time and O(k) space.

* **Complexity Analysis**:

  - **Time Complexity:** O(n) where n is the string length. First pass: count all characters (n iterations). 
    Second pass: find first non-repeating character (worst case n iterations). Total: 2n = O(n).
  
  - **Space Complexity:** O(k) where k is the number of unique characters in the string. The hash table 
    stores at most k entries (bounded by alphabet size in many cases, e.g., 26 for lowercase English letters).

* **Use Cases**:

  - Text processing and search algorithms where finding unique characters is needed
  - Data validation and deduplication tasks
  - Interview preparation for demonstrating hash table and iteration order understanding
  - String manipulation in real-world applications (e.g., finding unique patterns in logs)
"""

from __future__ import annotations

from typing import Optional


def find_first_non_repeating(s: str) -> Optional[str]:
    if not s:
        return None

    freq = {}

    # Count character frequencies
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Return first character with frequency of 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    return None