""" Verify linked list class works with ints. """

from linked_list import LinkedList, generate_randint_linked_list


def test_init_():
    """ Empty. Also _len_ and is_empty. """
    empty_ll = LinkedList()
    assert empty_ll.head is None
    assert empty_ll.tail is None
    assert len(empty_ll) == 0
    assert empty_ll.is_empty()

def test_single():
    """ Single element. """
    val = 1
    single_ll = LinkedList( [val] )
    assert single_ll is not None
    assert single_ll.head == single_ll.tail
    assert single_ll.head.value == val
    assert len(single_ll) == 1

def test_multi():
    """ Multiple elements. """
    val = 4
    multi_ll = LinkedList( list( range(1, val+1) ) )
    assert len(multi_ll) == val
    assert multi_ll.tail.value == val

def test_generate_randint_linked_list():
    """ Multiple random elements. """
    val = 6
    lo_val = 0
    hi_val = 99
    multi_rand_ll = \
        generate_randint_linked_list(val, lo_val, hi_val)
    assert len(multi_rand_ll) == val
    assert multi_rand_ll.head.value >= lo_val
    assert multi_rand_ll.tail.value <= hi_val
    single_ll = \
        generate_randint_linked_list(1, lo_val, hi_val)
    assert single_ll.is_empty() is False
    assert len(single_ll) == 1

def test_str_():
    """ Representation. """
    zeros_ll = LinkedList( [0, 0, 0] )
    assert str(zeros_ll) == '0 -> 0 -> 0'

def test_eq_():
    """ Equality. """
    compare_ll = LinkedList( [44, 42, 43, -10] )
    other_none = None
    assert compare_ll != other_none
    not_instance = "NoLL"
    assert compare_ll != not_instance
    empty_ll = LinkedList()
    assert compare_ll != empty_ll
    both_empty_ll = LinkedList()
    assert empty_ll == both_empty_ll
    dif_len_ll = LinkedList( [-39] )
    assert compare_ll != dif_len_ll
    dif_elements_same_len_ll = LinkedList( [44, 42, 43, -11] )
    assert compare_ll != dif_elements_same_len_ll
    same_ll = LinkedList( [44, 42, 43, -10] )
    assert compare_ll == same_ll

def test_add():
    """ Add single element. """
    add_ll = LinkedList( [-4, -3, -2] )
    add_ll.add(-1)
    assert add_ll.tail.value == -1
    assert add_ll.head.value == -4
    assert len(add_ll) == 4
    single_ll = LinkedList()
    single_ll.add(10)
    assert single_ll.head.value == single_ll.tail.value == 10
    assert single_ll.is_empty() is False
    assert len(single_ll) == 1

def test_add_to_beginning():
    """ Replace head. """
    beg_ll = LinkedList( [49, 34] )
    beg_ll.add_to_beginning(-3)
    assert beg_ll.head.value == -3
    assert beg_ll.tail.value == 34
    assert len(beg_ll) == 3
    single_ll = LinkedList()
    single_ll.add_to_beginning(88)
    assert single_ll.head.value == single_ll.tail.value == 88
    assert single_ll.is_empty() is False
    assert len(single_ll) == 1

def test_add_multiple():
    """ Add list. """
    multi_ll = LinkedList()
    multi_ll.add_multiple( [6, 7, 8] )
    assert multi_ll.is_empty() is False
    assert len(multi_ll) == 3
    multi_ll.add_multiple( [11, 12, 13] )
    assert len(multi_ll) == 6
    multi_ll.add_multiple( [0] )
    assert len(multi_ll) == 7
    assert multi_ll.head.value == 6
    assert multi_ll.tail.value == 0
    assert multi_ll == LinkedList( [6, 7, 8, 11, 12, 13, 0] )
