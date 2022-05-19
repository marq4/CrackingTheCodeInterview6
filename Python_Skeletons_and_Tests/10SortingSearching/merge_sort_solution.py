"""
Example explanation:
    If initial array is empty, None, or has a single element: do nothing.
    array_Original = [5, 8, 3, 1]
    middle = 2
    left_O = [5, 8]
    rite_O = [3, 1]
    RECURSE!
        array_2l = [5, 8]           array_2r = [3, 1]
        middle = 1                  middle = 1
        left_2l = [5]               left_2r = [3]
        rite_2l = [8]               rite_2r = [1]
        A single-element array is sorted.
        Recursive calls ___________ simply return.
        Var add keeps track of position to add to array_2l/array_2r.
        add = 0                     add = 0
        While left_2l and           While left_2r and
        rite_2l are neither         rite_2r are neither
        None nor empty do:          None nor empty do:
            Compare leftmost        Compare leftmost
            elements, pop_left      elements, pop_left
            smallest and overwrite  smallest and overwrite
            array_2l[add].          array_2r[add].
                        Add any leftover elements.
"""

def solution(array: list) -> None:
    """ Sorts in place.
    * Base case: single-element array (or empty or None).
    * Divide in half: get middle, create 2 new arrays.
    * Recurse on each sub array.
    * Merge (and sort) halves and leftovers.
    """
    if array and len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        rite = array[middle:]

        solution(left)
        solution(rite)

        add = 0
        while left and rite:
            if left[0] < rite[0]:
                array[add] = left.pop(0)
            else:
                array[add] = rite.pop(0)
            add += 1
        while left:
            array[add] = left.pop(0)
            add += 1
        while rite:
            array[add] = rite.pop(0)
            add += 1
