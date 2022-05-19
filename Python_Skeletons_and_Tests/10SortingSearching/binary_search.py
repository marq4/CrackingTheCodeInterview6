"""
Binary search: O(log(n)).
TDD: it is recommended to run the tests before coding.
To automatically test your code in Win from Git Bash do:
    python -m pytest tests/verify_binary_search_tests.py -v
"""


# If this function is renamed, also change last line.
# Comment-out the one you don't want to test (iterative or recursive).
def binary_search(array: list, val: int) -> int:
    """ Return index of val or -1 if not found. """
    assert is_sorted(array)
    #return binary_search_iterative(array, val)
    return binary_search_recursive(array, val, 0, len(array)-1)


def binary_search_recursive(arr: list, val: int, low: int, high: int) -> int:
    """ TODO. """
    # Implement your solution here.
    if arr and val and low and high:
        return -1
    return -1


def binary_search_iterative(arr: list, val: int) -> int:
    """ TODO. """
    # Implement your solution here.
    if arr and val:
        return -1
    return -1

def is_sorted(array: list) -> bool:
    """ Verify array of ints is sorted.
    None is not sorted. Empty array is sorted. """
    if array is None:
        return False
    return all( array[i] <= array[i+1] for i in range(len(array)-1) )


def main():
    """ Visually verify solution. """
    ordered_arr = [-67, 3, 6, 7, 8, 21, 35, 78, 82, 99, 102]
    print( 'Indices =>   0   1  2  3  4  5   6   7   8   9   10')
    print(f"Array   => {ordered_arr}")
    find_value = int( input('Value to find: ') )
    index = binary_search(ordered_arr, find_value)
    print(f"Found @ {index}")

# Simple visual test:
if __name__ == "__main__":
    main()


# For pytest. Also rename here:     VVVVVVVVVVV
binary_search_function =            binary_search
