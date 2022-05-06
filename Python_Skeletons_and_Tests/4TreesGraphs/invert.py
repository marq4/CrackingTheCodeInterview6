"""
Invert a binary tree.
TDD: it is recommended to run the tests before coding.
To automatically test your code in Win from Git Bash do:
    python -m pytest tests/test_sanity_binary_tree_0.py -v
"""

from binary_tree import (BinaryTree, BinaryTreeNode,
                         generate_randint_binary_tree)


# If this function is renamed, also change last line.
def invert(binary_tree: BinaryTree) -> None:
    """ Calls auxiliary recursive function. """
    if binary_tree is not None and binary_tree:
        recursive_invert(binary_tree.root)

def recursive_invert(root: BinaryTreeNode) -> None:
    """ Inverts in place. """
    # Implement your solution here.
    root.value = root.value


def main():
    """ Generate some random numbers and
    visually verify solution. """
    numbers_bt = generate_randint_binary_tree(4, 0, 22)
    print(numbers_bt)
    invert(numbers_bt)
    print(f"\n After inverting:\n\n{numbers_bt} ")

# Simple visual test:
if __name__ == "__main__":
    main()


# For pytest. Also rename here:     VVVVVVVVVVV
invert_function =                   invert
