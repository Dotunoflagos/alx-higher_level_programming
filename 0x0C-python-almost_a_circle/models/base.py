#!/usr/bin/python3
"""
Base model
"""
import json
import os


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filen = "{}.json".format(cls.__name__)
        save = []
        with open(filen, "w") as f:
            for ob in list_objs:
                save.append(ob.to_dictionary())
            f.write(cls.to_json_string(save))