#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    indez = len(my_list)
    for i in my_list:
        indez = indez - 1
        print('{:d}'.format(my_list[indez]))
