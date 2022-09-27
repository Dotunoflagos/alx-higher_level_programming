#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        for i in my_list:
            for j in my_list:
                if i > j:
                    continue   
                else:
                    i = j
                    continue
        return i
    return "None"
