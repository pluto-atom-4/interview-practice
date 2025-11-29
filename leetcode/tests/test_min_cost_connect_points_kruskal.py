import pytest

from leetcode.min_cost_connect_points_kruskal import min_cost_connect_points_kruskal


@pytest.mark.parametrize("points, expected", [
    ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
    ([[3,12],[-2,5],[-4,1]], 18),
    ([[0,0],[1,1],[1,0],[-1,1]], 4),
    ([[0,0]], 0),
    ([[0,0],[1,0]], 1),
])
def test_min_cost_connect_points_kruskal(points, expected):
    assert min_cost_connect_points_kruskal(points) == expected
