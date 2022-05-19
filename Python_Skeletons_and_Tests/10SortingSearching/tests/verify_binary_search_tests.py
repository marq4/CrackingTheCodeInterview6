""" Automatically validate your implementation. """

from binary_search import binary_search_function, is_sorted

# Not testing None or array out of order to avoid AssertionError.

def test_is_sorted():
    """ Array is in order. Array is not in order. """
    none_existing = None
    assert not is_sorted(none_existing)
    order_arr = [0, 4, 6, 22, 27, 78, 93]
    assert is_sorted(order_arr)
    descending_arr = list( range(-8, -23, -3) )
    assert not is_sorted(descending_arr)
    ascending_arr = list( range(8, 23, 3) )
    assert is_sorted(ascending_arr)
    weird_arr = [-4, 56, 23, 0, 56, -34, 836, 0, 11, 111, 1]
    assert not is_sorted(weird_arr)

def test_empty():
    """ Array is empty. """
    empty_arr = []
    assert binary_search_function(empty_arr, 56) < 0

def test_single():
    """ Array has a single element. """
    single_arr = [1]
    assert binary_search_function(single_arr, 1) == 0
    assert binary_search_function(single_arr, 0) < 0
    assert binary_search_function(single_arr, 100) < 0
    assert len(single_arr) == 1

def test_duplicates():
    """ Array is all duplicates. """
    duplicates_arr = [4, 4, 4, 4, 4, 4]
    assert binary_search_function(duplicates_arr, 44) < 0
    assert binary_search_function(duplicates_arr, 4) == 2
    assert binary_search_function(duplicates_arr, -4) < 0
    assert duplicates_arr == [4] * 6

def test_basic():
    """ Small array no duplicates. """
    small_arr = [1, 2, 3, 4]
    assert binary_search_function(small_arr, 4) == 3
    assert binary_search_function(small_arr, 1) == 0
    assert binary_search_function(small_arr, 7) < 0
    assert binary_search_function(small_arr, 0) < 0

def test_advanced():
    """ Large array with duplicates. """
    advanced_arr = [-6, -2, 0, 0, 0, 3, 45, 120, 125, 987, 999]
    assert binary_search_function(advanced_arr, 0) == 2
    assert binary_search_function(advanced_arr, 999) == 10
    assert binary_search_function(advanced_arr, -6) == 0
    assert binary_search_function(advanced_arr, 45) == 6
    assert binary_search_function(advanced_arr, 47) < 0
    assert binary_search_function(advanced_arr, 103) < 0
    assert advanced_arr == [-6, -2, 0, 0, 0, 3, 45, 120, 125, 987, 999]
