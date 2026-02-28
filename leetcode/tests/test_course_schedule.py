import pytest

from leetcode.course_schedule import can_finish


@pytest.mark.parametrize("numCourses, prerequisites, expected", [
    (2, [[1, 0]], True),                     # Example 1
    (2, [[1, 0], [0, 1]], False),            # Example 2
    (1, [], True),                           # Single course
    (3, [[1,0],[2,1]], True),                # Simple chain
    (3, [[1,0],[0,1]], False),               # Simple cycle
    (4, [[1,0],[2,1],[3,2]], True),          # Long chain
    (4, [[1,0],[2,1],[0,2]], False),         # Cycle in chain
])
def test_canFinish(numCourses, prerequisites, expected):
    assert can_finish(numCourses, prerequisites) == expected
