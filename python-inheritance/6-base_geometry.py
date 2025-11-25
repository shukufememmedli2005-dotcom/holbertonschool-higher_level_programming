#!/usr/bin/python3
"""Defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Raises an exception since area is not implemented."""
        raise Exception("area() is not implemented")
