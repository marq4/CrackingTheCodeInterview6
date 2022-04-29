""" Automatically validate your implementation. """

from linked_list import LinkedList
from remove_duplicates_1 import remove_duplicates_function


def test_none():
    """ List is None. """
    non_existing = None
    remove_duplicates_function(non_existing)
    assert non_existing is None

def test_empty():
    """ List is empty. """
    empty_ll = LinkedList()
    remove_duplicates_function(empty_ll)
    assert empty_ll == LinkedList()

def test_single():
    """ List has a single element. """
    single_ll = LinkedList( [56] )
    remove_duplicates_function(single_ll)
    assert single_ll == LinkedList( [56] )

def test_no_duplicates():
    """ List has 3 elements but is unique. """
    should_not_change_ll = LinkedList( [10, 20, 30] )
    remove_duplicates_function(should_not_change_ll)
    assert should_not_change_ll == LinkedList( [10, 20, 30] )

def test_basic_middle():
    """ List has a duplicate in the middle. """
    middle_ll = LinkedList( [1, 2, 1, 3,] )
    remove_duplicates_function(middle_ll)
    assert middle_ll == LinkedList( [1, 2, 3] )

def test_intermediate_first_last():
    """ List's first and last elements are duplicates. """
    first_last_ll = LinkedList( [0, 22, 33, 0] )
    remove_duplicates_function(first_last_ll)
    assert first_last_ll == LinkedList( [0, 22, 33] )

def test_advanced_many_duplicates():
    """ List has many duplicates. """
    many_ll = LinkedList( [-6, -6, 0, -8, -6, -6, 0, 0] )
    remove_duplicates_function(many_ll)
    assert len(many_ll) == 3
    assert many_ll == LinkedList( [-6, 0, -8] )

def test_all_duplicates():
    """ List has all duplicates. """
    all_ll = LinkedList( [4, 4, 4, 4, 4, 4, 4] )
    remove_duplicates_function(all_ll)
    assert len(all_ll) == 1
    assert all_ll == LinkedList( [4] )
