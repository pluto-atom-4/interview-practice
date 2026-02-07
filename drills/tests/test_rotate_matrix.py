"""
FUNCTION rotate_matrix_90_clockwise(matrix):
    IF matrix is empty OR matrix[0] is empty:
        RETURN an empty list

    num_rows = length of matrix
    num_cols = length of matrix[0]

    // Initialize a new matrix with swapped dimensions (cols x rows)
    INITIALIZE rotated_matrix as (num_cols x num_rows) filled with 0s

    FOR r FROM 0 TO num_rows - 1:
        FOR c FROM 0 TO num_cols - 1:
            // The original row index becomes part of the new column index calculation
            // The original column index becomes the new row index
            rotated_matrix[c][num_rows - 1 - r] = matrix[r][c]

    RETURN rotated_matrix

"""

import pytest

from drills.rotate_matrix import rotate_matrix_90_clockwise


@pytest.mark.parametrize(
    "matrix, expected",
    [
        (
            [
                [1, 2],
                [3, 4],
            ],
            [
                [3, 1],
                [4, 2],
            ],
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3],
            ],
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            [
                [4, 1],
                [5, 2],
                [6, 3],
            ],
        ),
        (
            [],
            [],
        ),
        (
            [[]],
            [],
        ),
    ],
)
def test_rotate_matrix_90_clockwise(matrix, expected):
    assert rotate_matrix_90_clockwise(matrix) == expected
