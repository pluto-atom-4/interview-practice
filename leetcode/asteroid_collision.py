"""
Asteroid Collision Problem - Stack Simulation Explained Step-by-Step
---------------------------------------------------------------------
The Asteroid Collision problem is a classic stack-based algorithm that simulates the collision of asteroids
in a 1D line. Each asteroid has a position and direction: positive values move right, negative values move left.
When two asteroids collide, the smaller one explodes. If they have equal size, both explode. This problem
demonstrates stack data structures for tracking state, collision detection logic, and event simulation, making
it essential for understanding state machines, cascading event processing, and interview problem solving.

Here is how the process works:

1. **Problem Setup**: Initialize a stack to track surviving asteroids.
   - Positive values represent asteroids moving right (→)
   - Negative values represent asteroids moving left (←)
   - Stack stores asteroids that haven't collided yet or survived collisions
   - Process asteroids in order from left to right
   - alive flag tracks if current asteroid survives until stack insertion

2. **Collision Detection**: Check if a collision occurs between asteroids.
   - Collision only happens: right-moving asteroid (> 0) meets left-moving asteroid (< 0)
   - Current asteroid ast < 0 (moving left) AND stack top stack[-1] > 0 (moving right)
   - Other combinations produce no collision: both same direction or moving away from each other
   - If collision not possible, add current asteroid to stack and continue

3. **Collision Resolution**: Determine outcome when collision is detected.
   - Compare absolute values: stack[-1] (top) vs -ast (current)
   - Top asteroid smaller: stack[-1] < -ast → top explodes, pop and continue loop
   - Current asteroid smaller: stack[-1] > -ast → current explodes, alive=False
   - Both equal: stack[-1] == -ast → both explode, pop stack and alive=False
   - Continue loop to handle cascading collisions with next asteroid below

4. **Cascading Collisions**: Handle chain reactions when asteroid survives.
   - While loop checks if current asteroid meets another from stack
   - After popping one asteroid from stack, might collide with asteroid below
   - Example: [5, 10, 5, -10] → 10 and 5 explode, then -10 collides with 5
   - Properly simulate physics by checking all potential collisions in sequence

5. **Survivor Addition**: Only add asteroids that survive all collision checks.
   - Check alive flag after while loop completes
   - If alive=True, asteroid survived all collisions or had none to begin with
   - Append only surviving asteroids to maintain correct final state
   - Stack now contains surviving asteroids in order

6. **Final Result**: Return the stack of surviving asteroids.
   - Stack represents final state after all collisions are resolved
   - Maintains left-to-right order from original asteroid sequence
   - Each element either had no collisions or won all collision encounters
   - Return as the final result

Example: asteroids = [5, 10, -5]
- Process 5: alive=True, no collision → stack = [5]
- Process 10: alive=True, 10 > 0, no collision possible → stack = [5, 10]
- Process -5: alive=True, -5 < 0 and stack[-1]=10 > 0 → collision!
  - 10 > 5, so -5 explodes (alive=False), don't add to stack
- Result: [5, 10]

Another example: asteroids = [8, -8]
- Process 8: alive=True, no collision → stack = [8]
- Process -8: alive=True, collision with 8
  - 8 == 8, both explode, pop stack and alive=False
- Result: []

Time Complexity: O(n) where n = number of asteroids
  - Each asteroid enters the stack at most once
  - Each asteroid exits the stack at most once
  - Single pass through input array, amortized constant work per asteroid

Space Complexity: O(n) for the stack
  - Worst case: no collisions occur, all asteroids survive
  - Stack can contain all n asteroids
  - Dominated by stack storage

Stack-Based Problem Patterns:
  - Simulation with state tracking: Use stack to maintain valid state
  - Collision/matching detection: Compare current with previous elements
  - Cascading events: While loop to handle chain reactions
  - Monotonic operations: Process elements maintaining properties

Related Stack Problems:
  - Daily Temperatures: Find next greater element
  - Trapping Rain Water: Stack tracks valid valleys
  - Evaluate Reverse Polish Notation: Stack for expression evaluation
  - Next Greater Element: Monotonic stack applications

This algorithm demonstrates stack-based simulation, collision resolution logic, cascading event handling,
and state machine design. Essential for understanding event processing, stack data structures, and the
pattern of comparing current elements with a maintained historical state in problems.
"""

from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    """
    Simulate asteroid collisions using a stack.
    Positive values move right, negative values move left.
    """
    stack = []
    for ast in asteroids:
        alive = True
        while alive and ast < 0 and stack and stack[-1] > 0:
            if stack[-1] < -ast:
                # top asteroid explodes, continue checking
                stack.pop()
                continue
            elif stack[-1] == -ast:
                # both explode
                stack.pop()
            # current asteroid explodes
            alive = False
        if alive:
            stack.append(ast)
    return stack
