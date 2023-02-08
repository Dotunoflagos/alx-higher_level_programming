#!/usr/bin/python3
"""method for student creation"""


def append_write(filename="", text=""):
    """method for student creation"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
