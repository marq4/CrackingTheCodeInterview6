"""
Unique Unbalanced Binary Tree (int).
"""

from enum import Enum
from random import randint


class Traversal(Enum):
    """ How to visit nodes.
        in:     L N R.
        pre:    N L R.
        post:   L R N.
    """
    IN_ORDER = 'In-order'
    PRE_ORDER = 'Pre-order'
    POST_ORDER = 'Post-order'


class BinaryTreeNode:
    """ Binary Tree Node (int, no parent pointer). """
    def __init__(self, val):
        self.value = val
        self.left = None
        self.rite = None

    def __len__(self):
        """ Obviously an int node always has length 1, so it makes no sense
        to try to get a node's length directly. """
        if self is None:
            return 0
        result = 1
        if self.left:
            result += len(self.left)
        if self.rite:
            result += len(self.rite)
        return result

    def __str__(self):
        return f"({self.value})"


    def contains(self, search_val: int) -> bool:
        """ Recursively search. """
        if self.value == search_val:
            return True
        if search_val < self.value:
            if self.left is None:
                return False
            return self.left.contains(search_val)
        if self.rite is None:
            return False
        return self.rite.contains(search_val)

    def insert(self, val: int) -> object:
        """ Recursively insert.
        :return: Pointer to the newly added node. """
        assert val != self.value, "It's supposed to be unique. "
        if val < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(val)
                return self.left
            return self.left.insert(val)
        if self.rite is None:
            self.rite = BinaryTreeNode(val)
            return self.rite
        return self.rite.insert(val)

    def traverse(self, traversal) -> str:
        """ Recursively traverse. """
        if self is None:
            return ''
        if traversal == Traversal.IN_ORDER:
            result = "\tLeft:"
            if self.left is not None:
                result += self.left.traverse(Traversal.IN_ORDER)
            result += f" Value:{self.value} Right:"
            if self.rite is not None:
                result += self.rite.traverse(Traversal.IN_ORDER)
            return result
        if traversal == Traversal.PRE_ORDER:
            result = f"\tValue:{self.value} Left:"
            if self.left is not None:
                result += self.left.traverse(Traversal.PRE_ORDER)
            result += ' Right:'
            if self.rite is not None:
                result += self.rite.traverse(Traversal.PRE_ORDER)
            return result
        if traversal == Traversal.POST_ORDER:
            result = "\tLeft:"
            if self.left is not None:
                result += self.left.traverse(Traversal.POST_ORDER)
            result += ' Right:'
            if self.rite is not None:
                result += self.rite.traverse(Traversal.POST_ORDER)
            result += f" Value:{self.value}"
            return result
        raise ValueError(f"Invalid traversal: {traversal} ")

    def get_node(self, search_val: int) -> object:
        """ Recursively search node with value search_val. """
        if search_val == self.value:
            return self
        if search_val < self.value:
            assert self.left is not None
            return self.left.get_node(search_val)
        assert self.rite is not None
        return self.rite.get_node(search_val)

class BinaryTree:
    """ Unique Unbalanced Binary Tree (int). """
    def __init__(self, root_val=None):
        if root_val is None:
            self.root = None
        else:
            self.root = BinaryTreeNode(root_val)

    def __str__(self, method=Traversal.PRE_ORDER) -> str:
        representation = 'UniqueUnbalancedBinaryTree (int) '
        representation += f"[{method.value}]: \n"
        representation += self.traverse(method)
        return representation + "\n} "

    def __len__(self) -> int:
        if self.root is None:
            return 0
        return len(self.root)


    def contains(self, search_val: int) -> bool:
        """ Only checks root and the recursion is done by the nodes.
        :return: True if search_val is found on tree. """
        if not self:
            return False
        if self.root.value == search_val:
            return True
        if self.root.left == self.root.rite == None:
            return False
        return self.root.contains(search_val)

    def get_node(self, search_val: int) -> object:
        """ Get the pointer to node with value search_val. """
        if not self.contains(search_val):
            return None
        if self.root.value == search_val:
            return self.root
        return self.root.get_node(search_val)

    def insert(self, val: int) -> object:
        """ Creates new root if tree is empty. Otherwise nodes recurse from root.
        :return: Pointer to the new node or old node if value already in tree. """
        if not self:
            self.root = BinaryTreeNode(val)
            return self.root
        if self.contains(val):
            return self.get_node(val)
        return self.root.insert(val)

    def traverse(self, traversal) -> str:
        """ Returns string representation. """
        if not self:
            return "\t<EMPTY>"
        return self.root.traverse(traversal)


def generate_randint_binary_tree(num: int, \
    min_val: int, max_val: int) -> BinaryTree:
    """ Generate a new BinaryTree with random ints.
    Keyword arguments:
    num -- the number of nodes to add to the BinaryTree.
    min_val -- lower bound inclusive.
    max_val -- upper bound inclusive.
    """
    genetated = BinaryTree()
    for _ in range(num):
        genetated.insert( randint(min_val, max_val) )
    return genetated


def binary_trees_are_identical(one_bt: BinaryTree, \
    another_bt: BinaryTree) -> bool:
    """ Equals methods not implemented as two different nodes
    are not equal even if they have the same value.
    Conditions:
    * None is not equal to anything, not even None. (Empty is falsy.)
    * Not identical if not instance of BinaryTree.
    * Even if (one, another) -> 2 sepparate instances, "one is another" is True!
    * Identical if both empty.
    * Not identical if different lengths.
    * Check branches and values. """
    if one_bt is None or another_bt is None:
        return False
    if not ( isinstance(one_bt, BinaryTree) and \
        isinstance(another_bt, BinaryTree) ):
        return False
    if one_bt.root is None and another_bt.root is None:
        return True
    if len(one_bt) != len(another_bt):
        return False
    return recursive_identity_check(one_bt.root, another_bt.root)

def recursive_identity_check(one_node: BinaryTreeNode, \
    another_node: BinaryTreeNode) -> bool:
    """ Compare nodes (pre-order).
    Base case: both None.
    Recurse: same position in tree, same value. """
    if not (one_node and another_node):
        return True
    if one_node and another_node:
        if one_node.value != another_node.value:
            return False
        if not recursive_identity_check(one_node.left, another_node.left):
            return False
        if not recursive_identity_check(one_node.rite, another_node.rite):
            return False
        return True
    return False
