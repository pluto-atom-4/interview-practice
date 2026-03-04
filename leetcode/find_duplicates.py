"""
## Problem Statement

Given an array of integers where each number appears once or twice, return all elements 
that appear exactly twice. The array length is n+1 and contains only integers in range [1, n]. 
The challenge is to solve this with O(1) extra space (no auxiliary hash table) and O(n) time 
while preserving the original array structure. This tests creative use of array indices as 
a hash table and in-place marking techniques.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **In-Place Sign Marking**:

Rather than using an external hash set or hash map (which requires O(n) extra space), 
I exploit the constraint that numbers are in range [1, n]. The array itself becomes a 
hash table: for each number x, I mark the position at index x-1 by negating its value. 
If I encounter a number x whose corresponding index is already negative, x is a duplicate. 
This achieves O(1) space and O(n) time while elegantly solving the problem through 
array indexing.

* Key Concepts:

  - **Why use array indices as a hash table instead of an external hash set?**
  
    The constraint that numbers are in range [1, n] means each number can directly map to 
    a valid array index via (number - 1). By using the sign of the value at each index as 
    a marker, we avoid allocating extra space. A hash set would require O(n) extra space. 
    This in-place approach is space-optimal and demonstrates understanding of problem 
    constraints and creative data structure usage.

  - **Why use sign (negative/positive) as the marker instead of modifying values directly?**
  
    Negating the sign preserves the original value's magnitude while adding state (negative = 
    "visited"). This is clever because: (1) it doesn't require extra space, (2) we can still 
    extract the original value using abs(), (3) it's reversible (negate again to restore), 
    and (4) it's a common technique in competitive programming. Directly modifying values 
    would lose information.

  - **Why use abs(x) to get the index and the original number?**
  
    When we encounter a number x (whether positive or negative due to previous visits), 
    abs(x) gives us the actual number and the index to check: idx = abs(x) - 1. This works 
    because abs() extracts the magnitude regardless of sign. Using abs() is essential here; 
    without it, negative numbers in the array would map to invalid indices.

  - **Why check if nums[idx] < 0 before marking?**
  
    This condition detects duplicates. If nums[idx] is already negative, it means we've 
    visited this index before, which means the current number x is a duplicate. On first 
    visit, nums[idx] is positive, so we negate it to mark it. This two-phase logic (check, 
    then mark) is the core of the algorithm.

  - **Why use a set to store duplicates instead of directly adding to a list?**
  
    Using a set prevents adding the same duplicate multiple times. If a number appears 
    exactly twice, we detect the duplicate once and add it to the set. If we used a list 
    without the set check, we might add it multiple times if we encountered it again. The 
    set guarantees uniqueness efficiently.

  - **Why sort the result before returning?**
  
    Sorting the output is a convention in interview problems—it ensures consistent, 
    deterministic output. This makes testing easier and shows attention to output clarity, 
    even though the problem doesn't strictly require sorting. It's a small touch that 
    demonstrates polish.

* **30-Second Pitch**:

I use the array itself as a hash table by exploiting the constraint that numbers are in 
range [1, n]. For each number x, I mark the index x-1 by negating the value at that position. 
If I encounter a number whose index is already negative, it's a duplicate. Using abs() to 
extract the original number and index, I detect all duplicates in a single pass with O(1) 
extra space. This is an elegant in-place solution that shows creative use of array indexing.

* **Rapid-Fire Version**:

- Array values are in range [1, n]; use indices as a hash table
- For each number x: check index x-1, negate if positive (mark as visited)
- If index x-1 is already negative: x is a duplicate
- Use abs(x) to extract the actual number and valid index
- Use set to avoid duplicate duplicates
- Sort result for deterministic output
- Time: O(n), Space: O(1) auxiliary (output set is unavoidable)
- Constraint-based solution: works only when numbers are in [1, n]

* **Ultra-Minimal One-Liner**:

- Use array indices as a hash table via sign negation to detect duplicates in O(n) time, O(1) space.

* **Complexity Analysis**:

- **Time Complexity:** O(n)
  - Single pass through the array: each element is visited once
  - For each element, index lookup and sign check are O(1)
  - set.add() is O(1) average case
  - Sorting k duplicates at the end is O(k log k), but k ≤ n, so overall remains O(n + k log k) ≈ O(n)
  
- **Space Complexity:** O(1) auxiliary space (excluding output)
  - No external hash table or array allocation
  - The set of duplicates is output, not auxiliary, so it doesn't count toward "extra space"
  - If we must count the output, it's O(k) where k is the number of duplicates found
  - This is space-optimal for the problem constraints

* **Use Cases and Constraints**:

- **Finding duplicates in bounded ranges:** When data is constrained (e.g., IDs from 1 to n), 
  in-place marking is superior to hash tables
- **Memory-constrained systems:** Embedded systems or real-time processing where O(1) auxiliary 
  space is critical
- **Competitive programming:** Classic technique for duplicate detection without extra space
- **Data validation:** Identifying repeated user IDs or inventory items in limited-range datasets
- **Interview pattern recognition:** Recognizing when problem constraints enable creative solutions 
  like array indexing as a hash table

---

"""

from typing import List


def find_duplicates(nums: List[int]) -> List[int]:
    """
    Return all elements that appear exactly twice in the array.

    Uses in-place marking:
    - For each number x, flip the sign of nums[x-1].
    - If nums[x-1] is already negative, x is a duplicate.
    """
    duplicates = set()

    for x in nums:
        idx = abs(x) - 1
        if nums[idx] < 0:
            duplicates.add(abs(x))
        else:
            nums[idx] = -nums[idx]

    return sorted(duplicates)
