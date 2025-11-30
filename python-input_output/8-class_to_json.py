#!/usr/bin/python3
"""Function that returns the dictionary description for JSON serialization."""


def class_to_json(obj):
    """
    Return the dictionary representation of an object's attributes
    suitable for JSON serialization.
    """
    return obj.__dict__.copy()
