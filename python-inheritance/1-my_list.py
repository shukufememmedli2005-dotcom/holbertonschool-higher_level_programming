#!/usr/bin/python3
"""
Module that defines the MyList class.
"""


class MyList(list):
    """
    A class that inherits from list and adds a method to print
    the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Does not modify the original list.
        """
        print(sorted(self))
