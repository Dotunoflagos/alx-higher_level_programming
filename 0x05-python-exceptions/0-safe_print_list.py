#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0 
        for a in my_list[:x]:
            print(a, end="")
            j +=1
        print("\n", end="")
        if x > j:
            return j
        else:
            return x
    except:
        j = 0 
        for a in my_list:
            print(a, end="")
            j +=1
        print("\n", end="")
        return j
    