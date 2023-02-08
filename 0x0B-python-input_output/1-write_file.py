#!/usr/bin/
"""method for student creation"""


def write_file(filename="", text=""):
    """method for student creation"""

    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
