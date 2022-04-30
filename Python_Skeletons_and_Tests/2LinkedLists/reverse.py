"""
Reverse a singly linked list.
TDD: it is recommended to run the tests before coding.
To automatically test your code in Win from Git Bash do:
    python -m pytest tests/verify_reversed_tests.py -v
"""

from linked_list import LinkedList, LinkedListNode, \
    generate_randint_linked_list


# To test this one, change main function and last line.
def reverse_iter(linked_list: LinkedList) -> None:
    """ TODO. """
    if ( linked_list is not None and not linked_list.is_empty() ):
        # Implement your solution here.
        pass


# If this function is renamed, also change last line.
def reverse(linked_list: LinkedList) -> None:
    """ Calls auxiliary recursive function. """
    if linked_list is not None:
        linked_list.head = recursive_reverse(linked_list.head)


def recursive_reverse(head: LinkedListNode) -> LinkedListNode:
    """ Returns new head. """
    # Implement your solution here.
    return head

def main():
    """ Generate some random numbers and
        visually verify solution. """
    numbers_ll = generate_randint_linked_list(4, 0, 22)
    print(numbers_ll)
    reverse(numbers_ll)
    print(f" After reversing:\n{numbers_ll} ")

# Simple visual test:
if __name__ == "__main__":
    main()


# For pytest. Also rename here:     VVVVVVVVVVV
reverse_function =                  reverse
