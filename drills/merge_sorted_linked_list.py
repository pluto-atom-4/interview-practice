"""
## Problem Statement

Merge two sorted singly linked lists into a single sorted linked list by comparing node values 
and rearranging pointers. The goal is to do this in-place (without creating new nodes) and 
maintain O(n + m) time complexity. This tests understanding of pointer manipulation, list traversal, 
and dummy node patterns—essential for linked list problems in interviews.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Two-Pointer Merge** with a **Dummy Node** pattern:

This approach leverages the fact that both input lists are already sorted. By comparing values 
at the current positions and attaching the smaller node to our merged list, we can build the 
result in a single pass. The dummy node eliminates the need for special-case handling of the head.

* Key Concepts:

  - Why use a dummy node?
The dummy node provides a consistent starting point for our merged list, eliminating edge case 
handling for attaching the first real node. Instead of branching logic to set the head, we simply 
advance the dummy's next pointer and return dummy.next at the end. This is a classic interview 
pattern that reduces code complexity.

  - Why compare with <= instead of <?
Using <= ensures stable merging: when values are equal, we take from head1 first, maintaining 
the relative order of equal elements from the original lists. This matters for certain problems 
where stability is required (though often not critical for this specific problem).

  - Why attach the remainder list directly?
Once one list is exhausted, the remaining nodes in the other list are already sorted, so we can 
simply link them directly without further comparison. This avoids unnecessary iterations and is 
a key optimization that keeps the algorithm O(n + m).

* Logic:

1. Create a dummy node (value doesn't matter) and initialize current pointer to it
2. While both lists have remaining nodes, compare their head values
3. Attach the node with the smaller value to current.next and advance that list's pointer
4. Move current forward to the newly attached node
5. Once one list is exhausted, attach the remaining nodes from the other list
6. Return dummy.next (the actual head of the merged list)

* **30-Second Pitch**:

I'm using a two-pointer merge with a dummy node. I compare values from both lists, attach the 
smaller node to my merged list, and advance that list's pointer. Once one list is done, I attach 
the rest of the other list directly since it's already sorted. This runs in O(n + m) time with 
O(1) space because I'm only rearranging pointers, not creating new nodes.

* **Rapid-Fire Version**:

- Compare nodes from both sorted lists at each step
- Attach the smaller value to the merged list
- Advance the pointer in the list we took from
- Continue until one list is empty
- Attach the remaining list directly (already sorted)
- Use dummy node to handle head placement cleanly
- Time: O(n + m), Space: O(1)

* **Ultra-Minimal One-Liner**:

Two-pointer merge of sorted linked lists using a dummy node to simplify head handling and 
rearrange pointers in O(n + m) time with O(1) space.

* **Complexity Analysis**:

- **Time Complexity:** O(n + m) where n and m are the lengths of the two lists. We visit each 
node exactly once, comparing and linking them.
- **Space Complexity:** O(1) because we only manipulate pointers and don't create new nodes or 
use additional data structures. The merged list reuses the original nodes.

* **Use Cases**:

Merging sorted linked lists is fundamental in problems like merging k sorted lists (using a heap 
or priority queue), implementing merge sort for linked lists, and combining multiple data streams 
in real-world systems (e.g., combining sorted log files, merging sorted database query results).
"""

from typing import Optional

from drills.singly_linked_list import SinglyLinkedListNode


def mergeLists(head1: Optional[SinglyLinkedListNode], head2: Optional[SinglyLinkedListNode]) -> Optional[SinglyLinkedListNode]:
    """
    Standard Two-Pointer Merge for sorted Singly Linked Lists.
    Time Complexity: O(n + m)
    Space Complexity: O(1) - we only rearrange pointers.
    """
    # Create a dummy node to act as the starting point
    dummy = SinglyLinkedListNode(0)
    current = dummy

    # Iterate while both lists have nodes
    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        # Move the pointer in the merged list forward
        current = current.next

    # If one list is longer than the other, attach the remainder
    if head1 is not None:
        current.next = head1
    elif head2 is not None:
        current.next = head2

    # The actual head is the node after the dummy
    return dummy.next