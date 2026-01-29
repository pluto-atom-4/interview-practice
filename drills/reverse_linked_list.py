from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional

"""
## Problem Statement

Reverse a singly linked list by rearranging node pointers so that the direction of traversal is inverted. 
This classic problem tests understanding of pointer manipulation, in-place algorithms, and linked list 
fundamentals—core skills for systems and algorithm interviews.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Three-Pointer Iterative Reversal**:

Iterate through the list once, maintaining three pointers to capture each node's next reference before 
modifying it. Reverse the direction of each pointer as we progress, transforming the list from forward to 
backward without requiring extra space or recursion.

* Key Concepts:

  - Why capture nxt = current.next before modifying current.next?
We need the address of the next node before we overwrite current.next. Without capturing it, we'd lose 
the reference and unable to continue traversal. This is the critical insight that prevents infinite loops 
or incomplete reversal.

  - Why use three pointers (prev, current, nxt) instead of fewer?
prev represents the reversed portion; current is the node being processed; nxt is the unreversed portion. 
With fewer pointers, we'd lose track of where to go next. Three pointers elegantly encapsulate the state 
needed for safe pointer reversal.

  - Why does the new head become prev after the loop?
After reversal, prev points to the last processed node—which was originally the tail and is now the head. 
The original head's next pointer becomes None (set when prev started as None), making it the new tail.

* Logic:

1. Initialize prev = None, current = head
2. While current is not None:
   a. Capture nxt = current.next (preserve reference)
   b. Point current.next back to prev (reverse the pointer)
   c. Move prev to current (advance reversed portion)
   d. Move current to nxt (advance to next unprocessed node)
3. Return prev as the new head

* **30-Second Pitch**:

I use three pointers to iteratively reverse the list in one pass. Before modifying each node's pointer, 
I save its next reference. Then I reverse its direction to point backward, slide all pointers forward, 
and repeat. After processing all nodes, the last processed node becomes the new head.

* **Rapid-Fire Version**:

- Three-pointer approach: prev, current, nxt
- Save nxt before reversing to avoid losing reference
- Reverse each pointer: current.next = prev
- Slide pointers: prev → current → nxt
- New head is the final prev

* **Ultra-Minimal One-Liner**:

- Iterative three-pointer reversal of linked list in O(n) time, O(1) space.

* **Complexity Analysis**:

- **Time Complexity:** O(n) — single pass through all n nodes
- **Space Complexity:** O(1) — only three pointers, no additional data structures

* **Use Cases**:

- Undo/redo stacks (reversing action history)
- Palindrome checking in linked lists
- Algorithmic foundations for more complex list manipulations
"""

@dataclass
class ListNode:
    value: int
    next: Optional["ListNode"] = None


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list.

    Example:
        1 -> 2 -> 3 -> None
        becomes
        3 -> 2 -> 1 -> None

    Time:  O(n)
    Space: O(1)
    """
    prev = None
    current = head

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev


# Helper utilities for tests
def build_linked_list(values: Iterable[int]) -> Optional[ListNode]:
    head = None
    tail = None

    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result
