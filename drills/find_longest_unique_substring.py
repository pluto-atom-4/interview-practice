"""
Problem Statement:
Given a string of characters, find the longest substring without repeating characters.
What's the time complexity?

Example: "abcabcbb" → "abc" (length 3).

Goal: achieve O(n) time complexity with a single pass.

Whiteboard Coding Challenge Notes:
Use a sliding window with two pointers: track the longest substring without repeats
by maintaining the last-seen index of each character in an array, enabling one-pass
linear-time processing.
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
