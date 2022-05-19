""" Automatically validate your implementation. """

from random import randint

from merge_sort import merge_sort_function


def test_none():
    """ Array is None. """
    non_existing = None
    merge_sort_function(non_existing)
    assert non_existing is None

def test_empty():
    """ Array is empty. """
    empty_arr = []
    merge_sort_function(empty_arr)
    assert len(empty_arr) == 0

def test_single():
    """ Array has a single element. """
    single_arr = [1]
    merge_sort_function(single_arr)
    assert single_arr == [1]

def test_duplicates():
    """ Array is all duplicates. """
    duplicates_arr = [4, 4, 4, 4, 4, 4]
    merge_sort_function(duplicates_arr)
    assert duplicates_arr == [4] * 6

def test_basic_in_order():
    """ Array is already in order. """
    order_arr = [45, 56, 98]
    merge_sort_function(order_arr)
    assert order_arr == [45, 56, 98]

def test_intermediate_descending():
    """ Small array in descending order. """
    small_arr = [8, 6, 2, 1]
    merge_sort_function(small_arr)
    assert small_arr == [1, 2, 6, 8]

def test_advanced():
    """ Large array with duplicates not in order. """
    advanced_arr = [45, 0, 34, 1, -5, 0, 31, 9, 8, 7, 23, 24, 0]
    merge_sort_function(advanced_arr)
    assert advanced_arr == [-5, 0, 0, 0, 1, 7, 8, 9, 23, 24, 31, 34, 45]

def test_random_numbers():
    """ Array of random ints. """
    minimum_value = -9999
    random_arr = []
    for _ in range(133):
        random_arr.append( randint(minimum_value, 9999) )
    merge_sort_function(random_arr)
    for number in random_arr:
        assert number >= minimum_value
        minimum_value = number
