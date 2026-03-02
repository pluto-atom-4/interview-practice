import pytest

from leetcode.group_anagrams import group_anagrams


@pytest.mark.parametrize(
    "words, expected_groups",
    [
        (
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [
                    {"eat", "tea", "ate"},
                    {"tan", "nat"},
                    {"bat"}
                ]
         ),
        ([""], [{""}]),
        (["a"], [{"a"}]),
    ]
)
def test_group_anagrams(words, expected_groups):
    result = group_anagrams(words)
    result_sets = [set(group) for group in result]
    for expected in expected_groups:
        assert expected in result_sets
    assert len(result_sets) == len(expected_groups)