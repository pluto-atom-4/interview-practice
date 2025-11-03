import pytest

from algorithms.devide_n_conquer.strassen import strassen


def test_strassen_2x2():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = strassen(A, B)
    expected = [[19, 22], [43, 50]]
    assert result == expected

def test_strassen_identity():
    A = [[1, 0], [0, 1]]
    B = [[9, 8], [7, 6]]
    result = strassen(A, B)
    assert result == B

def test_strassen_1x1():
    A = [[3]]
    B = [[7]]
    assert strassen(A, B) == [[21]]
