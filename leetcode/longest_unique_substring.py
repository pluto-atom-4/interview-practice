"""
Longest Unique Substring (Also Known As Longest Substring Without Repeating Characters)
----------------------------------------------------------------------------------------
The Longest Unique Substring problem finds the longest substring of a given string that contains
no repeating characters. This problem is a classic sliding window algorithm that's essential for
interviews as it demonstrates understanding of the sliding window technique, hash tables for character
tracking, and efficient string manipulation.

The key insight is using a sliding window with a character index tracker to dynamically shrink the
window when a duplicate character is encountered, maintaining an invariant that the current window
always contains unique characters.

Here is how the process works:

1. **Handle Edge Cases**: Check for None or empty input.
   - Return empty string if input is None or empty
   - Prevents errors in subsequent operations
   - Ensures graceful handling of degenerate input

2. **Initialize Tracking Structure**: Create a dictionary/array to track character positions.
   - Dictionary maps each character to its last seen index
   - Allows O(1) lookup to detect if a character is in the current window
   - ASCII assumption: 256 possible characters for standard text
   - Initialize all positions to -1 (not seen yet)

3. **Sliding Window Initialization**: Set up window boundaries and tracking variables.
   - start: left boundary of the current window
   - end: right boundary (expands as we iterate)
   - maxLen: length of the longest unique substring found so far
   - maxStart: starting index of the longest substring

4. **Expand Window Right**: Iterate through the string with the end pointer.
   - For each character, check if it's in the current window
   - Current window contains characters from index start to end
   - A character is in the window if lastSeen[c] >= start

5. **Handle Duplicate Characters**: Shrink window from the left when a duplicate is found.
   - If character was seen inside the window (lastSeen[c] >= start)
   - Move start pointer to lastSeen[c] + 1 to exclude the previous occurrence
   - This maintains the invariant: current window has no duplicates
   - No need to remove characters manually; just move the start pointer

6. **Update Character Position**: Record the current position of the character.
   - lastSeen[c] = end
   - This is done after handling duplicates so the new position is recorded
   - Enables detection of future duplicates

7. **Update Maximum**: Check if current window is longer than the best found so far.
   - currentLen = end - start + 1
   - If currentLen > maxLen: update both maxLen and maxStart
   - Track the starting position to reconstruct the substring

8. **Extract Result**: Return the substring using maxStart and maxLen.
   - Reconstruct the longest unique substring from the original string
   - Return empty string if no characters were processed

Example Walkthrough: s = "abcabcbb"
- Start at 'a': window "a", maxLen=1, maxStart=0
- 'b': window "ab", maxLen=2, maxStart=0
- 'c': window "abc", maxLen=3, maxStart=0
- 'a' (duplicate): move start to 1, window "bca", maxLen still 3
- 'b' (duplicate): move start to 2, window "cab", maxLen still 3
- 'c' (duplicate): move start to 3, window "ab", maxLen still 3
- 'b' (duplicate): move start to 4, window "b", maxLen still 3
- 'b' (duplicate): move start to 5, window "b", maxLen still 3
- Result: substring from index 0 with length 3 = "abc"

Time Complexity: O(n) - single pass through the string with two pointers (start, end)
                 Each character is visited at most twice (once by end pointer, once by start pointer)
                 Character lookup and position update in dictionary are O(1) operations

Space Complexity: O(min(m, n)) - where n is string length, m is character set size (256 for ASCII)
                  Dictionary stores at most m characters
                  For typical ASCII: O(256) = O(1)

Algorithm Style: Imperative sliding window with character tracking
                Two-pointer technique for optimal substring handling
                Dictionary-based state management for O(1) duplicate detection

This algorithm is essential for understanding sliding window patterns, which are fundamental
for solving many substring/subarray problems in technical interviews.
"""

from typing import Tuple


def find_longest_unique_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.

    Args:
        s: Input string to search

    Returns:
        The longest substring with all unique characters.
        Returns empty string if input is None, empty, or has no valid substring.

    Time Complexity: O(n) - single pass through the string
    Space Complexity: O(min(m, n)) - character position tracking dictionary
    """
    if not s:
        return ""

    # Dictionary to track the last seen index of each character
    last_seen = {}

    max_len = 0
    start = 0  # sliding window start
    max_start = 0  # start index of the longest unique substring

    for end in range(len(s)):
        char = s[end]

        # If character seen inside current window, move start pointer
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1

        # Update the last seen index of current character
        last_seen[char] = end
        current_len = end - start + 1

        # Update max if current window is longer
        if current_len > max_len:
            max_len = current_len
            max_start = start

    # Return the longest unique substring
    return s[max_start : max_start + max_len]


def find_longest_unique_substring_with_length(s: str) -> Tuple[str, int]:
    """
    Find the longest substring without repeating characters and return both substring and length.

    Args:
        s: Input string to search

    Returns:
        Tuple of (longest_substring, length)

    Time Complexity: O(n)
    Space Complexity: O(min(m, n))
    """
    result = find_longest_unique_substring(s)
    return result, len(result)
