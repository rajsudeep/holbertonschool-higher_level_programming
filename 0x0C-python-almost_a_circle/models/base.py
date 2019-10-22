#!/usr/bin/python3
"""
Class Base -
manages the id attribute

"""
from json import dumps, loads
from os import path


class Base:
    """ creates an identifier for an instance """
    __nb_objects = 0

    def __init__(self, id=None):
        """ inits an id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON representation of dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save objects to a file """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="UTF-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        obj = None
        if cls.__name__ == "Rectangle":
            obj = cls(2, 3)
        elif cls.__name__ == "Square":
            obj = cls(2)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ loads a file and returns a list of instances from it """
        if not path.isfile("{}.json".format(cls.__name__)):
            return []
        with open("{}.json".format(cls.__name__), "r", encoding="utf-8") as f:
                return [cls.create(**obj) for obj in cls.from_json_string(
                    f.read())]
