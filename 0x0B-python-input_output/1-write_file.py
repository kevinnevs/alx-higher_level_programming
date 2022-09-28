#!/usr/bin/python3
"""
write_file
"""


def write_file(filename="", text=""):
    """
    writes a str to a filename
    creates file if doesn't exist
    overwites the content of file if exists
    """

    with open(filename, mode="w", encoding="utf-8") as writeFile:
        if len(text) > 0:
            writeFile.write(text)
        else:
            writeFile.write(text)
    return len(text)
