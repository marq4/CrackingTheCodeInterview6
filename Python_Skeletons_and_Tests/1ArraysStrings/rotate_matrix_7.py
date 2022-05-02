"""
1.7: Given an NxN matrix (each cell 4 bytes),
    rotate by 90° in place.
TDD: it is recommended to run the tests before coding.
To automatically test your code in Win from Git Bash do:
    python -m pytest tests/verify_matrix_rotated_tests_7.py -v
"""

from typing import List
from random import randint


# If this function is renamed, also change last line.
def rotate_matrix(matrix: List[ List[int] ]) -> None:
    """ TODO. """
    if ( matrix is not None and len(matrix) != 0 ):
        # Implement your solution here.
        pass


def generate_randint_matrix(num: int, \
    min_val: int, max_val: int) -> List[ List[int] ]:
    """ Generate a new int 2D matrix with random ints.
    Keyword arguments:
    num -- the rows/cols of the matrix.
    min_val -- cell lower bound inclusive.
    max_val -- cell upper bound inclusive.
    """
    generated = [
        [ randint(min_val, max_val) for _ in range(num) ]
        for _ in range(num)
                ]
    return generated

def generate_inc_matrix(dimensions: int) \
    -> List[ List[int] ]:
    """ Return a dimensions x dimensions
        int matrix with incremental values per cell. """
    return [ [ ( (w+1) + dimensions*q ) \
        for w in range(dimensions) ] \
        for q in range(dimensions) ]

def get_inc_matrix_pretty_print(matrix: \
    List[ List[int] ]) -> str:
    """ Return comprehensive represention of 2D matrix. """
    return ( "\n".join( [
        "\t".join( [str(cell) for cell in row] )
        for row in matrix] ) )

def display_matrix(display_me: List[ List[int] ]) -> None:
    """ Simply print each row of 2D matrix. """
    for row in display_me:
        print(row)


def main():
    """ Generate some random numbers and
        visually verify solution. """
    rand_mx = generate_randint_matrix(3, 0, 9)
    print()
    print("Randint matrix: ")
    display_matrix(rand_mx)
    rotate_matrix(rand_mx)
    print("\n After rotating 90 degrees: ")
    display_matrix(rand_mx)
    print("\n")
    print("Incremental matrix: ")
    incremental_matrix = generate_inc_matrix(5)
    print( get_inc_matrix_pretty_print(incremental_matrix) )
    rotate_matrix(incremental_matrix)
    print("\n After rotating 90 degrees: ")
    print( get_inc_matrix_pretty_print(incremental_matrix) )

# Simple visual test:
if __name__ == "__main__":
    main()


# For pytest. Also rename here:     VVVVVVVVVVV
rotate_matrix_function =            rotate_matrix


def wrong_return(number: int) -> list:
    """ Should make mypy fail. """
    return number is not None
