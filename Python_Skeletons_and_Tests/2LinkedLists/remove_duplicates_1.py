"""
2.1: Remove duplicates from an unsorted linked list.
TDD: it is recommended to run the tests before coding.
To automatically test your code in Win from Git Bash do:
    python -m pytest tests/verify_duplicates_removed_tests_1.py -v
"""

from linked_list import LinkedList, generate_randint_linked_list


# If this function is renamed, also change last line.
def remove_duplicates(linked_list: LinkedList) -> None:
    """ TODO. """
    if ( linked_list is None or linked_list.is_empty() ):
        return
    # Implement your solution here:


def main():
    """ Generate some random numbers and
        visually verify solution. """
    numbers_ll = generate_randint_linked_list(7, 0, 4)
    print(numbers_ll)
    remove_duplicates(numbers_ll)
    print(f" After removing duplicates:\n{numbers_ll} ")

# Simple visual test:
if __name__ == "__main__":
    main()


# For pytest. Also rename here:     VVVVVVVVVVV
remove_duplicates_function =        remove_duplicates
