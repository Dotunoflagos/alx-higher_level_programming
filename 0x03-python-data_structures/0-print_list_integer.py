#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print('{:d}'.format(i))

a = [7,0,98,8,7,8]
print_list_integer(a)