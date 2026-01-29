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
