""" Automatically validate your implementation. """

from rotate_matrix_7 import rotate_matrix_function, \
    get_inc_matrix_pretty_print, generate_randint_matrix, \
    generate_inc_matrix


def test_sanity_generate_randint_matrix():
    """ Randint matrix. """
    dimensions = 2
    lo_val = 5
    hi_val = 7
    rand_mx = generate_randint_matrix(dimensions, lo_val, hi_val)
    assert rand_mx is not None
    assert len(rand_mx) == dimensions
    assert rand_mx[0][0] <= hi_val and rand_mx[0][0] >= lo_val

def test_sanity_generate_inc_matrix():
    """ Incremental matrix. """
    dimensions = 3
    inc_mx = generate_inc_matrix(dimensions)
    assert inc_mx is not None
    assert len(inc_mx[0]) == dimensions
    assert inc_mx[0][0] == 1

def test_sanity_get_inc_matrix_pretty_print():
    """ Incremental matrix representation. """
    expected = "1\t2\n3\t4"
    actual = get_inc_matrix_pretty_print([[1, 2], [3, 4]])
    assert actual is not None
    assert expected == actual


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
