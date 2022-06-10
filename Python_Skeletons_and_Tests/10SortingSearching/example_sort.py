""" Common code to all sorting algorithms. """

from random import randint

from binary_search import is_sorted


def simple_test_visual(sort_function):
    """ Generate some random numbers and
        visually verify solution. """
    assert sort_function
    numbers_array = []
    for _ in range(10):
        numbers_array.append( randint(0, 99) )
    print(numbers_array)
    sort_function(numbers_array)
    print(f" After merge sort:\n{numbers_array}")
    assert is_sorted(numbers_array)
