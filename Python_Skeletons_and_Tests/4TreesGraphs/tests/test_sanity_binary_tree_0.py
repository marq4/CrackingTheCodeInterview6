""" Verify BinaryTree class works with ints. """

from binary_tree import (BinaryTree, binary_trees_are_identical,
                         generate_randint_binary_tree)


def test_init_len_empty():
    """ Empty, _init_ and _len_. """
    empty_bt = BinaryTree()
    assert empty_bt is not None
    assert empty_bt.root is None
    assert bool(empty_bt) is False
    assert len(empty_bt) == 0

def test_init_single():
    """ Single element. """
    val = 11
    single_bt = BinaryTree(val)
    assert single_bt is not None
    assert single_bt.root is not None
    assert single_bt.root.left is None
    assert single_bt.root.rite is None
    assert single_bt.root.value == val
    assert single_bt.root.value != val-2
    assert bool(single_bt) is True
    assert len(single_bt) == 1

def test_insert():
    """ Insert assorted, increasing and decresing elements. """
    val = 45
    right_val = val+3
    left_val = val-103
    empty_bt = BinaryTree()
    empty_bt.insert(val)
    assert empty_bt.root.value == val
    empty_bt.insert(right_val)
    empty_bt.insert(left_val)
    empty_bt.insert(val)
    assert empty_bt.root.rite.value == right_val
    assert empty_bt.root.left.value == left_val
    assert len(empty_bt) == 3
    single_bt = BinaryTree(val)
    single_bt.insert(val)
    assert single_bt.root.value == val
    assert single_bt.root.left is None
    assert len(single_bt) == 1
    inc_bt = BinaryTree(0)
    inc_bt.insert(5)
    inc_bt.insert(55)
    inc_bt.insert(555)
    inc_bt.insert(55)
    assert len(inc_bt) == 4
    assert inc_bt.root.value == 0
    assert inc_bt.root.rite.rite.rite.value == 555
    assert inc_bt.root.left is None
    dec_bt = BinaryTree(0)
    dec_bt.insert(-5)
    dec_bt.insert(-55)
    dec_bt.insert(-555)
    dec_bt.insert(-55)
    assert len(dec_bt) == 4
    assert dec_bt.root.value == 0
    assert dec_bt.root.left.left.left.value == -555
    assert dec_bt.root.rite is None

def test_contains_get_node():
    """ Contains and doesn't contain value. """
    val = 10
    empty_bt = BinaryTree()
    assert empty_bt.contains(val) is False
    single_bt = BinaryTree(val)
    assert single_bt.contains(val)
    assert single_bt.contains(13) is False
    assert single_bt.get_node(val) is single_bt.root
    assert single_bt.get_node(val+3) is None
    small_bt = BinaryTree(10)
    small_bt.insert(4)
    small_bt.insert(1)
    small_bt.insert(14)
    assert small_bt.get_node(14) is small_bt.root.rite
    assert small_bt.get_node(1) is small_bt.root.left.left
    assert small_bt.get_node(1) is not small_bt.root
    assert small_bt.get_node(1) is not small_bt.root.rite
    assert small_bt.get_node(11) is None
    assert small_bt.get_node(10) is not single_bt.root
    small_bt.insert(11)
    assert small_bt.root.rite.left.value == 11

def test_generate_randint_binary_tree():
    """ Multiple random elements. """
    val = 6
    lo_val = 0
    hi_val = 99
    multi_rand_bt = generate_randint_binary_tree(val, lo_val, hi_val)
    assert len(multi_rand_bt) == val
    assert multi_rand_bt.root.value >= lo_val
    assert multi_rand_bt.root.value <= hi_val
    single_bt = generate_randint_binary_tree(1, lo_val, hi_val)
    assert bool(single_bt) is True
    assert len(single_bt) == 1

def test_binary_trees_are_identical_basic():
    """ Identical if both contain same elements in same positions. """
    none = None
    assert binary_trees_are_identical(none, None) is False
    empty_bt = BinaryTree()
    assert binary_trees_are_identical(empty_bt, none) is False
    assert binary_trees_are_identical( empty_bt, BinaryTree() )
    val = 864
    single_bt = BinaryTree(val)
    assert binary_trees_are_identical(single_bt, single_bt)
    assert binary_trees_are_identical( single_bt, BinaryTree(val) )
    same_bt = BinaryTree()
    same_bt.insert(val)
    assert binary_trees_are_identical(single_bt, same_bt)
    small_bt = BinaryTree(5)
    small_bt.insert(8)
    assert binary_trees_are_identical(small_bt, none) is False
    another_bt = BinaryTree(5)
    assert binary_trees_are_identical(small_bt, another_bt) is False
    another_bt.insert(8)
    assert binary_trees_are_identical(small_bt, another_bt)
    another_bt.insert(8)
    assert binary_trees_are_identical(small_bt, another_bt)
    another_bt.insert(6)
    assert binary_trees_are_identical(small_bt, another_bt) is False
    same_size_bt = BinaryTree(3)
    same_size_bt.insert(4)
    same_size_bt.insert(1)
    assert len(same_size_bt) == 3
    different_value_bt = BinaryTree(3)
    different_value_bt.insert(4)
    different_value_bt.insert(0)
    assert binary_trees_are_identical(same_size_bt, different_value_bt) is False

def test_binary_trees_are_identical_advanced():
    """ Go deeper. """
    deep_bt = BinaryTree(11)
    deep_bt.insert(-2)
    deep_bt.insert(6)
    deep_bt.insert(17)
    deep_bt.insert(19)
    deep_bt.insert(18)
    assert len(deep_bt) == 6
    assert binary_trees_are_identical(deep_bt, deep_bt)
    assert binary_trees_are_identical(deep_bt, None) is False
    advanced_bt = BinaryTree(11)
    advanced_bt.insert(-2)
    advanced_bt.insert(17)
    assert binary_trees_are_identical(deep_bt, advanced_bt) is False
    advanced_bt.insert(6)
    advanced_bt.insert(19)
    assert binary_trees_are_identical(deep_bt, advanced_bt) is False
    advanced_bt.insert(18)
    assert binary_trees_are_identical(deep_bt, advanced_bt)
    assert advanced_bt.root.rite.rite.left.value == 18
    advanced_bt.root.rite.rite.left.value = 200
    assert binary_trees_are_identical(deep_bt, advanced_bt) is False

def test_validity():
    """ Make sure values to the right are greater than current,
    and values to the right are lesser. """
    medium_bt = BinaryTree(100)
    medium_bt.insert(45)
    assert medium_bt.root.left.value == 45
    medium_bt.insert(42)
    assert medium_bt.root.left.left.value == 42
    medium_bt.insert(187)
    medium_bt.insert(55)
    assert medium_bt.root.left.rite.value == 55
