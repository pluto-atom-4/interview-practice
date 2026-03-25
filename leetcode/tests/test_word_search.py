import pytest

from leetcode.word_search import exist


@pytest.mark.parametrize(
    "board, word, expected",
    [
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCCED",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "SEE",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCB",
            False,
        ),
    ],
)
def test_exist(board, word, expected):
    assert exist(board, word) == expected

