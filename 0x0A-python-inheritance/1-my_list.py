#!/usr/bin/python3
"""
Funct that prints list in ascending order
"""


class MyList(list):
    """
    Contains list
    """
    def print_sorted(self):
        """
        prints list in sorted order
        """
        print(sorted(self))
