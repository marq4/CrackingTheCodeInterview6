""" Automatically validate your implementation. """

from linked_list import LinkedList
from reverse import reverse_function


def test_none():
    """ List is None. """
    non_existing = None
    reverse_function(non_existing)
    assert non_existing is None

def test_empty():
    """ List is empty. """
    empty_ll = LinkedList()
    reverse_function(empty_ll)
    assert empty_ll == LinkedList()

def test_single():
    """ List has a single element. """
    single_ll = LinkedList( [56] )
    reverse_function(single_ll)
    assert single_ll == LinkedList( [56] )

def test_all_same():
    """ List has all same elements. """
    same_ll = LinkedList( [4, 4, 4, 4] )
    reverse_function(same_ll)
    assert same_ll == LinkedList( [4, 4, 4, 4] )

def test_basic_two_elements():
    """ List has 2 different elements. """
    basic_ll = LinkedList( [1, 2] )
    reverse_function(basic_ll)
    assert basic_ll == LinkedList( [2, 1] )

def test_intermediate_multiple_different_elements():
    """ List has multiple different elements. """
    multi_ll = LinkedList( [9, 19, 29, 39, 49] )
    reverse_function(multi_ll)
    assert multi_ll == LinkedList( [49, 39, 29, 19, 9] )

def test_advanced_multiple_elements():
    """ List has multiple elements. """
    multi_ll = LinkedList( [0, 2, 0, 4, 5, 6, -1, 0] )
    reverse_function(multi_ll)
    assert multi_ll == LinkedList( [0, -1, 6, 5, 4, 0, 2, 0] )

