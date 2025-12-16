"""
String to Integer (atoi) Algorithm Explained Step-by-Step
----------------------------------------------------------
The String to Integer (atoi) problem is a classic string parsing algorithm that converts a string
to a signed 32-bit integer. This problem tests string manipulation, edge case handling, and understanding
of valid input parsing. It's commonly asked in technical interviews to assess attention to detail and
robust error handling. The algorithm must handle whitespace, signs, digits, and boundary constraints.

Here is how the process works:

1. **Whitespace Trimming**: Remove leading whitespace characters.
   - Use lstrip() to remove all leading spaces from the input string
   - After trimming, if the string is empty, return 0 immediately
   - This handles edge cases where input is only whitespace

2. **Sign Detection**: Identify and extract the sign prefix.
   - Check if the first character (after trimming) is '+' or '-'
   - If '-' is found, set sign = -1; otherwise sign = 1
   - Determine the starting index for digit reading (skip sign if present)
   - This correctly handles negative numbers and explicit positive sign

3. **Digit Parsing**: Read consecutive digits from the string.
   - Iterate through characters starting from the determined index
   - Stop when encountering the first non-digit character
   - Collect all consecutive digits into a list or string
   - Ignore all characters after the first non-digit is encountered

4. **String to Integer Conversion**: Convert the collected digits to an integer.
   - Join the digit list into a single string
   - Use int() to convert the string to an integer
   - Multiply by the sign to apply negative/positive adjustment
   - Handle the case where no digits were found (return 0)

5. **Range Clamping (32-bit Integer Bounds)**: Enforce the INT32 range.
   - INT_MIN = -2^31 = -2,147,483,648
   - INT_MAX = 2^31 - 1 = 2,147,483,647
   - If result < INT_MIN, return INT_MIN (underflow)
   - If result > INT_MAX, return INT_MAX (overflow)
   - This prevents values outside the 32-bit signed integer range

6. **Edge Cases to Handle**:
   - Only whitespace: return 0
   - Only sign without digits: return 0
   - Non-digit characters before digits: return 0
   - Leading zeros in digits: handled by int() conversion
   - Overflow/underflow: clamped to INT32 bounds
   - Mixed valid/invalid characters: stop at first invalid character

Example: myAtoi("42")
- Trim: "42"
- Sign: 1 (positive)
- Digits: ['4', '2']
- Convert: int("42") * 1 = 42
- Clamp: 42 (within bounds)
- Result: 42

Example: myAtoi("  -42")
- Trim: "-42"
- Sign: -1
- Digits: ['4', '2']
- Convert: int("42") * -1 = -42
- Clamp: -42 (within bounds)
- Result: -42

Example: myAtoi("4193 with words")
- Trim: "4193 with words"
- Sign: 1
- Digits: ['4', '1', '9', '3'] (stop at space)
- Convert: int("4193") * 1 = 4193
- Clamp: 4193 (within bounds)
- Result: 4193

Time Complexity: O(n) where n is the length of the input string (single pass through string)
Space Complexity: O(d) where d is the number of digits (for storing collected digits)

This algorithm demonstrates robust string parsing, state management, and boundary handling—
essential skills for systems programming, input validation, and parsing tasks in interviews.
"""


INT_MIN = -2**31
INT_MAX = 2**31 - 1


def myAtoi(s: str) -> int:
    """
    Pure functional-style implementation of atoi.
    """

    # Step 1: trim leading whitespace
    trimmed = s.lstrip()

    # If empty after trimming → return 0
    if not trimmed:
        return 0

    # Step 2: determine sign
    sign = -1 if trimmed[0] == '-' else 1
    start_index = 1 if trimmed[0] in "+-" else 0

    # Step 3: read digits only
    digits = []
    for ch in trimmed[start_index:]:
        if not ch.isdigit():
            break
        digits.append(ch)

    if not digits:
        return 0

    # Convert digit list → integer
    num = int("".join(digits)) * sign

    # Step 4: clamp to 32-bit signed range
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num
