import pytest
from introsort import partition


# def test_extract_smallest():
#     test_arr = [1, 2, 3, 4, 5, 6]
#
#     smallest, modified_test_arr = extract_smallest(test_arr)
#
#     assert smallest == 1
#
#
# def test_extract_empty_array():
#     with pytest.raises(IndexError):
#         extract_smallest([])

def test_partition():

    test_arr = [3, 8, 2, 5, 1, 4, 7, 6]

    pivot_ind = partition(test_arr, 0, len(test_arr))
    assert test_arr[pivot_ind] == 3
