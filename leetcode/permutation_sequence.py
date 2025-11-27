"""
Permutation Sequence Algorithm Explained Step-by-Step
-----------------------------------------------------
The Permutation Sequence problem asks to find the kth permutation of numbers [1..n].
A naive approach would generate all n! permutations and return the kth one, which is inefficient.
The optimal solution uses the factorial number system to directly calculate the kth permutation
without generating all permutations. This problem demonstrates the power of mathematical insight
and combinatorics in algorithm design, and is essential for understanding permutation generation,
combinatorial number systems, and interview-level optimization techniques.

Here is how the process works:

1. **Factorial Number System Understanding**:
   - For n numbers, there are n! total permutations
   - These permutations can be divided into groups based on the first digit
   - For each position, there are (n-1)! permutations with that digit in the first position
   - Example: n=3 has 3! = 6 permutations divided into 3 groups of 2 permutations each
   - This hierarchical grouping is the key insight for finding the kth permutation

2. **Index Conversion (0-indexed)**:
   - Convert k from 1-indexed to 0-indexed by subtracting 1
   - This simplifies the modular arithmetic calculations
   - k -= 1 ensures we work with indices starting from 0
   - Example: if k=2 (2nd permutation), convert to index 1

3. **Iterative Selection by Position**:
   - Start from the leftmost position (most significant digit)
   - For each position, calculate factorial of remaining positions: f = (i-1)!
   - Determine which element should go in current position: index = k // f
   - This index tells us which available number to select at this position
   - Remove the selected number from available pool to avoid duplicates

4. **Modular Arithmetic for Remaining Positions**:
   - After selecting an element, update k for the next iteration: k %= f
   - This gives us the position within the subgroup of remaining permutations
   - Ensures we correctly navigate through permutation groups
   - Example: if k=5 for n=3, k becomes 5 % 2 = 1 for next iteration

5. **Greedy Construction**:
   - Build result string by appending selected digits one at a time
   - Convert each selected number to string as it's added
   - The sequence of selections automatically generates the kth permutation
   - No backtracking or recursive calls needed - purely iterative and mathematical

6. **Final Result**:
   - After processing all positions, result contains the kth permutation
   - Join all digits into a single string and return
   - The algorithm guarantees this is the exact kth permutation (1-indexed)

Example Walkthrough: n=3, k=3 (3rd permutation)
- Initial: numbers=[1,2,3], k=2 (0-indexed)
- Position 1: f=2, index=2//2=1, select numbers[1]=2, k=2%2=0
- Position 2: f=1, index=0//1=0, select numbers[0]=1, k=0%1=0
- Position 3: f=0, index=0//0=0, select numbers[0]=3
- Result: "213" (the 3rd permutation in lexicographic order)

Time Complexity: O(n²) - outer loop runs n times, each pop() operation is O(n) in worst case
Space Complexity: O(n) - for numbers list and result array

Key Insights:
- Uses factorial number system (mixed radix representation) of permutations
- Avoids generating all permutations (which would be O(n!) time)
- Demonstrates combinatorial mathematics and clever indexing
- Shows how mathematical properties can drastically optimize algorithms
- Essential for interview problems involving permutations and large n values

This algorithm is fundamental for:
- Permutation generation without brute force
- Understanding combinatorial number systems
- Solving interview problems with large constraint limits
- Optimizing problems that seem to require exponential solutions
"""

from math import factorial


def get_permutation(n: int, k: int) -> str:
    """
    Return the kth permutation sequence of numbers [1..n].
    Uses factorial number system to avoid generating all permutations.
    """
    numbers = list(range(1, n + 1))
    k -= 1  # convert to 0-index
    result = []

    for i in range(n, 0, -1):
        f = factorial(i - 1)
        index = k // f
        result.append(str(numbers[index]))
        numbers.pop(index)
        k %= f

    return "".join(result)
