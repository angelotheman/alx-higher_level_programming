#!/usr/bin/python3
"""
Module - 11
- class: Student
- public method: def to_json
- public method: def reload_from_json
- instantiation: first name, lastname, age
"""


class Student:
    """Defines a student object"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student

        Args:
            first_name (str): First name of student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student if in attrs"""
        if attrs is not None:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student instance with json"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
