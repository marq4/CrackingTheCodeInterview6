"""
Based on: GitHub/careercup/CtCI-6th-Edition-Python.
Please first validate this file. In Win from Git Bash do:
    python -m pytest tests/test_sanity_linked_list_0 -v
"""

from random import randint


class LinkedListNode:
    """ DLL Node. """
    def __init__(self, val: int, next_node=None, prev_node=None):
        self.value = val
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)

class LinkedList:
    """ Doubly linked list. """
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        traverse = self.head
        while traverse:
            yield traverse
            traverse = traverse.next

    def __str__(self):
        values = [ str(node) for node in self ]
        return ' -> '.join(values)

    def __len__(self):
        """ If length is 0 the instance is falsy. """
        length = 0
        traverse = self.head
        while traverse:
            length += 1
            traverse = traverse.next
        return length


    def add(self, value: int):
        """ Add new value to end of LinkedList.
        Instance is False if it's empty -- if it's length is 0. """
        if not self:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        """ Add new value to beginning of LinkedList. """
        if not self:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def add_multiple(self, values: list) -> None:
        """ Add new values to end of LinkedList. """
        for val in values:
            self.add(val)


def generate_randint_linked_list(num: int, \
    min_val: int, max_val: int) -> LinkedList:
    """ Generate a new LinkedList with random ints.
    Keyword arguments:
    num -- the number of nodes to add to the LinkedList.
    min_val -- lower bound inclusive.
    max_val -- upper bound inclusive. """
    generated = LinkedList()
    for _ in range(num):
        generated.add( randint(min_val, max_val) )
    return generated


def linked_lists_are_identical(one_ll: LinkedList, \
    another_ll: LinkedList) -> bool:
    """ Equals methods not implemented as two different nodes
    are not equal even if they have the same value.
    Conditions:
    * None is not equal to anything, not even None. (Empty is falsy.)
    * Not identical if not instance of LinkedList.
    * Even if (one, another) -> 2 sepparate instances, "one is another" is True!
    * Identical if both empty.
    * Check node pairs. """
    # MUST compare to None, as an empty list with length 0 is False:
    if one_ll is None or another_ll is None:
        return False
    if not ( isinstance(one_ll, LinkedList) and \
        isinstance(another_ll, LinkedList) ):
        return False
    len_one = len(one_ll)
    len_another = len(another_ll)
    if len_one == len_another:
        if len_one == 0:
            return True
    else:
        return False
    for one_node, another_node in zip(one_ll, another_ll):
        if one_node.value != another_node.value:
            return False
    return True
