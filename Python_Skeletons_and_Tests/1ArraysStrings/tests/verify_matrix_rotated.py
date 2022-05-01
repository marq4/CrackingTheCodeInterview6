""" Automatically validate your implementation. """

from rotate_matrix_7 import rotate_matrix_function


def test_none():
    """ Matrix is None. """
    non_existing = None
    rotate_matrix_function(non_existing)
    assert non_existing is None

def test_empty():
    """ Matrix is empty. """
    empty_mx = []
    rotate_matrix_function(empty_mx)
    assert not empty_mx

def test_1x1():
    """ Matrix is a single cell. """
    single_mx = [[1]]
    rotate_matrix_function(single_mx)
    assert single_mx == [[1]]

def test_basic_2x2():
    """ Matrix is 2x2. """
    small_mx = [[1, 2], [3, 4]]
    rotate_matrix_function(small_mx)
    assert small_mx == [[3, 1], [4, 2]]

def test_intermediate_3x3():
    """ Matrix is 3x3. """
    medium_mx = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
    rotate_matrix_function(medium_mx)
    assert medium_mx == \
        [[77, 44, 11], [88, 55, 22], [99, 66, 33]]

def test_advanced_5x5():
    """ Matrix is 5x5. """
    inc = 1
    large_mx = []
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(inc)
            inc += 1
        large_mx.append(row)
    rotate_matrix_function(large_mx)
    assert large_mx == [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]
