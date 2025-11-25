#!/usr/bin/python3
"""Function to check if an object is an instance of a subclass of a given class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass (direct or indirect) of a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
