#!/usr/bin/python3
"""
Module - 9
- class: Student
- public method: def to_json
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

    def to_json(self):
        """Get a dictionary representation of the student"""
        return self.__dict__
