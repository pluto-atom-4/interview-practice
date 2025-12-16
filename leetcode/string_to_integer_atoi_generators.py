"""
String to Integer (atoi) - Generator Pipeline Implementation
-------------------------------------------------------------
This is a functional programming variant of the atoi algorithm using Python generators and
pipeline-style processing. While generators add complexity, they demonstrate advanced Python
techniques like lazy evaluation, composable iterators, and functional style. This implementation
highlights an alternative approach to string processing without explicitly building intermediate
lists, though for interviews, the straightforward iterative approach (string_to_integer_atoi.py)
is typically preferred for clarity.

Core Algorithm Steps (Same as standard implementation):

1. **Whitespace Trimming**: Remove leading whitespace.
   - Use lstrip() to remove all leading spaces from the input string
   - After trimming, if the string is empty, return 0 immediately

2. **Sign Detection**: Identify the sign prefix.
   - Check the first character for '+' or '-'
   - Set sign = -1 if '-', otherwise sign = 1
   - Slice the rest of the string starting after the sign (if present)

3. **Digit Parsing**: Read consecutive digits from the string.
   - Define a generator expression to stream digits: (ch for ch in rest if ch.isdigit())
   - Note: This generator in the code is created but not fully utilized
   - Instead, collect digits manually until the first non-digit is encountered
   - This hybrid approach maintains clarity while demonstrating generator syntax

4. **String to Integer Conversion**: Convert collected digits to an integer.
   - Join the digit list into a single string
   - Use int() to convert the string to an integer
   - Multiply by the sign to apply the sign adjustment

5. **Range Clamping**: Enforce 32-bit integer bounds.
   - INT_MIN = -2^31, INT_MAX = 2^31 - 1
   - Use max(INT_MIN, min(INT_MAX, num)) for compact clamping
   - This is a Pythonic one-liner alternative to explicit if statements

Functional Programming Concepts Demonstrated:

- **Generators**: Lazy evaluation with generator expressions
- **Slicing**: Functional string manipulation without mutation
- **Built-ins**: Use of max/min for conditional logic
- **Composability**: Chaining operations functionally (though partially implemented here)

Key Difference from Standard Implementation:
- Uses max/min for clamping instead of explicit if statements
- Demonstrates generator expression syntax (though not fully utilized)
- More concise but potentially less readable for interviews

Example: myAtoi_generators("  -42")
- Trim: "-42"
- Sign: -1
- Rest: "42"
- Collected digits: ['4', '2']
- Convert: int("42") * -1 = -42
- Clamp: max(-2147483648, min(2147483647, -42)) = -42
- Result: -42

Time Complexity: O(n) where n is the length of the input string
Space Complexity: O(d) where d is the number of digits

Interview Note: While this demonstrates functional programming knowledge, the straightforward
iterative version is clearer and more maintainable. Use this style only when your interviewer
specifically asks for functional approaches or advanced Python techniques.
"""

INT_MIN = -2**31
INT_MAX = 2**31 - 1

def myAtoi_generators(s: str) -> int:
    """
    Pure functional atoi using generator pipelines.
    """

    # Step 1: trim leading whitespace
    trimmed = s.lstrip()
    if not trimmed:
        return 0

    # Step 2: detect sign
    first = trimmed[0]
    sign = -1 if first == "-" else 1
    rest = trimmed[1:] if first in "+-" else trimmed

    # Step 3: stream digits until non-digit
    digits = (ch for ch in rest if ch.isdigit())

    # Collect digits until first non-digit
    collected = []
    for ch in rest:
        if not ch.isdigit():
            break
        collected.append(ch)

    if not collected:
        return 0

    num = int("".join(collected)) * sign

    # Step 4: clamp
    return max(INT_MIN, min(INT_MAX, num))
