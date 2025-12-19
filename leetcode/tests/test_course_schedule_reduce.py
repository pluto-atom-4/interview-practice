import pytest

from leetcode.course_schedule_reduce import canFinish_reduce


@pytest.mark.parametrize("numCourses, prerequisites, expected", [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False),
    (3, [[1,0],[2,1]], True),
    (3, [[1,0],[0,1]], False),
])
def test_canFinish_reduce(numCourses, prerequisites, expected):
    assert canFinish_reduce(numCourses, prerequisites) == expected
