#!/usr/bin/python3
"""
Module - Base Class

- Base of all classes
- private class instance: __nb_objects
- staticmethod:
    - def to_json_string(list_dictionaries)
    - def from_json_string(json_string)
- classmethod:
    - def save_to_file(cls, list_objs)
    - def create(cls, **dictionary)
    - def load_from_file(cls)
"""
import json


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
        if list_dictionaries is None or list_dictionaries == []:
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
            data = cls.to_json_string([obj.to_dictionary()
                                      for obj in list_objs])

        filename = cls.__name__ + "json"

        with open(filename, "w", encoding="UTF-8") as textfile:
            textfile.write(data)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set using **dictionary"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise NotImplementedError("create method not implemented \
                    for class {}".format(cls.__name__))

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Loads instance from class"""
        filename = cls.__name__ + "json"

        try:
            with open(filename, "r", encoding="UTF-8") as textfile:
                json_string = textfile.read()
        except FileNotFoundError:
            return []

        if not json_string:
            return []

        json_list = json.loads(json_string)
        instances = [cls.create(**data) for data in json_list]
        return instances
