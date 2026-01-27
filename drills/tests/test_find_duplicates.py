
import pytest

from drills.find_duplicates import find_duplicates


class TestFindDuplicates:
    @pytest.mark.parametrize("input_list, expected_output", [
        ([1, 2, 3, 2, 4, 5, 1], [1, 2]),
        ([10, 20, 30, 40], []),
        ([], []),
        ([1, 1, 1, 1], [1]),
    ])
    def test_find_duplicates(self, input_list, expected_output):
        assert find_duplicates(input_list) == expected_output

    def test_edge_case_out_of_range(self):
        """Test handling of out-of-range values gracefully."""
        input_list = [1, 2, 3, 4, 33, 5, 6, 7, 8, 9, 10]  # 33 is out of range for length 10
        expected_output = []
        assert find_duplicates(input_list) == expected_output
