#!/usr/bin/python3
"""
Module - Base Class

- Base of all classes
- private class instance: __nb_objects
- staticmethod: 
    - def to_json_string(list_dictionaries)
    - def from_json_string(json_string)
- classmethod: def save_to_file(cls, list_objs)
"""


class Base:
    """A definition of the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class with optional id"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of the argument"""
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of the file"""
        if list_objs is None:
            data = "[]"
        else:
            data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        filename = cls.__name__ + "json"

        with open(filename, "w", encoding="UTF-8") as textfile:
            textfile.write(data)
