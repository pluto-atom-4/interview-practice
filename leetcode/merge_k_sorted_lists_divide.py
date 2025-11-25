"""
Merge K Sorted Lists (Divide-and-Conquer Approach) - LeetCode Problem
----------------------------------------------------------------------
The Merge K Sorted Lists problem can also be solved using a divide-and-conquer strategy.
This approach recursively divides the k lists into halves, conquers by merging smaller groups,
and combines results. This demonstrates the divide-and-conquer paradigm and achieves better
cache efficiency compared to heap-based approaches for certain input distributions.

Here is how the process works:

1. **Base Case - Single List**: When left and right indices point to the same list.
   - If left == right, we've isolated one individual list
   - Return that single list directly without any merging
   - This is the termination condition for recursion

2. **Divide Strategy**: Recursively split the lists into two halves.
   - Calculate midpoint: mid = (left + right) // 2
   - Left half: merge_range(lists, left, mid)
   - Right half: merge_range(lists, mid + 1, right)
   - Continue dividing until reaching base cases (single lists)

3. **Conquer Phase - Merge Two Lists**: Combine results from left and right halves.
   - Take two already-sorted linked lists (from left and right recursive calls)
   - Merge them using a two-pointer technique into one sorted list
   - Compare values from both lists and attach smaller node to result
   - Advance pointer in the list whose node was used

4. **Two-Pointer Merging Logic**: Efficiently merge two sorted linked lists.
   - Initialize dummy node and current pointer for result list
   - While both lists have remaining nodes, compare and attach the smaller one
   - After one list is exhausted, attach the remaining nodes from the other
   - This simple linear merge takes O(n + m) time for lists of sizes n and m

5. **Combining Results**: Return merged list from the top-level recursion.
   - The first divide_merge_range call processes the entire array
   - It returns the result of merging all k lists
   - Recursion handles the hierarchical combining automatically

6. **Recursive Tree Structure**: Understand the divide-and-conquer tree pattern.
   - Top level: divides k lists into two groups of k/2
   - Middle levels: recursive division continues with halving
   - Bottom level: base cases return individual lists
   - Result: O(log k) levels with merging happening at each level

Example: lists = [[1,4,5], [1,3,4], [2,6]]
- Level 1 divide: Split into [1,4,5] | [1,3,4], [2,6]
- Level 2: Merge (1,3,4) and (2,6) → (1,2,3,4,6)
- Level 3: Merge (1,4,5) and (1,2,3,4,6) → (1,1,2,3,4,4,5,6)

Time Complexity: O(N log k) where N = total nodes, k = number of lists
  - Merging happens at O(log k) recursion levels
  - Each level processes all N nodes once
  - Total comparisons and operations: O(N log k)

Space Complexity: O(log k) for recursion call stack depth
  - Recursion depth is O(log k) due to binary division
  - No additional data structures beyond the recursion stack

This divide-and-conquer approach is elegant and demonstrates important algorithmic principles.
It's particularly efficient when considering cache locality and is often preferred in practice.
"""

from typing import List, Optional

from leetcode.merge_k_sorted_lists import ListNode, build_linked_list


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next

def merge_k_lists_divide(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    def merge_range(lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = merge_range(lists, left, mid)
        l2 = merge_range(lists, mid + 1, right)
        return merge_two_lists(l1, l2)

    return merge_range(lists, 0, len(lists) - 1)
