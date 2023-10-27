import pytest
from introsort import *


def test_extract_empty_array():
    with pytest.raises(IndexError):
        extract_smallest([])


def test_partition():
    # test partitioning, check that pivot is in the proper posotion after swapping
    test_arr = [3, 8, 2, 5, 1, 4, 7, 6]

    pivot_ind = partition(test_arr, 0, len(test_arr))
    assert test_arr[pivot_ind] == 3


def test_introsotrt():
    # test introsort, use sorted builtin func to do comparison on arrays
    test_arr = [3, 8, 2, 5, 1, 4, 7, 6, -1, -100]
    test_arr_sorted = sorted(test_arr)

    introsort(test_arr)
    assert test_arr == test_arr_sorted


def test_do_heapsort():
    # test that heap sorts array properly
    test_arr = [3, 8, 2, 5, 1, 4, 7, 6, -1, -100]

    do_heapsort(test_arr, start=0, end=len(test_arr))
    print(test_arr)
