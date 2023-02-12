#!/usr/bin/python3
"""
Base model
"""
import json
import os
import re
from random import randint
from turtle import Pen


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of polygons to a file in CSV format.

        Args:
            list_objs (list): A list of polygons.
        """
        file_name = '{}.csv'.format(cls.__name__)
        poly_fmt_fxns = {
            'Rectangle': lambda x: '{},{:d},{:d},{:d},{:d}'.format(
                x.id, x.width, x.height, x.x, x.y),
            'Square': lambda x: '{},{:d},{:d},{:d}'.format(
                x.id, x.size, x.x, x.y),
        }
        vals_list = []
        if list_objs is not None:
            poly_name = cls.__name__
            for obj in list_objs:
                if (type(obj) is cls) and (poly_name in poly_fmt_fxns):
                    vals_list.append('{}\n'.format(
                        poly_fmt_fxns[poly_name](obj)))
        with open(file_name, mode='w', encoding='utf-8') as file:
            file.writelines(vals_list)

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of polygons from a file in CSV format.

        Returns:
            list: A list of polygons.
        """
        poly_name = cls.__name__
        file_name = '{}.csv'.format(poly_name)
        poly_fmt_fxns = {
            'Rectangle': lambda x: {
                'id': int(x[0]),
                'width': int(x[1]),
                'height': int(x[2]),
                'x': int(x[3]),
                'y': int(x[4]),
            },
            'Square': lambda x: {
                'id': int(x[0]),
                'size': int(x[1]),
                'x': int(x[2]),
                'y': int(x[3]),
            },
        }
        poly_fmt = {
            'Rectangle': r'\s*[^,]+,[^,]+,[^,]+,[^,]+,[^,]+',
            'Square': r'\s*[^,]+,[^,]+,[^,]+,[^,]+',
        }
        lines = []
        attr_dicts = []
        if os.path.isfile(file_name):
            with open(file_name, mode='r') as file:
                for line in file.readlines():
                    attrs_match = re.match(poly_fmt[poly_name], line)
                    if attrs_match is not None:
                        cols = line.strip().split(',')
                        attr_dicts.append(poly_fmt_fxns[poly_name](cols))
        cls_list = list(map(lambda x: cls.create(**x), attr_dicts))
        return cls_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws the polygons in each list using Turtle graphics.

        Args:
            list_rectangles (list): A list of Rectangle objects.
            list_squares (list): A list of Square objects.
        """
        poly_list = []
        funcs = {
            'hex_to_rgb': lambda x: (x >> 16, (x >> 8) % 0xff, x % 0xff)
        }
        pen = Pen()
        screen = pen.getscreen()
        poly_list.extend(list_rectangles)
        poly_list.extend(list_squares)
        wind_width = max(
            [max(map(lambda x: x.width + x.x, poly_list)) + 4, 460.8])
        wind_height = max(
            [max(map(lambda x: x.height + x.y, poly_list)) + 4, 259.2])
        screen.setup(width=wind_width, height=wind_height)
        screen.setworldcoordinates(0, wind_height, wind_width, 0)
        pen.speed('slowest')
        pen.degrees()
        pen.pensize(2)
        pen.hideturtle()
        for i in range(len(poly_list)):
            rect = poly_list[i]
            pen.up()
            pen.forward(rect.x)
            pen.right(90)
            pen.backward(rect.y)
            pen.showturtle()
            pen.down()
            pen.begin_poly()
            pen.fillcolor(funcs['hex_to_rgb'](randint(0, 0xffffff)))
            pen.pencolor(funcs['hex_to_rgb'](randint(0, 0xffffff)))
            pen.begin_fill()
            pen.backward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.backward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.end_fill()
            pen.end_poly()
            pen.up()
            # move to start pos
            pen.hideturtle()
            pen.right(90)
            pen.backward(rect.y)
            pen.left(90)
            pen.forward(rect.x)
            pen.right(180)
        while True:
            c = input('Enter "q" to quit: ')
            if c == 'q':
                break