"""
Valid Parentheses Problem Explained Step-by-Step
-------------------------------------------------
The Valid Parentheses problem is a classic stack-based algorithm that validates whether a string
of brackets is properly balanced and correctly ordered. This problem demonstrates the stack data
structure for pattern matching and is fundamental for parsing, compiler design, and syntax validation.

Here is how the process works:

1. **Stack Data Structure**: Use a stack to track opening brackets.
   - Push opening brackets ('(', '[', '{') onto the stack
   - When encountering closing brackets, check if the top matches
   - Stack ensures LIFO (Last In First Out) matching of pairs

2. **Matching Pairs Mapping**: Create a dictionary to map closing brackets to opening brackets.
   - This allows O(1) lookup to verify bracket pairs match
   - Pairs: ')' → '(', ']' → '[', '}' → '{'
   - Simplifies validation logic and improves code readability

3. **Three-State Validation**: For each character, perform one of three actions.
   - If opening bracket: push to stack (prepare for matching)
   - If closing bracket: check stack top matches, then pop
   - If invalid character: return False immediately (early termination)

4. **Closing Bracket Validation**: When encountering a closing bracket.
   - Check if stack is empty (unmatched closing bracket)
   - Check if top of stack matches the closing bracket
   - Both conditions must be true; otherwise, return False
   - Pop the matched opening bracket from stack

5. **Final Verification**: After processing all characters.
   - Stack must be empty for valid parentheses
   - Non-empty stack means unmatched opening brackets
   - Return True only if stack is completely empty

6. **Algorithm Flow**:
   - Initialize empty stack and closing-to-opening bracket mapping
   - Iterate through each character in the string
   - For each character, determine if it's opening, closing, or invalid
   - Perform appropriate stack operation or validation
   - Return final validation result (empty stack check)

Example: s = "({[]})"
- Process: '(' push, '{' push, '[' push, ']' pop match, '}' pop match, ')' pop match
- Stack states: ['('] → ['(', '{'] → ['(', '{', '['] → ['(', '{'] → ['('] → []
- Result: True (all brackets matched and properly closed)

Example: s = "({[}])"
- Process: '(' push, '{' push, '[' push, '}' check fails ([ doesn't match })
- Result: False (brackets not properly ordered)

Time Complexity: O(n) where n = len(s), single pass through string with O(1) stack operations
Space Complexity: O(n) worst case for stack (all opening brackets), typically O(1) for valid strings

This algorithm demonstrates stack applications for pattern matching and is essential for understanding
parsing algorithms, expression evaluation, syntax checkers, and code editors with bracket matching features.
"""


def is_valid_parentheses(s: str) -> bool:

    """
    Determine if the input string of parentheses is valid.
    Valid means:
      - Every opening bracket has a matching closing bracket.
      - Brackets close in the correct order.
    """

    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in pairs.values():  # opening bracket
            stack.append(ch)
        elif ch in pairs:  # closing bracket
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            # invalid character for this problem
            return False

    return len(stack) == 0
