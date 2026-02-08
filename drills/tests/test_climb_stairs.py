"""
FUNCTION climb_stairs(n):
    IF n <= 0: RETURN 0
    IF n EQUALS 1: RETURN 1
    IF n EQUALS 2: RETURN 2

    // Base cases: ways(1) = 1, ways(2) = 2
    // We only need the last two values to calculate the current one
    prev_2_steps = 1
    prev_1_step = 2

    FOR i FROM 3 TO n:
        // Current ways is the sum of taking 1 step from (n-1)
        // and taking 2 steps from (n-2)
        current = prev_1_step + prev_2_steps

        // Slide the window forward
        prev_2_steps = prev_1_step
        prev_1_step = current

    RETURN prev_1_step
"""

import pytest

from drills.climb_stairs import climb_stairs


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (10, 89),
        (20, 10946),
    ],
)
def test_climb_stairs(n, expected):
    assert climb_stairs(n) == expected


def test_large_input():
    # Just verifying it runs efficiently and returns an integer
    result = climb_stairs(100)
    assert isinstance(result, int)
    assert result > 0
