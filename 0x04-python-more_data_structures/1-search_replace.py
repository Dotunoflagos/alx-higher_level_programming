#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    final = my_list[:]
    while i < len(my_list):
        if final[i] == search:
            final[i] = replace
        i += 1
    return final
