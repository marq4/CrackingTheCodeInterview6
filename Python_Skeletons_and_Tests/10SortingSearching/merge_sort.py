"""
Merge sort: O(n log(n)).
TDD: it is recommended to run the tests before coding.
To automatically test your code in Win from Git Bash do:
    Uncomment the line to import merge_sort on tests/verify_sorted_tests.py.
    python -m pytest tests/verify_sorted_tests.py -v
"""

from random import randint

from binary_search import is_sorted


# If this function is renamed, also change last line.
def merge_sort(array: list) -> None:
    """ TODO. """
    # Implement your solution here.
    if array:
        return


def main():
    """ Generate some random numbers and
        visually verify solution. """
    numbers_array = []
    for _ in range(10):
        numbers_array.append( randint(0, 99) )
    print(numbers_array)
    merge_sort(numbers_array)
    print(f" After merge sort:\n{numbers_array}")
    assert is_sorted(numbers_array)

# Simple visual test:
if __name__ == "__main__":
    main()


# For pytest. Also rename here:     VVVVVVVVVVV
merge_sort_function =               merge_sort
