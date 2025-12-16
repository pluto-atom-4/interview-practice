"""
String to Integer (atoi) - State Machine with functools.reduce
---------------------------------------------------------------
This is an advanced functional programming variant of the atoi algorithm using functools.reduce
and an explicit state machine encoded in tuples. This approach demonstrates pure functional
programming, state encapsulation, and the reducer pattern popular in functional languages and
Redux-style state management. While powerful for certain domains, this approach is less common
in technical interviews and may be considered over-engineered for this problem.

Core Algorithm: State Machine Approach

The algorithm uses a state machine with four states and a reducer function that processes
each character sequentially, updating the state tuple (stage, sign, value).

State Transitions:

1. **"start" State**: Initial state, process whitespace and determine sign.
   - If character is space ' ': stay in "start" state (skip whitespace)
   - If character is '+' or '-': transition to "sign" state with appropriate sign flag
   - If character is digit: transition to "digits" state and accumulate the digit value
   - If character is anything else: transition to "done" state with value 0 (invalid input)

2. **"sign" State**: State after processing sign, now expect digits.
   - If character is digit: transition to "digits" state with accumulated digit
   - If character is anything else: transition to "done" state with value 0 (no digits after sign)

3. **"digits" State**: Processing consecutive digits, accumulate numeric value.
   - If character is digit: stay in "digits" state, update value: value * 10 + digit
   - If character is anything else: transition to "done" state with current accumulated value
   - Note: The accumulation uses: new_value = value * 10 + int(ch)

4. **"done" State**: Final state, no more processing.
   - All subsequent characters are ignored, state remains unchanged
   - This implements the "stop at first non-digit" behavior

How functools.reduce Works:

- reduce(function, iterable, initial_value) applies function sequentially to each element
- Starting with initial_value ("start", 1, 0), it processes each character
- The reducer function (step) receives current state and current character
- Returns the updated state, which becomes input for the next character
- After processing all characters, the final state is returned

Example Walkthrough: myAtoi_reduce("  -42")

Initial State: ("start", 1, 0)

Character ' ':  state = ("start", 1, 0)
Character ' ':  state = ("start", 1, 0)
Character '-':  state = ("sign", -1, 0)   [moved to "sign" stage, sign = -1]
Character '4':  state = ("digits", -1, 4) [moved to "digits" stage, value = 4]
Character '2':  state = ("digits", -1, 42) [accumulated: 4 * 10 + 2 = 42]

Final State: ("digits", -1, 42)
Extract: sign = -1, value = 42
Result: -1 * 42 = -42
Clamp: max(-2147483648, min(2147483647, -42)) = -42
Output: -42

Advantages of This Approach:

- **Pure Functional**: No mutable state, all operations return new state tuples
- **State Encapsulation**: All relevant data is contained in the state tuple
- **Clear Transitions**: State machine pattern is explicit and easy to reason about
- **Composability**: The reducer can be extended or modified easily for variants

Disadvantages for Interviews:

- **Complexity**: More complex than straightforward iteration for most interviewers
- **Python Style**: Not idiomatic Python; more typical in Lisp/Haskell than Python
- **Debugging**: State tuples can be harder to debug than explicit variables
- **Readability**: Less immediately clear what's happening compared to imperative style

Key Techniques Demonstrated:

- State Machine Pattern: Explicit state tracking with discrete stages
- Functional Reducer: Using reduce() instead of explicit loops
- Tuple Unpacking: Decomposing and recomposing state tuples
- Functional Composition: Pure functions without side effects

Time Complexity: O(n) where n is the length of the input string
Space Complexity: O(1) for state tracking (state tuple is fixed size)

Interview Recommendation: Use the standard iterative version for clarity. Show this version
only if the interviewer specifically asks for functional programming techniques or you want
to demonstrate advanced Python knowledge after solving the main problem correctly.
"""

from functools import reduce

INT_MIN = -2**31
INT_MAX = 2**31 - 1

def myAtoi_reduce(s: str) -> int:
    """
    Pure functional atoi using functools.reduce.
    State machine encoded in the reducer.
    """

    # State fields:
    # (stage, sign, value)
    # stage: "start", "sign", "digits", "done"

    def step(state, ch):
        stage, sign, value = state

        if stage == "done":
            return state

        if stage == "start":
            if ch == " ":
                return state
            if ch in "+-":
                return ("sign", -1 if ch == "-" else 1, 0)
            if ch.isdigit():
                return ("digits", sign, int(ch))
            return ("done", sign, 0)

        if stage == "sign":
            if ch.isdigit():
                return ("digits", sign, int(ch))
            return ("done", sign, 0)

        if stage == "digits":
            if ch.isdigit():
                new_value = value * 10 + int(ch)
                return ("digits", sign, new_value)
            return ("done", sign, value)

        return state

    # Initial state: stage="start", sign=1, value=0
    _, sign, value = reduce(step, s, ("start", 1, 0))

    result = sign * value
    return max(INT_MIN, min(INT_MAX, result))
