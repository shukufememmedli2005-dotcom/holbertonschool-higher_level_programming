#!/usr/bin/python3
"""Module 7-base_geometry.py: BaseGeometry class."""

class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Public instance method that is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
