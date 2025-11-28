"""
Asteroid Collision Problem Explained Step-by-Step
---------------------------------------------------
The Asteroid Collision problem is a classic stack-based algorithm that simulates the collision of asteroids
in a 1D line. Each asteroid has a position and direction: positive values move right, negative values move left.
When two asteroids collide, the smaller one explodes. If they have equal size, both explode. This problem
demonstrates stack data structures for tracking state and is essential for understanding collision detection,
event simulation, and stack-based problem solving in interviews.

Here is how the process works:

1. **Problem Setup**: Initialize a stack to track surviving asteroids.
   - Positive values represent asteroids moving right (→)
   - Negative values represent asteroids moving left (←)
   - Stack stores asteroids that haven't collided yet
   - Process asteroids in order from left to right

2. **Collision Detection**: Check if a collision occurs.
   - Collision only happens when right-moving asteroid meets left-moving asteroid
   - Current asteroid (ast < 0) moving left AND stack top (> 0) moving right
   - Other combinations (both moving same direction or away from each other) = no collision
   - If no collision possible, add current asteroid and continue to next

3. **Resolution Logic**: When collision detected, determine the outcome.
   - Top asteroid smaller: explodes, pop from stack and check next collision with current
   - Current asteroid smaller: explodes, mark alive=False and skip adding it
   - Both equal: both explode, pop from stack and mark alive=False
   - Use loop to handle cascading collisions with multiple stack asteroids

4. **Stack Processing**: Continue checking until no more collisions.
   - While loop handles chain reactions (one asteroid colliding with multiple)
   - Each iteration either removes top asteroid or causes current to explode
   - alive flag tracks if current asteroid survives for final stack insertion
   - After while loop, add current asteroid if it survived all collisions

5. **Survivor Addition**: Only add asteroids that survive all collisions.
   - If alive remains True after all collision checks, append to stack
   - Represents asteroids that either had no collisions or won all their collisions
   - Stack now contains all surviving asteroids in order of appearance

6. **Final Result**: Return the stack of surviving asteroids.
   - Stack represents final state after all collisions resolved
   - Maintains left-to-right order from original input
   - Each element survived or was the last standing after collisions
   - Return this as the final result

Example: asteroids = [5, 10, -5]
- Process 5: stack = [5]
- Process 10: 10 > 0 (moving right, no collision with 5) → stack = [5, 10]
- Process -5: -5 < 0 (moving left) meets 10 > 0 (moving right) → collision!
  - 10 > 5, so -5 explodes (alive = False)
  - 10 survives → stack = [5, 10]
- Result: [5, 10]

Time Complexity: O(n) where n = number of asteroids
- Each asteroid enters and exits the stack at most once
- Single pass through input with constant work per iteration

Space Complexity: O(n) for the stack
- Worst case: no collisions, all asteroids added to stack
- In-place processing would require modifications to input

This algorithm demonstrates stack-based simulation, collision detection logic, and handling cascading events.
Essential for understanding state machines, event processing, and stack-based problem solving.
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
