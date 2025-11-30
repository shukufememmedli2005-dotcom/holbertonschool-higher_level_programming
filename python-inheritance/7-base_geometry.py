#!/usr/bin/python3
"""Module BaseGeometry
Defines a BaseGeometry class with area and integer validation.
"""

class BaseGeometry:
    """BaseGeometry class with unimplemented area method and integer validation."""

    def area(self):
        """Raises an exception since area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
