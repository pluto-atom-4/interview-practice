"""
## Problem Statement

Rotate a 2D matrix 90 degrees clockwise without mutating the original matrix.
The goal is to return a new rotated matrix efficiently. This tests understanding of 
coordinate transformation, 2D array indexing, and matrix operations—common in 
graphics, game development, and technical interviews.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Coordinate Transformation**:

This approach solves the rotation by mapping each element from the original matrix
to its new position in the rotated matrix using a mathematical transformation formula.
Rather than physically rotating the matrix, we calculate where each element should go
based on the geometric properties of a 90-degree clockwise rotation.

* Key Concepts:

  - **Why use coordinate transformation instead of transpose-then-reverse?**
Direct transformation is more intuitive for rotation and avoids intermediate steps.
For a clockwise rotation, the mapping formula `rotated[c][rows - 1 - r] = matrix[r][c]`
directly computes the destination from source: column becomes row, and row position
becomes inverted column. This is easier to understand and remember during interviews.

  - **Why does rotated[c][rows - 1 - r] = matrix[r][c] work geometrically?**
In a 90-degree clockwise rotation, the leftmost column becomes the top row. Specifically,
element at matrix[r][c] moves to position [c][rows - 1 - r]. The new row index is the
old column index (c), and the new column index is the inverted row (rows - 1 - r). This
transformation preserves the geometric layout of the rotation.

  - **Why create a new matrix with swapped dimensions [cols][rows]?**
A 90-degree rotation transforms an m×n matrix into an n×m matrix (dimensions swap).
Initializing the result with dimensions [cols][rows] ensures we have the correct shape
before filling elements. This prevents index out-of-bounds errors and clearly documents
the dimension change.

* Logic:

1. Handle edge cases: return empty list for null or empty input matrices
2. Extract original matrix dimensions: rows and cols
3. Create new rotated matrix with swapped dimensions: [cols][rows] initialized with zeros
4. Iterate through each element in the original matrix
5. Use coordinate transformation to place each element in its new position
6. Return the fully populated rotated matrix

* **30-Second Pitch**:

I'm rotating the matrix 90 degrees clockwise by applying a coordinate transformation
formula. For each element at position (r, c) in the original matrix, I calculate its
new position in the result matrix using the transformation (r, c) → (c, rows - 1 - r).
This efficiently maps each element to its destination in O(n*m) time with a new matrix
of swapped dimensions.

* **Rapid-Fire Version**:

- Use coordinate transformation formula: rotated[c][rows - 1 - r] = matrix[r][c]
- Swap matrix dimensions: new matrix is [cols][rows] instead of [rows][cols]
- Single pass through original matrix—linear time complexity
- Straightforward and interview-friendly (no intermediate steps needed)

* **Ultra-Minimal One-Liner**:

- Direct coordinate transformation maps each element (r, c) to (c, rows - 1 - r) in a new swapped-dimension matrix.

* **Complexity Analysis**:

- **Time Complexity:** O(n × m) where n = rows and m = cols. We iterate through every element exactly once.
- **Space Complexity:** O(n × m) for the new rotated matrix. We create a completely new matrix of size m × n (dimensions swapped).

* **Use Cases**:

- Image processing: rotating images 90 degrees (common in photo editing)
- Game development: rotating game boards or level layouts
- Graphics transformations: rotating coordinate systems or sprites
- Data visualization: reorienting data matrices for different presentations
- Technical interviews: tests 2D array indexing, coordinate geometry, and problem-solving skills

"""

from __future__ import annotations

from typing import List


def rotate_matrix_90_clockwise(matrix: List[List[int]]) -> List[List[int]]:
    """
    Rotate a 2D matrix 90 degrees clockwise.

    This function returns a *new* rotated matrix and does not mutate the input.

    Example:
        [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
        ]
        becomes
        [
          [7, 4, 1],
          [8, 5, 2],
          [9, 6, 3]
        ]
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])

    # New matrix with swapped dimensions
    rotated = [[0] * rows for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            rotated[c][rows - 1 - r] = matrix[r][c]

    return rotated
