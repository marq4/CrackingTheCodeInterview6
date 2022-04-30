"""
Reverse a singly linked list.
TDD: it is recommended to run the tests before coding.
To automatically test your code in Win from Git Bash do:
    python -m pytest tests/verify_linked_list_reversed_tests.py -v
"""

from linked_list import LinkedList, generate_randint_linked_list


# If this function is renamed, also change last line.
def reverse(linked_list: LinkedList) -> LinkedList:
    """ TODO. """
    if ( linked_list is None or linked_list.is_empty() ):
        return linked_list
    # Implement your solution here:
    return None


def main():
    """ Generate some random numbers and
        visually verify solution. """
    numbers_ll = generate_randint_linked_list(7, 0, 4)
    print(numbers_ll)
    reverse(numbers_ll)
    print(f" After reversing:\n{numbers_ll} ")

# Simple visual test:
if __name__ == "__main__":
    main()


# For pytest. Also rename here:     VVVVVVVVVVV
reverse_function =                  reverse
