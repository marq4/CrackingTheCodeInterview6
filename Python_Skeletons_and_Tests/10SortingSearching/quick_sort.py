"""
Quick sort: O(n log(n)).
TDD: it is recommended to run the tests before coding.
To automatically test your code in Win from Git Bash do:
    Uncomment the line to import quick_sort on tests/verify_sorted_tests.py.
    python -m pytest tests/verify_sorted_tests.py -v
"""

from example_sort import simple_test_visual


# If this function is renamed, also change last line.
def quick_sort(array: list) -> None:
    """ Call internal recursive function with 0, length of array -1. """
    if array:
        recurs(array, 0, len(array)-1)

def recurs(arr: list, low: int, high: int) -> None:
    """ TODO. """
    # Implement your solution here.
    if arr:
        low = high
        high = low


if __name__ == "__main__":
    simple_test_visual(quick_sort)


# For pytest. Also rename here:     VVVVVVVVVVV
quick_sort_function =               quick_sort
