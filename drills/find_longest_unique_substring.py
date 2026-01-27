"""
## Problem Statement

Given a string of characters, find the longest contiguous substring without repeating characters.
Example: "abcabcbb" → "abc" (length 3). The goal is to achieve O(n) time complexity with a single pass through the string.
This problem tests sliding window mastery, hash table usage, and efficient pointer manipulation.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using the **Sliding Window with Character Tracking** approach:

This technique uses two pointers and a hash table to maintain the rightmost index of each character,
allowing us to efficiently skip over repeated characters without rescanning. By tracking where each
character was last seen, we can jump the left pointer directly past previous occurrences, guaranteeing
one pass through the string.

* Key Concepts:

  - **Character Tracking with Hash Table (Why?):**
Why: Enables O(1) lookup of whether a character exists in current window and where it was last seen.
How: Use a dictionary mapping each character to its most recent index. When a repeat is found, immediately
move the left pointer past the previous occurrence. This eliminates nested loops that would cause O(n²) complexity.

  - **Left Pointer Advancement (Why?):**
Why: Moves the window boundary when a repeated character is encountered, shrinking the window to exclude the repeat.
How: When character at position i is already in the window (last_seen[char] >= start), move start to last_seen[char] + 1.
This ensures every character in the active window [start, i] is unique.

  - **Max Length Tracking (Why?):**
Why: Preserves the best solution found so far, requiring minimal memory overhead.
How: After each character addition, check if current window length (i - start + 1) exceeds max_length.
If so, update max_length and store start_pos/end_pos for reconstruction.

* Logic:

1. Initialize empty hash table for character tracking, set start pointer to 0, reset max_length to 0
2. Iterate through each character by index (i) in the string
3. For each character, check if it exists in the current window (last_seen[char] >= start)
4. If character repeats in window, move start pointer to position after the previous occurrence (last_seen[char] + 1)
5. Update last_seen[char] to current index i (every character's position gets refreshed)
6. Calculate current window length and compare against max_length
7. If current length exceeds max_length, store new maximum and record current boundaries
8. Return the longest substring with its metadata (substring content, start index, end index, length)

* **30-Second Pitch**:

I use a sliding window with character tracking—a dictionary stores each character's most recent index. As I iterate,
if I encounter a repeated character in my current window, I jump my start pointer directly past its previous occurrence.
This avoids rescanning and keeps everything linear. I track the longest valid window I've seen, and return it with
its boundaries and length. The beauty is one pass through the string with O(k) space, where k is unique characters.

* **Rapid-Fire Version**:

- Sliding window: two pointers (start, end via loop index)
- Hash table: maps character → most recent index for O(1) repeats detection
- Repeat handling: move left pointer directly past previous occurrence, no nested loops
- Window shrinking: happens implicitly when start jumps forward
- Single pass: O(n) time because each character is visited exactly once
- Space trade-off: O(k) space where k ≤ 256 (unique characters)

* **Ultra-Minimal One-Liner**:

Sliding window with hash table tracking character positions enables one-pass O(n) detection of longest unique substring.

* **Complexity Analysis**:

- **Time Complexity:** O(n) where n = string length. Each character is visited exactly once by the right pointer (loop),
  and the left pointer only moves forward monotonically. No inner loops or rescans occur.

- **Space Complexity:** O(min(k, m)) where k = unique characters in string, m = max_char_set limit (default 256).
  The hash table stores at most 256 keys (or fewer if string has fewer unique characters). Independent of input size.

* **Use Cases**:

- Interview screening: Tests fundamental data structure knowledge (hash tables, sliding window)
- Substring optimization: Problems requiring longest/shortest substrings with constraints
- Pattern detection: Finding non-repeating sequences in DNA strands, network packets, or log analysis
- Video streaming: Finding longest buffer windows without frame duplication
"""
from typing import NamedTuple


class LongestSubstringResult(NamedTuple):
    substring: str
    start: int
    end: int
    length: int

def find_longest_unique_substring(
    s: str,
    max_char_set: int = 256,  # Allow limiting character set
    allowed_chars: set = None  # Optional character filter
) -> LongestSubstringResult:
    """
    Finds the longest substring without repeating characters.

    This function uses a sliding window approach with two pointers and a dictionary
    to track the last seen index of each character. It runs in O(n) time complexity.

    Args:
        s (str): Input string.
        max_char_set (int): Maximum number of unique characters allowed in the result.
                           If exceeded, the sliding window resets. Default: 256 (ASCII).
        allowed_chars (set): Optional set of allowed characters to consider.
                           If provided, only characters in this set are processed.
                           Default: None (all characters allowed).

    Returns:
        LongestSubstringResult: Named tuple containing:
            - substring: The longest substring without repeating characters
            - start: Start index of the substring
            - end: End index of the substring
            - length: Length of the substring

    Examples:
        >>> find_longest_unique_substring("abcabcbb")
        LongestSubstringResult(substring='abc', start=0, end=2, length=3)

        >>> find_longest_unique_substring("abcabcbb", allowed_chars={'a', 'b'})
        LongestSubstringResult(substring='ab', start=0, end=1, length=2)

        >>> find_longest_unique_substring("abcdef", max_char_set=3)
        LongestSubstringResult(substring='abc', start=0, end=2, length=3)
    """
    if not s:
        return LongestSubstringResult("", 0, 0, 0)
    
    # Validate max_char_set parameter
    if max_char_set <= 0:
        raise ValueError("max_char_set must be positive")

    last_seen = {}  # Dictionary to store the last seen index of each character
    start = 0       # Start index of the current substring
    max_length = 0  # Length of the longest substring found
    longest_substring = ""  # The longest substring without repeating characters
    start_pos = 0   # Start index of the longest substring
    end_pos = 0     # End index of the longest substring

    # Sliding window: for each character, check if it exists in the current window (last_seen[char] >= start).
    # If yes, move `start` to skip the old occurrence. Update `last_seen` with current index.
    # Track the longest substring without repeating characters.
    # Time: O(n), Space: O(k) where k = min(unique characters, max_char_set).
    for i, char in enumerate(s):
        # Skip characters not in allowed_chars if the filter is provided
        if allowed_chars is not None and char not in allowed_chars:
            continue

        # If we exceed max_char_set limit, shrink the window from the left
        if len(last_seen) >= max_char_set and char not in last_seen:
            # Remove the leftmost character from tracking
            left_char = s[start]
            if left_char in last_seen:
                del last_seen[left_char]
            start += 1

        # Handle repeated character within the current window
        if char in last_seen and last_seen[char] >= start:
            # Character is repeated within the current window
            start = last_seen[char] + 1  # Move start to one position after the last occurrence

        last_seen[char] = i  # Update the last seen index of the character

        # Calculate current substring length by counting allowed characters between start and i
        if allowed_chars is not None:
            # Count only allowed characters in current window
            current_length = sum(1 for j in range(start, i + 1) if s[j] in allowed_chars)
        else:
            # Count all characters in current window
            current_length = i - start + 1

        if current_length > max_length:
            max_length = current_length
            # Extract substring with only allowed characters if filter is applied
            if allowed_chars is not None:
                longest_substring = "".join(s[j] for j in range(start, i + 1) if s[j] in allowed_chars)
            else:
                longest_substring = s[start:i + 1]
            start_pos = start  # Track start index of longest substring
            end_pos = i  # Track end index of longest substring

    return LongestSubstringResult(
        substring=longest_substring,
        start=start_pos,
        end=end_pos,
        length=max_length
    )
