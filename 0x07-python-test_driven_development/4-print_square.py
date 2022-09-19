#!/usr/bin/python3
"""
print_square prints a square with the character #
"""


def print_square(size):
    """
    Prints a square with a size
    Checks if "size" is an int
    Checks if "size" less than 0
    Checks if "size" is a float & less than 0
    Checks if "size" is equal to 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == float and size <= 0:
        raise TypeError("size must be an integer")
    if size == 0:
        return None

    for row in range(size):
        print('#' * size)
