import pytest

from leetcode.asteroid_collision import asteroid_collision


@pytest.mark.parametrize("asteroids, expected", [
    ([5,10,-5], [5,10]),       # Example 1
    ([8,-8], []),              # Example 2
    ([10,2,-5], [10]),         # Example 3
    ([3,5,-6,2,-1,4], [-6,2,4]), # Example 4
    ([1,2,3], [1,2,3]),        # No collisions
    ([-2,-1,1,2], [-2,-1,1,2]) # Different directions, no collisions
])
def test_asteroid_collision_cases(asteroids, expected):
    assert asteroid_collision(asteroids) == expected

def test_empty_input():
    assert asteroid_collision([]) == []

def test_single_asteroid():
    assert asteroid_collision([5]) == [5]
    assert asteroid_collision([-5]) == [-5]
