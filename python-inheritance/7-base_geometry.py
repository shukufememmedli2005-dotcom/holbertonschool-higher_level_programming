#!/usr/bin/python3
"""BaseGeometry class with area() and integer_validator()"""

class BaseGeometry:
    """Base class for geometry"""

    def area(self):
        """Public instance method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as integer greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
