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
