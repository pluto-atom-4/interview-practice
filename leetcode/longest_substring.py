"""
## Problem Statement

Find the length of the longest contiguous substring without repeating characters. 
Given a string, return the maximum length of any substring that doesn't contain duplicate characters.
This tests sliding window optimization and hash table usage for tracking state.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Sliding Window with Hash Map**:

The sliding window technique maintains a dynamic range [left, right] of the string, expanding 
by moving the right pointer and contracting by moving the left pointer when duplicates are 
encountered. A hash map tracks the most recent index of each character, allowing O(1) duplicate 
detection and instant calculation of the new left boundary.

* Key Concepts:

  - **Why track the last index of each character in a hash map?**
  
    Storing the most recent position of each character enables O(1) lookup to detect duplicates 
    and immediately calculate where to move the left pointer. Without this, you'd need to search 
    backward or maintain a separate set, which would be less efficient. This design choice allows 
    the left pointer to skip directly past the previous occurrence of the duplicate character.

  - **Why check `last_seen[ch] >= left` before moving the left pointer?**
  
    This condition ensures we only move left if the duplicate character is actually within the 
    current window. Characters seen before the left boundary (outside the window) don't matter 
    because they're no longer part of our substring. Without this check, we'd incorrectly shrink 
    the window and lose valid longer substrings.

  - **Why update max_len at the end of each iteration?**
  
    After adjusting the window boundaries (left and right), we calculate the current window size 
    as `right - left + 1`. Tracking this after every character ensures we capture the longest 
    valid substring encountered. This is efficient because we only update once per character, 
    not once per potential substring.

* **30-Second Pitch**:

I use a sliding window approach with a hash map to track character positions. As I scan left 
to right, I expand the window by moving the right pointer. When I encounter a duplicate character 
that's inside my current window, I move the left pointer to just after the previous occurrence. 
By maintaining the character positions in a map, I can do this in constant time. The maximum 
window size I encounter is my answer—all in a single pass through the string.

* **Ultra-Minimal One-Liner**:

- Sliding window with hash map tracking last character positions for O(n) single-pass duplicate detection.

* **Complexity Analysis**:

- **Time Complexity:** O(n) where n is the string length. Each character is visited at most twice: 
  once by the right pointer and once by the left pointer advancing. The hash map operations 
  (lookup, insert, update) are O(1).
  
- **Space Complexity:** O(min(n, m)) where n is the string length and m is the character set size. 
  The hash map stores at most one entry per unique character. In the worst case (all unique 
  characters), it stores up to n characters; in practice, it's bounded by the charset size.

* **Use Cases**:

- Finding the longest run of unique characters in telemetry or sequence data
- Detecting repeating patterns in passwords (no repeated characters for x characters)
- Optimizing string processing in real-time systems where minimal passes are critical
- Foundation for more complex substring problems (longest with k distinct characters, etc.)

---

"""

from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """
    Return the length of the longest substring without repeating characters.

    Uses a sliding window with a dictionary tracking the last index of each character.
    Runs in O(n) time.
    """
    last_seen: Dict[str, int] = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1

        last_seen[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len
