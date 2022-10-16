#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(my_list[:x])
        j = 0 
        for a in my_list:
            j +=1
        if x > j:
            return j
        else:
            return x
    except:
        print(my_list)
