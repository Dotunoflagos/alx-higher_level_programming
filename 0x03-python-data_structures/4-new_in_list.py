#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_my = my_list[:]
    if my_list is None:
        pass
    elif (idx < 0):
        return list_my
    elif (idx > len(my_list) - 1):
        return list_my
    else:
        list_my[idx] = element
        return list_my
