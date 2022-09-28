#!/usr/bin/python3
"""
append_write
"""


def append_write(filename="", text=""):
    """
    appends text to a file
    """

    with open(filename, mode="a", encoding="utf-8") as appendWrite:
        appendWrite.write(text)
    return len(text)
