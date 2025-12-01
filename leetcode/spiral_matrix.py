"""
Spiral Matrix Traversal - Complete Algorithm Explanation
----------------------------------------------------------
The Spiral Matrix problem requires traversing a 2D matrix in a spiral pattern, starting from the outer edges
and working towards the center. This involves moving right, down, left, and up in a cyclical manner while
respecting boundary constraints. This is a fundamental matrix manipulation problem used in interviews to test
spatial reasoning, boundary handling, and problem-solving skills.

Here is how the process works:

1. **Boundary Initialization**: Set up four boundary pointers to track traversal limits.
   - top: row index for traversing left-to-right (starts at 0)
   - bottom: row index for traversing right-to-left (starts at len(matrix) - 1)
   - left: column index for traversing bottom-to-top (starts at 0)
   - right: column index for traversing top-to-bottom (starts at len(matrix[0]) - 1)
   - These pointers shrink inward after each directional traversal

2. **Right Traversal**: Move from left to right along the top boundary.
   - Iterate from column 'left' to column 'right' in the 'top' row
   - Append all elements: matrix[top][j] for j in range(left, right + 1)
   - Increment 'top' pointer after completing this traversal
   - This moves the top boundary inward since we've processed the top row

3. **Down Traversal**: Move from top to bottom along the right boundary.
   - Iterate from row 'top' to row 'bottom' in the 'right' column
   - Append all elements: matrix[i][right] for i in range(top, bottom + 1)
   - Decrement 'right' pointer after completing this traversal
   - This moves the right boundary inward since we've processed the right column

4. **Left Traversal**: Move from right to left along the bottom boundary.
   - Only execute if top <= bottom (still have rows to process)
   - Iterate from column 'right' to column 'left' in the 'bottom' row
   - Append all elements: matrix[bottom][j] for j in range(right, left - 1, -1)
   - Decrement 'bottom' pointer after completing this traversal
   - This moves the bottom boundary inward since we've processed the bottom row

5. **Up Traversal**: Move from bottom to top along the left boundary.
   - Only execute if left <= right (still have columns to process)
   - Iterate from row 'bottom' to row 'top' in the 'left' column
   - Append all elements: matrix[i][left] for i in range(bottom, top - 1, -1)
   - Increment 'left' pointer after completing this traversal
   - This moves the left boundary inward since we've processed the left column

6. **Termination Condition**: Continue until boundaries cross.
   - While loop condition: top <= bottom and left <= right
   - When boundaries cross, all elements have been visited
   - Inner checks (if top <= bottom, if left <= right) prevent duplicate elements

Example: matrix = [[1,2,3],[4,5,6],[7,8,9]]
- Right: [1,2,3], Down: [6,9], Left: [8,7], Up: [4], Right: [5]
- Result: [1,2,3,6,9,8,7,4,5]

Example: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
- Right: [1,2,3,4], Down: [8,12], Left: [11,10,9], Up: [5], Right: [6,7], Down: [11]
- Result: [1,2,3,4,8,12,11,10,9,5,6,7]

Time Complexity: O(m * n) where m = rows, n = columns (visit each element exactly once)
Space Complexity: O(1) excluding output array (only use constant boundary pointers)

This algorithm demonstrates boundary tracking, directional traversal, and state management in matrix problems.
It's essential for understanding 2D array manipulations, coordinate systems, and problem-solving techniques.
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Return all elements of the matrix in spiral order.
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
