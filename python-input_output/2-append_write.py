#!/usr/bin/python3
"""
Function that appends a string to a text file (UTF-8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
