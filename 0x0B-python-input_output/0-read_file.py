#!/usr/bin/python3
"""method for student creation"""


def read_file(filename=""):
    """method for student creation"""

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
