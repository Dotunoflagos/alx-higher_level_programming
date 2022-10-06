#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    unm = sorted(a_dictionary)
    for index in unm:
        print('{}: {}'.format(index, a_dictionary[index]))
