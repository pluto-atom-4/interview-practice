"""
Stack Data Structure Explained Step-by-Step
---------------------------------------------
A Stack is a linear data structure that follows the LIFO (Last-In-First-Out) principle, where the last
element added is the first one to be removed. Stacks are fundamental for many algorithms including depth-first
search (DFS), expression evaluation, backtracking, and memory management. Understanding stacks is critical
for parsing, recursion, and solving problems related to nested structures.

Here is how the Stack works:

1. **LIFO Principle**: Last-In-First-Out ordering.
   - Most recently added element is removed first
   - Like a stack of plates: add on top, remove from top
   - Contrasts with Queue (FIFO: First-In-First-Out)

2. **Push Operation**: Add an element to the top of the stack.
   - Insert element at the end of the underlying list
   - Time Complexity: O(1) amortized (Python list append)
   - Updates the stack size by incrementing

3. **Pop Operation**: Remove and return the top element.
   - Remove and return the last element from the list
   - Time Complexity: O(1) for single pop
   - Raise IndexError if stack is empty (error handling)
   - Returns the most recently added element

4. **Peek Operation**: View the top element without removing it.
   - Access the last element without modification
   - Time Complexity: O(1)
   - Useful for checking what's next without consuming
   - Raise IndexError if stack is empty (error handling)

5. **isEmpty Check**: Determine if the stack is empty.
   - Check if underlying list has zero elements
   - Time Complexity: O(1)
   - Essential for preventing errors before pop/peek operations
   - Common pattern in many algorithms

6. **Size Query**: Get the current number of elements.
   - Return the length of underlying list
   - Time Complexity: O(1)
   - Supports both size() method and __len__ magic method
   - Enables Pythonic len(stack) syntax

Key Applications:
- **Expression Evaluation**: Converting infix to postfix, evaluating postfix expressions
- **Depth-First Search (DFS)**: Iterative DFS implementation using explicit stack
- **Backtracking**: Restoring state during recursive problem solving
- **Parentheses Matching**: Validating balanced brackets and delimiters
- **Function Call Stack**: Managing recursive calls and memory (system level)
- **Undo/Redo Operations**: Browser history, text editor operations
- **Tower of Hanoi**: Classic recursive algorithm with stack intuition

Example Operations:
- Create: stack = Stack()
- Push: stack.push(1), stack.push(2), stack.push(3)
- Peek: top = stack.peek() → returns 3
- Pop: value = stack.pop() → returns 3, stack now has [1, 2]
- Check: stack.is_empty() → returns False
- Size: stack.size() → returns 2

Time Complexity Analysis:
- Push: O(1) amortized
- Pop: O(1)
- Peek: O(1)
- isEmpty: O(1)
- Size: O(1)

Space Complexity: O(n) where n is the number of elements in the stack

This implementation uses Python's dynamic list which handles resizing automatically.
For interview contexts, be prepared to discuss:
- Why stacks are LIFO vs queues being FIFO
- Real-world applications (browser back button, function calls)
- How to detect problems that require stacks (nested structures, DFS)
- Trade-offs between iterative (stack) and recursive solutions
- How system stack differs from user-defined stacks
"""


class Stack:
    """Simple stack implementation using Python list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __len__(self):
        return self.size()

    def __repr__(self):
        return f"Stack({self._items})"
