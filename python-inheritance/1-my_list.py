#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """MyList inherits from list and can print a sorted version."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original."""
        print(sorted(self))
