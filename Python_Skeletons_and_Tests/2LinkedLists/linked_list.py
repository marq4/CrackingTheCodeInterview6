"""
From: GitHub/careercup/CtCI-6th-Edition-Python.
Please first validate this file. In Win from Git Bash do:
    python -m pytest Tests/sanity_linked_list_tests_0.py
"""

from random import randint


class LinkedListNode:
    """ DLL Node. """
    def __init__(self, val, next_node=None, prev_node=None):
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
        length = 0
        traverse = self.head
        while traverse:
            length += 1
            traverse = traverse.next
        return length

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if isinstance( other, type(self) ):
            if self.is_empty() and other.is_empty():
                return True
            if len(self) != len(other):
                return False
            for self_node, other_node in zip(self, other):
                if self_node.value != other_node.value:
                    return False
            return True
        return False


    def is_empty(self) -> bool:
        """ LinkedList is empty if head is None. """
        return self.head is None

    def add(self, value):
        """ Add new value to end of LinkedList. """
        if self.is_empty():
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        """ Add new value to beginning of LinkedList. """
        if self.is_empty():
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
    max_val -- upper bound inclusive.
    """
    generated = LinkedList()
    for _ in range(num):
        generated.add( randint(min_val, max_val) )
    return generated
