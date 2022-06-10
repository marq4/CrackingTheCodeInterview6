"""
Merge sort: O(n log(n)).
TDD: it is recommended to run the tests before coding.
To automatically test your code in Win from Git Bash do:
    Uncomment the line to import merge_sort on tests/verify_sorted_tests.py.
    python -m pytest tests/verify_sorted_tests.py -v
"""

from sort_example import simple_test_visual


# If this function is renamed, also change last line.
def merge_sort(array: list) -> None:
    """ TODO. """
    # Implement your solution here.
    if array:
        return


if __name__ == "__main__":
    simple_test_visual(merge_sort)


# For pytest. Also rename here:     VVVVVVVVVVV
merge_sort_function =               merge_sort
