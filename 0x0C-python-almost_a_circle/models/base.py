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
import csv


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

        filename = cls.__name__ + ".json"

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
        filename = cls.__name__ + ".json"

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves JSON to CSV"""
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)

            if list_objs is not None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attributes = ["id", "width", "height", "x", "y"]
                else:
                    attributes = ["id", "size", "x", "y"]

                writer = csv.DicWriter(csv_file, fieldnames=attributes)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads JSON from CSV"""
        filename = cls.__name__ + ".csv"
        instances = []

        try:
            with open(filename, "r", newline="") as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    row = [int(value) for value in row]
                    if cls.__name__ == "Rectangle":
                        instances.append(cls.create(id=row[0],
                                                    width=row[1],
                                                    height=row[2],
                                                    x=row[3], y=row[4]))
                    elif cls.__name__ == "Sqaure":
                        instances.append(cls.create(id=row[0],
                                                    size=row[1],
                                                    x=row[2], y=row[3]))
        except FileNotFoundError:
            pass

        return instances
