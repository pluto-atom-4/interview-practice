"""
## Problem Statement

Detect whether a singly linked list contains a cycle. The challenge is to do this efficiently 
without using extra space (O(1) space). This problem tests understanding of pointer manipulation, 
two-pointer techniques, and cycle detection algorithms commonly asked in technical interviews.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Floyd's Cycle-Finding Algorithm (Tortoise and Hare)**:

Floyd's algorithm is optimal for cycle detection because it requires only O(1) extra space 
and O(n) time, making it ideal for space-constrained environments. The two-pointer approach 
elegantly uses movement patterns to detect cycles without storing visited nodes.

* Key Concepts:

  - **Why two pointers with different speeds?**
  Moving pointers at different speeds (1 and 2) guarantees convergence if a cycle exists. 
  If no cycle exists, the fast pointer reaches the end. If a cycle exists, the fast pointer 
  will eventually "lap" the slow pointer within the cycle, and they will meet at the same node.

  - **Why this guarantees detection?**
  In a cycle of length L, the relative speed is 1 step per iteration. If the slow pointer is 
  anywhere in the cycle, the fast pointer gains exactly 1 position each iteration. This means 
  the fast pointer will eventually catch up to the slow pointer within L iterations.

* Logic:

1. Initialize both pointers (slow and fast) at the head node
2. Check if head exists; if empty list, no cycle possible
3. Loop while the fast pointer and its next node exist (ensuring we can move 2 steps)
4. Move slow pointer 1 step and fast pointer 2 steps each iteration
5. If pointers meet at the same node, a cycle exists—return True
6. If fast pointer reaches the end (null), no cycle exists—return False

* **30-Second Pitch**:

I'm using Floyd's Tortoise and Hare algorithm. I maintain two pointers moving at different speeds: 
one moves one step per iteration, the other moves two steps. If a cycle exists, the faster pointer 
will eventually lap and meet the slower pointer. If we reach the end without meeting, there's no cycle. 
This runs in O(n) time with O(1) space, making it optimal for memory constraints.

* **Rapid-Fire Version**:

- Two pointers: slow (1 step) and fast (2 steps)
- Loop until fast pointer reaches end or pointers meet
- If they meet → cycle exists
- If fast reaches null → no cycle
- Time: O(n), Space: O(1)—optimal for space-constrained scenarios

* **Ultra-Minimal One-Liner**:

Use two pointers at different speeds; if they meet, a cycle exists; if fast reaches the end, they don't.

* **Complexity Analysis**:

- **Time Complexity:** O(n) where n is the number of nodes. In the worst case without a cycle, we traverse 
  the entire list. With a cycle, we traverse the list until the pointers meet, which happens within n steps.
  
- **Space Complexity:** O(1) as we only use two pointer variables regardless of input size.

* **Use Cases**:

- **Linked list validation:** Detecting corrupted or circular data structures
- **Memory leak detection:** Identifying infinite loops in data traversal
- **Graph algorithms:** Adapted for cycle detection in directed/undirected graphs
- **Interview contexts:** Core problem for demonstrating pointer manipulation and optimization skills
"""

from typing import Optional

from drills.singly_linked_list import SinglyLinkedListNode


def has_cycle(head: Optional[SinglyLinkedListNode]) -> bool:
    """
    Detects a cycle using Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return False

    slow = head  # Moves 1 step
    fast = head  # Moves 2 steps

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If they meet, there is a cycle
        if slow == fast:
            return True

    return False