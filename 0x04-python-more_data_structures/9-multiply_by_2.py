#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for index in a_dictionary:
        new[index] *= 2
    return new
