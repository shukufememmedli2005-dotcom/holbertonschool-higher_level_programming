#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of the Student instance.
        If attrs is a list of strings, return only those attributes.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(type(x) is str for x in attrs):
            filtered = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered[key] = self.__dict__[key]
            return filtered

        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dictionary.
        Keys are attribute names; values are attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
