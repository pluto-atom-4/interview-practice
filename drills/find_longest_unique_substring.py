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

1. Initialize `start` pointer (window beginning), `max_length` and `longest_substring` trackers
2. Iterate through each character with its index `i`
3. Check if the character exists in `last_seen` AND its index is within current window (`>= start`)
4. If yes, move `start` to one position after the character's previous occurrence (skip the old instance)
5. Update `last_seen[char]` with current index
6. Calculate current window length and update max_length and longest_substring if improved
7. Return the longest_substring after processing all characters

* **30-Second Pitch**:

I use a sliding window with character tracking—a dictionary stores each character's most recent index.
As I iterate through the string, when I encounter a repeated character within the current
window, I move the start pointer to skip the old occurrence. This ensures each character
is visited twice at most—once to expand the window, once as the start pointer. The time
complexity is O(n) with a single pass and O(1) space (at most 256 ASCII characters).

* **Rapid-Fire Version**:

- Sliding window approach with two pointers (start and end via loop index)
- Hash table stores last seen index, not just presence
- When duplicate found within window: move start past previous occurrence
- Single pass: O(n) time, O(1) space (bounded character set)
- Track max_length and longest_substring during iteration

* **Ultra-Minimal One-Liner**:

- Sliding window with character position tracking in a hash table finds the longest unique substring in O(n) time by jumping past repeated characters.

* **Complexity Analysis**:

- **Time Complexity:** O(n) – Single pass through the string; each character is visited at most twice (once by end pointer, once by start pointer advancing past it)
- **Space Complexity:** O(min(m, k)) where m is string length and k is the character set size; in practice O(1) for fixed alphabets (≤256 ASCII, ≤26 lowercase, etc.)

* **Use Cases**:

- Interview screening: Tests fundamental data structure knowledge (hash tables, sliding window)
- Substring optimization: Problems requiring longest/shortest substrings with constraints
- Pattern detection: Finding non-repeating sequences in DNA strands, network packets, or log analysis
- Video streaming: Finding longest buffer windows without frame duplication
"""


def find_longest_unique_substring(s: str) -> str:
    """
    Finds the longest substring without repeating characters.

    This function uses a sliding window approach with two pointers and a dictionary
    to track the last seen index of each character. It runs in O(n) time complexity.

    Args:
        s (str): Input string.

    Returns:
        str: The longest substring without repeating characters.
    """
    if not s:
        return ""

    last_seen = {}  # Dictionary to store the last seen index of each character
    start = 0  # Start index of the current substring
    max_length = 0  # Length of the longest substring found
    longest_substring = ""  # The longest substring without repeating characters

    # For each character at index `end`, check if it exists in the current window (using `lastSeen[c] >= start`). If yes, move `start` to skip the old occurrence. Update `lastSeen` and compute window length. Returns the longest unique substring. Time: O(n), Space: O(1) with ASCII assumption (fixed 256 characters).
    for i, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            # Character is repeated within the current window
            start = last_seen[char] + 1 # Move start to one position after the last occurrence

        last_seen[char] = i  # Update the last seen index of the character

        wk_current_length = i - start + 1  # Calculate current substring length
        if wk_current_length > max_length:
            max_length = wk_current_length
            longest_substring = s[start : i + 1]  # Update the longest substring

    return longest_substring
