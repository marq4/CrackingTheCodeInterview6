""" Automatically validate your implementation. """

from binary_tree import BinaryTree, BinaryTreeNode, binary_trees_are_identical
from invert import invert_function


def test_none():
    """ Tree is None. """
    non_existing = None
    invert_function(non_existing)
    assert non_existing is None

def test_empty():
    """ Tree is empty. """
    empty_bt = BinaryTree()
    invert_function(empty_bt)
    assert binary_trees_are_identical( empty_bt, BinaryTree() )

def test_single():
    """ Tree has a single element. """
    single_bt = BinaryTree(9)
    invert_function(single_bt)
    assert binary_trees_are_identical( single_bt, BinaryTree(9) )

def test_basic():
    """ Simple 3-node tree. """
    basic_bt = BinaryTree(0)
    basic_bt.insert(-4)
    basic_bt.insert(8)
    invert_function(basic_bt)
    expected_bt = BinaryTree(0)
    expected_bt.root.rite = BinaryTreeNode(-4)
    expected_bt.root.left = BinaryTreeNode(8)
    assert binary_trees_are_identical(basic_bt, expected_bt)

def test_advanced():
    """ Tree has many levels and is unbalanced. """
    advanced_bt = BinaryTree(100)
    advanced_bt.insert(156)
    advanced_bt.insert(105)
    advanced_bt.insert(90)
    advanced_bt.insert(166)
    advanced_bt.insert(158)
    advanced_bt.insert(13)
    advanced_bt.insert(49)
    expected_bt = BinaryTree(100)
    expected_bt.root.rite = BinaryTreeNode(90)
    expected_bt.root.rite.rite = BinaryTreeNode(13)
    expected_bt.root.rite.rite.left = BinaryTreeNode(49)
    expected_bt.root.left = BinaryTreeNode(156)
    expected_bt.root.left.left = BinaryTreeNode(166)
    expected_bt.root.left.left.rite = BinaryTreeNode(158)
    expected_bt.root.left.rite = BinaryTreeNode(105)
    assert binary_trees_are_identical(advanced_bt, expected_bt)
