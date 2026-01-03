"""
Valid Parentheses (Regex-Based) Problem Explained Step-by-Step
---------------------------------------------------------------
This is an alternative approach to the Valid Parentheses problem using regular expressions
instead of a stack. The regex-based method repeatedly removes valid bracket pairs until no
more can be removed. If the string becomes empty, all brackets are valid. This approach
demonstrates regex pattern matching and iterative reduction for bracket validation.

Here is how the process works:

1. **Input Validation**: Check for invalid characters early.
   - Use regex pattern [^()\[\]{} ] to detect non-bracket characters
   - Return False immediately if any invalid characters found
   - This filtering step ensures we only process valid bracket characters

2. **Regex Pattern Matching**: Create a pattern to match valid adjacent pairs.
   - Pattern: \(\)|\[]|{} represents three valid closing pairs
   - () matches left and right parentheses together
   - [] matches left and right square brackets together
   - {} matches left and right curly braces together
   - The pipe (|) operator means "or" (any of these three pairs)

3. **Iterative Reduction Strategy**: Repeatedly remove valid pairs.
   - Each iteration removes one or more consecutive valid pairs
   - After removal, new pairs may become adjacent (cascade effect)
   - Continue until no more pairs can be removed (previous == current)
   - This handles nested and mixed bracket scenarios

4. **Termination Condition**: Process stops when nothing changes.
   - Store previous string state before regex substitution
   - Compare after substitution to detect if changes occurred
   - When prev == s (no changes), exit the loop
   - This prevents infinite loops and signals completion

5. **Final Validation**: Check if string is completely empty.
   - Empty string means all brackets were paired and removed
   - Non-empty string means unmatched brackets remain
   - Return True only if result string is empty

6. **Algorithm Flow**:
   - Reject strings with invalid characters using regex search
   - Initialize previous string tracker for loop control
   - Loop: Substitute valid pairs with empty string
   - Continue until no substitutions occur (prev == current)
   - Return whether final result is empty string

Example: s = "({[]})"
- Initial: "({[]})"
- Pass 1: "({[]})" → "({)" (removed [])
- Pass 2: "({)" → "()" (removed {})
- Pass 3: "()" → "" (removed ())
- Result: True (string becomes empty)

Example: s = "({[}])"
- Initial: "({[}])"
- Pass 1: "({[}])" → "({[}])" (no valid adjacent pairs to remove)
- No changes, exit loop
- Result: False (string is not empty)

Time Complexity: O(n²) worst case - regex substitution is O(n), and we may do O(n) iterations
Space Complexity: O(n) for storing intermediate strings

Advantages: Simple, readable, leverages regex engine optimizations
Disadvantages: Slower than stack approach due to repeated string operations and iterations
Regex-based approach is useful for demonstrating pattern matching but not optimal for production use.

This algorithm demonstrates regex pattern matching and iterative problem-solving approaches,
useful for understanding text processing, pattern recognition, and algorithmic trade-offs.
"""

import pytest

from leetcode.valid_parentheses import is_valid_parentheses
from leetcode.valid_parentheses_regex import is_valid_parentheses_regex


@pytest.mark.parametrize(
    "func",
    [is_valid_parentheses, is_valid_parentheses_regex]
)
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(((((())))))", True),
        ("(((()", False),
        ("abc", False),
    ]
)
def test_valid_parentheses(func, input_str, expected):
    assert func(input_str) == expected
