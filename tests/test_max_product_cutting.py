import pytest

from algorithms.greedy.max_product_cutting import max_product_cutting


@pytest.mark.parametrize("n, expected", [
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 6),
    (6, 9),
    (7, 12),
    (8, 18),
    (10, 36),
    (15, 243),
])
def test_max_product_cutting(n, expected):
    assert max_product_cutting(n) == expected

def test_edge_cases():
    assert max_product_cutting(0) == 0
    assert max_product_cutting(1) == 0
