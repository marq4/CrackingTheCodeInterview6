"""
1.7: Given an NxN matrix (each cell 4 bytes),
    rotate by 90° in place.
TDD: it is recommended to run the tests before coding.
To automatically test your code in Win from Git Bash do:
    python -m pytest tests/verify_matrix_rotated.py -v
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
    generated = [ \
        [ randint(min_val, max_val) for _ in range(num) ] \
        for _ in range(num) \
                ]
    return generated

def display_matrix(display_me: List[ List[int] ]) -> None:
    """ Comprehensive pretty print of 2D matrix. """
    for row in display_me:
        print(row)


def main():
    """ Generate some random numbers and
        visually verify solution. """
    example_mx = generate_randint_matrix(4, 0, 9)
    display_matrix(example_mx)
    rotate_matrix(example_mx)
    print("\n After rotating 90 degrees: ")
    display_matrix(example_mx)

# Simple visual test:
if __name__ == "__main__":
    main()


# For pytest. Also rename here:     VVVVVVVVVVV
rotate_matrix_function =            rotate_matrix
