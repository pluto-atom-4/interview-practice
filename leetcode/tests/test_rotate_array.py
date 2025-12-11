import pytest

from leetcode.rotate_array import rotate, rotate_in_place


@pytest.mark.parametrize("nums, k, expected", [
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    ([-1,-100,3,99], 2, [3,99,-1,-100]),
    ([1], 10, [1]),
    ([], 5, []),
])
def test_rotate(nums, k, expected):
    assert rotate(nums, k) == expected


def test_rotate_in_place():
    nums = [1,2,3,4,5,6,7]
    rotate_in_place(nums, 3)
    assert nums == [5,6,7,1,2,3,4]

    nums2 = [-1,-100,3,99]
    rotate_in_place(nums2, 2)
    assert nums2 == [3,99,-1,-100]
