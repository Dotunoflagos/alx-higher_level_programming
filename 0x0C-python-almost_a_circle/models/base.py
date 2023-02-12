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
        if list_objs == "[]" or list_objs is None or list_objs == "":
            with open(filen, "w") as f:
                f.write("[]")
            return

        save = []
        with open(filen, "w") as f:
            for ob in list_objs:
                save.append(ob.to_dictionary())
            f.write(cls.to_json_string(save))

    @staticmethod
    def from_json_string(json_string):
        if json_string == "[]" or json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """file to instances"""
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as file:
            stuff = cls.from_json_string(file.read())
        return [cls.create(**index) for index in stuff]
        
